---
name: jtbd-to-stories-uxr
description: >
  This skill translates jobs-to-be-done insights into design requirements and user stories.
  Use when asked to convert JTBD findings into actionable stories, write design requirements
  from research, or bridge research insights to product backlog items. Also consider when
  engineering needs user stories grounded in research rather than assumptions. Suggest when
  the user is about to write user stories without referencing the JTBD framework.
department: design
agent: ux-research-lead
version: 1.0.0
complexity: medium
related-skills: []
---

# jtbd-to-stories-uxr

## Agent: UX Research Lead

L2 UX research lead (1x) (moved from Product, now reports to Head of Design) responsible for planning and leading user research to directly inform design decisions.

Department ethos: [ideal-design.md](../../../../departments/design/ideal-design.md)

## Skill Description

Translates jobs-to-be-done insights into design requirements and user stories that give product and engineering teams research-grounded direction for what to build.

## When to Use

- When a JTBD framework has been completed and the product team needs actionable user stories to begin design and development work.
- When existing user stories feel disconnected from user research and need to be rewritten or validated against JTBD findings.
- When a new product area needs its initial set of user stories derived from research rather than stakeholder assumptions.

## Workflow

1. **JTBD Review**: Review the prioritised JTBD framework, focusing on the highest-priority jobs and their associated outcomes and pain points. Identify which jobs map to the current product scope. Deliverable: scoped job selection with prioritisation rationale.
2. **Outcome Decomposition**: Break each selected job's desired outcomes into discrete, testable design requirements. Each requirement should describe a user-observable behaviour, not an implementation detail. Deliverable: design requirements list mapped to jobs.
3. **User Story Writing**: Write user stories in the format: "As a [persona/segment], I want to [action], so that [outcome from JTBD]." Include acceptance criteria derived from the outcome metrics identified in the JTBD framework. Deliverable: user story set with acceptance criteria.
4. **Context & Constraint Annotation**: Annotate each story with the research context: which interviews or data points support it, what circumstances trigger the job, and any constraints or edge cases identified in research. Deliverable: annotated story cards.
5. **Design Team Handoff**: Review the story set with the design team to ensure the requirements are clear enough to begin ideation without ambiguity. Resolve any questions about user intent or scope. Deliverable: design-ready story backlog.

## Anti-Patterns

- **Implementation-prescriptive stories**: Writing stories that specify UI solutions ("I want a dropdown to filter") instead of user outcomes ("I want to narrow results to what's relevant"). *Why*: prescriptive stories constrain design exploration and may encode suboptimal solutions.
- **Orphaned stories**: Writing user stories without tracing them back to specific JTBD data. *Why*: stories without research provenance are indistinguishable from assumptions and lose the evidentiary advantage of the JTBD process.
- **Oversized stories**: Combining multiple jobs or outcomes into single large stories. *Why*: large stories resist estimation, delay validation, and make it impossible to measure which job outcome is being served.
- **Skipping acceptance criteria**: Delivering stories without measurable acceptance criteria tied to JTBD outcomes. *Why*: without criteria, the team cannot verify whether the implementation actually serves the user job.

## Output

**On success**: Produces a design-ready user story backlog containing stories mapped to JTBD, acceptance criteria derived from outcome metrics, research context annotations, and prioritisation. Delivered as structured backlog items in the team's project management tool or as a shared document.

**On failure**: Report which jobs could not be translated into stories (e.g., job too abstract, insufficient outcome data), what additional research or stakeholder input is needed, and recommend specific follow-up activities.

## Related Skills

- [`jtbd-mapper`](../jtbd-mapper/SKILL.md) — Produces the JTBD framework this skill consumes.
- [`ux-flow-designer-uxr`](../ux-flow-designer-uxr/SKILL.md) — User flows are designed from the stories and requirements produced here.
- [`prototype-usability-validator`](../prototype-usability-validator/SKILL.md) — Usability testing validates whether implementations satisfy the story acceptance criteria.
