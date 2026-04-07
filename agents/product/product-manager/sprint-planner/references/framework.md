# Framework: Sprint Planning

## Core Model

Capacity-based sprint planning that matches committed stories to available team capacity with dependency ordering, risk buffers, and explicit sprint goals.

## Capacity Calculation

| Team Member | Available Days | Meeting Overhead | On-Call | Net Availability | Story Points (at velocity) |
|-------------|---------------|-----------------|---------|-----------------|--------------------------|
| Engineer A | 10 | -1.5 | 0 | 8.5 | ~8 SP |
| Engineer B | 8 (PTO) | -1.5 | -1 | 5.5 | ~5 SP |
| **Team Total** | | | | | **~13 SP** |

## Capacity Utilisation Targets

| Zone | Utilisation | Description |
|------|-------------|-------------|
| Optimal | 70-80% | Room for unplanned work and healthy pace |
| Acceptable | 80-85% | Tight but manageable with minimal disruption |
| Risky | 85-95% | Any disruption causes spillover |
| Overloaded | >95% | Spillover guaranteed; team morale at risk |

## Story Selection Protocol

1. Pull from top of groomed backlog (priority order)
2. Verify each story is sprint-ready: has estimate, acceptance criteria, no unresolved blockers
3. Fill to 80% capacity, leaving 20% buffer
4. Sequence by dependency order (prerequisites first)
5. Assign by expertise and load balance (no person at >85% individual utilisation)

## Sprint Goal Pattern

A sprint goal must be:
- **Outcome-oriented**: "Users can complete checkout with saved payment methods" (not "implement payment stories")
- **Achievable**: The committed stories, if delivered, achieve the goal
- **Singular**: One primary goal per sprint (secondary goals noted but deprioritised if conflict arises)

## Risk Annotation Format

Flag stories with:
- **External dependency**: Story depends on another team's delivery (name the team and expected date)
- **Uncertain estimate**: First-time technical territory or estimate confidence < 70%
- **High complexity**: Story touches 3+ services or requires data migration

## Buffer Allocation

- Default buffer: 20% of team capacity
- If sprint contains 2+ high-risk stories: increase buffer to 25%
- If team is running at >90% sprint completion rate for 3+ sprints: reduce buffer to 15%
