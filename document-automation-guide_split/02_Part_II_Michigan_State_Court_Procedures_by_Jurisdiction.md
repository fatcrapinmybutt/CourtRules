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
