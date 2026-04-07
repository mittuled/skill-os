# Scoring Rubric: compliance-ga-reviewer-legal

Evaluates the completeness of a GA compliance review covering checklist assembly, implementation verification, gap remediation, and legal sign-off rigour.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Checklist Completeness | 25% | Coverage of all applicable regulatory requirements from prior scans, PRD NFRs, and newly enacted regulations |
| 2 | Implementation Verification | 30% | Rigour of verifying actual product implementation against each compliance requirement with evidence |
| 3 | Gap Classification | 25% | Quality of gap severity classification (hard blocker vs. soft blocker) with remediation tracking |
| 4 | Sign-Off Rigour | 20% | Formality and completeness of compliance clearance documentation including conditions and post-launch obligations |

| **Total** | | **100%** | |

## Scale

Each criterion is scored **0-10**:
- **0**: No evidence / completely absent
- **5**: Partially present with significant gaps
- **10**: Fully present, comprehensive, no gaps

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 – 10.0 | Exceptional | All requirements verified with evidence, no gaps remaining, sign-off memo complete with documented assumptions | Issue unconditional GA clearance |
| A | 8.0 – 8.9 | Strong | Requirements verified, minor non-blocking gaps documented with remediation timelines | Issue clearance with documented conditions |
| B | 7.0 – 7.9 | Good | Most requirements verified, some gaps in evidence documentation, sign-off conditions identified | Issue conditional clearance with 30-day remediation deadline |
| C | 5.0 – 6.9 | Adequate | Checklist assembled but verification incomplete for some items, gap classification needs refinement | Delay clearance until verification gaps are closed |
| D | 3.0 – 4.9 | Weak | Significant verification gaps, hard blockers unresolved, sign-off cannot be issued | Block GA: resolve hard blockers before re-review |
| F | 0.0 – 2.9 | Failing | No systematic compliance verification performed | Block GA: full compliance review required |

## Signal Tables

### Checklist Completeness

| Score | Evidence |
|-------|----------|
| 9-10 | All regulatory requirements from compliance scans cross-referenced, PRD NFRs mapped, post-scan regulatory changes identified, checklist covers privacy (GDPR, CCPA), accessibility (WCAG 2.1 AA), data protection, sector-specific rules, and international requirements |
| 7-8 | Major regulatory requirements captured, PRD NFRs included, most post-scan changes identified |
| 5-6 | Core requirements listed but missing cross-reference to original compliance scan or PRD NFR appendix |
| 3-4 | Partial checklist with obvious regulatory gaps or missing entire requirement categories |
| 0-2 | No compliance checklist assembled |

### Implementation Verification

| Score | Evidence |
|-------|----------|
| 9-10 | Each requirement verified against production implementation with evidence references (screenshots, test results, DPA execution confirmations, accessibility audit reports), privacy policies reviewed for accuracy, cookie consent tested, age-gating validated |
| 7-8 | Most requirements verified with evidence, minor gaps in evidence documentation |
| 5-6 | Verification performed for high-priority items, lower-priority items self-attested by engineering without independent verification |
| 3-4 | Verification based on PRD compliance rather than actual implementation testing |
| 0-2 | No implementation verification performed |

### Gap Classification

| Score | Evidence |
|-------|----------|
| 9-10 | Each gap classified as hard blocker or soft blocker with clear rationale, remediation owner assigned, target dates set, risk acceptance documented for soft blockers with executive sign-off |
| 7-8 | Gaps classified with owners assigned, most target dates set |
| 5-6 | Gaps identified but classification rationale unclear or inconsistent across items |
| 3-4 | Gaps listed without severity classification or remediation ownership |
| 0-2 | No gap analysis performed |

### Sign-Off Rigour

| Score | Evidence |
|-------|----------|
| 9-10 | Formal compliance memo issued with scope statement, assumptions, conditions, accepted risks with rationale, post-launch obligations, and review expiration date |
| 7-8 | Sign-off memo with conditions and accepted risks documented |
| 5-6 | Sign-off issued but missing conditions documentation or post-launch obligations |
| 3-4 | Informal approval without formal documentation |
| 0-2 | No sign-off process followed |
