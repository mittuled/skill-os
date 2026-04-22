---
name: accessibility-checker-design
description: >
  This skill checks design outputs against accessibility standards before handoff to
  engineering. Use when asked to verify WCAG compliance on a design file, review colour
  contrast ratios, or validate focus and interaction states for assistive technology. Also
  consider when a design review surfaces accessibility questions. Suggest when a designer
  is about to mark a Figma file as ready-for-dev without accessibility annotations.
department: design
agent: head-of-design
version: 1.0.0
complexity: medium
related-skills:
  - accessibility-auditor-design
  - design-review-runner
  - component-mapper-design
triggers:
  - "check accessibility"
  - "design a11y check"
  - "accessibility check"
  - "wcag compliance check"
  - "a11y check"
---

# accessibility-checker-design

## Agent: Head of Design

L1 design leader (1x) responsible for design strategy, review governance, and accessibility oversight. Oversees UX Research and Content Design as sub-disciplines reporting into Design.

Department ethos: [ideal-design.md](../../../../departments/design/ideal-design.md)

## Skill Description

Checks design outputs against accessibility standards before handoff to engineering, catching compliance gaps while changes are still inexpensive.

## When to Use

- When a design deliverable is approaching dev-ready status and needs accessibility sign-off.
- When new components or patterns are being added to the design system and require accessibility validation.
- When a designer requests a pre-review accessibility check before the formal design review.
- When colour palette, typography scale, or spacing token updates may affect existing contrast ratios or touch target sizes.

## Workflow

1. **Collect design artifacts**: Gather the Figma file, component specs, and interaction state documentation for the surfaces being checked. Deliverable: checklist of design artifacts under review.
2. **Run contrast and token checks**: Verify all text/background combinations meet WCAG 2.1 AA contrast minimums (4.5:1 normal text, 3:1 large text). Confirm touch targets meet 44x44pt minimum. Check that colour is not the sole indicator of state. Deliverable: contrast and sizing compliance matrix.
3. **Validate interaction states**: Confirm every interactive element has documented focus, hover, active, disabled, and error states. Verify focus order annotations exist and follow logical reading order. Deliverable: interaction state coverage checklist.
4. **Check content accessibility**: Verify alt text specifications for images, ARIA label annotations for icons and controls, and heading hierarchy documentation. Confirm error messages are descriptive and adjacent to the triggering field. Deliverable: content accessibility notes.
5. **Document findings**: Record each issue with the specific WCAG criterion violated, the affected component or screen, and a recommended fix. Deliverable: accessibility check report with pass/fail summary.
6. **Gate or approve**: Issue a clear pass/conditional-pass/fail verdict. Conditional passes must list required fixes before dev handoff. Deliverable: sign-off status communicated to designer and product.

## Anti-Patterns

- **Checklist theatre**: Running through compliance items without actually testing with real token values or inspecting the Figma file layer structure. *Why*: superficial checks miss issues like incorrect layer naming that breaks screen reader output or decorative images marked as meaningful.
- **Colour-only focus**: Checking only colour contrast while ignoring keyboard navigation, focus management, and ARIA annotations. *Why*: contrast is the most visible accessibility dimension but accounts for a fraction of real-world barriers.
- **Blocking without guidance**: Failing a design without specifying what needs to change and which WCAG criterion applies. *Why*: designers cannot fix what they do not understand; vague rejections create rework cycles and erode trust in the review process.

## Output

**On success**: Produces an accessibility check report with pass/fail verdict per criterion, specific findings with WCAG references, and recommended fixes. Delivered to the designer and attached to the design file before dev handoff.

**On failure**: Report which design artifacts could not be checked, the reason (missing interaction states, incomplete token documentation, inaccessible Figma file), and what the designer must provide to unblock the check.

## Related Skills

- [`accessibility-auditor-design`](../accessibility-auditor-design/SKILL.md) -- Pre-handoff checks prevent issues that would otherwise surface in post-launch audits.
- [`design-review-runner`](../design-review-runner/SKILL.md) -- Design reviews should include accessibility as a standing criterion.
- [`component-mapper-design`](../../../design/ux-ui-designer/component-mapper-design/SKILL.md) -- Component mapping must account for accessibility attributes baked into design system components.
