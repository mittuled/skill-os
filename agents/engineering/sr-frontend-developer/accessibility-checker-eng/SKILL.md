---
name: accessibility-checker-eng
description: >
  This skill checks frontend implementations against WCAG accessibility standards during development. Use when asked to review a component for accessibility, validate ARIA usage, or ensure keyboard navigability. Also consider when a design spec lacks accessibility annotations. Suggest when a developer opens a PR for a new interactive component.
department: engineering
agent: sr-frontend-developer
version: 1.0.0
complexity: simple
related-skills:
  - ../accessibility-auditor/SKILL.md
  - ../design-implementer/SKILL.md
  - ../component-mapper-eng/SKILL.md
triggers:
  - "check accessibility"
  - "a11y check"
  - "accessibility verification"
  - "WCAG compliance check"
  - "frontend accessibility check"
---

# accessibility-checker-eng

## Agent: Sr. Frontend Developer

L3 senior frontend developer (Nx) responsible for implementing UI components, ensuring accessibility, and validating cross-platform compatibility.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Checks frontend implementations against WCAG 2.1 AA standards during active development, catching accessibility violations before they reach code review or QA.

## When to Use

- A developer submits a PR containing new or modified interactive UI components.
- A component uses custom ARIA attributes that need validation against the ARIA authoring practices spec.
- The design spec for a feature lacks explicit accessibility annotations.
- A CI pipeline flags accessibility linting warnings that need human triage.

## Workflow

1. **Identify check targets**: Determine which components or pages in the current changeset require accessibility review. Deliverable: component checklist.
2. **Run inline linting**: Execute eslint-plugin-jsx-a11y or equivalent linting rules against the changed files. Deliverable: linting report with flagged violations.
3. **Validate semantics**: Verify correct use of semantic HTML elements, heading hierarchy, landmark regions, and ARIA roles/properties. Deliverable: semantic correctness checklist.
4. **Test keyboard interaction**: Confirm all interactive elements are focusable, operable via keyboard, and have visible focus indicators. Deliverable: keyboard navigation pass/fail per component.
5. **Report findings**: Document violations with specific element references, WCAG criterion, and suggested fix. Deliverable: review comments on the PR or inline annotations.

## Anti-Patterns

- **Treating linting as sufficient.** Passing automated lint rules does not guarantee accessibility; custom widgets require manual semantic review. *Why*: linters catch syntax-level issues but miss logical accessibility failures.
- **Adding ARIA to fix bad HTML.** Using ARIA roles to compensate for non-semantic markup creates fragile solutions. *Why*: native HTML semantics are more robust and widely supported than ARIA overrides.
- **Deferring checks to QA.** Waiting until QA to catch accessibility issues increases fix cost and delays releases. *Why*: shifting left on accessibility reduces rework by catching issues when context is fresh.

## Output

**On success**: Produces PR review comments or an inline annotation report identifying each accessibility issue with WCAG criterion, severity, element reference, and fix suggestion. Clean results yield an explicit accessibility approval on the PR.

**On failure**: Report which components could not be checked (e.g., missing rendered preview, dynamic content requiring runtime), what was partially verified, and what additional context is needed.

## Related Skills

- [`accessibility-auditor`](../accessibility-auditor/SKILL.md) -- performs the pre-release audit; this skill catches issues during development.
- [`design-implementer`](../design-implementer/SKILL.md) -- builds the components this skill checks.
- [`component-mapper-eng`](../component-mapper-eng/SKILL.md) -- maps design to implementation; accessibility requirements should be captured during mapping.
