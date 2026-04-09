---
name: phase-planner-eng
description: >
  This skill plans the engineering activities and milestones for each delivery phase. Use when asked
  to create a phase plan, define the engineering roadmap for a delivery, or sequence work across
  sprints. Also consider when effort estimates and team allocations are ready but no execution
  timeline exists. Suggest when a project is about to start execution without a structured phase plan.
department: engineering
agent: vp-engineering
version: 1.0.0
complexity: medium
related-skills:
  - ../../../engineering/vp-engineering/effort-estimator-eng/SKILL.md
  - ../../../engineering/vp-engineering/milestone-definer-eng/SKILL.md
  - ../team-allocator/SKILL.md
triggers:
  - "plan engineering phase"
  - "phase planning"
  - "engineering phase plan"
  - "sprint phase plan"
  - "delivery phase planning"
---

# phase-planner-eng

## Agent: VP Engineering

L1 engineering leader (1x) responsible for spec intake review, team allocation, architecture oversight, velocity monitoring, and go-live approvals. Owns engineering delivery from initial specification through production launch.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Plans the engineering activities, milestones, and sprint allocation for each delivery phase, producing a sequenced execution timeline.

## When to Use

- When an approved spec has effort estimates and team allocations but no execution timeline.
- When a multi-phase delivery needs its phases defined with clear boundaries and handoff criteria.
- When a delivery is being re-planned after a significant scope change or team reallocation.

## Workflow

1. **Collect inputs**: Gather effort estimates, team allocation, dependency map, architecture decisions, and milestone definitions. Deliverable: planning inputs checklist.
2. **Define phase boundaries**: Divide the delivery into phases with clear entry and exit criteria. Align boundaries to meaningful integration points or demo-able increments. Deliverable: phase boundary definitions.
3. **Sequence activities**: Map tasks to sprints within each phase, respecting dependency ordering and team capacity. Identify the critical path. Deliverable: sprint-level activity timeline with critical path highlighted.
4. **Identify phase risks**: Flag risks specific to each phase (e.g., key-person dependency, external API availability, infrastructure provisioning lead time). Deliverable: per-phase risk annotations.
5. **Publish plan**: Document the phase plan with timeline, milestones, team assignments, and risk callouts. Deliverable: phase plan document distributed to all stakeholders.

## Anti-Patterns

- **Waterfall in disguise**: Creating sequential phases where each phase is a monolithic block with no iterative feedback loops. *Why*: large phases without checkpoints hide problems until they are expensive to fix.
- **Ignoring the critical path**: Planning without identifying which tasks are on the critical path. *Why*: non-critical-path optimizations waste effort while the actual bottleneck goes unaddressed.
- **Calendar-stuffing**: Filling every sprint to 100% capacity with zero slack. *Why*: no slack means no ability to absorb surprises, turning every unexpected issue into a schedule slip.

## Output

**On success**: Produces a phase plan document containing phase boundaries with entry/exit criteria, sprint-level activity timeline, critical path, milestone dates, team assignments, and risk annotations. Delivered to the project management tool and stakeholders.

**On failure**: Report which planning inputs are missing or inconsistent, the impact on plan reliability, and what must be resolved before planning can complete.

## Related Skills

- [`effort-estimator-eng`](../../../engineering/vp-engineering/effort-estimator-eng/SKILL.md) -- effort estimates are a required input to phase planning.
- [`milestone-definer-eng`](../../../engineering/vp-engineering/milestone-definer-eng/SKILL.md) -- milestones defined here anchor the phase plan.
