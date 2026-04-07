# Analytics Effort Estimate

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Analytics Lead name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | effort-estimator-data |
| Initiative | [PRD or ticket link] |

## Executive Summary

[2-3 sentences stating the total analyst-days required, confidence level, and the primary risk to the estimate.

GUIDANCE: Example: "The [feature name] analytics workstream requires 14–18 analyst-days across instrumentation, pipeline, and dashboard deliverables at medium confidence. The primary risk is the dependency on the mobile SDK release, which if delayed by one sprint adds 4 analyst-days due to context switching."]

## Requirements Extracted

[List of all analytics deliverables parsed from the PRD or initiative brief.

GUIDANCE:
- Good: Each deliverable is traceable to a specific PRD requirement or metric goal.
- Bad: A generic list of "instrumentation" and "dashboard" without tracing to what metrics they support.
- Format: Bullet list with source reference.]

- [ ] [Deliverable 1] — from [PRD section / metric definition]
- [ ] [Deliverable 2] — from [PRD section / metric definition]

## Task Breakdown

[Detailed decomposition of every work unit with size and rationale.

GUIDANCE:
- Good: Each row has a task name, category, size, analyst-days midpoint, complexity factors applied, and dependency flag.
- Bad: "Instrumentation: 5 days." Break down to individual events or surfaces.
- Format: Table.]

| Task | Category | Size | Days (Low–High) | Complexity Factors | Dependency |
|------|---------|------|----------------|-------------------|-----------|
| [Task name] | [Schema / SDK / Pipeline / Dashboard / QA / Model] | [S/M/L/XL] | [N–N] | [List adjustments applied] | [None / blocks: task N / blocked by: X] |
| QA and verification | QA | — | [20–30% of impl total] | — | Follows all implementation |
| Stakeholder review | Review | — | [0.5 × 2 cycles] | — | Follows QA |
| **Total** | | | **[N–N days]** | | |

## Dependencies

[All external dependencies that could affect the timeline.

GUIDANCE:
- Good: Each dependency has an owner, required-by date, and mitigation plan.
- Bad: "Depends on engineering." Specify the exact deliverable and owner.
- Format: Table.]

| Dependency | Owner | Required By Sprint | Risk if Delayed | Mitigation |
|-----------|-------|-------------------|----------------|-----------|
| [Dependency name] | [Team / person] | [Sprint N] | [Impact on analytics timeline] | [Mitigation plan] |

## Estimate Summary

[Rollup by category with confidence range.

GUIDANCE:
- Good: Low/mid/high range with explicit confidence level and the assumptions driving the range.
- Bad: Single number presented without range.
- Format: Table.]

| Category | Low (days) | Mid (days) | High (days) |
|---------|-----------|-----------|------------|
| Instrumentation (schema + SDK) | | | |
| Pipeline / data model | | | |
| Dashboard build | | | |
| QA and verification | | | |
| Stakeholder reviews | | | |
| **Total** | | | |

**Confidence Level:** [High / Medium / Low]
**Confidence Rationale:** [State the conditions driving the confidence level]

## Recommendations

[Prioritized list of risks or scope decisions that affect the estimate.

GUIDANCE:
- P1: Dependencies that must be resolved before implementation can begin.
- P2: Scope items that can be descoped to hit a tighter timeline.
- P3: Instrumentation items with low metric impact that can be deferred.]

## Appendices

### A. Methodology

[Document velocity baseline used (historical sprint actuals), complexity factors applied, and QA percentage used.]

### B. Supporting Data

[Relevant PRD sections, instrumentation spec excerpts, or comparable past estimates used for calibration.]
