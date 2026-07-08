## 5. Step-by-Step: Scan a Source Document

### When to Use

Use the `scan` command when you already have an existing court document (a prior order, a complaint you received, a case file) and want to extract the key fields automatically to pre-populate templates.

### Command Syntax

```bash
python processor.py scan <FILE> [OPTIONS]
```

### Options

| Option | Description |
|---|---|
| `--text-only` | Print raw extracted text without field parsing (for debugging) |
| `--output FILE` | Save extracted fields to a JSON file for later use |

### Step-by-Step Procedure

**Step 1:** Obtain the source document as a PDF or TXT file.

**Step 2:** If the PDF is a scanned image (not text-searchable), first convert it using OCR:
   - Use Adobe Acrobat: File → Save As → PDF (OCR option)
   - Use free tool: smallpdf.com, ilovepdf.com, or ABBYY FineReader
   - Command line: `ocrmypdf input.pdf output.pdf`

**Step 3:** Run the scan command:
```bash
python processor.py scan /path/to/complaint.pdf
```

**Step 4:** Review the extracted fields table. Verify accuracy.

**Step 5:** Save extracted fields to JSON for reuse:
```bash
python processor.py scan complaint.pdf --output case_fields.json
```

**Step 6:** If extraction missed some fields, you can view raw text to diagnose:
```bash
python processor.py scan complaint.pdf --text-only > raw_text.txt
```

### What Gets Extracted

The scanner looks for:
- `case_number` — Pattern: `24-12345-CZ`, `2024-000123-DO`, etc.
- `court_name` — "Circuit Court for the County of Muskegon", etc.
- `county` — The county name
- `plaintiff_name` / `defendant_name` — Party names from caption
- `judge_name` — Assigned judge
- `plaintiff_attorney_name` / `plaintiff_attorney_bar` — Attorney info
- `filing_date` — Date the document was filed
- `hearing_date` / `hearing_time` / `hearing_location` — Scheduled hearings
- `amount_claimed` — Dollar amounts in dispute
- `marriage_date` / `separation_date` — Domestic relations dates
- `minor_children` — Names/ages of children
- `property_address` — Real property descriptions
- `support_amount` — Support obligation amounts
- `conviction` / `sentence_imposed` — Criminal case details

---
