#!/usr/bin/env python3
"""
processor.py — Michigan Court Document Processor
=================================================

A command-line tool that:
  1. Scans PDF and TXT files to extract legal case information
  2. Populates court document templates with extracted (and user-supplied) data
  3. Covers all Michigan jurisdictions: Circuit Courts, Muskegon County,
     Court of Appeals, Supreme Court, Federal (W.D. Mich., 6th Cir.)

COMMANDS
--------
  scan           Extract fields from a PDF or TXT source file
  fill           Render a specific template with field values
  auto           One-step: scan a source file, then fill a template
  list-templates List all available document templates
  fields         Show the field placeholders in a specific template

QUICK START
-----------
  # 1. Install dependencies
  pip install -r requirements.txt

  # 2. See all available templates
  python processor.py list-templates

  # 3. Scan an existing document to extract case information
  python processor.py scan my_complaint.pdf

  # 4. Fill a template (you will be prompted for any missing fields)
  python processor.py fill michigan/circuit/civil/summons --prompt

  # 5. Auto-mode: scan source + fill template in one step
  python processor.py auto my_complaint.pdf michigan/circuit/civil/answer
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich import print as rprint

from extractor import extract_fields, extract_text_only
from renderer import (
    render_template,
    list_templates,
    find_template,
    get_template_fields,
)

console = Console()

# ---------------------------------------------------------------------------
# CLI group
# ---------------------------------------------------------------------------

@click.group()
@click.version_option("1.0.0", prog_name="court-doc-processor")
def cli():
    """Michigan Court Document Processor.

    Scans PDF/TXT files to extract case data, then populates court document
    templates across all Michigan and federal jurisdictions.
    """


# ---------------------------------------------------------------------------
# scan
# ---------------------------------------------------------------------------

@cli.command()
@click.argument("source", type=click.Path(exists=True))
@click.option("--text-only", is_flag=True,
              help="Print raw extracted text instead of structured fields.")
@click.option("--output", "-o", type=click.Path(),
              help="Save extracted fields to a JSON file.")
def scan(source: str, text_only: bool, output: str | None):
    """Extract case fields from a PDF or TXT SOURCE file.

    SOURCE can be any PDF or plain-text file.  The tool will attempt to
    identify common legal fields (case number, party names, court, dates,
    attorneys, etc.) using pattern matching.

    \b
    Examples:
      python processor.py scan complaint.pdf
      python processor.py scan motion.txt --output fields.json
      python processor.py scan order.pdf --text-only
    """
    source_path = Path(source)

    if text_only:
        console.rule("[bold blue]Raw Extracted Text")
        text = extract_text_only(source_path)
        console.print(text)
        return

    with console.status(f"[bold green]Scanning {source_path.name}..."):
        fields = extract_fields(source_path)

    if not fields:
        console.print(
            Panel(
                "[yellow]No fields could be automatically extracted.\n"
                "The PDF may be image-based (scanned) and require OCR.\n"
                "Use [bold]--text-only[/bold] to see raw text, or supply "
                "field values manually with the [bold]fill[/bold] command.",
                title="Scan Result",
                border_style="yellow",
            )
        )
        return

    table = Table(title=f"Extracted Fields — {source_path.name}",
                  show_header=True, header_style="bold cyan")
    table.add_column("Field", style="cyan", no_wrap=True)
    table.add_column("Extracted Value", style="green")

    for key, value in sorted(fields.items()):
        table.add_row(key, value)

    console.print(table)

    if output:
        out_path = Path(output)
        out_path.write_text(json.dumps(fields, indent=2))
        console.print(f"[bold green]Fields saved to:[/bold green] {out_path}")


# ---------------------------------------------------------------------------
# fill
# ---------------------------------------------------------------------------

@cli.command()
@click.argument("template_key")
@click.option("--fields-file", "-f", type=click.Path(exists=True),
              help="JSON file containing field values (e.g. from 'scan --output').")
@click.option("--set", "-s", "field_overrides", multiple=True,
              metavar="FIELD=VALUE",
              help="Set a field value directly, e.g. -s case_number=24-1234-CZ")
@click.option("--prompt", "-p", is_flag=True,
              help="Interactively prompt for any missing field values.")
@click.option("--output", "-o", type=click.Path(),
              help="Write rendered document to a file instead of stdout.")
@click.option("--mark-missing/--no-mark-missing", default=True,
              help="Mark unfilled fields as <<<FIELD_NAME>>> in output (default: on).")
def fill(template_key: str, fields_file: str | None, field_overrides: tuple,
         prompt: bool, output: str | None, mark_missing: bool):
    """Render a court document TEMPLATE with field values.

    TEMPLATE_KEY is the relative path to the template file (without .txt
    extension), e.g.:  michigan/circuit/civil/summons

    Use [bold]list-templates[/bold] to see all available keys.

    \b
    Examples:
      python processor.py fill michigan/circuit/civil/summons \\
          -s case_number=24-12345-CZ -s plaintiff_name="Jane Doe" --prompt

      python processor.py fill michigan/coa/claim-of-appeal \\
          -f extracted_fields.json --output claim_of_appeal.txt
    """
    # Build fields dict from all sources
    fields: dict[str, str] = {}

    if fields_file:
        loaded = json.loads(Path(fields_file).read_text())
        fields.update(loaded)

    for override in field_overrides:
        if "=" in override:
            k, _, v = override.partition("=")
            fields[k.strip()] = v.strip()

    try:
        result = render_template(
            template_key,
            fields,
            prompt_missing=prompt,
            mark_missing=mark_missing,
        )
    except FileNotFoundError as exc:
        console.print(f"[bold red]Error:[/bold red] {exc}")
        sys.exit(1)

    if output:
        out_path = Path(output)
        out_path.write_text(result)
        console.print(f"[bold green]Document written to:[/bold green] {out_path}")
    else:
        console.rule(f"[bold blue]{template_key}")
        console.print(result)


# ---------------------------------------------------------------------------
# auto
# ---------------------------------------------------------------------------

@cli.command()
@click.argument("source", type=click.Path(exists=True))
@click.argument("template_key")
@click.option("--set", "-s", "field_overrides", multiple=True,
              metavar="FIELD=VALUE",
              help="Override or add field values.")
@click.option("--prompt", "-p", is_flag=True,
              help="Prompt for any fields not auto-extracted.")
@click.option("--output", "-o", type=click.Path(),
              help="Write rendered document to a file.")
def auto(source: str, template_key: str, field_overrides: tuple,
         prompt: bool, output: str | None):
    """One-step: scan SOURCE, then render TEMPLATE_KEY.

    Extracts fields from SOURCE automatically, then uses them to populate the
    specified template.  Use --prompt to be asked for any fields that could
    not be auto-detected.

    \b
    Examples:
      python processor.py auto complaint.pdf michigan/circuit/civil/answer
      python processor.py auto case_file.pdf michigan/coa/claim-of-appeal \\
          --prompt --output claim_of_appeal.txt
    """
    source_path = Path(source)

    with console.status(f"[bold green]Scanning {source_path.name}..."):
        fields = extract_fields(source_path)

    # Apply overrides
    for override in field_overrides:
        if "=" in override:
            k, _, v = override.partition("=")
            fields[k.strip()] = v.strip()

    # Show what was found
    if fields:
        console.print(f"[green]✓ Extracted {len(fields)} field(s) from source.[/green]")
    else:
        console.print("[yellow]⚠ No fields auto-extracted. Manual entry will be needed.[/yellow]")

    try:
        result = render_template(
            template_key,
            fields,
            prompt_missing=prompt,
            mark_missing=True,
        )
    except FileNotFoundError as exc:
        console.print(f"[bold red]Error:[/bold red] {exc}")
        sys.exit(1)

    if output:
        out_path = Path(output)
        out_path.write_text(result)
        console.print(f"[bold green]Document written to:[/bold green] {out_path}")
    else:
        console.rule(f"[bold blue]{template_key}")
        console.print(result)


# ---------------------------------------------------------------------------
# list-templates
# ---------------------------------------------------------------------------

@cli.command("list-templates")
@click.option("--jurisdiction", "-j",
              help="Filter by jurisdiction prefix, e.g. 'michigan/circuit' or 'federal'.")
@click.option("--search", "-q",
              help="Search templates by keyword.")
def list_templates_cmd(jurisdiction: str | None, search: str | None):
    """List all available document templates.

    \b
    Examples:
      python processor.py list-templates
      python processor.py list-templates --jurisdiction michigan/coa
      python processor.py list-templates --search divorce
    """
    if search:
        templates = find_template(search)
    else:
        templates = list_templates(jurisdiction)

    if not templates:
        console.print("[yellow]No templates found matching your criteria.[/yellow]")
        return

    # Group by jurisdiction
    by_jur: dict[str, list] = {}
    for t in templates:
        jur = t["jurisdiction"]
        by_jur.setdefault(jur, []).append(t)

    for jur, tmps in sorted(by_jur.items()):
        table = Table(
            title=f"[bold cyan]{jur}[/bold cyan]",
            show_header=True,
            header_style="bold",
        )
        table.add_column("Template Key", style="green")
        table.add_column("Document Name")
        for t in sorted(tmps, key=lambda x: x["name"]):
            table.add_row(t["key"], t["name"].replace("-", " ").title())
        console.print(table)


# ---------------------------------------------------------------------------
# fields
# ---------------------------------------------------------------------------

@cli.command()
@click.argument("template_key")
def fields(template_key: str):
    """Show all placeholder field names required by TEMPLATE_KEY.

    \b
    Example:
      python processor.py fields michigan/circuit/civil/summons
    """
    try:
        field_list = get_template_fields(template_key)
    except FileNotFoundError as exc:
        console.print(f"[bold red]Error:[/bold red] {exc}")
        sys.exit(1)

    table = Table(title=f"Fields in: {template_key}", show_header=True,
                  header_style="bold cyan")
    table.add_column("#", style="dim")
    table.add_column("Field Name", style="cyan")
    table.add_column("Description")

    # Load friendly descriptions from field_mappings.json if available
    mappings_path = Path(__file__).parent / "config" / "field_mappings.json"
    descriptions: dict[str, str] = {}
    if mappings_path.exists():
        config = json.loads(mappings_path.read_text())
        for k, v in config.items():
            if isinstance(v, dict) and "description" in v:
                descriptions[k] = v["description"]

    for i, field_name in enumerate(field_list, 1):
        desc = descriptions.get(field_name, "")
        table.add_row(str(i), field_name, desc)

    console.print(table)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    cli()
