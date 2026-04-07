# Sprint Review Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Tech Lead / author name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | sprint-reviewer-eng |

## Executive Summary

[2-3 sentences stating the sprint number, overall delivery score, velocity, and the single most important finding.
GUIDANCE: Lead with the delivery headline. Example: "Sprint 14 delivered 34 of 40 committed points (85%), with velocity declining for the second consecutive sprint. The primary carryover cause was an unresolved database migration dependency that blocked 3 backend tasks. Retrospective action: assign a dependency owner at sprint kickoff for all cross-team work items."]

## Delivery Assessment

[Per-task completion status with evidence.

GUIDANCE:
- Good: "Task BE-42 — COMPLETE. Evidence: 100% unit tests passing (CI link), demo recorded, product owner signed off."
- Bad: "Most tasks done, a few not finished"
- Format: Table with one row per task; color coding is optional but evidence column is mandatory]

| Task ID | Title | Status | Points | Evidence | Root Cause (if incomplete) |
|---------|-------|--------|--------|----------|--------------------------|
| [BE-01] | [Title] | Complete / Partial / Incomplete | [N] | [Link or description] | — |
| [FE-01] | [Title] | Complete / Partial / Incomplete | [N] | [Link or description] | [Scope creep / estimation error / blocker / etc.] |

**Delivery Summary**: [N] of [N] tasks complete. [N] points delivered of [N] committed ([X%]).

## Carryover List

[Tasks not completed, with root cause and disposition for next sprint.

GUIDANCE:
- Good: "BE-42 blocked by DB migration owned by platform team. Will carry to Sprint 15 and assign blocker owner. Scope unchanged."
- Bad: "Some tasks weren't done, will try again next sprint"
- Format: Table with root cause category and next sprint disposition]

| Task ID | Title | Points | Root Cause Category | Disposition | Owner |
|---------|-------|--------|--------------------|----|-------|
| [ID] | [Title] | [N] | [Scope creep / Estimation error / External blocker / Technical discovery / Priority change] | [Carry / Deprioritize / Split] | [Name] |

## Velocity Analysis

[Sprint velocity vs. recent trend.

GUIDANCE:
- Good: Include a data table for the last 5 sprints; call out the trend direction
- Bad: "Velocity was fine"
- Format: Table of last 5 sprints with delivered points; trend direction statement]

| Sprint | Committed Points | Delivered Points | Completion Rate |
|--------|-----------------|-----------------|----------------|
| Sprint [N-4] | [N] | [N] | [X%] |
| Sprint [N-3] | [N] | [N] | [X%] |
| Sprint [N-2] | [N] | [N] | [X%] |
| Sprint [N-1] | [N] | [N] | [X%] |
| Sprint [N] (current) | [N] | [N] | [X%] |

**Trend**: [Stable / Improving / Declining — one sentence with specific numbers]

**Estimation accuracy**: Actual delivered was [X%] of committed. Consistent over/under-estimation in: [task type or workstream, if any pattern visible].

## Blocker Log

[All blockers raised during the sprint with resolution status.

GUIDANCE:
- Good: Document every blocker, time-to-identify, time-to-resolve, and whether it caused a task miss
- Bad: Omit resolved blockers because "they're done"
- Format: Table]

| Blocker | Raised On | Resolved On | Time to Resolve | Caused Missed Task? |
|---------|----------|------------|----------------|---------------------|
| [Description] | [Date] | [Date / Unresolved] | [Xh / Xd] | [Yes — task ID / No] |

## Retrospective Actions

[What we learned and specific actions for the next sprint.

GUIDANCE:
- Good: "Action: PM to provide DB migration timeline at sprint kickoff. Owner: PM Sarah. Due: Sprint 15 kickoff."
- Bad: "Communicate better"
- Format: Separate what went well from what didn't; actions must have owners and deadlines]

### What Went Well
- [Specific positive outcome with evidence]

### What Didn't Go Well
- [Specific issue with root cause]

### Actions for Next Sprint

| Action | Owner | Due |
|--------|-------|-----|
| [Specific, measurable action] | [Name] | [Sprint N+1 kickoff / YYYY-MM-DD] |

## Recommendations

[Prioritized next steps based on sprint findings.
GUIDANCE: Be specific — generic advice is not actionable]

- **P1**: [Immediate change for next sprint — e.g., "Reduce Sprint 15 commitment by 15% to account for ongoing infrastructure migration dependency"]
- **P2**: [Process improvement — e.g., "Add dependency owner field to all tasks with external dependencies at backlog grooming"]
- **P3**: [Longer-term improvement — e.g., "Calibrate estimation for API integration tasks, which consistently over-run by 2×"]

## Appendices

### A. Methodology

[Sprint dates, total team members, how evidence was collected (CI reports, demo recordings, product owner sign-offs), DORA metrics if tracked (deployment frequency, lead time, MTTR, change failure rate)]

### B. Supporting Data

[Links to CI/CD pipeline results, velocity chart, blocker log in project tool, and demo recordings]
