---
name: component-mapper-eng
description: >
  This skill maps design components to engineering implementation plans and identifies reusable component patterns. Use when asked to break down a design into buildable components, identify shared patterns, or plan a component library extension. Also consider when design handoff includes unfamiliar component structures. Suggest when a new feature design contains components not yet in the codebase.
department: engineering
agent: sr-frontend-developer
version: 1.0.0
complexity: medium
related-skills:
  - ../design-implementer/SKILL.md
  - ../accessibility-checker-eng/SKILL.md
triggers:
  - "map components"
  - "component mapping"
  - "design to component map"
  - "UI component inventory"
  - "map design components"
---

# component-mapper-eng

## Agent: Sr. Frontend Developer

L3 senior frontend developer (Nx) responsible for implementing UI components, ensuring accessibility, and validating cross-platform compatibility.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Maps design components to engineering implementation plans by identifying reusable patterns, determining component hierarchy, and producing a build plan that the design implementer can execute against.

## When to Use

- A new feature design is handed off and the engineering team needs to identify which components exist, which need creation, and which can be composed from existing primitives.
- The design system is being extended and new patterns need classification as atoms, molecules, or organisms.
- Multiple features share visual patterns that should be consolidated into shared components.
- A design handoff includes complex interactive components whose implementation strategy is not immediately obvious.

## Workflow

1. **Inventory design components**: Walk through the design file and list every distinct visual and interactive element. Deliverable: component inventory with names, descriptions, and design-file references.
2. **Match against existing library**: Compare each inventoried component against the current component library and design system. Deliverable: mapping table showing existing matches, partial matches, and net-new components.
3. **Identify reusable patterns**: Group components that share structure, behaviour, or styling into candidate abstractions. Deliverable: reuse analysis listing shared patterns and proposed shared components.
4. **Define component hierarchy**: Establish parent-child relationships, prop interfaces, and composition patterns for each component. Deliverable: component tree diagram with prop-flow annotations.
5. **Estimate implementation effort**: Size each new or modified component by complexity (simple, medium, complex) and flag dependencies on backend APIs or design tokens. Deliverable: effort estimate per component with dependency notes.
6. **Produce build plan**: Sequence the components for implementation, starting with leaf nodes and shared primitives, then composites. Deliverable: ordered build plan ready for sprint planning.

## Anti-Patterns

- **One-to-one design-to-component mapping.** Creating a unique component for every design element produces a bloated, unmaintainable component library. *Why*: reuse reduces bundle size, testing surface, and maintenance burden.
- **Mapping without the component library.** Skipping the existing library check leads to duplicate implementations of components that already exist. *Why*: duplication creates visual inconsistency and doubles maintenance cost.
- **Ignoring prop interface design.** Mapping components without defining their API leads to rigid implementations that resist composition. *Why*: well-defined prop interfaces are the contract between components and their consumers.
- **Deferring accessibility requirements.** Omitting accessibility needs from the mapping forces retrofit during implementation. *Why*: accessibility constraints (keyboard interaction model, ARIA roles) shape component architecture.

## Output

**On success**: Produces a component mapping table (existing vs. new), a component hierarchy diagram, a reuse analysis, and a sequenced build plan with effort estimates. Delivered to the design implementer and sprint planner.

**On failure**: Report which design elements could not be mapped (e.g., ambiguous interaction specs, missing states), what partial mapping was achieved, and what design clarifications are needed to proceed.

## Related Skills

- [`design-implementer`](../design-implementer/SKILL.md) -- executes the build plan this skill produces.
- [`accessibility-checker-eng`](../accessibility-checker-eng/SKILL.md) -- validates that mapped components meet accessibility standards during implementation.
