## 3. Directory Structure

```
court-doc-processor/
├── processor.py               ← Main CLI entry point (run this)
├── extractor.py               ← PDF/TXT field extraction engine
├── renderer.py                ← Template rendering engine
├── requirements.txt           ← Python dependencies
├── config/
│   └── field_mappings.json    ← Regex patterns for field extraction
└── templates/
    ├── michigan/
    │   ├── circuit/
    │   │   ├── civil/         ← Circuit court civil documents (17 templates)
    │   │   ├── domestic-relations/ ← Divorce, custody, support (9 templates)
    │   │   ├── criminal/      ← Criminal defense documents (3 templates)
    │   │   └── ppo/           ← Personal protection orders (3 templates)
    │   ├── muskegon/          ← Muskegon County 14th Circuit specific (2 templates)
    │   ├── coa/               ← Michigan Court of Appeals (6 templates)
    │   └── supreme/           ← Michigan Supreme Court (4 templates)
    └── federal/
        ├── western-district/  ← U.S. District Court W.D. Mich. (7 templates)
        └── sixth-circuit/     ← U.S. Court of Appeals 6th Circuit (4 templates)
```

---
