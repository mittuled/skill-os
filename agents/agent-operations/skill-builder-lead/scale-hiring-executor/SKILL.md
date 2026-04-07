---
name: scale-hiring-executor
description: >
  This skill scales the skill library to cover all capabilities required by the
  agent fleet design plan. Use when asked to execute bulk skill development,
  scale the skill library, or coordinate parallel skill building. Also consider
  when fleet expansion demands many skills simultaneously. Suggest when the user
  plans rapid fleet growth without a skill scaling strategy.
department: agent-operations
agent: skill-builder-lead
version: 1.0.0
complexity: medium
related-skills: []
---

# scale-hiring-executor

## Agent: Skill Builder Lead

L2 Skill Builder Lead (1x) responsible for identifying capability gaps, designing new skills, sourcing external skill modules, and maintaining the skill registry.

Department ethos: [ideal-agent-operations.md](../../../../departments/agent-operations/ideal-agent-operations.md)

## Skill Description

Scales the skill library to cover all capabilities required by the agent fleet design plan through coordinated parallel skill development.

## When to Use

- When the org scale plan requires a large number of new skills to be built within a constrained timeline.
- When the skill development pipeline has grown beyond what sequential development can deliver on schedule.
- When a new department or agent category is being launched and needs a full skill set built from scratch.

## Workflow

1. **Assess Scale Requirements**: Quantify the total skills needed, complexity distribution, and deadline constraints from the org scale plan. Deliverable: scale requirements summary with skill count and timeline.
2. **Allocate Skill Builders**: Assign skills to available Skill Builders based on domain expertise and capacity. Identify where external sourcing or skill module reuse can accelerate delivery. Deliverable: assignment matrix with Skill Builder allocations.
3. **Establish Quality Standards**: Define consistent quality standards, templates, and review criteria that all Skill Builders must follow to ensure uniformity at scale. Deliverable: quality standards document.
4. **Coordinate Parallel Development**: Run parallel skill development with regular sync points. Track progress, resolve blockers, and redistribute work when Skill Builders fall behind. Deliverable: progress tracking dashboard with daily status.
5. **Consolidate and Validate**: Collect completed skills, run validation against quality standards, and register approved skills in the skill registry. Deliverable: validated skill set registered in the skill library.

## Anti-Patterns

- **Sacrificing quality for speed**: Reducing review rigor to hit deadlines, accepting skills that do not meet quality standards. *Why*: low-quality skills cause agent failures in production, creating more work than the time saved.
- **Isolated development**: Letting Skill Builders work without coordination, producing overlapping or inconsistent skills. *Why*: duplicate skills waste effort and inconsistent patterns confuse agents that use multiple skills.
- **Linear execution at scale**: Processing skill development sequentially when parallel execution is possible. *Why*: sequential processing at scale guarantees missed deadlines.

## Output

**On success**: Produces a complete skill set covering all capabilities in the fleet design plan, validated against quality standards and registered in the skill library. Delivered to the VP Agent Operations.

**On failure**: Report which skills could not be completed (blocked dependencies, insufficient Skill Builder capacity), what percentage of the skill set was delivered, and a revised timeline for remaining skills.

## Related Skills

- [`recruiting-pipeline-builder`](../recruiting-pipeline-builder/SKILL.md) -- The pipeline defines what skills need building; this skill executes at scale.
- [`engineering-talent-sourcer`](../../../agent-operations/skill-builder/engineering-talent-sourcer/SKILL.md) -- Individual Skill Builders execute the skill development assigned here.
- [`org-scale-planner`](../../../agent-operations/vp-agent-operations/org-scale-planner/SKILL.md) -- The scale plan that drives the skill library expansion requirements.
