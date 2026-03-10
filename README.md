# CourtRules

A comprehensive Michigan and Federal court rules reference, multi-state case law guide, and **automated court document processor** that scans PDF/TXT files and populates templates for every judicial process in all Michigan jurisdictions.

---

## ⚡ Document Automation Tool

The [`court-doc-processor/`](court-doc-processor/) directory contains a full Python tool that:
- **Scans** PDF and TXT files to extract case information automatically
- **Populates** 44 document templates across all jurisdictions (Muskegon Circuit, COA, Supreme Court, W.D. Mich., 6th Circuit)
- **Covers** civil, domestic relations, criminal, PPO, appellate, and federal documents

```bash
# Quick start
cd court-doc-processor
pip install -r requirements.txt
python processor.py list-templates          # See all 44 templates
python processor.py scan my_case.pdf        # Extract fields from existing doc
python processor.py fill michigan/circuit/civil/summons --prompt   # Fill a template
python processor.py auto my_case.pdf michigan/coa/claim-of-appeal  # One-step
```

**See [document-automation-guide.md](document-automation-guide.md) for the full procedural guide.**
**See [court-doc-processor/README.md](court-doc-processor/README.md) for tool usage instructions.**

---

## Table of Contents

### Michigan Court Rules (MCR)
- [Michigan Supreme Court Rules](michigan-supreme-court-rules.md) — MCR 1–9 complete cascading list
- [Michigan Court of Appeals Rules](michigan-court-of-appeals-rules.md) — MCR 7.200 series, procedures and requirements
- [Michigan Trial Court & General Rules Overview](michigan-trial-court-rules.md) — MCR 2, 3, 4, 5, 6 series

### Federal Courts in Michigan
- [U.S. District Court — Western District of Michigan Local Rules](federal-western-district-rules.md)
- [U.S. District Court — Eastern District of Michigan Local Rules](federal-eastern-district-rules.md)
- [U.S. Court of Appeals — Sixth Circuit Rules](sixth-circuit-rules.md)

### Multi-State Case Law by Topic
- [Parental Alienation — Case Law](caselaw-parental-alienation.md)
- [Malicious Prosecution — Case Law](caselaw-malicious-prosecution.md)
- [Intentional Infliction of Emotional Distress (IIED) — Case Law](caselaw-iied.md)
- [Fraud on the Court — Case Law](caselaw-fraud-on-court.md)
- [Perjury — Case Law](caselaw-perjury.md)

### Litigation Guides
- [Litigating Higher Court Cases: Requirements and Strategy](litigating-higher-courts.md)
- [Document Automation Guide: Procedural Instructions for All Jurisdictions](document-automation-guide.md)

---

> **Disclaimer:** This reference is for educational and informational purposes only and does not constitute legal advice. Court rules change; always verify current rules at official court websites and with a licensed attorney.
