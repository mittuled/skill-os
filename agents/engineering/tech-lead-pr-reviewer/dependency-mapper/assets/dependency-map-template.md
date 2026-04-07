# Dependency Map

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Tech Lead / author name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | dependency-mapper |

## Executive Summary

[2-3 sentences stating the project/initiative, total tasks mapped, critical path length, and number of cross-team blockers.
GUIDANCE: Lead with the critical path finding. Example: "This map covers 23 tasks across 4 teams for the Payments v2 initiative. The critical path is 34 days (BE-01 → BE-07 → FE-03 → QA-02). Three cross-team blockers require owner assignment before sprint planning."]

## Task and Service Inventory

[All tasks and services included in this mapping exercise.

GUIDANCE:
- Good: List every task by ID, owning team, and estimated duration
- Bad: "All the tasks for this project"
- Format: Table grouped by team]

| Task ID | Title | Team | Duration (days) | Status |
|---------|-------|------|----------------|--------|
| [BE-01] | [Title] | Backend | [N] | [Not started / In progress / Complete] |
| [FE-01] | [Title] | Frontend | [N] | [Not started / In progress / Complete] |
| [INF-01] | [Title] | Infrastructure | [N] | [Not started / In progress / Complete] |

## Dependency Edge List

[All identified dependency relationships between tasks.

GUIDANCE:
- Good: Include both hard (blocking) and soft (preferred) dependencies; note the reason for each
- Bad: Only list hard blockers, omit soft dependencies
- Format: Table with edge type]

| From Task | To Task | Edge Type | Reason |
|-----------|---------|-----------|--------|
| [BE-01] | [FE-01] | Hard | FE requires BE endpoint to exist before integration can begin |
| [INF-01] | [BE-01] | Hard | Service requires DB provisioned first |
| [BE-03] | [BE-05] | Soft | Prefers sequential to reduce merge conflicts on shared module |
| [BE-02] | [FE-02] | Hard | Schema change affects API contract; FE must update after BE lands |

## Critical Path Analysis

[The longest chain of hard dependencies determines the minimum delivery timeline.

GUIDANCE:
- Good: Show the full path with task durations; calculate total minimum days
- Bad: Omit this section because "the project manager will figure it out"
- Format: Ordered path list with cumulative duration]

**Critical path**: [Task A] → [Task B] → [Task C] → [Task D]

| Step | Task | Duration | Cumulative Days |
|------|------|----------|----------------|
| 1 | [Task A] | [N days] | [N] |
| 2 | [Task B] | [N days] | [N] |
| 3 | [Task C] | [N days] | [N] |
| **Total** | | | **[N days]** |

**Minimum delivery date** (from today): [YYYY-MM-DD]

## Cross-Team Blocker Register

[Dependencies that cross team boundaries and require active coordination.

GUIDANCE:
- Good: Every cross-team dependency has a named owner from each side and a resolution date
- Bad: "Team A depends on Team B for a few things"
- Format: Table with bi-lateral owners]

| Blocker Task | Blocked Task | Blocking Team | Owner (Blocking) | Blocked Team | Owner (Blocked) | Resolution Date |
|-------------|-------------|--------------|-----------------|-------------|----------------|----------------|
| [INF-01] | [BE-01] | Infrastructure | [Name] | Backend | [Name] | [YYYY-MM-DD] |

## Dependency Graph (Text Representation)

[Visual representation of the DAG. Use a text-based diagram when tooling is unavailable.

GUIDANCE:
- Good: Show branching structure and critical path highlighted
- Bad: Omit the visual because it's "too complex"
- Format: Indented text or Mermaid diagram syntax]

```
INF-01
└── BE-01
    ├── BE-02
    │   └── FE-02
    └── BE-07 [CRITICAL PATH]
        └── FE-03 [CRITICAL PATH]
            └── QA-02 [CRITICAL PATH] ← GA gate
BE-03
└── BE-05
    └── FE-01
```

## Update Schedule

[When this map will be reviewed and by whom.

GUIDANCE: Dependency maps go stale fast; set a recurring review cadence]

| Trigger | Action | Owner |
|---------|--------|-------|
| Weekly (every Monday) | Review for new dependencies or resolved blockers | [Tech Lead name] |
| Any task marked complete | Update downstream task status and re-check critical path | [Task owner] |
| New task added to project | Add edges and re-run critical path calculation | [Tech Lead name] |
| Any blocker unresolved > 48h | Escalate and update map with resolution plan | [Tech Lead name] |

## Recommendations

[Actions required before this map is used for sprint planning.
GUIDANCE: Focus on gaps that would break the map's accuracy]

- **P1**: [Critical path tasks without owners — must assign before planning]
- **P2**: [Cross-team blockers without resolution dates — must get commitments]
- **P3**: [Soft dependencies to convert to hard if violation risk is high]

## Appendices

### A. Methodology

[How tasks were inventoried (backlog export, spec review), how dependencies were identified (engineering workshops, architecture review), cycle detection method if used]

### B. Supporting Data

[Link to project management tool, task list export, architecture diagram, previous dependency maps for comparison]
