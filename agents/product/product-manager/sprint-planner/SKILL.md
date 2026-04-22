---
name: sprint-planner
description: >
  This skill plans sprints by selecting, sequencing, and assigning stories from the groomed
  backlog based on capacity, priority, and dependency order. Use when asked to build a sprint
  plan, balance workload across the team, or decide which stories fit into available capacity.
  Also consider when sprint velocity has been volatile and the team needs a more disciplined
  selection process. Suggest when the user is about to start a sprint without a documented plan
  matching committed stories to available capacity.
department: product
agent: product-manager
version: 1.0.0
complexity: medium
related-skills:
  - market-sizer
  - backlog-populator
  - risk-register-builder
triggers:
  - "sprint planning"
  - "plan sprint"
  - "sprint-planning-facilitator"
  - "capacity planning"
---

# sprint-planner

## Agent: Product Manager
L2 product manager (multi-instance) responsible for customer discovery, requirements extraction, sprint planning, backlog management, and go-live approval. Bridges customer needs and engineering delivery.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Plans the sprint by selecting and sequencing stories from the groomed backlog, matching committed work to available team capacity and dependency constraints.

## When to Use
- When a new sprint is starting and the team needs to select which stories from the backlog to commit to based on capacity and priority
- When mid-sprint disruptions (sick days, production incidents, dependency delays) require re-planning the remaining sprint scope
- When sprint velocity has been inconsistent and the team needs a structured approach to capacity-based story selection rather than gut-feel loading

## Workflow
1. **Calculate available capacity**: Determine each team member's available hours for the sprint, accounting for holidays, on-call rotations, meetings, and planned absences. Sum to get total team capacity in story points or hours. Deliverable: capacity table with per-person availability and team total.
2. **Review groomed backlog**: Pull the top-priority stories from the groomed backlog. Confirm each has acceptance criteria, an estimate, and no unresolved blockers. Flag any story that is not sprint-ready. Deliverable: sprint-candidate list ordered by priority with readiness status.
3. **Select and sequence stories**: Fill the sprint from the top of the candidate list until capacity is reached, leaving a 10-20% buffer for unplanned work. Sequence stories by dependency order — prerequisites first, dependents after. Assign owners based on expertise and load balance. Deliverable: sprint plan table with story, estimate, owner, sequence order, and dependency links.
4. **Identify risks and buffers**: Flag stories with external dependencies, uncertain estimates, or first-time technical territory. Ensure the buffer allocation covers at least one high-risk story slipping. Deliverable: risk annotations on flagged stories with contingency notes.
5. **Commit and communicate**: Present the sprint plan to the team for commitment. Record any objections or adjustments. Lock the plan with a sprint goal statement summarising the sprint's primary outcome. Deliverable: committed sprint plan with sprint goal, team sign-off, and start date. [GATE]

## Anti-Patterns
- **Capacity stuffing**: Loading the sprint to 100% of theoretical capacity with no buffer for unplanned work. *Why*: Every sprint has interruptions — production issues, clarification loops, sick days. A fully loaded sprint guarantees spillover, which trains the team to treat commitments as aspirational.
- **Priority inversion**: Selecting a lower-priority story because it is easier or more interesting while a higher-priority story sits unassigned. *Why*: Sprint planning exists to enforce priority discipline — inverting priorities undermines the roadmap and delays the most valuable work.
- **Estimate-free commitments**: Committing to stories that have not been estimated, relying on "it should be small." *Why*: Unestimated work is the leading cause of sprint overcommitment because the team cannot compare demand to capacity without numbers.

## Output
**On success**: A committed sprint plan containing the sprint goal, selected stories with estimates, owner assignments, sequence order, dependency links, capacity utilisation percentage, and risk annotations — formatted as a markdown table or project tracker export ready for the sprint kickoff.

**On failure**: Report which stories could not be included (missing estimates, unresolved blockers, insufficient capacity), what capacity gaps exist, and recommend specific grooming actions or backlog adjustments needed before the sprint can be fully planned.

## Related Skills
- [`market-sizer`](../market-sizer/SKILL.md) — sibling skill under the same agent — combine with market-sizer for end-to-end coverage
- [`backlog-populator`](../backlog-populator/SKILL.md) — sibling skill under the same agent — combine with backlog-populator for end-to-end coverage
- [`risk-register-builder`](../risk-register-builder/SKILL.md) — sibling skill under the same agent — combine with risk-register-builder for end-to-end coverage
