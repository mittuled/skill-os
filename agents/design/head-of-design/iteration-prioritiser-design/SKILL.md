---
name: iteration-prioritiser-design
description: >
  This skill prioritises the design iteration backlog based on user feedback, usability data,
  and business impact. Use when asked to rank design improvements, triage post-launch feedback
  into the design backlog, or decide which design debt to address next. Also consider when
  the iteration backlog has grown without a clear priority order. Suggest when session
  analysis or accessibility audit findings need to be sequenced for action.
department: design
agent: head-of-design
version: 1.0.0
complexity: medium
related-skills:
  - accessibility-auditor-design
  - iteration-design-p
  - effort-estimator-design
triggers:
  - "prioritise design iterations"
  - "design iteration priority"
  - "rank design changes"
  - "prioritise design work"
  - "design backlog prioritisation"
---

# iteration-prioritiser-design

## Agent: Head of Design

L1 design leader (1x) responsible for design strategy, review governance, and accessibility oversight. Oversees UX Research and Content Design as sub-disciplines reporting into Design.

Department ethos: [ideal-design.md](../../../../departments/design/ideal-design.md)

## Skill Description

Prioritises the design iteration backlog by scoring improvement candidates against user impact, business value, design effort, and accessibility severity.

## When to Use

- When the design iteration backlog contains more items than the team can address in the current cycle and sequencing decisions are needed.
- When post-launch user feedback, session analysis, or accessibility audit findings generate a batch of design improvements that need ranking.
- When product or engineering requests a prioritized list of design changes for sprint planning.

## Workflow

1. **Inventory backlog items**: Collect all pending design iterations from feedback channels, audit reports, session analysis findings, and stakeholder requests. Normalize each item using the format defined in the [prioritisation framework](references/prioritisation-framework.md): problem statement, affected surface, and source. Deliverable: normalized iteration backlog.
2. **Score each item**: Apply the weighted scoring model from the [prioritisation framework](references/prioritisation-framework.md) — user impact (35%), business value (25%), effort inversion (25%), and accessibility severity (15%). Every score must cite a source. Deliverable: scored backlog with rationale per item.
3. **Apply prioritization framework**: Assign items to P0/P1/P2/P3 tiers per the composite score thresholds in the [prioritisation framework](references/prioritisation-framework.md). Deliverable: tiered priority list.
4. **Validate with stakeholders**: Share the proposed prioritization with product and engineering to confirm alignment with roadmap and technical constraints. Adjust based on dependencies or conflicting priorities. Deliverable: agreed-upon prioritized backlog.
5. **Communicate and track**: Publish the prioritized list to the team, update backlog tooling, and establish a re-prioritization cadence per the trigger conditions in the [prioritisation framework](references/prioritisation-framework.md). Deliverable: published priority list with review schedule.

## Anti-Patterns

- **Loudest-voice prioritization**: Ranking items based on who requested them rather than evidence of user or business impact. *Why*: stakeholder volume does not correlate with user need; this approach neglects the users who are not in the room.
- **Ignoring design debt**: Perpetually deprioritizing design system inconsistencies, accessibility gaps, and interaction state completeness in favor of new feature work. *Why*: design debt compounds; inconsistent patterns slow future design work and erode user trust.
- **Static priority lists**: Setting priorities once and never revisiting as new data arrives. *Why*: user feedback, analytics, and business context change continuously; stale priorities lead to wasted effort on superseded problems.

## Output

**On success**: Produces a tiered, scored design iteration backlog with rationale for each priority decision, stakeholder alignment confirmation, and a scheduled re-prioritization cadence. Delivered to design, product, and engineering leads.

**On failure**: Report which backlog items could not be scored (missing user data, undefined business metrics, unclear scope), what partial prioritization was achieved, and what data is needed to complete the ranking.

## Related Skills

- [`accessibility-auditor-design`](../accessibility-auditor-design/SKILL.md) -- Audit findings are a primary input to the iteration backlog.
- [`iteration-design-p`](../../../design/visual-interaction-designer/iteration-design-p/SKILL.md) -- Prioritized items flow to the Visual Interaction Designer for execution.
- [`effort-estimator-design`](../effort-estimator-design/SKILL.md) -- Effort estimates are a required input to the prioritization scoring rubric.
