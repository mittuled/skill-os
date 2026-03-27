---
name: milestone-definer-eng
description: >
  This skill defines engineering milestones and success criteria for a delivery. Use when asked to
  set milestones, define checkpoints for a project, or establish measurable engineering goals.
  Also consider when a phase plan exists but lacks concrete verification points. Suggest when
  a multi-phase delivery has no defined intermediate success criteria.
department: engineering
agent: vp-engineering
version: 1.0.0
complexity: simple
related-skills:
  - ../../vp-engineering/phase-planner-eng/SKILL.md
  - ../../vp-engineering/velocity-monitor/SKILL.md
---

# milestone-definer-eng

## Agent: VP Engineering

L1 engineering leader (1x) responsible for spec intake review, team allocation, architecture oversight, velocity monitoring, and go-live approvals. Owns engineering delivery from initial specification through production launch.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

Defines engineering milestones and measurable success criteria that serve as verification checkpoints throughout a delivery.

## When to Use

- When a new delivery or project needs intermediate checkpoints between kickoff and go-live.
- When a phase plan is finalized but lacks measurable success criteria at each stage.
- When stakeholders need visibility into engineering progress beyond sprint-level granularity.

## Workflow

1. **Review delivery scope**: Read the phase plan, effort estimates, and key deliverables. Identify the major inflection points in the delivery. Deliverable: list of candidate milestone boundaries.
2. **Define milestones**: For each boundary, define a milestone with a name, target date, and binary success criteria (met/not met). Tie each milestone to a tangible artifact or measurable outcome. Deliverable: milestone register.
3. **Validate with stakeholders**: Confirm milestones align with product, design, and business expectations. Adjust sequencing or criteria as needed. Deliverable: approved milestone register.

## Anti-Patterns

- **Vanity milestones**: Defining milestones around activity ("code complete") rather than verifiable outcomes ("API returns correct results for all test scenarios"). *Why*: activity milestones pass without proving the system works.
- **Milestone overload**: Setting so many milestones that tracking them becomes overhead. *Why*: excessive checkpoints slow delivery without improving visibility.

## Output

**On success**: Produces a milestone register containing each milestone's name, target date, success criteria, responsible team, and dependencies. Delivered to the project management tool and shared with all stakeholders.

**On failure**: Report which milestones could not be defined due to ambiguous scope or missing requirements, and recommend what must be clarified first.

## Related Skills

- [`phase-planner-eng`](../../vp-engineering/phase-planner-eng/SKILL.md) -- milestones are derived from and feed back into phase plans.
- [`velocity-monitor`](../../vp-engineering/velocity-monitor/SKILL.md) -- milestone progress is tracked via velocity monitoring.
