---
name: internal-demo-design
description: >
  This skill runs internal design showcases to align stakeholders on design direction. Use
  when asked to present design work to leadership, demo a prototype to the wider team, or
  facilitate a design show-and-tell. Also consider when a major design direction change needs
  cross-functional buy-in. Suggest when a design initiative has been running for multiple
  sprints without stakeholder visibility.
department: design
agent: head-of-design
version: 1.0.0
complexity: simple
related-skills: []
triggers:
  - "design demo"
  - "demo the design"
  - "internal design demo"
  - "present design"
  - "design showcase"
---

# internal-demo-design

## Agent: Head of Design

L1 design leader (1x) responsible for design strategy, review governance, and accessibility oversight. Oversees UX Research and Content Design as sub-disciplines reporting into Design.

Department ethos: [ideal-design.md](../../../../departments/design/ideal-design.md)

## Skill Description

Runs internal design showcases to align stakeholders on design direction, surface cross-functional feedback early, and build shared understanding of design rationale.

## When to Use

- When a design initiative reaches a milestone that warrants cross-functional visibility (concept exploration complete, visual direction chosen, prototype ready).
- When leadership or adjacent teams have not seen design progress and alignment risk is growing.
- When the design team wants to share reusable patterns, system updates, or process improvements with the wider organization.

## Workflow

1. **Define demo objectives**: Clarify what decision or alignment the demo should achieve -- directional buy-in, feedback on a specific interaction, awareness of a system update. Select the appropriate demo type from the [demo framework](references/demo-framework.md). Deliverable: demo brief with objectives and audience list.
2. **Prepare demo materials**: Assemble the prototype, Figma walkthrough, or presentation. Structure the narrative following the problem → rationale → open questions format in the [demo framework](references/demo-framework.md). Calibrate prototype fidelity to the demo objective. Deliverable: demo deck or interactive prototype with speaker notes.
3. **Facilitate the session**: Present the work, narrate design decisions and tradeoffs, and guide the audience through interactive elements. Use the feedback collection format from the [demo framework](references/demo-framework.md) to capture actionable items in real time. Deliverable: session recording and raw feedback notes.
4. **Synthesize and distribute**: Compile feedback into themes, identify action items, and share a summary with attendees and the broader design team within 24 hours. Deliverable: demo summary with feedback themes and next steps.

## Anti-Patterns

- **Demo without context**: Showing screens without explaining the problem being solved, the user need, or the design constraints. *Why*: stakeholders cannot give useful feedback on a solution when they do not understand the problem; feedback becomes aesthetic opinion.
- **Treating demos as approval gates**: Using the showcase as a decision-making meeting instead of an alignment and feedback opportunity. *Why*: demos that require sign-off create pressure to present polished work only, which kills early-stage feedback when it is most valuable.
- **Skipping open questions**: Presenting only decisions already made without surfacing areas of uncertainty. *Why*: the primary value of a demo is cross-functional input; withholding open questions wastes the audience's expertise.

## Output

**On success**: Produces a demo summary containing key feedback themes, action items with owners, decisions confirmed, and open questions to resolve. Delivered to all attendees and the design team channel.

**On failure**: Report why the demo could not be completed (missing prototype, unavailable stakeholders, unclear objectives), what was partially shown, and a proposed reschedule date.

## Related Skills

- [`design-review-runner`](../design-review-runner/SKILL.md) -- Demos generate feedback that may feed into formal design reviews.
- [`inter-phase-design-reviewer`](../inter-phase-design-reviewer/SKILL.md) -- Phase gate reviews may follow a demo that surfaces blocking concerns.
