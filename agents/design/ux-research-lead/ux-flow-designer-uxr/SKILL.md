---
name: ux-flow-designer-uxr
description: >
  This skill designs user flows informed by research findings. Use when asked to create user
  flows, map interaction paths, or design task flows for a feature. Also consider when a
  product has user stories but no visualised flow showing how users move through the
  experience. Suggest when the user is about to build UI screens without a documented
  flow connecting them.
department: design
agent: ux-research-lead
version: 1.0.0
complexity: medium
related-skills: []
---

# ux-flow-designer-uxr

## Agent: UX Research Lead

L2 UX research lead (1x) (moved from Product, now reports to Head of Design) responsible for planning and leading user research to directly inform design decisions.

Department ethos: [ideal-design.md](../../../../departments/design/ideal-design.md)

## Skill Description

Designs user flows informed by research findings, mapping the paths users take through a product experience to accomplish their jobs-to-be-done.

## When to Use

- When user stories and JTBD insights are ready and the design team needs visualised flows before starting screen-level UI design.
- When an existing user flow has known usability issues (identified through testing or analytics) and needs to be redesigned with research-backed improvements.
- When a new feature spans multiple screens or states and the team needs a shared understanding of the interaction sequence before wireframing.

## Workflow

1. **Input Assembly**: Gather user stories, JTBD framework, research insights, and any existing analytics (funnel data, heatmaps) relevant to the flow being designed. Deliverable: flow design brief with research inputs listed.
2. **Happy Path Mapping**: Map the primary user flow (happy path) as a sequence of user actions, system responses, and state transitions. Annotate each step with the user's goal at that moment. Deliverable: happy path flow diagram.
3. **Edge Case & Error Path Mapping**: Identify and map branching paths: error states, empty states, permission boundaries, and alternative paths based on user segment or context. Deliverable: complete flow diagram with all paths.
4. **Research Validation**: Cross-reference the designed flow against research findings. Verify that the flow addresses known pain points, matches observed mental models, and does not introduce patterns users struggled with in testing. Deliverable: research-validated flow with annotations.
5. **Design Team Review**: Walk through the flow with the UI design team to ensure it is implementable and to surface any interaction questions before wireframing begins. Deliverable: reviewed and approved flow diagram.

## Anti-Patterns

- **Happy-path-only design**: Mapping only the ideal path without considering errors, edge cases, or alternative routes. *Why*: users rarely follow the happy path exclusively; unmapped edge cases become undefined UI states that engineering implements inconsistently.
- **Flow without research grounding**: Designing flows based on logical assumptions rather than observed user behaviour and mental models. *Why*: logically correct flows that contradict user expectations create confusion even when they are technically efficient.
- **Over-detailed flows**: Including implementation-level detail (API calls, database writes) in user flow diagrams. *Why*: implementation detail clutters the flow and shifts the conversation from user experience to technical architecture.
- **Skipping the review handoff**: Delivering flow diagrams to the UI team without a walkthrough. *Why*: flow diagrams contain implicit decisions that are only surfaced through conversation; silent handoffs produce misinterpretations.

## Output

**On success**: Produces a complete user flow diagram containing happy path, error and edge case paths, state transitions, and research-validation annotations. Delivered as a shareable diagram (Figma, FigJam, or Miro) with a design team walkthrough.

**On failure**: Report which flow segments could not be designed due to missing inputs (e.g., undefined business rules, insufficient research on a user segment), what assumptions were made, and recommend specific inputs needed to complete the flow.

## Related Skills

- [`jtbd-to-stories-uxr`](../jtbd-to-stories-uxr/SKILL.md) — User stories and requirements provide the input for flow design.
- [`prototype-usability-validator`](../prototype-usability-validator/SKILL.md) — Designed flows are prototyped and validated through usability testing.
- [`feedback-loop-formaliser-uxr`](../../../design/ux-researcher/feedback-loop-formaliser-uxr/SKILL.md) — Post-launch feedback on flows feeds back into flow redesign.
