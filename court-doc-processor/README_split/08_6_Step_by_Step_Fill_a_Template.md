## 6. Step-by-Step: Fill a Template

### When to Use

Use the `fill` command when you want to render a specific template, either using fields from a JSON file (from a previous `scan`) or by entering values manually.

### Command Syntax

```bash
python processor.py fill <TEMPLATE_KEY> [OPTIONS]
```

### Options

| Option | Description |
|---|---|
| `-f FILE` | Load fields from a JSON file (output of `scan --output`) |
| `-s FIELD=VALUE` | Set a specific field value directly |
| `--prompt` | Interactively prompt for any unfilled fields |
| `-o FILE` | Write output to a file instead of printing to screen |
| `--mark-missing` | Mark unfilled fields as `<<<FIELD_NAME>>>` (default: on) |
| `--no-mark-missing` | Do not mark unfilled fields |

### Step-by-Step Procedure

**Step 1:** Identify the template you need:
```bash
python processor.py list-templates
python processor.py list-templates --search custody  # search by keyword
```

**Step 2:** See what fields the template requires:
```bash
python processor.py fields michigan/circuit/civil/summons
```

**Step 3a:** Fill using previously scanned fields + prompts for missing ones:
```bash
python processor.py fill michigan/circuit/civil/summons \
    -f case_fields.json \
    --prompt \
    -o output_summons.txt
```

**Step 3b:** Fill by providing all values on the command line:
```bash
python processor.py fill michigan/circuit/civil/summons \
    -s case_number="24-12345-CZ" \
    -s county="Muskegon" \
    -s judge_name="Hon. Timothy Burns" \
    -s plaintiff_name="Sarah Johnson" \
    -s defendant_name="ABC Corp" \
    -s filing_date="March 10, 2026" \
    -s plaintiff_attorney_name="Robert Davis" \
    -s attorney_firm="Davis Law Firm PLLC" \
    -s attorney_address="100 W. Western Ave, Muskegon, MI 49440" \
    -s attorney_phone="(231) 555-7890" \
    -s attorney_email="rdavis@davis.com" \
    -s plaintiff_attorney_bar="P56789" \
    -s court_address="990 Terrace St, Muskegon, MI 49442" \
    -o summons_output.txt
```

**Step 4:** Review the output file. All unfilled fields show as `<<<FIELD_NAME>>>`.

**Step 5:** Either re-run with the missing fields added, or edit the output file directly to fill in remaining `<<<...>>>` markers.

**Step 6:** Print or save the completed document.

---
