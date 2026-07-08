## 1. Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# List all available templates
python processor.py list-templates

# Scan an existing document to extract case info
python processor.py scan my_document.pdf

# Fill a template manually (prompts for missing fields)
python processor.py fill michigan/circuit/civil/summons --prompt

# One-step: scan + fill in one command
python processor.py auto my_complaint.pdf michigan/circuit/civil/answer --prompt
```

---
