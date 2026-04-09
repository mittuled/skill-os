---
name: team-allocator
description: >
  This skill allocates engineering team members to tasks and projects based on capacity and skill
  fit. Use when asked to staff a project, assign engineers to a delivery, or rebalance team
  assignments. Also consider when a new phase begins or when attrition changes available capacity.
  Suggest when a project is understaffed relative to its effort estimate.
department: engineering
agent: vp-engineering
version: 1.0.0
complexity: medium
related-skills:
  - ../../../engineering/vp-engineering/effort-estimator-eng/SKILL.md
  - ../../../engineering/vp-engineering/phase-planner-eng/SKILL.md
  - ../velocity-monitor/SKILL.md
triggers:
  - "allocate team"
  - "team allocation"
  - "assign engineers"
  - "resource allocation"
  - "engineering staffing"
---

# team-allocator

## Agent: VP Engineering

L1 engineering leader (1x) responsible for spec intake review, team allocation, architecture oversight, velocity monitoring, and go-live approvals. Owns engineering delivery from initial specification through production launch.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Allocates engineering team members to tasks and projects based on capacity, skill fit, and delivery priorities.

## When to Use

- When a new project or delivery phase needs staffing decisions.
- When team capacity changes due to attrition, hiring, or competing priorities.
- When velocity data indicates a team is over- or under-resourced relative to its commitments.

## Workflow

1. **Inventory capacity**: Map available engineers, their current allocations, skill profiles, and time-off schedules. Deliverable: capacity matrix.
2. **Match skills to needs**: Compare delivery requirements (tech stack, domain knowledge, seniority) against available skill profiles. Identify gaps requiring hiring, contractors, or cross-training. Deliverable: skill-fit analysis.
3. **Propose allocations**: Assign engineers to projects and phases, balancing utilization (target 70-80% to preserve slack for unplanned work), skill growth, and key-person risk. Deliverable: draft allocation plan.
4. **Validate with leads**: Review proposed allocations with tech leads to confirm feasibility and flag conflicts. Deliverable: validated allocation plan.
5. **Publish and communicate**: Finalize allocations and communicate to all affected teams. Deliverable: published allocation plan with start dates.

## Anti-Patterns

- **100% utilization targeting**: Allocating every engineer to full capacity with no slack. *Why*: zero slack means any unplanned work (bugs, incidents, support) immediately creates schedule slips.
- **Hero dependency**: Assigning critical-path work to a single engineer without backup. *Why*: key-person risk turns PTO or attrition into delivery crises.
- **Skill hoarding**: Always assigning the same expert to the same type of work. *Why*: it optimizes short-term velocity at the cost of bus factor and team growth.

## Output

**On success**: Produces an allocation plan containing engineer assignments by project and phase, utilization percentages, identified skill gaps, and key-person risk flags. Delivered to engineering leadership and tech leads.

**On failure**: Report which roles could not be staffed, the impact on delivery timelines, and recommended mitigations (hiring, scope reduction, timeline extension).

## Related Skills

- [`effort-estimator-eng`](../../../engineering/vp-engineering/effort-estimator-eng/SKILL.md) -- effort estimates determine how many engineers are needed.
- [`phase-planner-eng`](../../../engineering/vp-engineering/phase-planner-eng/SKILL.md) -- phase plans define the timeline that allocations must fit.
