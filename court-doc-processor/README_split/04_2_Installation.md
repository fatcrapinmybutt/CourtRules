## 2. Installation

### System Requirements

- Python 3.8 or later
- pip (Python package manager)
- Internet access (first-time install only)

### Install Steps

```bash
# Step 1: Navigate to the tool directory
cd court-doc-processor

# Step 2: (Recommended) Create a virtual environment
python3 -m venv venv
source venv/bin/activate          # Linux/Mac
venv\Scripts\activate             # Windows

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Verify installation
python processor.py --version
# Output: court-doc-processor, version 1.0.0
```

### Dependencies Installed

| Package | Purpose |
|---|---|
| `pdfplumber` | Extract text from text-based PDFs (primary extractor) |
| `pypdf` | Fallback PDF text extraction |
| `click` | Command-line interface framework |
| `rich` | Rich terminal output (tables, colors, panels) |
| `jinja2` | Template rendering |
| `python-dateutil` | Date parsing from extracted text |

> **Note on Scanned (Image) PDFs:** The tool extracts text from *text-based* PDFs. If your PDF is a scanned image, the extraction will return empty results. In that case, use an OCR tool (such as Adobe Acrobat, ABBYY FineReader, or free online tools) to convert the scanned PDF to searchable text before running the scan command.

---
