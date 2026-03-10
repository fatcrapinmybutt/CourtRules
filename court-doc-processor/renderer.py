"""
renderer.py — Template rendering engine for court documents.

Loads a template file and substitutes {{FIELD_NAME}} placeholders with
extracted or user-supplied field values.

Usage (as a module):
    from renderer import render_template, list_templates, find_template
    output = render_template("michigan/circuit/civil/summons", fields)
    print(output)
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from typing import Optional

TEMPLATES_DIR = Path(__file__).parent / "templates"

# Placeholder pattern: {{FIELD_NAME}} or {{ FIELD_NAME }}
_PLACEHOLDER_RE = re.compile(r"\{\{\s*([A-Za-z0-9_]+)\s*\}\}")

# Marker used in output to flag unfilled fields
_UNFILLED_MARKER = "<<<{}>>>"

# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def render_template(
    template_key: str,
    fields: dict[str, str],
    *,
    prompt_missing: bool = False,
    mark_missing: bool = True,
) -> str:
    """Render a template with the supplied field values.

    Args:
        template_key:    Relative path to the template (without .txt extension),
                         e.g. "michigan/circuit/civil/summons".
        fields:          Dict mapping field names to values.
        prompt_missing:  If True, interactively prompt for missing fields on
                         stdin (use in interactive CLI mode).
        mark_missing:    If True, unfilled placeholders are wrapped in
                         <<<FIELD_NAME>>> so users can spot them easily.

    Returns:
        The rendered document text.
    """
    template_path = _resolve_template(template_key)
    try:
        template_text = template_path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        raise FileNotFoundError(
            f"Could not read template file '{template_path}': {exc}"
        ) from exc
    return _substitute(template_text, fields,
                       prompt_missing=prompt_missing,
                       mark_missing=mark_missing)


def render_text(
    template_text: str,
    fields: dict[str, str],
    *,
    prompt_missing: bool = False,
    mark_missing: bool = True,
) -> str:
    """Render a template from raw text instead of a file path."""
    return _substitute(template_text, fields,
                       prompt_missing=prompt_missing,
                       mark_missing=mark_missing)


def list_templates(jurisdiction: Optional[str] = None) -> list[dict]:
    """Return a list of all available templates, optionally filtered by
    jurisdiction prefix (e.g. "michigan/circuit/civil")."""
    results = []
    search_root = TEMPLATES_DIR
    if jurisdiction:
        search_root = TEMPLATES_DIR / jurisdiction.replace(".", "/")

    for path in sorted(search_root.rglob("*.txt")):
        relative = path.relative_to(TEMPLATES_DIR)
        parts = list(relative.parts)
        # Build jurisdiction label from directory components
        jur_parts = parts[:-1]  # drop the filename
        template_name = path.stem
        results.append({
            "key": str(relative.with_suffix("")),
            "jurisdiction": "/".join(jur_parts),
            "name": template_name,
            "path": str(path),
        })
    return results


def find_template(keyword: str) -> list[dict]:
    """Search for templates whose path contains the given keyword."""
    keyword_lower = keyword.lower()
    return [t for t in list_templates()
            if keyword_lower in t["key"].lower()
            or keyword_lower in t["name"].lower()]


def get_template_fields(template_key: str) -> list[str]:
    """Return the list of placeholder field names in a given template."""
    template_path = _resolve_template(template_key)
    template_text = template_path.read_text()
    return sorted(set(_PLACEHOLDER_RE.findall(template_text)))


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _resolve_template(key: str) -> Path:
    """Resolve a template key (with or without .txt) to an absolute Path."""
    # Try exact match first
    candidates = [
        TEMPLATES_DIR / key,
        TEMPLATES_DIR / (key + ".txt"),
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    # Try fuzzy: find a template whose key contains the given string
    matches = find_template(key)
    if len(matches) == 1:
        return Path(matches[0]["path"])
    if len(matches) > 1:
        keys_str = "\n  ".join(m["key"] for m in matches)
        raise FileNotFoundError(
            f"Ambiguous template key '{key}'. Matches:\n  {keys_str}"
        )
    raise FileNotFoundError(
        f"Template not found: '{key}'\n"
        f"Use 'python processor.py list-templates' to see all available templates."
    )


def _substitute(
    text: str,
    fields: dict[str, str],
    *,
    prompt_missing: bool,
    mark_missing: bool,
) -> str:
    """Replace all {{FIELD}} placeholders in text with values from fields."""
    missing: set[str] = set()

    def replacer(match: re.Match) -> str:
        field_name = match.group(1)
        if field_name in fields and fields[field_name]:
            return fields[field_name]
        if prompt_missing:
            value = input(f"  Enter value for [{field_name}]: ").strip()
            if value:
                fields[field_name] = value  # cache for repeated occurrences
                return value
        missing.add(field_name)
        if mark_missing:
            return _UNFILLED_MARKER.format(field_name)
        return match.group(0)  # leave original placeholder

    result = _PLACEHOLDER_RE.sub(replacer, text)

    if missing:
        missing_list = ", ".join(sorted(missing))
        print(
            f"[renderer] Note: {len(missing)} field(s) not filled in: {missing_list}",
            file=sys.stderr,
        )

    return result


# ---------------------------------------------------------------------------
# CLI usage when run directly
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python renderer.py <template_key>  [field=value ...]")
        print("       python renderer.py list")
        sys.exit(1)

    if sys.argv[1] == "list":
        for t in list_templates():
            print(f"  {t['key']}")
        sys.exit(0)

    template_key = sys.argv[1]
    fields: dict[str, str] = {}
    for arg in sys.argv[2:]:
        if "=" in arg:
            k, _, v = arg.partition("=")
            fields[k.strip()] = v.strip()

    print(render_template(template_key, fields, prompt_missing=True))
