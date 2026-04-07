# Phase Plan

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Product Manager] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | phase-planner |

## Executive Summary

[2-3 sentences summarizing the initiative, number of phases, total estimated duration, and the critical path.
GUIDANCE: Lead with the initiative goal and the delivery timeline. Do not restate methodology.]

## Initiative Overview

[Brief description of the initiative and why it requires phased delivery.

GUIDANCE:
- Good: "User Permissions Overhaul: Replace the current binary admin/member role system with granular RBAC. Phased delivery required because the migration involves data backfill, UI changes, and API contract changes that cannot ship atomically."
- Bad: "We are doing a project in phases."
- Format: 2-3 sentences covering what, why phased, and what decision this plan supports]

## Phase Definitions

[One subsection per phase with entry criteria, exit criteria, activities, and deliverables.

GUIDANCE:
- Good: "**Phase 1: Discovery (2 weeks)**\nEntry: Initiative approved, PM assigned.\nExit: Validated problem statement, user journey map with 5+ interview inputs, technical spike results.\nActivities: 8 user interviews, competitive audit, engineering spike on migration feasibility.\nDeliverables: Problem statement doc, journey map, spike report."
- Bad: "Phase 1: Research stuff"
- Format: Subsection per phase with Entry, Exit, Activities, Deliverables as labeled fields]

## Activity Matrix

[Activities organized by phase and owner.

GUIDANCE:
- Good: Table with Phase, Activity, Owner, Duration, Dependencies columns
- Bad: Bullet list of activities without ownership
- Format: Markdown table with one row per activity]

## Timeline

[Phase sequence with durations, dependencies, and critical path highlighted.

GUIDANCE:
- Good: "Phase 1 (W1-W2) → Phase 2 (W3-W4) → Phase 3 (W5-W8) → Phase 4 (W9-W10). Critical path: Phase 1 discovery → Phase 3 build (design and build are parallel from W3). Total: 10 weeks."
- Bad: "About 2-3 months"
- Format: Sequential phase listing with week ranges and dependency arrows, critical path called out]

## Risk Register

[Top 1-2 risks per phase with likelihood, impact, and mitigation.

GUIDANCE:
- Good: Table with Phase, Risk, Likelihood (L/M/H), Impact (L/M/H), Mitigation, Owner
- Bad: "There are some risks"
- Format: Markdown table, one row per risk]

## Recommendations

[Prioritized actions to finalize or improve the phase plan.
GUIDANCE: Each recommendation should be:
- Specific (not "plan better" but "schedule engineering spike for migration feasibility before Phase 1 exit")
- Actionable (assignable to a person/team)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[Phase planning approach: phase taxonomy from framework, estimation method (historical velocity, analogous projects), risk scoring criteria.]

### B. Supporting Data

[Historical velocity data, analogous project timelines, stakeholder input summaries, capacity snapshots.]
