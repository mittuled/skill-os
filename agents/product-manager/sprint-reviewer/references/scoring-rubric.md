# Scoring Rubric: sprint-reviewer

Evaluates the thoroughness of sprint output review against acceptance criteria and the quality of shippability decisions.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Acceptance Criteria Verification | 30% | Completeness of line-by-line review of each story against its acceptance criteria |
| 2 | Non-Functional Compliance | 20% | Verification of performance, accessibility, and error-handling requirements |
| 3 | Shippability Classification | 25% | Quality of ship / ship-with-caveat / reject bucketing with documented rationale |
| 4 | Follow-Up Actions | 25% | Completeness of follow-up tickets and communication of results |

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
| A+ | 9.0 – 10.0 | Exceptional | Every story reviewed line-by-line against criteria, NFRs verified, shippability decisions documented with rationale, follow-up tickets filed with clear remediation steps | Use as template for future sprint reviews |
| A | 8.0 – 8.9 | Strong | All stories reviewed, most NFRs checked, clear shippability decisions, follow-ups created | Minor process refinements only |
| B | 7.0 – 7.9 | Good | Most stories reviewed against criteria, shippability decisions present but some rationale missing | Add rationale documentation to caveated items |
| C | 5.0 – 6.9 | Adequate | Stories reviewed at summary level, NFR checks incomplete, some stories lack clear ship/reject decision | Re-review stories with missing decisions before release |
| D | 3.0 – 4.9 | Weak | Partial review, no NFR verification, shippability decisions inconsistent | Block release until full review completes |
| F | 0.0 – 2.9 | Failing | No meaningful sprint review performed | Conduct full sprint review before any release decision |

## Signal Tables

### Acceptance Criteria Verification

| Score | Evidence |
|-------|----------|
| 9-10 | Every committed story has each acceptance criterion marked pass/partial/fail with specific evidence. Edge cases and negative cases verified. Demo recordings or QA reports referenced per story. |
| 7-8 | All stories reviewed, most criteria checked, but some edge cases not explicitly verified |
| 5-6 | Stories reviewed at summary level; criteria checked for happy path only, edge cases skipped |
| 3-4 | Only high-priority stories reviewed; remaining stories assumed complete based on developer assertion |
| 0-2 | No acceptance criteria verification performed |

### Non-Functional Compliance

| Score | Evidence |
|-------|----------|
| 9-10 | Performance benchmarks checked against targets, accessibility audit completed, error handling verified for all failure modes, regression test results reviewed |
| 7-8 | Performance and accessibility checked, most error states verified |
| 5-6 | Performance spot-checked, accessibility not verified, some error states reviewed |
| 3-4 | NFR verification mentioned but no specific checks documented |
| 0-2 | No NFR verification performed |

### Shippability Classification

| Score | Evidence |
|-------|----------|
| 9-10 | Every story classified as ship/ship-with-caveat/reject with documented rationale. Caveats include specific gaps and acceptance conditions. Reject decisions include remediation steps and re-review dates. |
| 7-8 | All stories classified, most have rationale, caveats documented |
| 5-6 | Stories classified but rationale missing for some decisions; caveats vague |
| 3-4 | Some stories classified, others left in ambiguous state |
| 0-2 | No shippability classification performed |

### Follow-Up Actions

| Score | Evidence |
|-------|----------|
| 9-10 | Follow-up tickets filed for every rejected and caveated story with clear remediation steps, owners, and re-review dates. Sprint review summary distributed to all stakeholders. |
| 7-8 | Follow-up tickets created for rejected stories, summary distributed |
| 5-6 | Some follow-up tickets created but missing remediation steps or owners |
| 3-4 | Issues noted verbally but no tickets filed |
| 0-2 | No follow-up actions taken |
