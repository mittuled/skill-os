# Iteration Priority Matrix: [Sprint / Iteration Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | Tech Lead |
| Sprint / Iteration | [Sprint N] |
| Prioritization Method | [RICE / MoSCoW / Value vs. Effort / ICE] |
| Skill | iteration-prioritiser-f |

## Prioritization Results

### RICE Scoring (Reach × Impact × Confidence / Effort)

| ID | Item | Reach | Impact (1–3) | Confidence (%) | Effort (weeks) | RICE Score | Priority |
|----|------|-------|-------------|---------------|----------------|-----------|---------|
| [TICKET-001] | [Feature name] | [N users/sprint] | [3] | [80%] | [0.5] | [(R×I×C)/E] | [P1] |
| [TICKET-002] | | | | | | | |

**Reach**: estimated users/customers affected per sprint
**Impact**: 3 = massive, 2 = high, 1 = medium, 0.5 = low, 0.25 = minimal
**Confidence**: % certainty in reach and impact estimates
**Effort**: person-weeks to implement

### Sprint Commitment (Sorted by Priority)

| Priority | ID | Item | Type | Points | Rationale |
|----------|----|----|------|--------|-----------|
| P1 | [TICKET-001] | [Title] | [Feature] | [5] | [Highest RICE score; unblocks customer workflow] |
| P1 | [TICKET-003] | | | | |
| P2 | [TICKET-005] | | | | |
| P3 | [TICKET-007] | | | | [If capacity permits] |

**Total committed**: [X pts]
**Team capacity**: [Y pts]
**Utilization**: [X/Y = Z%] (target 80–85%)

## Items Explicitly Deferred

| ID | Item | Reason | Next Sprint? |
|----|------|--------|-------------|
| [TICKET-010] | [Title] | [Dependency not ready / Lower RICE] | [Yes/No] |

## Trade-off Notes

[Any explicit trade-offs made in this prioritization:]

1. [e.g., "Deferred TICKET-008 (tech debt) to unblock TICKET-001 (customer feature) — tech debt to be addressed Sprint N+1"]
