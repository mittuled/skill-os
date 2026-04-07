# Framework: phase-planner-eng

Guides engineering phase planning by structuring phases around integration points, critical path analysis, and capacity-aware sprint allocation.

## Phase Boundary Rules

Each phase must have:

| Element | Description |
|---------|-------------|
| Entry Criteria | What must be true before the phase starts (e.g., "Architecture ADR approved") |
| Exit Criteria | What must be true before the phase is considered complete |
| Demo Increment | What can be demonstrated to stakeholders at phase end |
| Handoff Artifacts | What the next phase needs from this phase |

## Phase Template

| Field | Content |
|-------|---------|
| Phase Name | Descriptive name (e.g., "Foundation", "Core Features", "Hardening") |
| Duration | Number of sprints |
| Entry Criteria | Bullet list |
| Objectives | 3-5 measurable outcomes |
| Sprint Allocation | Per-sprint task groupings |
| Critical Path | Ordered list of blocking tasks with owners |
| Risks | Phase-specific risks with mitigations |
| Exit Criteria | Bullet list with verification method |

## Critical Path Analysis Method

1. List all tasks with their durations and dependencies.
2. Build a directed acyclic graph (DAG) of task dependencies.
3. Calculate the longest path through the graph — this is the critical path.
4. The critical path duration equals the minimum possible phase duration.
5. Mark all tasks on the critical path as P1 priority.
6. Identify tasks with float (slack time) that can shift without affecting the deadline.

## Capacity Planning

Target **70-80% utilization** per sprint to preserve slack for:

| Slack Category | Allocation |
|----------------|-----------|
| Unplanned work (bugs, incidents) | 10-15% |
| Code review and collaboration | 5-10% |
| Personal development / meetings | 5-10% |

### Sprint Capacity Formula

```
Available capacity = (engineers × sprint_days × hours_per_day) × 0.75
Task allocation = Available capacity - (incident_buffer + review_buffer)
```

## Common Phase Structures

### Two-Phase Delivery (3-6 sprints)

| Phase | Focus | Duration |
|-------|-------|----------|
| Build | Core features, infrastructure, integration | 60-70% of sprints |
| Harden | Testing, performance, operational readiness | 30-40% of sprints |

### Three-Phase Delivery (6-12 sprints)

| Phase | Focus | Duration |
|-------|-------|----------|
| Foundation | Architecture, scaffolding, data model, API contracts | 20-30% |
| Build | Feature development, integration, initial testing | 40-50% |
| Harden | Load testing, security review, observability, documentation | 20-30% |

### Four-Phase Delivery (12+ sprints)

| Phase | Focus | Duration |
|-------|-------|----------|
| Discovery | Spikes, PoCs, architecture design | 10-15% |
| Foundation | Scaffolding, core infrastructure, API contracts | 15-20% |
| Build | Feature development across teams | 40-50% |
| Harden | Testing, performance, operational readiness, GA prep | 20-25% |
