# Team Allocation Plan

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [VP Engineering / author name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | team-allocator |

## Executive Summary

[2-3 sentences identifying the project/phase, total engineers allocated, average utilization, and the most significant capacity risk.
GUIDANCE: Lead with the capacity verdict. Example: "This plan allocates 6 engineers across 3 workstreams for Payments v2 Phase 2 (2026-04-01 to 2026-05-01). Average utilization is 72%, preserving buffer for unplanned work. The critical risk is the backend workstream: one engineer owns the database migration and no backup has been cross-trained, creating key-person risk."]

## Capacity Matrix

[All engineers available for this period with their current allocations and constraints.

GUIDANCE:
- Good: Include actual names (or anonymized IDs), skills, current commitment %, and time-off schedule
- Bad: "We have 6 engineers available"
- Format: Table with one row per engineer]

| Engineer | Role | Skills | Current Allocation | Available Capacity | Time Off (this period) | Notes |
|----------|------|--------|-------------------|-------------------|----------------------|-------|
| [Name / ID] | [Senior BE / FE / Fullstack / etc.] | [Tech stack, domain] | [N%] | [100 − allocation %] | [Dates or None] | [On-call rotation, etc.] |

**Total available capacity**: [N] engineer-weeks

## Skill-Fit Analysis

[Match delivery requirements against available profiles. Identify gaps.

GUIDANCE:
- Good: Explicitly call out skill gaps and proposed mitigations (cross-training, contractor, scope reduction)
- Bad: Assign engineers to workstreams without checking skill match
- Format: Table per workstream]

| Workstream | Required Skills | Required Seniority | Available Match | Gap? | Mitigation |
|-----------|----------------|-------------------|----------------|------|-----------|
| [Backend API] | [Go, PostgreSQL, distributed systems] | Senior | [Engineer name(s)] | [None / Yes — describe] | [If gap: contractor / cross-train / reduce scope] |
| [Frontend] | [React, TypeScript, accessibility] | Mid | [Engineer name(s)] | [None / Yes] | |
| [Infrastructure] | [Terraform, Kubernetes, GCP] | Senior | [Engineer name(s)] | [None / Yes] | |

## Allocation Plan

[Final engineer-to-project assignments with utilization targets.

GUIDANCE:
- Target 70–80% utilization per engineer — 20–30% slack absorbs unplanned work
- Never assign a critical-path workstream to a single engineer without backup
- Format: Table]

| Engineer | Workstream | Allocation % | Sprint Days | Effective Capacity | Key-Person Risk? |
|----------|-----------|-------------|------------|-------------------|-----------------|
| [Name] | [Workstream] | [70%] | [N] | [N days × 70%] | [Yes / No] |

**Total allocated capacity**: [N] engineer-days
**Committed delivery effort**: [N] engineer-days
**Buffer**: [N] engineer-days ([X%] — target ≥ 20%)

## Key-Person Risk Register

[Engineers whose absence would directly threaten delivery.

GUIDANCE:
- Good: Name the risk, the mitigation plan, and the backup person identified
- Bad: Omit this section because "we trust the team"
- Format: Table]

| Engineer | Risk Scenario | Workstream Impact | Backup Plan | Backup Owner |
|----------|--------------|------------------|-------------|-------------|
| [Name] | [PTO / attrition / illness] | [Critical path impact description] | [Cross-train [Name] on [domain] / Contractor on standby / Scope reduction] | [Manager or Tech Lead] |

## Skill Gaps and Hiring Recommendations

[Any delivery roles that cannot be staffed from current headcount.

GUIDANCE:
- Good: Specify exact role, required skills, needed start date, and interim mitigation if hiring takes time
- Bad: "We might need more engineers"
- Format: List]

| Gap | Required Role | Needed By | Interim Mitigation | Hiring Recommendation |
|-----|--------------|-----------|-------------------|-----------------------|
| [Description] | [Title + skills] | [YYYY-MM-DD] | [Contractor / scope reduction / defer] | [Yes — urgent / No — next cycle] |

## Recommendations

[Prioritized actions to finalize allocations.
GUIDANCE: P1 items block delivery start]

- **P1**: [Critical gap that must be resolved before delivery begins — e.g., "Identify backup for DB migration workstream by 2026-04-01"]
- **P2**: [Action to reduce key-person risk — e.g., "Schedule cross-training sessions for infrastructure workstream in Sprint 1"]
- **P3**: [Capacity improvement for future phases — e.g., "Begin hiring for senior BE role; target availability for Phase 3"]

## Appendices

### A. Methodology

[Data sources (HRIS, time-tracking, sprint records), capacity model used (historical velocity, working days minus overhead), validation process (tech lead review sessions)]

### B. Supporting Data

[Effort estimates from effort-estimator-eng skill, phase plan timeline, team skills inventory, current sprint allocations from project management tool]
