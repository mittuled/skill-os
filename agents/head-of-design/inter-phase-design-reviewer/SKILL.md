---
name: inter-phase-design-reviewer
description: >
  This skill reviews design deliverables at phase boundaries before progression to the next
  stage. Use when asked to gate a design between discovery and definition, definition and
  production, or production and handoff. Also consider when a project is about to transition
  phases without a formal design quality check. Suggest when a design moves from wireframes
  to visual design without documented approval.
department: design
agent: head-of-design
version: 1.0.0
complexity: medium
related-skills: []
---

# inter-phase-design-reviewer

## Agent: Head of Design

L1 design leader (1x) responsible for design strategy, review governance, and accessibility oversight. Oversees UX Research and Content Design as sub-disciplines reporting into Design.

Department ethos: [ideal-design.md](../../../departments/design/ideal-design.md)

## Skill Description

Reviews design deliverables at phase boundaries to ensure quality, completeness, and readiness criteria are met before the project progresses to the next design or development phase.

## When to Use

- When a design project is transitioning between phases (discovery to definition, definition to production, production to handoff).
- When a milestone review is required by the project governance framework before committing resources to the next phase.
- When a previously paused project resumes and the existing design artifacts need revalidation against current standards.

## Workflow

1. **Identify phase exit criteria**: Retrieve the expected deliverables and quality bar for the current phase. Map each criterion to a verifiable artifact (Figma file, user flow document, research synthesis, prototype). Deliverable: phase exit checklist.
2. **Collect deliverables**: Gather all design artifacts produced during the phase. Verify completeness against the checklist -- missing items are automatic blockers. Deliverable: deliverable inventory with gap flags.
3. **Evaluate quality**: Assess each deliverable against design system compliance, accessibility standards, interaction completeness (all states documented), content readiness, and alignment with the product brief. Deliverable: quality assessment per deliverable.
4. **Document findings**: Record issues as blocking (must resolve before progression) or advisory (can address in the next phase with tracked tickets). Deliverable: phase review findings document.
5. **Issue phase gate decision**: Approve progression, conditionally approve with mandatory fixes, or block with required rework scope. Communicate to project stakeholders. Deliverable: phase gate verdict with rationale.

## Anti-Patterns

- **Rubber-stamping**: Approving phase transitions without thoroughly inspecting deliverables because the timeline is tight. *Why*: undiscovered gaps compound across phases; a missing interaction state in definition becomes a production crisis at handoff.
- **Moving goalposts**: Introducing new criteria at the gate that were not part of the original phase definition. *Why*: designers cannot hit a target they did not know existed; new requirements belong in the next phase scope, not as retroactive blockers.
- **Phase gate as single point of failure**: Making the Head of Design the only reviewer, creating a bottleneck. *Why*: single-reviewer gates slow velocity and miss domain-specific issues that product or engineering reviewers would catch.

## Output

**On success**: Produces a phase gate decision document containing the exit checklist with pass/fail per criterion, blocking and advisory findings, and a clear progression verdict. Delivered to the project team, product manager, and engineering lead.

**On failure**: Report which deliverables could not be evaluated, the reason (missing artifacts, inaccessible files, undefined phase criteria), and what must be provided to complete the gate review.

## Related Skills

- [`design-review-runner`](../design-review-runner/SKILL.md) -- Phase gate reviews build on the same review mechanics but with higher-stakes progression decisions.
- [`accessibility-checker-design`](../accessibility-checker-design/SKILL.md) -- Accessibility compliance is a standing phase gate criterion.
- [`effort-estimator-design`](../effort-estimator-design/SKILL.md) -- Phase gate outcomes may trigger re-estimation of remaining design effort.
