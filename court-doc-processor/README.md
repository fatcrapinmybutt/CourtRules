# Michigan Court Document Automation Guide
## Step-by-Step Procedural Instructions for Scanning, Extracting, and Populating Court Document Templates

> **Disclaimer:** This tool is for educational and organizational purposes only and does not constitute legal advice. Always verify documents with a licensed Michigan attorney before filing.

---

## Table of Contents

1. [Quick Start](#1-quick-start)
2. [Installation](#2-installation)
3. [Directory Structure](#3-directory-structure)
4. [All Available Templates](#4-all-available-templates)
5. [Step-by-Step: Scan a Source Document](#5-step-by-step-scan-a-source-document)
6. [Step-by-Step: Fill a Template](#6-step-by-step-fill-a-template)
7. [Step-by-Step: Auto Mode (Scan + Fill)](#7-step-by-step-auto-mode-scan--fill)
8. [Field Reference — All Placeholders Explained](#8-field-reference--all-placeholders-explained)
9. [Jurisdiction-by-Jurisdiction Filing Checklists](#9-jurisdiction-by-jurisdiction-filing-checklists)
10. [Frequently Asked Questions](#10-frequently-asked-questions)

---

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

## 4. All Available Templates

### Michigan Circuit Court — Civil (17 templates)
| Template Key | Document | Rule |
|---|---|---|
| `michigan/circuit/civil/summons` | Summons | MCR 2.102 |
| `michigan/circuit/civil/complaint-general` | General Complaint | MCR 2.111 |
| `michigan/circuit/civil/answer` | Answer with Affirmative Defenses | MCR 2.111 |
| `michigan/circuit/civil/motion-general` | General Motion | MCR 2.119 |
| `michigan/circuit/civil/brief-support-motion` | Brief in Support of Motion | MCR 2.119 |
| `michigan/circuit/civil/notice-hearing` | Notice of Hearing | MCR 2.119 |
| `michigan/circuit/civil/proposed-order` | Proposed Order | MCR 2.602 |
| `michigan/circuit/civil/judgment` | Judgment | MCR 2.601 |
| `michigan/circuit/civil/affidavit` | Affidavit | MCR 2.119 |
| `michigan/circuit/civil/default` | Request for Entry of Default | MCR 2.603(A) |
| `michigan/circuit/civil/default-judgment` | Motion for Default Judgment | MCR 2.603(B) |
| `michigan/circuit/civil/proof-of-service` | Proof of Service | MCR 2.104 |
| `michigan/circuit/civil/interrogatories` | Interrogatories | MCR 2.309 |
| `michigan/circuit/civil/request-for-production` | Request for Production | MCR 2.310 |
| `michigan/circuit/civil/request-for-admissions` | Requests for Admission | MCR 2.312 |
| `michigan/circuit/civil/notice-of-deposition` | Notice of Deposition | MCR 2.306(B) |
| `michigan/circuit/civil/subpoena` | Subpoena (Duces Tecum / Ad Testificandum) | MCR 2.506 |

### Michigan Circuit Court — Domestic Relations (9 templates)
| Template Key | Document | Rule |
|---|---|---|
| `michigan/circuit/domestic-relations/complaint-divorce-no-children` | Complaint for Divorce (no children) | MCR 3.206 |
| `michigan/circuit/domestic-relations/complaint-divorce-with-children` | Complaint for Divorce (with children) | MCR 3.206 |
| `michigan/circuit/domestic-relations/motion-custody` | Motion Regarding Custody | MCR 3.212 |
| `michigan/circuit/domestic-relations/motion-parenting-time` | Motion Regarding Parenting Time | MCR 3.212 |
| `michigan/circuit/domestic-relations/motion-support-modification` | Motion to Modify Support | MCR 3.212 |
| `michigan/circuit/domestic-relations/uccjea-affidavit` | UCCJEA Affidavit | MCL 722.1209 |
| `michigan/circuit/domestic-relations/verified-financial-statement` | Verified Financial Statement | MCR 3.213 |
| `michigan/circuit/domestic-relations/judgment-divorce` | Judgment of Divorce | MCR 3.211 |
| `michigan/circuit/domestic-relations/motion-post-judgment` | Post-Judgment Motion | MCR 3.212 |

### Michigan Circuit Court — Criminal Defense (3 templates)
| Template Key | Document | Rule |
|---|---|---|
| `michigan/circuit/criminal/motion-suppress` | Motion to Suppress Evidence | MCR 6.110 |
| `michigan/circuit/criminal/motion-dismiss-criminal` | Motion to Dismiss | MCR 6.110 |
| `michigan/circuit/criminal/sentencing-memorandum` | Sentencing Memorandum | MCR 6.425 |

### Michigan Circuit Court — PPO (3 templates)
| Template Key | Document | Rule |
|---|---|---|
| `michigan/circuit/ppo/petition-ppo-domestic` | Petition for PPO (Domestic) | MCR 3.310 |
| `michigan/circuit/ppo/petition-ppo-stalking` | Petition for PPO (Stalking) | MCR 3.310 |
| `michigan/circuit/ppo/motion-modify-terminate-ppo` | Motion to Modify/Terminate PPO | MCR 3.310(C) |

### Muskegon County — 14th Circuit (2 templates)
| Template Key | Document |
|---|---|
| `michigan/muskegon/local-cover-sheet` | Muskegon County Case Cover Sheet |
| `michigan/muskegon/muskegon-scheduling-order-request` | Request for Scheduling Conference |

### Michigan Court of Appeals (6 templates)
| Template Key | Document | Rule |
|---|---|---|
| `michigan/coa/claim-of-appeal` | Claim of Appeal | MCR 7.204 |
| `michigan/coa/application-leave-appeal` | Application for Leave to Appeal | MCR 7.205 |
| `michigan/coa/appellant-brief` | Appellant's Brief | MCR 7.210 |
| `michigan/coa/appellee-brief` | Appellee's Brief | MCR 7.210 |
| `michigan/coa/reply-brief` | Reply Brief | MCR 7.210(B)(3) |
| `michigan/coa/motion-reconsideration-coa` | Motion for Reconsideration | MCR 7.217 |

### Michigan Supreme Court (4 templates)
| Template Key | Document | Rule |
|---|---|---|
| `michigan/supreme/application-leave-appeal-sc` | Application for Leave to Appeal | MCR 7.302 |
| `michigan/supreme/bypass-application` | Application for Bypass of COA | MCR 7.304 |
| `michigan/supreme/brief-on-merits` | Brief on Merits | MCR 7.306 |
| `michigan/supreme/motion-reconsideration-sc` | Motion for Reconsideration | MCR 7.309 |

### Federal — Western District of Michigan (7 templates)
| Template Key | Document | Rule |
|---|---|---|
| `federal/western-district/civil-complaint-1983` | § 1983 Civil Rights Complaint | 42 U.S.C. § 1983 |
| `federal/western-district/civil-complaint-diversity` | Diversity Jurisdiction Complaint | 28 U.S.C. § 1332 |
| `federal/western-district/civil-cover-sheet-js44` | Civil Cover Sheet (JS-44) | LCivR 3.1 |
| `federal/western-district/ifp-motion` | Motion to Proceed In Forma Pauperis | 28 U.S.C. § 1915 |
| `federal/western-district/motion-federal` | Federal Court Motion | LCivR 7.1 |
| `federal/western-district/notice-of-appeal-federal` | Notice of Appeal | FRAP 3 |
| `federal/western-district/certificate-of-appealability` | Application for COA | 28 U.S.C. § 2253 |

### Federal — Sixth Circuit (4 templates)
| Template Key | Document | Rule |
|---|---|---|
| `federal/sixth-circuit/brief-appellant-6th-cir` | Appellant's Brief | 6 Cir. R. 28 |
| `federal/sixth-circuit/brief-appellee-6th-cir` | Appellee's Brief | 6 Cir. R. 28 |
| `federal/sixth-circuit/reply-brief-6th-cir` | Reply Brief | 6 Cir. R. 28 |
| `federal/sixth-circuit/petition-certiorari` | Petition for Certiorari (SCOTUS) | Sup. Ct. R. 14 |

---

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

## 7. Step-by-Step: Auto Mode (Scan + Fill)

### When to Use

Use the `auto` command for the most streamlined workflow: provide a source document and a target template in one command.

### Command Syntax

```bash
python processor.py auto <SOURCE_FILE> <TEMPLATE_KEY> [OPTIONS]
```

### Step-by-Step Procedure

```bash
# Example: Received a complaint, need to draft an answer

# Step 1: Auto-extract and fill the answer template
python processor.py auto \
    received_complaint.pdf \
    michigan/circuit/civil/answer \
    --prompt \
    -o draft_answer.txt

# Example: Have a prior divorce judgment, need to file a custody modification
python processor.py auto \
    existing_judgment.pdf \
    michigan/circuit/domestic-relations/motion-custody \
    --prompt \
    -o motion_custody_draft.txt
```

**Step 1:** Run the auto command with `--prompt` so you are asked for any fields not extracted.

**Step 2:** Answer each prompt. Press Enter to skip (field will be marked `<<<...>>>`).

**Step 3:** Review the output file.

**Step 4:** Edit remaining `<<<FIELD_NAME>>>` markers in your text editor.

**Step 5:** Have the document reviewed by a licensed attorney before filing.

---

## 8. Field Reference — All Placeholders Explained

| Field Name | Description | Example Value |
|---|---|---|
| `case_number` | Court case number | `24-12345-CZ` |
| `court_name` | Full court name | `Circuit Court for the County of Muskegon` |
| `county` | County name | `Muskegon` |
| `division` | Federal court division | `Southern Division` |
| `plaintiff_name` | Plaintiff's full name | `Sarah Johnson` |
| `defendant_name` | Defendant's full name | `ABC Corporation` |
| `judge_name` | Assigned judge | `Hon. Timothy Burns` |
| `filing_date` | Date of filing | `March 10, 2026` |
| `hearing_date` | Hearing date | `April 15, 2026` |
| `hearing_time` | Hearing time | `9:00 a.m.` |
| `hearing_location` | Courtroom/building | `Courtroom 3, 990 Terrace St` |
| `plaintiff_attorney_name` | Plaintiff's attorney | `Robert Davis` |
| `plaintiff_attorney_bar` | Michigan bar number | `P56789` |
| `defendant_attorney_name` | Defendant's attorney | `Jane Smith` |
| `defendant_attorney_bar` | Defense bar number | `P99999` |
| `attorney_firm` | Law firm name | `Davis Law Firm PLLC` |
| `attorney_address` | Attorney's address | `100 W. Western Ave, Muskegon, MI 49440` |
| `attorney_phone` | Attorney's phone | `(231) 555-7890` |
| `attorney_email` | Attorney's email | `rdavis@davis.com` |
| `cause_of_action` | Type of claim | `Breach of Contract` |
| `amount_claimed` | Dollar amount | `$75,000` |
| `motion_type` | Motion type phrase | `FOR SUMMARY DISPOSITION` |
| `motion_subject` | Subject of motion | `Summary Disposition Under MCR 2.116(C)(10)` |
| `moving_party` | Party filing motion | `Plaintiff` |
| `relief_sought` | Relief requested | `granting summary disposition` |
| `marriage_date` | Date of marriage | `June 15, 2010` |
| `separation_date` | Date of separation | `January 1, 2023` |
| `child_1_name` / `child_1_dob` | First child's info | `Emma Johnson` / `March 5, 2015` |
| `custody_arrangement` | Custody type | `Joint legal and physical custody` |
| `parenting_time_schedule` | Parenting time details | `Every other week, Wed overnights...` |
| `support_amount` | Support amount | `$850` |
| `judgment_amount` | Judgment dollar amount | `45,000.00` |
| `coa_case_number` | COA assigned number | `367890` |
| `lower_court_case_number` | Trial court case number | `24-12345-CZ` |
| `sc_case_number` | Supreme Court number | `SC 168001` |
| `conviction` | Criminal conviction | `Assault, MCL 750.81` |
| `sentence_imposed` | Criminal sentence | `18 months probation` |

---

## 9. Jurisdiction-by-Jurisdiction Filing Checklists

### Michigan Circuit Court — Muskegon County (14th Circuit)

**Filing a New Civil Case:**
- [ ] Complete Complaint using `complaint-general` template
- [ ] Complete Summons using `summons` template
- [ ] Complete Muskegon Cover Sheet using `muskegon/local-cover-sheet` template
- [ ] File at: 990 Terrace St, Muskegon, MI 49442
- [ ] Pay filing fee (varies by amount in controversy — check current schedule)
- [ ] Serve Summons and Complaint within 91 days (MCR 2.102)
- [ ] File Proof of Service using `proof-of-service` template

**Filing a Divorce with Minor Children:**
- [ ] Complaint for Divorce: `complaint-divorce-with-children`
- [ ] Summons: `summons`
- [ ] UCCJEA Affidavit: `uccjea-affidavit`
- [ ] Verified Financial Statement: `verified-financial-statement`
- [ ] Muskegon Cover Sheet: `muskegon/local-cover-sheet`
- [ ] File with Muskegon County Circuit Court — Family Division
- [ ] Pay filing fee
- [ ] Serve Defendant
- [ ] Proof of Service filed
- [ ] Await FOC investigation / scheduling order

**Filing a Post-Judgment Custody Motion:**
- [ ] Motion: `motion-custody`
- [ ] Brief in Support: `brief-support-motion`
- [ ] Notice of Hearing: `notice-hearing`
- [ ] Serve on opposing party
- [ ] File with Muskegon Circuit Court
- [ ] Attend hearing (FOC referee or circuit judge)
- [ ] Submit Proposed Order: `proposed-order`

**Filing a PPO:**
- [ ] Petition for PPO: `petition-ppo-domestic` or `petition-ppo-stalking`
- [ ] File with Circuit Court Clerk (emergency — same day)
- [ ] Judge reviews ex parte (typically within 24 hours)
- [ ] If granted: serve on Respondent
- [ ] Proof of Service filed

---

### Michigan Court of Appeals

**Filing an Appeal of Right (Civil):**
- [ ] **Day 1 (within 21 days of order):** File `claim-of-appeal` with trial court clerk
- [ ] **Day 1–7:** Order transcript from court reporter (MCR 7.204(F))
- [ ] Pay COA filing fee ($375)
- [ ] Receive COA case number
- [ ] **Day 56 (after claim filed):** File `appellant-brief`
- [ ] **Day 91:** Appellee files `appellee-brief`
- [ ] **Day 112:** File optional `reply-brief`
- [ ] Await scheduling for oral argument or submission
- [ ] COA issues published or unpublished opinion
- [ ] If needed: file `motion-reconsideration-coa` within 21 days

**Filing an Application for Leave (Interlocutory):**
- [ ] File `application-leave-appeal` within 21 days of interlocutory order
- [ ] Include copy of order as appendix
- [ ] Pay filing fee
- [ ] Await COA response (grant, deny, or peremptory disposition)

---

### Michigan Supreme Court

**Application for Leave to Appeal from COA:**
- [ ] **Within 56 days of COA decision:** File `application-leave-appeal-sc`
- [ ] Include COA opinion as appendix
- [ ] Include trial court judgment
- [ ] Identify grounds (MCR 7.302(D)): conflict, public interest, constitutional question
- [ ] Opposing party has 28 days to respond
- [ ] Await Supreme Court order granting/denying leave
- [ ] If granted: submit `brief-on-merits` per Court's briefing schedule
- [ ] If denied: consider petition for certiorari to U.S. Supreme Court (if federal question)

---

### Federal Court — Western District of Michigan

**Filing a Federal Complaint:**
- [ ] Complete `civil-complaint-1983` (§ 1983) or `civil-complaint-diversity`
- [ ] Complete `civil-cover-sheet-js44`
- [ ] If unable to pay filing fee: complete `ifp-motion`
- [ ] File via CM/ECF (www.miwd.uscourts.gov) or paper (pro se)
- [ ] Pay $405 filing fee (or IFP waiver)
- [ ] Complete Rule 26(f) conference within 21 days of defendant's appearance
- [ ] Submit proposed scheduling order

**Filing a Federal Motion:**
- [ ] Complete `motion-federal`
- [ ] Seek concurrence from opposing counsel (LCivR 7.1(a))
- [ ] State concurrence status in motion
- [ ] File via CM/ECF
- [ ] Await response (21 days) then reply (14 days)

**Federal Appeal to Sixth Circuit:**
- [ ] **Within 30 days of final judgment:** File `notice-of-appeal-federal`
- [ ] File with District Court Clerk (not Sixth Circuit)
- [ ] Pay $505 filing fee to District Court
- [ ] Order transcript within 14 days
- [ ] **Day 40 (after record docketed in 6th Cir.):** File `brief-appellant-6th-cir`
- [ ] **Day 70:** Appellee files `brief-appellee-6th-cir`
- [ ] **Day 91:** File optional `reply-brief-6th-cir`
- [ ] Participate in Sixth Circuit mediation program if invited
- [ ] Await oral argument scheduling

**Certiorari to U.S. Supreme Court:**
- [ ] **Within 90 days of Sixth Circuit judgment:** File `petition-certiorari`
- [ ] File with U.S. Supreme Court Clerk, 1 First St. NE, Washington, DC 20543
- [ ] Pay $300 filing fee or file IFP application (Rule 39)
- [ ] Await response (grant rate ~1-2%)

---

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
