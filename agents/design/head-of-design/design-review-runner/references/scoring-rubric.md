# Scoring Rubric: design-review-runner

Evaluates the quality, thoroughness, and actionability of a design review session.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Scope Definition | 15% | Review type, screens, and evaluation criteria were defined before the session began |
| 2 | Artifact Completeness | 15% | Figma files, prototypes, and reference materials were present and up to date |
| 3 | Criteria-Grounded Feedback | 25% | Feedback references design principles, heuristics, or user data rather than personal preference |
| 4 | State Coverage | 20% | Review addressed all interaction states: happy path, empty, error, loading, and edge cases |
| 5 | Action Item Quality | 15% | Issues were logged as actionable items with severity, owner, and definition of done |
| 6 | Verdict Clarity | 10% | Review outcome (approved / conditional / re-review) was clearly communicated with rationale |
| **Total** | | **100%** | |

## Scale: 0–10. Composite = Σ(score × weight)

## Grade Bands

| Grade | Score | Label | Description | Action |
|-------|-------|-------|-------------|--------|
| A+ | 9.0–10.0 | Exceptional | Criteria-grounded review covering all states; clear verdict with prioritised action items | Ship verdict; track actions to closure |
| A | 8.0–8.9 | Strong | Thorough review with minor gaps in edge-case coverage or action item specificity | Ship verdict; note gaps for follow-up |
| B | 7.0–7.9 | Good | Solid review of primary flows; some interaction states or criteria underchecked | Ship conditional verdict; schedule re-check |
| C | 5.0–6.9 | Adequate | Review completed but missing key states or producing opinion-based feedback without criteria | Revise action items; reschedule partial re-review |
| D | 3.0–4.9 | Weak | Significant scope gaps; feedback not actionable; verdict unclear | Full re-review required with defined criteria |
| F | 0.0–2.9 | Failing | Review was a rubber-stamp or devolved into aesthetic debate without substantive evaluation | Cancel outcome; define criteria and reschedule |

## Signal Tables

### Criteria-Grounded Feedback

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Every feedback item cites a specific design principle, heuristic, WCAG criterion, or user data point |
| 7–8 | Most feedback items cite criteria; occasional preference-based comment appears but is rare |
| 5–6 | Mix of criteria-grounded and preference-based feedback; criteria are cited inconsistently |
| 3–4 | Majority of feedback is opinion-based; design principles referenced vaguely if at all |
| 0–2 | Review is entirely aesthetic debate with no reference to principles, heuristics, or evidence |

### State Coverage

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | All states reviewed: happy path, empty, error, loading, disabled, edge cases documented |
| 7–8 | Happy path and primary error states reviewed; some edge cases deferred with tickets |
| 5–6 | Happy path reviewed thoroughly; error and empty states partially covered |
| 3–4 | Only happy-path visuals reviewed; interaction states largely skipped |
| 0–2 | Single state reviewed; no acknowledgement of other required states |
