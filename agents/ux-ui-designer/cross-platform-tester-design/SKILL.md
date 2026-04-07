---
name: cross-platform-tester-design
description: >
  This skill tests designs across platforms and devices to ensure consistent user experience.
  Use when asked to verify responsive behavior, check platform-specific adaptations, or
  validate designs on multiple screen sizes and input methods. Also consider when a design
  targets both web and native platforms. Suggest when a feature is about to ship on a new
  platform without design verification on that surface.
department: design
agent: ux-ui-designer
version: 1.0.0
complexity: medium
related-skills: []
---

# cross-platform-tester-design

## Agent: UX/UI Designer

L2 UX/UI designer (Nx) responsible for user flow design, wireframing, prototyping, and component mapping.

Department ethos: [ideal-design.md](../../../departments/design/ideal-design.md)

## Skill Description

Tests designs across platforms, devices, and screen sizes to verify consistent experience quality, responsive behavior, and platform convention adherence.

## When to Use

- When a design targets multiple platforms (web, iOS, Android) and needs verification that platform-specific conventions are respected.
- When responsive breakpoint behavior needs validation across mobile, tablet, and desktop viewports.
- When a new device category (foldable, large-screen tablet, wearable) is added to the support matrix.
- When QA or engineering reports visual inconsistencies between platforms and the design source needs verification.

## Workflow

1. **Define test matrix**: Determine coverage tiers (Tier 1 must-test, Tier 2 should-test, Tier 3 edge case) using the [platform test matrix](references/platform-test-matrix.md). List target platforms, devices, screen sizes, orientations, input methods, and accessibility modes. Deliverable: platform test matrix for this release.
2. **Prepare test artifacts**: Ensure Figma frames exist for each breakpoint and platform variant. Verify that prototypes cover platform-specific interactions per the interaction parity table in the [platform test matrix](references/platform-test-matrix.md). Deliverable: test-ready design artifacts per platform.
3. **Execute visual comparison**: Review each screen at every breakpoint against the visual check dimensions in the [platform test matrix](references/platform-test-matrix.md). Check layout reflow, typography scaling, image cropping, touch target sizing, and spacing token application. Deliverable: visual comparison report with annotated screenshots.
4. **Test interaction parity**: Verify interaction flows against the platform-specific patterns in the [platform test matrix](references/platform-test-matrix.md). Confirm navigation, modals, bottom sheets, and back gestures follow platform conventions. Deliverable: interaction parity checklist.
5. **Document deviations**: Record every inconsistency using the deviation severity scale in the [platform test matrix](references/platform-test-matrix.md). Distinguish intentional platform adaptations from unintentional drift. Deliverable: deviation report with fix recommendations.

## Anti-Patterns

- **Desktop-first bias**: Testing only desktop breakpoints and assuming mobile will "just reflow." *Why*: mobile layouts require deliberate content prioritization, touch target sizing, and gesture design that cannot be inferred from a desktop layout.
- **Pixel-matching across platforms**: Expecting identical appearance on iOS, Android, and web instead of respecting each platform's conventions (Material Design, Human Interface Guidelines). *Why*: forcing iOS patterns on Android (or vice versa) violates user expectations and increases interaction friction.
- **Ignoring input method differences**: Testing only mouse interactions and neglecting touch, keyboard, and voice input. *Why*: each input method has different target size requirements, hover state availability, and focus management needs.

## Output

**On success**: Produces a cross-platform test report containing the test matrix, visual comparison with annotated screenshots, interaction parity checklist, and a deviation report with severity and fix recommendations. Delivered to the designer, engineering team, and QA.

**On failure**: Report which platforms or devices could not be tested (missing Figma frames, unavailable prototypes, inaccessible device lab), what partial coverage was achieved, and what is needed to complete testing.

## Related Skills

- [`wireframe-builder`](../wireframe-builder/SKILL.md) -- Wireframes should define responsive behavior that cross-platform testing validates.
- [`design-implementer-review`](../design-implementer-review/SKILL.md) -- Implementation reviews on each platform verify that cross-platform design specs were built correctly.
- [`accessibility-checker-design`](../../head-of-design/accessibility-checker-design/SKILL.md) -- Cross-platform testing must include accessibility verification per platform.
