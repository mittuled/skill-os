---
name: design-review-runner
description: >
  This skill facilitates design reviews to assess quality, consistency, and alignment with
  product goals. Use when asked to run a design crit, evaluate a deliverable against design
  system standards, or assess whether a design is ready for handoff. Also consider when
  multiple designers are working on the same surface and consistency is at risk. Suggest
  when a design file has not been reviewed before entering dev-ready status.
department: design
agent: head-of-design
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "run a design review"
  - "crit this design"
  - "is this design ready for handoff"
  - "check design against the system"
---

# design-review-runner

## Agent: Head of Design

L1 design leader (1x) responsible for design strategy, review governance, and accessibility oversight. Oversees UX Research and Content Design as sub-disciplines reporting into Design.

Department ethos: [ideal-design.md](../../../../departments/design/ideal-design.md)

## Skill Description

Facilitates structured design reviews to assess quality, design system consistency, accessibility compliance, and alignment with product goals before progression.

## When to Use

- When a design deliverable reaches a review milestone (wireframe review, visual review, pre-handoff review).
- When cross-functional stakeholders need alignment on a design direction before committing engineering resources.
- When multiple designers contribute to the same product area and consistency must be validated.
- When a design has been revised significantly and needs re-evaluation against original acceptance criteria.

## Workflow

1. **Set review scope and criteria**: Define the review type (exploratory, refinement, or pre-handoff), the specific screens or flows under review, and the evaluation criteria (design system compliance, accessibility, interaction completeness, content quality). Use the [scoring rubric](references/scoring-rubric.md) to anchor criteria weights. Deliverable: review agenda with criteria checklist.
2. **Prepare review artifacts**: Ensure the Figma file is up to date, prototypes are linked, and any relevant user research or competitive analysis is referenced. Verify component usage against the design system library. Deliverable: review-ready artifact package.
3. **Facilitate the review session**: Walk through each screen or flow against the criteria. Capture feedback as actionable items, not opinions. Distinguish between blocking issues (must fix before progression) and suggestions (may address in future iteration). Deliverable: structured feedback log with severity tags.
4. **Synthesize and assign**: Group feedback by theme (visual consistency, interaction gaps, accessibility, content). Assign each action item to the responsible designer with a clear definition of done. Deliverable: action item register with owners.
5. **Issue verdict**: Declare the review outcome -- approved, conditionally approved (with required fixes listed), or requires re-review. Record the outcome in the [design review report template](assets/design-review-report-template.md) and communicate to design, product, and engineering. Deliverable: review verdict document.

## Anti-Patterns

- **Aesthetic debates without criteria**: Allowing review conversations to devolve into subjective preference discussions without referencing design principles, heuristics, or user data. *Why*: opinion-based feedback is not actionable and wastes review time; criteria-grounded feedback improves the design.
- **Skipping interaction states**: Reviewing only the happy-path visual and ignoring empty states, error states, loading states, and edge cases. *Why*: engineering will encounter these states during implementation and will improvise if design has not specified them.
- **Review as gatekeeping**: Using the review to assert authority rather than to improve the work collaboratively. *Why*: designers stop bringing work early if reviews feel punitive, which means problems surface later when they are more expensive to fix.

## Output

**On success**: Produces a review verdict (approved / conditional / re-review) with a structured feedback log, action items with owners, and a clear list of blocking issues. Delivered to the designer, product manager, and engineering lead.

**On failure**: Report why the review could not be completed (missing artifacts, unavailable stakeholders, undefined criteria), what was partially reviewed, and the rescheduled review date. Every blocker must have a named owner.

## Related Skills

- [`accessibility-checker-design`](../accessibility-checker-design/SKILL.md) -- Accessibility is a standing review criterion and may trigger a dedicated check.
- [`inter-phase-design-reviewer`](../inter-phase-design-reviewer/SKILL.md) -- Phase gate reviews are a specialized form of design review with higher stakes.
- [`design-implementer-review`](../../../design/ux-ui-designer/design-implementer-review/SKILL.md) -- Post-implementation reviews verify that review feedback was faithfully built.
