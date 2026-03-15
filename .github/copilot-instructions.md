# GitHub Copilot Instructions for CourtRules

## Project Overview
This repository contains a comprehensive list of Michigan Court Rules and related legal systems. It serves as an authoritative reference for Michigan court procedures, rules, and requirements.

## Golden Elite Omega Level Standards

### Code Quality
- Write clean, precise, and well-documented code befitting a court of law.
- All logic must be unambiguous — like a court order, every instruction must leave no room for misinterpretation.
- Follow existing conventions in the repository without deviation.
- Prefer clarity over cleverness; the law is clear, so should your code be.

### Legal Domain Context
- This project deals with Michigan Court Rules. Always treat legal content with accuracy and precision.
- When generating or editing court rule content, verify that terminology matches official Michigan Court Rule language.
- Never invent or fabricate legal rule numbers, citations, or statutory references.
- Cross-reference Michigan Court Rules (MCR) and Michigan Rules of Evidence (MRE) when relevant.

### Documentation
- Every public-facing piece of content should be documented clearly enough that a layperson could understand it.
- Use plain language where possible, while retaining necessary legal terminology.
- Include citations to official sources (e.g., MCR 1.101, MRE 404) when referencing specific rules.

### Naming Conventions
- Use descriptive, unambiguous names for files, variables, and functions.
- Prefer `kebab-case` for file names and `camelCase` for variables/functions in scripts.
- Rule-related identifiers should mirror official rule designations (e.g., `mcr-2-116`, `mre-404`).

### Structure and Organization
- Organize court rules by their official chapter/part structure as defined by the Michigan Supreme Court.
- Group related rules together; do not scatter related concepts across unrelated locations.
- Maintain a clear, hierarchical structure that mirrors the official court rules hierarchy.

### Contribution Standards
- All changes must be traceable to an official Michigan Court Rule source.
- Pull requests must include a description of which rule(s) are affected and why the change is needed.
- Breaking changes to existing rule structures require explicit justification.

### Security and Privacy
- Never include personally identifiable information (PII) in rule content or examples.
- Do not include real case numbers, party names, or judge names in example content.
- Treat all content as public-facing; write accordingly.

### Testing and Validation
- When scripts or automation are added, include tests that validate rule parsing and structure.
- Ensure any generated outputs match official Michigan Court Rule formatting.
