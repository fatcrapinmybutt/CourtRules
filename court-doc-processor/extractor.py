"""
extractor.py — Field extraction engine for court documents.

Reads PDF and TXT source files and extracts structured field values
(case number, party names, court, dates, etc.) using the regex patterns
defined in config/field_mappings.json.

Usage (as a module):
    from extractor import extract_fields
    fields = extract_fields("path/to/file.pdf")
    # Returns dict[str, str]
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Optional heavy imports — degrade gracefully if not installed
# ---------------------------------------------------------------------------
try:
    import pdfplumber
    _HAS_PDFPLUMBER = True
except ImportError:
    _HAS_PDFPLUMBER = False

try:
    from pypdf import PdfReader
    _HAS_PYPDF = True
except ImportError:
    _HAS_PYPDF = False

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
CONFIG_PATH = Path(__file__).parent / "config" / "field_mappings.json"

# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def extract_fields(source_path: str | Path, extra_text: str = "") -> dict[str, str]:
    """Extract legal document fields from a PDF or TXT file.

    Args:
        source_path: Path to the source PDF or TXT file.
        extra_text:  Any additional raw text to include in the scan
                     (e.g., text pasted directly by the user).

    Returns:
        A dictionary mapping field names (e.g. "case_number") to extracted
        values.  Fields that could not be extracted are omitted from the
        returned dict (so callers can use .get() with defaults or prompt the
        user to fill in missing values).
    """
    source_path = Path(source_path)
    raw_text = _read_text(source_path) + "\n" + extra_text
    mappings = _load_mappings()
    return _apply_mappings(raw_text, mappings)


def extract_text_only(source_path: str | Path) -> str:
    """Return the raw text content of a PDF or TXT file without any field
    extraction.  Useful for debugging extraction patterns."""
    return _read_text(Path(source_path))


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _read_text(path: Path) -> str:
    """Read raw text from PDF or TXT file."""
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return _read_pdf(path)
    elif suffix == ".rtf":
        # RTF files contain formatting codes that interfere with field
        # extraction.  Warn the user and attempt a best-effort read; for
        # clean results, convert the RTF to plain text first (e.g. with
        # LibreOffice: `libreoffice --headless --convert-to txt input.rtf`).
        print(
            "[extractor] WARNING: RTF files may contain formatting codes that "
            "interfere with extraction.  Convert to .txt first for best results.",
            file=sys.stderr,
        )
        try:
            return path.read_text(errors="replace")
        except Exception:
            return ""
    elif suffix in (".txt", ".md"):
        try:
            return path.read_text(errors="replace")
        except OSError as exc:
            print(f"[extractor] Could not read file {path}: {exc}", file=sys.stderr)
            return ""
    else:
        # Try as plain text for unknown extensions
        try:
            return path.read_text(errors="replace")
        except Exception:
            return ""


def _read_pdf(path: Path) -> str:
    """Extract text from PDF.  Tries pdfplumber first (better layout), then
    falls back to pypdf, then returns an empty string with a warning."""
    if _HAS_PDFPLUMBER:
        try:
            with pdfplumber.open(path) as pdf:
                pages = [page.extract_text() or "" for page in pdf.pages]
            return "\n".join(pages)
        except Exception as exc:
            print(f"[extractor] pdfplumber failed: {exc}. Trying pypdf...",
                  file=sys.stderr)

    if _HAS_PYPDF:
        try:
            reader = PdfReader(str(path))
            pages = []
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    pages.append(text)
            return "\n".join(pages)
        except Exception as exc:
            print(f"[extractor] pypdf failed: {exc}.", file=sys.stderr)

    print(
        "[extractor] WARNING: Neither pdfplumber nor pypdf is available. "
        "Install them with:  pip install pdfplumber pypdf",
        file=sys.stderr,
    )
    return ""


def _load_mappings() -> dict:
    """Load field extraction regex patterns from config/field_mappings.json."""
    if not CONFIG_PATH.exists():
        print(
            f"[extractor] WARNING: Field mappings config not found at {CONFIG_PATH}",
            file=sys.stderr,
        )
        return {}
    with CONFIG_PATH.open() as fh:
        return json.load(fh)


def _apply_mappings(text: str, mappings: dict) -> dict[str, str]:
    """Apply all regex patterns to raw text and return extracted field values."""
    results: dict[str, str] = {}
    for field_name, config in mappings.items():
        patterns = config if isinstance(config, list) else [config]
        for pattern_str in patterns:
            match = re.search(pattern_str, text,
                              re.IGNORECASE | re.MULTILINE | re.DOTALL)
            if match:
                # Use named group "value" if present, otherwise group 1
                try:
                    value = match.group("value").strip()
                except IndexError:
                    try:
                        value = match.group(1).strip()
                    except IndexError:
                        value = match.group(0).strip()
                if value:
                    results[field_name] = value
                    break  # first matching pattern wins
    return results


# ---------------------------------------------------------------------------
# CLI usage when run directly
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extractor.py <path/to/file.pdf|.txt> [--text-only]")
        sys.exit(1)

    path_arg = sys.argv[1]
    if "--text-only" in sys.argv:
        print(_read_text(Path(path_arg)))
    else:
        fields = extract_fields(path_arg)
        for k, v in sorted(fields.items()):
            print(f"{k:35s} = {v!r}")
