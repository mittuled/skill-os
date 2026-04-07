# Sprint Review Summary

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Product Manager] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | sprint-reviewer |

## Executive Summary

[2-3 sentences summarizing stories reviewed, shippability distribution, and the release recommendation.
GUIDANCE: Lead with how many stories ship vs. rejected and the overall release decision.]

## Shippability Matrix

[Per-story classification with rationale.

GUIDANCE:
- Good: Table with Story ID, Title, Classification (Ship / Ship-with-Caveat / Reject), Criteria Met (X/Y), Key Finding, Follow-Up Action
- Bad: "Everything looks good"
- Format: Markdown table, one row per committed story]

## Acceptance Criteria Results

[Detailed per-story criteria review.

GUIDANCE:
- Good: Per-story subsection with criterion-by-criterion pass/partial/fail status. Example: "T-001: Create Custom Role. AC1 (form display): PASS. AC2 (save success): PASS. AC3 (duplicate name error): PARTIAL — error displays but not inline, shows as toast. AC4 (no permissions error): PASS."
- Bad: "All criteria met"
- Format: Subsection per story with numbered criteria and status]

## Non-Functional Compliance

[Performance, accessibility, and error-handling verification.

GUIDANCE:
- Good: Table with Story ID, Performance (target/actual), Accessibility (verified Y/N), Error Handling (verified Y/N), Regression Status
- Bad: "Performance is fine"
- Format: Markdown table with specific metrics where applicable]

## Follow-Up Tickets

[Tickets filed for rejected or caveated stories.

GUIDANCE:
- Good: Table with Ticket ID, Story Reference, Issue Description, Remediation Steps, Owner, Re-Review Date
- Bad: "Filed some tickets"
- Format: Markdown table, one row per follow-up ticket]

## Recommendations

[Actions before release.
GUIDANCE: Each recommendation should be:
- Specific (not "fix issues" but "convert toast error to inline validation on T-001 duplicate name check before release")
- Actionable (assignable to a person/team)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[Review approach: line-by-line acceptance criteria verification, QA report cross-reference, non-functional compliance check per skill scoring rubric.]

### B. Supporting Data

[Demo recordings, QA reports, performance test results, accessibility audit outputs.]
