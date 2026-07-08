## Part I — The Document Automation System

### What This Tool Does

The `court-doc-processor/` directory contains a Python tool that:

1. **Scans** existing PDF and TXT court documents to automatically extract case information (case number, party names, attorney info, dates, court name, etc.)
2. **Matches** extracted fields to template placeholders
3. **Populates** 44 document templates across all Michigan and federal jurisdictions with the extracted (and manually entered) data
4. **Outputs** completed draft documents ready for attorney review and filing

### The Two-Step Workflow

```
STEP 1: SCAN                           STEP 2: FILL
┌──────────────────────┐               ┌─────────────────────────┐
│  Source Document     │               │  Template               │
│  (PDF or TXT)        │──EXTRACT──►  │  {{case_number}}        │
│                      │  fields       │  {{plaintiff_name}}     │
│  Existing complaint, │               │  {{judge_name}}         │
│  court order, case   │               │  {{filing_date}}        │
│  info sheet, etc.    │               │  ...                    │
└──────────────────────┘               └──────────┬──────────────┘
                                                   │ RENDER
                                                   ▼
                                       ┌─────────────────────────┐
                                       │  Completed Draft        │
                                       │  Document               │
                                       │  (ready for attorney    │
                                       │  review + filing)       │
                                       └─────────────────────────┘
```

---
