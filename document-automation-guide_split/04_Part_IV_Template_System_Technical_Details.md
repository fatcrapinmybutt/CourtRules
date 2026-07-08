## Part IV — Template System: Technical Details

### Placeholder Format

All templates use the `{{field_name}}` placeholder syntax:
```
Case No. {{case_number}}
Hon. {{judge_name}}
{{plaintiff_name}},
    Plaintiff,
```

### How Fields Are Extracted

The extractor in `extractor.py` uses regular expressions from `config/field_mappings.json` to find common patterns:

| Pattern Type | Example |
|---|---|
| Case number | `24-12345-CZ`, `2024-000123-DO` |
| Court name | "Circuit Court for the County of..." |
| Party names | Lines before/after "Plaintiff," "Defendant," |
| Judge name | Lines after "Hon." or "Honorable" |
| Dates | Month Day, Year or MM/DD/YYYY |
| Bar numbers | `P-12345` or `P12345` |
| Dollar amounts | `$75,000.00` |
| Email addresses | Standard email format |

### Adding Custom Templates

1. Create a new `.txt` file in the appropriate directory
2. Use `{{field_name}}` for all variable content
3. Field names should match existing field names in `field_mappings.json` for auto-extraction to work
4. Run `python processor.py list-templates` to verify it is discovered

### Adding Custom Field Patterns

Edit `config/field_mappings.json`:
```json
"my_custom_field": [
    "My Field Label[:\\s]+(?P<value>[A-Za-z0-9 .-]{3,50})"
]
```

---
