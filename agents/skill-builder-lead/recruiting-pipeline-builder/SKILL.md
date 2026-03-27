---
name: recruiting-pipeline-builder
description: >
  This skill builds the active skill development pipeline for every capability
  gap before the delivery phase needs it. Use when asked to plan skill
  development, prioritize capability gaps, or create a skill backlog. Also
  consider when new agent roles are planned but skills are undefined. Suggest
  when the user adds agents to the fleet without queuing skill development.
department: agent-operations
agent: skill-builder-lead
version: 1.0.0
complexity: medium
related-skills: []
---

# recruiting-pipeline-builder

## Agent: Skill Builder Lead

L2 Skill Builder Lead (1x) responsible for identifying capability gaps, designing new skills, sourcing external skill modules, and maintaining the skill registry.

Department ethos: [ideal-agent-operations.md](../../../departments/agent-operations/ideal-agent-operations.md)

## Skill Description

Builds the active skill development pipeline for every capability gap before the delivery phase needs it.

## When to Use

- When a capability assessment reveals gaps that require new skills to be built.
- When a new delivery phase is approaching and the skill backlog needs prioritization against deadlines.
- When multiple Skill Builders need coordinated work assignments to avoid duplication and ensure coverage.

## Workflow

1. **Intake Capability Gaps**: Collect all capability gaps from the team capability assessor, hiring plan, and agent health reports. Deduplicate and categorize by domain and urgency. Deliverable: prioritized capability gap backlog.
2. **Define Skill Specifications**: For each gap, write a skill specification: what the skill must do, acceptance criteria, complexity estimate, and target agent. Deliverable: skill specification per gap.
3. **Sequence Pipeline**: Order skill development by delivery phase deadlines, dependency chains, and Skill Builder availability. Assign each skill to a Skill Builder. Deliverable: skill development pipeline with assignments and target dates.
4. **Track Progress**: Monitor Skill Builder progress against the pipeline schedule. Identify blocked or at-risk skills early. Deliverable: pipeline status report with blockers.
5. **Quality Gate**: Review completed skills against specifications before they enter the skill registry. Reject skills that do not meet acceptance criteria. Deliverable: quality gate results with approval or revision notes.

## Anti-Patterns

- **Reactive pipeline**: Building skills only after delivery is blocked, instead of maintaining a forward-looking pipeline. *Why*: reactive development creates emergency pressure that degrades skill quality.
- **Pipeline without specifications**: Assigning skill development with vague descriptions instead of clear specifications. *Why*: Skill Builders without clear specs produce skills that miss the actual capability need.
- **Ignoring dependencies**: Sequencing skills independently without considering which skills depend on others. *Why*: a downstream skill cannot be tested if its upstream dependency is not yet built.

## Output

**On success**: Produces a skill development pipeline containing prioritized gap backlog, skill specifications, assignments, and timeline. Delivered to the VP Agent Operations and Skill Builders.

**On failure**: Report which gaps could not be specified (ambiguous requirements, missing domain expertise), what pipeline was built, and what inputs are needed to complete specifications.

## Related Skills

- [`team-capability-assessor`](../../vp-agent-operations/team-capability-assessor/SKILL.md) -- Provides the capability gaps that feed the pipeline.
- [`scale-hiring-executor`](../scale-hiring-executor/SKILL.md) -- Executes the pipeline at scale when many skills are needed simultaneously.
- [`engineering-talent-sourcer`](../../skill-builder/engineering-talent-sourcer/SKILL.md) -- Individual Skill Builders execute assignments from this pipeline.
