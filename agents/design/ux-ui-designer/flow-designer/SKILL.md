---
name: flow-designer
description: >
  This skill creates detailed interaction flows for specific user journeys. Use when asked
  to design a task flow, map micro-interactions within a journey, or specify step-by-step
  interaction sequences. Also consider when a wireframe needs interaction detail added. Suggest
  when a prototype is being built without documented interaction flows.
department: design
agent: ux-ui-designer
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "design the user flow"
  - "map the interaction flow"
  - "create a task flow for this journey"
  - "how should this flow work step by step"
---

# flow-designer

## Agent: UX/UI Designer

L2 UX/UI designer (Nx) responsible for user flow design, wireframing, prototyping, and component mapping.

Department ethos: [ideal-design.md](../../../../departments/design/ideal-design.md)

## Skill Description

Creates detailed interaction flows that specify the step-by-step sequences, decision points, branching logic, and micro-interactions within specific user journeys.

## When to Use

- When a user journey has been identified and needs detailed interaction-level design (screen transitions, input validation sequences, progressive disclosure steps).
- When a wireframe or visual design needs interaction annotation -- what happens on tap, swipe, long-press, or keyboard shortcut.
- When engineering requests precise interaction specifications to implement a complex multi-step flow (onboarding, checkout, multi-part form).
- When usability testing reveals confusion in a flow and the interaction sequence needs redesign.

## Workflow

1. **Define flow scope**: Identify the user journey, entry points, and exit points. Clarify the task the user is completing and the success criteria. Deliverable: flow scope statement with entry/exit conditions.
2. **Map decision points and branches**: Document every decision the user or system makes during the flow. Include conditional paths (validation errors, permission requests, empty data), edge cases (timeout, connectivity loss), and alternative paths. Deliverable: flow diagram with decision nodes and branch conditions.
3. **Specify interactions per step**: For each step, define the trigger (tap, swipe, keyboard, system event), the response (animation, state change, navigation), timing (duration, easing), and feedback (haptic, visual, auditory). Deliverable: interaction specification table per step.
4. **Annotate error and recovery paths**: Design what happens when things go wrong at each step -- validation failure, API error, timeout. Specify recovery actions available to the user. Deliverable: error path annotations added to flow diagram.
5. **Validate against heuristics**: Check the flow against Nielsen's heuristics -- visibility of system status, user control, error prevention, recognition over recall. Deliverable: heuristic evaluation notes with recommended refinements.

## Anti-Patterns

- **Happy-path-only flows**: Designing only the ideal sequence and ignoring error, edge case, and recovery paths. *Why*: users encounter errors frequently; undesigned error states force engineering to improvise, producing inconsistent and confusing experiences.
- **Over-specified micro-interactions**: Defining animation curves and timing for every minor state change regardless of user impact. *Why*: excessive specification slows both design and engineering without proportional user benefit; focus interaction detail where it matters (transitions, feedback, orientation).
- **Flows without context**: Designing interaction sequences disconnected from the broader user journey and entry/exit conditions. *Why*: a flow that starts at "step 1" without specifying how the user arrived cannot account for context-dependent behavior.

## Output

**On success**: Produces a flow diagram with decision nodes and branching logic, an interaction specification table per step, error and recovery path annotations, and heuristic evaluation notes. Delivered as annotated Figma pages linked to the relevant prototype.

**On failure**: Report which parts of the flow could not be specified (undefined business rules, missing API behavior documentation, unresolved product decisions), what partial flow was created, and the questions that must be answered.

## Related Skills

- [`ux-flow-designer`](../ux-flow-designer/SKILL.md) -- End-to-end user flows provide the high-level structure that interaction flows detail.
- [`prototype-creator`](../prototype-creator/SKILL.md) -- Interaction flows are the specification that prototypes bring to life.
- [`wireframe-builder`](../wireframe-builder/SKILL.md) -- Wireframes define layout; flow design adds interaction behavior on top.
