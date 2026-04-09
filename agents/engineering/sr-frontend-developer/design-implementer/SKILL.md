---
name: design-implementer
description: >
  This skill implements approved UI designs in code with fidelity to the design specification. Use when asked to build a feature from a design file, translate mockups to components, or implement a design system update. Also consider when pixel-level fidelity is required for a brand-sensitive surface. Suggest when a design handoff is complete and the component mapping is ready.
department: engineering
agent: sr-frontend-developer
version: 1.0.0
complexity: medium
related-skills:
  - ../component-mapper-eng/SKILL.md
  - ../accessibility-checker-eng/SKILL.md
  - ../cross-platform-tester/SKILL.md
  - ../accessibility-auditor/SKILL.md
triggers:
  - "implement design"
  - "convert design to code"
  - "design to code"
  - "frontend design implementation"
  - "build UI from design"
---

# design-implementer

## Agent: Sr. Frontend Developer

L3 senior frontend developer (Nx) responsible for implementing UI components, ensuring accessibility, and validating cross-platform compatibility.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Implements approved UI designs in production code with fidelity to the design specification, translating visual mockups and interaction specs into accessible, performant, and maintainable frontend components.

## When to Use

- A design handoff is complete and the component mapping plan is available.
- A design system update introduces new tokens, patterns, or component variants that need code implementation.
- A feature requires pixel-level visual fidelity for a brand-sensitive or marketing surface.
- An existing component needs visual or interaction updates based on a revised design spec.
- A prototype needs to be elevated to production-quality implementation.

## Workflow

1. **Review design spec**: Study the design file including all states (default, hover, active, disabled, error, loading, empty), responsive breakpoints, and interaction annotations. Deliverable: implementation checklist covering every state and breakpoint.
2. **Consume component map**: Reference the component mapping plan to identify which components to build, reuse, or extend. Deliverable: confirmed build order aligned with the mapping plan.
3. **Implement structure**: Build the HTML/JSX structure using semantic elements, correct heading hierarchy, and landmark regions. Deliverable: structural markup passing semantic validation.
4. **Apply styling**: Implement visual design using design tokens (spacing, colour, typography) from the design system. Ensure responsive behaviour matches breakpoint specs. Deliverable: styled components matching design at all breakpoints.
5. **Add interactions**: Implement hover states, transitions, animations, form validation feedback, and dynamic behaviour per the interaction spec. Deliverable: interactive components matching motion and behaviour specs.
6. **Verify fidelity**: Overlay the implementation against the design file to confirm pixel-level alignment on key screens. Deliverable: fidelity comparison showing deviations within acceptable tolerance.
7. **Submit for review**: Open a PR with before/after screenshots, component documentation, and links to the design file. Deliverable: reviewable PR with visual evidence of fidelity.

## Anti-Patterns

- **Implementing without reviewing all states.** Building only the happy-path state and retrofitting error, loading, and empty states causes inconsistent UX. *Why*: every state is a user experience; missing states are broken experiences.
- **Hardcoding values instead of tokens.** Using raw hex colours or pixel values instead of design tokens breaks theme support and makes system-wide changes impossible. *Why*: tokens are the single source of truth for visual consistency.
- **Ignoring responsive specs.** Building for desktop and hoping mobile "works" results in broken layouts on smaller screens. *Why*: mobile traffic often exceeds desktop; both are primary targets.
- **Skipping design overlay verification.** Assuming the implementation matches without visual comparison allows drift to accumulate. *Why*: small deviations compound across components into a noticeably inconsistent product.

## Output

**On success**: Produces production-ready frontend components matching the design specification across all states and breakpoints, with semantic HTML, design-token-based styling, and interactive behaviour. Delivered as a PR with visual fidelity evidence and component documentation.

**On failure**: Report which design elements could not be implemented (e.g., missing assets, undefined interaction specs, unsupported animations), what partial implementation was completed, and what design clarifications are needed.

## Related Skills

- [`component-mapper-eng`](../component-mapper-eng/SKILL.md) -- produces the component mapping plan this skill executes against.
- [`accessibility-checker-eng`](../accessibility-checker-eng/SKILL.md) -- checks the implemented components for accessibility compliance.
- [`cross-platform-tester`](../cross-platform-tester/SKILL.md) -- validates the implementation across browsers and devices.
