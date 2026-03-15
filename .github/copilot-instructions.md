# GitHub Copilot Instructions for CourtRules

## Project Overview

This repository is the authoritative reference implementation for Michigan Court Rules (MCR) and related legal systems. Every file, data structure, script, and piece of documentation must reflect the official language and hierarchy established by the Michigan Supreme Court.

The target audience includes attorneys, clerks, litigants, and legal researchers. Accuracy is non-negotiable. When in doubt, omit rather than invent.

---

## Golden Elite Omega Level Standards

### 1. Legal Accuracy — The Prime Directive

- **Never fabricate** rule numbers, sub-rule letters, statutory citations, or case law references. If you are unsure whether a rule exists, leave a `TODO` with a reference to the official source that must be verified.
- All rule text must be sourced from the **Michigan Supreme Court's official published rules** available at `https://courts.michigan.gov/rules/`.
- When referencing a rule, use the full canonical citation format: `MCR 2.116(C)(10)`, `MRE 803(3)`, `MCL 600.2301`.
- Distinguish clearly between:
  - **MCR** — Michigan Court Rules (procedural)
  - **MRE** — Michigan Rules of Evidence (evidentiary)
  - **MCL** — Michigan Compiled Laws (statutory)
  - **SCAO** — State Court Administrative Office forms and instructions

### 2. Repository Structure

Organize all content according to the official MCR chapter hierarchy:

```
Chapter 1  — General Provisions
Chapter 2  — Civil Procedure
Chapter 3  — Special Proceedings and Actions
Chapter 4  — District Court
Chapter 5  — Probate Court
Chapter 6  — Criminal Procedure
Chapter 7  — Appellate Rules
Chapter 8  — Administrative Rules of Court
Chapter 9  — Professional Disciplinary Proceedings
```

- Each chapter lives in its own directory, named `chapter-N/` (e.g., `chapter-2/`).
- Each rule lives in its own file, named after the rule number: `mcr-2-116.md` or `mcr-2-116.json`.
- Sub-rules are **not** split into separate files; they live within the parent rule file.
- Evidence rules follow the same pattern under `mre/`: e.g., `mre/mre-404.md`.

### 3. File and Content Formatting

#### Markdown files (`.md`)
Every rule file must open with a YAML front matter block:

```yaml
---
rule: MCR 2.116
title: Motion for Summary Disposition
chapter: 2
subchapter: null
effective_date: "2021-01-01"
source: "https://courts.michigan.gov/rules/documents/MCR%202.116.pdf"
---
```

Follow front matter with:
1. `## Rule Text` — verbatim official rule text, quoted or clearly attributed.
2. `## Summary` — plain-language explanation accessible to a layperson.
3. `## Key Provisions` — bulleted list of the most important sub-rules.
4. `## Related Rules` — links to related MCR/MRE/MCL rules.
5. `## Practice Notes` (optional) — procedural tips that do **not** constitute legal advice.

#### JSON / data files (`.json`)
Use the following schema for structured rule data:

```json
{
  "rule": "MCR 2.116",
  "title": "Motion for Summary Disposition",
  "chapter": 2,
  "effective_date": "2021-01-01",
  "source": "https://courts.michigan.gov/rules/documents/MCR%202.116.pdf",
  "text": "...",
  "sub_rules": [
    { "id": "A", "text": "..." },
    { "id": "B", "text": "..." }
  ],
  "related_rules": ["MCR 2.118", "MCR 2.119"]
}
```

### 4. Naming Conventions

| Asset | Convention | Example |
|---|---|---|
| Directories | `kebab-case` | `chapter-2/`, `mre/` |
| Rule content files | `{prefix}-{chapter}-{rule}.{ext}` | `mcr-2-116.md`, `mre-404.json` |
| Scripts / utilities | `kebab-case` | `validate-rules.js`, `build-index.sh` |
| JS/TS variables & functions | `camelCase` | `getRuleById()`, `ruleNumber` |
| JS/TS constants | `UPPER_SNAKE_CASE` | `MAX_CHAPTER_NUMBER` |
| CSS classes | `kebab-case` | `.rule-summary`, `.chapter-header` |

Sub-rule references in code must use the canonical string form: `"MCR 2.116(C)(10)"` — never abbreviate or reorder.

### 5. Code Quality

- Write code as if a judge will read it: precise, well-commented at decision points, and free of ambiguity.
- Prefer **explicit** over implicit. Never rely on type coercion or undocumented behavior.
- Functions must do one thing. If a function validates, parses, *and* formats, split it.
- All public functions and exported constants must have JSDoc / docstring comments that describe purpose, parameters, return value, and any thrown errors.
- Linting rules (ESLint, Prettier, etc.) defined in the repository are **law** — do not suppress them without documented justification.

### 6. Commit Messages

Follow the Conventional Commits specification:

```
<type>(<scope>): <short summary>

<body — optional, wrap at 72 chars>

<footer — optional, references issues/PRs>
```

Types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `style`
Scope: chapter number or system name (e.g., `mcr-2`, `mre`, `scripts`, `ci`)

Examples:
```
docs(mcr-2): add MCR 2.116 summary disposition rule
feat(scripts): add rule schema validator
fix(mre-404): correct sub-rule (b)(2) citation text
```

### 7. Pull Request Standards

Every PR must include:
- **Which rules are affected** — list each `MCR`/`MRE`/`MCL` reference.
- **Source of truth** — a link to the official Michigan Supreme Court document confirming the change.
- **Plain-language summary** — one paragraph a layperson could understand.
- **Breaking change flag** — if any existing rule identifier, schema field, or file path changes.

PRs that add or modify rule text without a verifiable official source **will not be merged**.

### 8. Security and Privacy

- **Zero PII tolerance**: No real names of parties, judges, attorneys, or case numbers anywhere in the repository — not in rule text, examples, tests, fixtures, or comments.
- Use clearly synthetic placeholders in examples: `Plaintiff A`, `Defendant B`, `Case No. XX-XXXX-XX`.
- Never commit credentials, API keys, or tokens.
- All external URLs must use `https://`.
- Dependencies must be reviewed for known vulnerabilities before being added.

### 9. Testing and Validation

- Every automation script must have corresponding tests in a `__tests__/` or `tests/` directory adjacent to the script.
- Tests must cover: valid input, invalid input, boundary values, and missing/null fields.
- A CI check must validate that all rule files conform to the required front matter schema before merging.
- Rule text diffs should be reviewed by a human — automated tests validate structure, not legal accuracy.

### 10. Accessibility and Inclusivity

- All user-facing text must meet WCAG 2.1 AA standards where applicable.
- Avoid legalese in summaries and navigation labels; use Michigan plain-language drafting guidelines.
- Provide alt text for any diagrams or charts depicting court processes.

---

## Quick Reference Cheat Sheet

| Task | Standard |
|---|---|
| Cite a rule | `MCR 2.116(C)(10)` — full canonical form |
| Name a rule file | `mcr-2-116.md` |
| Name a chapter directory | `chapter-2/` |
| Reference statutory law | `MCL 600.2301` |
| Reference evidence rule | `MRE 803(3)` |
| Placeholder party name | `Plaintiff A`, `Defendant B` |
| Placeholder case number | `Case No. XX-XXXX-XX` |
| Commit type for new rule | `docs(mcr-N): ...` |
| Commit type for new feature | `feat(scope): ...` |
