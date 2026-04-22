---
name: component-mapper-design
description: >
  This skill maps product requirements to design system components and identifies gaps
  requiring new components or variants. Use when asked to audit component coverage for a
  feature, identify design system gaps, or plan component work for a new surface. Also
  consider when a designer is building custom elements that may already exist in the system.
  Suggest when a wireframe introduces patterns not present in the component library.
department: design
agent: ux-ui-designer
version: 1.0.0
complexity: medium
related-skills:
  - wireframe-builder
  - accessibility-checker-design
  - design-implementer-review
triggers:
  - "map components for this feature"
  - "what design system components do we need"
  - "find component gaps"
  - "audit component coverage"
---

# component-mapper-design

## Agent: UX/UI Designer

L2 UX/UI designer (Nx) responsible for user flow design, wireframing, prototyping, and component mapping.

Department ethos: [ideal-design.md](../../../../departments/design/ideal-design.md)

## Skill Description

Maps product requirements and design deliverables to existing design system components, identifying coverage gaps that require new components, variants, or token updates.

## When to Use

- When a new feature design is underway and the designer needs to determine which existing components to reuse versus what must be created.
- When the design system is being audited for coverage against current product surfaces.
- When a wireframe or visual design introduces interaction patterns that may already exist in the component library under a different name.
- When engineering flags inconsistent component usage across screens and requests a canonical mapping.

## Workflow

1. **Inventory requirements**: Extract every UI element, pattern, and interaction from the design brief or wireframes. Classify each element by atomic level (atom, molecule, organism, template) using the [atomic design framework](references/atomic-design-framework.md). Deliverable: UI element inventory with atomic classification.
2. **Map to existing components**: For each element, search the design system library for an existing match. Apply the semantic matching rules in the [atomic design framework](references/atomic-design-framework.md) — verify role, interaction behaviour, and state availability, not just visual similarity. Record exact component name, variant, and coverage status. Deliverable: component mapping table.
3. **Identify gaps**: Flag elements with no existing component match, partial matches requiring new variants, or missing token coverage. Use the severity classification in the [atomic design framework](references/atomic-design-framework.md) to tag each gap as blocking or non-blocking. Deliverable: gap register with severity.
4. **Propose gap resolution**: Apply the gap resolution decision tree in the [atomic design framework](references/atomic-design-framework.md) to recommend the appropriate path for each gap. Estimate effort per resolution using the framework's effort table. Deliverable: gap resolution plan.
5. **Align with system owners**: Review the gap resolution plan with the design system maintainer to confirm feasibility, naming conventions, and timeline. Deliverable: approved resolution plan with assignments.

## Anti-Patterns

- **Detaching and customizing**: Detaching a Figma component instance to make local modifications instead of requesting a proper variant. *Why*: detached instances do not receive library updates, creating visual drift and multiplying maintenance effort across every file that copied the hack.
- **Name-blind mapping**: Mapping by visual similarity alone without verifying semantic meaning and interaction behavior. *Why*: two elements may look identical but serve different purposes (e.g., a card vs. a selectable list item), leading to incorrect ARIA roles and broken accessibility.
- **Ignoring token coverage**: Mapping components without checking that the required colour, spacing, and typography tokens exist for the target context (dark mode, compact density). *Why*: missing tokens force hard-coded values that break when themes or density settings change.

## Output

**On success**: Produces a component mapping table linking every UI element to a design system component (or gap entry), a gap register with resolution recommendations, and an approved plan for new components or variants. Delivered to the designer, design system maintainer, and engineering lead.

**On failure**: Report which requirements could not be mapped (missing design system documentation, inaccessible Figma library, undefined interaction states), what partial mapping was achieved, and what access or documentation is needed.

## Related Skills

- [`wireframe-builder`](../wireframe-builder/SKILL.md) -- Wireframes are a primary input for component mapping; mapping should happen before visual design begins.
- [`accessibility-checker-design`](../../../design/head-of-design/accessibility-checker-design/SKILL.md) -- Component mapping must verify that accessibility attributes (ARIA roles, focus behavior) are baked into system components.
- [`design-implementer-review`](../design-implementer-review/SKILL.md) -- Implementation reviews verify that the mapped components were used correctly in code.
