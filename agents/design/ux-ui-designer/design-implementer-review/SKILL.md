---
name: design-implementer-review
description: >
  This skill reviews engineering implementations of design to verify fidelity against the
  original design specs. Use when asked to do a design QA pass, check implementation accuracy,
  or verify that redlines and interaction specs were followed. Also consider when a feature
  is in staging and ready for visual inspection. Suggest when engineering marks a UI task
  as complete without a design fidelity check.
department: design
agent: ux-ui-designer
version: 1.0.0
complexity: medium
related-skills: []
---

# design-implementer-review

## Agent: UX/UI Designer

L2 UX/UI designer (Nx) responsible for user flow design, wireframing, prototyping, and component mapping.

Department ethos: [ideal-design.md](../../../../departments/design/ideal-design.md)

## Skill Description

Reviews engineering implementations against design specifications to verify visual fidelity, interaction correctness, and accessibility compliance before release.

## When to Use

- When an engineering implementation reaches staging or review and needs design sign-off on visual and interaction fidelity.
- When a designer needs to verify that redlines, spacing tokens, and typography scales were applied correctly in code.
- When interaction states (hover, focus, active, disabled, error, loading, empty) need verification in the live implementation.
- When a design system component update has been implemented and needs validation against the Figma source of truth.

## Workflow

1. **Prepare comparison baseline**: Open the Figma design specs alongside the staging implementation. Confirm which screens, states, and breakpoints are in scope. Use the [implementation review report template](assets/implementation-review-report-template.md) as the working document throughout the review. Deliverable: populated review scope section.
2. **Check visual fidelity**: Compare spacing, typography (font family, size, weight, line height), colour tokens, border radii, elevation/shadow, and iconography against Figma redlines. Score visual fidelity using the [scoring rubric](references/scoring-rubric.md). Deliverable: visual fidelity checklist with pass/fail per element.
3. **Verify interaction behavior**: Test all interactive states per the interaction state checklist in the [report template](assets/implementation-review-report-template.md) — hover, focus, active, disabled, loading, error, empty. Verify transitions and animations match specified timing. Deliverable: interaction verification checklist.
4. **Test responsive behavior**: Resize the viewport across all specified breakpoints per the responsive checklist in the [report template](assets/implementation-review-report-template.md). Verify layout reflow, content truncation rules, and component adaptation. Deliverable: responsive behavior checklist.
5. **Validate accessibility implementation**: Confirm focus order, ARIA labels, keyboard navigation, colour contrast in the live DOM, and screen reader announcements per the accessibility checklist in the [report template](assets/implementation-review-report-template.md). Deliverable: accessibility implementation checklist.
6. **File deviations and issue verdict**: Document every deviation with a screenshot, expected behaviour (Figma reference), actual behaviour, and severity rating from the [scoring rubric](references/scoring-rubric.md). Issue the review verdict in the [report template](assets/implementation-review-report-template.md). Deliverable: deviation log filed as tickets; completed report delivered to engineer and engineering lead.

## Anti-Patterns

- **Eyeballing without specs**: Reviewing the implementation by "feel" without comparing against specific Figma redlines and token values. *Why*: subjective assessment misses subtle spacing, colour, and typography deviations that compound into a visually inconsistent product.
- **Happy-path-only review**: Checking only the default state and skipping error, loading, empty, and edge case states. *Why*: these states are where implementation most commonly diverges from design because they receive less attention during development.
- **Filing deviations without context**: Reporting "this looks wrong" without specifying the expected value, the Figma reference, and the actual rendered value. *Why*: vague bug reports create back-and-forth between designer and engineer, slowing resolution.

## Output

**On success**: Produces a design implementation review report with visual fidelity, interaction, responsive, and accessibility checklists, plus a deviation log with screenshots and Figma references. Delivered to the implementing engineer and engineering lead, with blocking issues filed as tickets.

**On failure**: Report which aspects of the implementation could not be reviewed (staging not deployed, missing states not yet built, inaccessible environment), what partial review was completed, and the conditions needed to resume.

## Related Skills

- [`component-mapper-design`](../component-mapper-design/SKILL.md) -- The component mapping table is the reference for which design system components should appear in the implementation.
- [`cross-platform-tester-design`](../cross-platform-tester-design/SKILL.md) -- Implementation reviews on multiple platforms extend the single-platform fidelity check.
- [`design-review-runner`](../../../design/head-of-design/design-review-runner/SKILL.md) -- Pre-implementation design reviews set the baseline that implementation reviews verify against.
