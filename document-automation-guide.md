# Michigan Court Document Automation: Comprehensive Procedural Guide

> **Disclaimer:** This guide is for educational and informational purposes only and does not constitute legal advice. Court rules change frequently; always verify current rules at official court websites. Consult a licensed Michigan attorney before filing any court document.

---

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

## Part II — Michigan State Court Procedures by Jurisdiction

### A. Michigan Circuit Courts — General

Circuit courts are Michigan's general trial courts of unlimited jurisdiction (MCL 600.151). Each county has a circuit court. The **14th Circuit Court** serves Muskegon County.

#### Filing Requirements

| Requirement | Details |
|---|---|
| Filing method | Paper (clerk's office) or e-filing via TrueFiling |
| Case caption | Required on all documents |
| Signature | Attorney's signature + bar number on all papers |
| Service | Must serve opposing party simultaneously; file Proof of Service |
| Fees | Vary by case type and amount (check current fee schedule) |

#### Document Sequence — New Civil Lawsuit

```
1. Summons               ← Issued by clerk; valid 91 days
2. Complaint             ← Filed with summons
3. Muskegon Cover Sheet  ← Muskegon-specific requirement
4. Service               ← Serve summons + complaint on defendant
5. Proof of Service      ← Filed with court within 7 days of service
6. Answer (by defendant) ← Due 21 days after service (MCR 2.108)
7. Scheduling Conference ← Per MCR 2.401
8. Discovery             ← Interrogatories, Requests for Production,
                           Depositions, Requests for Admissions
9. Motion Practice       ← Motions + Briefs + Notices of Hearing
10. Final Pretrial       ← Witness lists, exhibit lists submitted
11. Trial
12. Judgment
```

#### Document Sequence — Domestic Relations (Divorce with Children)

```
1. Complaint for Divorce (with children)
2. Summons
3. UCCJEA Affidavit (required — MCR 3.206(A)(2)(c))
4. Verified Financial Statement (FOC 23 style)
5. Muskegon Cover Sheet
6. Service on Defendant
7. Proof of Service filed
8. Answer by Defendant (21 days after service)
9. FOC Interview / Investigation
10. Temporary Orders hearing (if needed)
    - Temporary custody order
    - Temporary support order
    - Temporary PPO (if domestic violence)
11. Discovery / Financial disclosures
12. Mediation (required in most Michigan circuit courts)
13. Trial / Evidentiary Hearing (if contested)
14. Judgment of Divorce entered
15. Post-judgment enforcement/modification (as needed)
```

#### Document Sequence — PPO (Emergency)

```
1. Petition for PPO (ex parte — emergency)
   - Domestic: petition-ppo-domestic
   - Stalking: petition-ppo-stalking
2. Judge reviews same day (usually within hours)
3. If granted: PPO issued (effective immediately)
4. Service on Respondent (typically by sheriff/process server)
5. Proof of Service filed
6. Respondent may file Motion to Modify/Terminate PPO
7. Hearing within 14 days if respondent files motion
```

---

### B. Muskegon County — 14th Circuit Court Specifics

**Location:**
- 990 Terrace St, Muskegon, MI 49442
- Phone: (231) 724-6251
- Hours: Monday–Friday, 8:00 AM – 5:00 PM
- E-Filing: TrueFiling (https://www.truefiling.com)

**Judges (verify current assignment):**
- Cases assigned to circuit judges by case type and rotation
- Family Division handles domestic relations matters

**Local Practice Notes:**
- **Muskegon Cover Sheet:** Required for new case filings (use `michigan/muskegon/local-cover-sheet`)
- **Scheduling:** Request scheduling conference using `michigan/muskegon/muskegon-scheduling-order-request`
- **FOC (Friend of the Court):** Office at same address; mandatory FOC involvement in all domestic relations matters
- **ADR:** Muskegon encourages mediation; check current local ADR requirements

---

### C. Michigan Court of Appeals (COA)

**Location:** Hall of Justice, 925 W. Ottawa, Lansing, MI 48909 (primary)
**Also:** Detroit, Grand Rapids, Troy
**Phone:** (517) 373-0786
**E-Filing:** TrueFiling

#### Appeal of Right vs. Application for Leave

| Type | When Available | Deadline | Documents |
|---|---|---|---|
| **Claim of Appeal (MCR 7.203(A))** | From final judgments; criminal convictions; certain enumerated orders | **21 days** from order | `claim-of-appeal` |
| **Application for Leave (MCR 7.203(B))** | All other orders; interlocutory appeals | **21 days** from order (up to 12 months with good cause) | `application-leave-appeal` |

#### COA Briefing Schedule (MCR 7.210)

```
Day 0:    Claim of Appeal / Application filed
Day 0-7:  Order transcript (if needed) — MCR 7.204(F)
Day 56:   Appellant's Brief due
Day 91:   Appellee's Brief due
Day 112:  Optional Reply Brief due (max 10 pages / 3,200 words)
Day 90+:  Oral argument (if scheduled) or submission on briefs
Day ???:  COA issues opinion (published or unpublished)
Day +21:  Deadline for Motion for Reconsideration (MCR 7.217)
Day +56:  Deadline for Application to Michigan Supreme Court
```

#### COA Brief Requirements (MCR 7.212(B))

- **Page limit:** 50 pages (or 16,000 words)
- **Reply brief:** 10 pages (or 3,200 words)
- **Font:** At least 12-point, double-spaced (or 13-point, 1.5-spaced)
- **Margins:** 1 inch all sides
- **Required sections:** Table of contents, index of authorities, statement regarding oral argument, jurisdictional statement, questions presented, statement of facts, standard of review, argument, conclusion, certificate of compliance

---

### D. Michigan Supreme Court

**Location:** Hall of Justice, 925 W. Ottawa, Lansing, MI 48909
**Phone:** (517) 373-0120

#### Application for Leave to Appeal (MCR 7.302)

**Deadline:** 56 days from COA decision

**Grounds for granting leave (MCR 7.302(D)):**
1. COA decision conflicts with a Supreme Court opinion
2. COA decision conflicts with another published COA opinion
3. Issue involves significant question of public interest
4. Issue involves substantial departure from law
5. Issue involves significant constitutional question

**Brief Requirements:** Same as COA briefs; 50 pages maximum

#### Bypass Application (MCR 7.304)

Allows bypassing the COA entirely and going directly to the Supreme Court from the circuit court. Reserved for cases of exceptional public importance.

**Deadline:** 42 days from final circuit court judgment

---

## Part III — Federal Court Procedures

### E. U.S. District Court — Western District of Michigan

**Grand Rapids (Southern Division):**
- 110 Michigan St. NW, Grand Rapids, MI 49503
- Phone: (616) 456-2381

**Marquette (Northern Division):**
- 202 W. Washington St., Marquette, MI 49855

**Kalamazoo Division:**
- 410 W. Michigan Ave., Kalamazoo, MI 49007

**E-Filing:** CM/ECF (https://www.miwd.uscourts.gov)

#### Federal Civil Lawsuit — Document Sequence

```
1. Civil Complaint (1983 or diversity)
2. Civil Cover Sheet (JS-44)
3. IFP Motion (if unable to pay $405 filing fee)
4. Summons issued by clerk
5. Service on defendant (within 90 days — FRCP 4(m))
6. Answer by defendant (21 days — FRCP 12(a))
7. Rule 26(f) Conference (within 21 days of defendant's appearance)
8. Rule 26(a)(1) Initial Disclosures (within 14 days of Rule 26(f) conference)
9. Scheduling Order (entered by Court)
10. Discovery (FRCP 26-37; LCivR 37.1)
11. Motion practice (LCivR 7.1 — concurrence requirement)
12. Summary Judgment briefing (if applicable)
13. Final Pretrial Conference + Order
14. Trial
15. Judgment
16. Notice of Appeal (within 30 days — FRAP 4(a)(1))
```

#### Western District Local Rules — Key Requirements

- **Concurrence:** Before filing any motion, must contact opposing counsel; state concurrence status in motion (LCivR 7.1(a))
- **Brief length:** Principal briefs ≤ 25 pages; reply briefs ≤ 10 pages (LCivR 7.3)
- **E-filing:** Required for attorneys; optional for pro se parties
- **Pro se:** Self-represented litigants may file paper documents at clerk's office
- **IFP screening:** If IFP granted, complaint screened under 28 U.S.C. § 1915A before service

---

### F. U.S. Court of Appeals — Sixth Circuit

**Location:** Potter Stewart U.S. Courthouse, 100 E. Fifth St., Cincinnati, OH 45202
**Website:** www.ca6.uscourts.gov
**CM/ECF E-Filing:** Required for attorneys

#### Notice of Appeal — Filing Location

File the Notice of Appeal at the **District Court Clerk's Office**, not the Sixth Circuit. The District Court sends the record to the Sixth Circuit.

#### Sixth Circuit Briefing Schedule (FRAP 31; 6 Cir. R. 31)

```
Day 0:    Notice of Appeal filed with District Court
Day 0-14: Order transcript (criminal: FRAP 10(b)(1))
Day ???:  Sixth Circuit dockets appeal; issues briefing schedule
Day +40:  Appellant's Brief due (from record docketed date)
Day +70:  Appellee's Brief due
Day +91:  Reply Brief due (optional)
Day ???:  Oral argument (if not waived)
Day ???:  Panel opinion issued
Day +45:  En banc petition deadline
```

#### Brief Requirements (6 Cir. R. 32; FRAP 32)

- **Word limit:** 13,000 words (principal briefs); 6,500 words (reply)
- **Font:** 14-point proportionally spaced or 12-point monospaced
- **Margins:** 1 inch all sides
- **Cover color:** Blue (appellant); red (appellee); grey (reply)
- **Required:** Corporate Disclosure Statement (6 Cir. R. 26.1)

#### Mediation Program

The Sixth Circuit operates a mandatory mediation program. Shortly after docketing, cases involving money, contracts, civil rights, or employment are typically referred to mediation. Participation is required.

---

### G. United States Supreme Court

**Location:** 1 First St. NE, Washington, DC 20543
**Phone:** (202) 479-3011

#### Certiorari Requirements (Supreme Court Rules 10–14)

**Deadline:** 90 days from Sixth Circuit judgment (28 U.S.C. § 2101(c))

**Grounds for certiorari (Rule 10):**
1. Circuit split — Sixth Circuit decision conflicts with another circuit
2. State court decision conflicts with federal court decision
3. Important federal question not yet settled by Supreme Court
4. Significant departure from accepted norms of judicial proceedings

**Format (Rule 33):**
- **Paid:** Booklet format, 6⅛" × 9¼", 40 pages max, black cover
- **IFP (Rule 39):** 8½" × 11", 40 pages max, double-spaced
- Filing fee: $300 (waived for IFP)

**Brief on merits (if certiorari granted):**
- Petitioner's brief: 15,000 words
- Respondent's brief: 15,000 words
- Reply: 6,000 words
- Oral argument: 30 minutes per side

---

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

## Part V — Important Deadlines Summary

| Court | Action | Deadline |
|---|---|---|
| Circuit Court (Civil) | Serve defendant | 91 days from summons issuance (MCR 2.102) |
| Circuit Court (Civil) | Defendant answers | 21 days after service (MCR 2.108) |
| Circuit Court | Respond to interrogatories | 28 days after service (MCR 2.309) |
| Michigan COA | Claim of Appeal | **21 days** from final order (MCR 7.204) |
| Michigan COA | Application for Leave | **21 days** from interlocutory order (MCR 7.205) |
| Michigan COA | Appellant's Brief | 56 days from claim/leave filed |
| Michigan COA | Reconsideration | 21 days from COA opinion (MCR 7.217) |
| Michigan Supreme Court | Application from COA | **56 days** from COA decision (MCR 7.305) |
| Michigan Supreme Court | Bypass from circuit | **42 days** from circuit judgment (MCR 7.304) |
| Federal District Court | Serve defendant | 90 days from filing (FRCP 4(m)) |
| Federal District Court | Defendant answers | 21 days after service (FRCP 12(a)) |
| Sixth Circuit | Notice of Appeal (civil) | **30 days** from judgment (FRAP 4(a)) |
| Sixth Circuit | Notice of Appeal (criminal) | **14 days** from judgment (FRAP 4(b)) |
| Sixth Circuit | Appellant's Brief | 40 days from record docketed (FRAP 31) |
| U.S. Supreme Court | Certiorari Petition | **90 days** from Sixth Circuit judgment |

---

> **Always verify deadlines with current court rules and with a licensed attorney. Missed deadlines can result in permanent loss of rights.**
