## 10. Frequently Asked Questions

**Q: My PDF extracts no fields. What's wrong?**
A: Your PDF may be a scanned image. Use `--text-only` to check: if you see no text, you need OCR conversion first. Try Adobe Acrobat's "Recognize Text" function or a free service like smallpdf.com.

**Q: Some fields are extracted incorrectly. Can I fix them?**
A: Yes. Use `-s FIELD=VALUE` to override any extracted field:
```bash
python processor.py fill michigan/circuit/civil/summons \
    -f extracted_fields.json \
    -s plaintiff_name="Correct Name" \
    --prompt -o output.txt
```

**Q: Can I add my own templates?**
A: Yes. Create a `.txt` file in the appropriate `templates/` subdirectory. Use `{{field_name}}` placeholders. The tool will automatically discover and list it.

**Q: Can I add new field extraction patterns?**
A: Yes. Edit `config/field_mappings.json`. Add a new key with a regex pattern using a named group `(?P<value>...)`. See the existing patterns for examples.

**Q: What's the `--mark-missing` option for?**
A: When enabled (the default), any `{{field_name}}` that was not filled becomes `<<<field_name>>>` in the output. This makes it easy to see what still needs to be filled in your text editor. Use `--no-mark-missing` if you want unfilled fields to remain as-is.

**Q: Can this tool file documents with the court electronically?**
A: No. This tool generates document text for you to review, sign, and file. You must file through the appropriate e-filing system (TrueFiling for Michigan state courts; CM/ECF for federal courts) or by paper.

**Q: Is the output ready to file?**
A: No — always have a licensed Michigan attorney review the completed document before filing. The templates provide structure and include required legal elements, but each case is unique and requires legal judgment.

---

> **For more information on court rules and procedures, see the reference documents in the parent directory:**
> - [Michigan Supreme Court Rules](../michigan-supreme-court-rules.md)
> - [Michigan Court of Appeals Rules](../michigan-court-of-appeals-rules.md)
> - [Federal Western District Rules](../federal-western-district-rules.md)
> - [Litigating Higher Courts Guide](../litigating-higher-courts.md)
