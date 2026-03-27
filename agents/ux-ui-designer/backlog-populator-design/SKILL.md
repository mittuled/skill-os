---
name: backlog-populator-design
description: >
  This skill populates the design backlog with well-defined design tasks aligned to the
  product roadmap. Use when asked to break down a design brief into backlog items, create
  design tickets from a spec, or prepare the design backlog for sprint planning. Also consider
  when the design backlog is empty despite active product initiatives. Suggest when a new
  design brief arrives without corresponding backlog entries.
department: design
agent: ux-ui-designer
version: 1.0.0
complexity: simple
related-skills: []
---

# backlog-populator-design

## Agent: UX/UI Designer

L2 UX/UI designer (Nx) responsible for user flow design, wireframing, prototyping, and component mapping.

Department ethos: [ideal-design.md](../../../departments/design/ideal-design.md)
Tool policy: [allowed-tools.yaml](../../../allowed-tools.yaml)

## Skill Description

Populates the design backlog with well-defined, estimable design tasks derived from design briefs and product roadmap items.

## When to Use

- When a design brief has been finalized and needs to be decomposed into actionable backlog items for sprint planning.
- When the product roadmap updates and new design work needs to be captured in the backlog.
- When the design backlog is stale or empty despite active product initiatives requiring design input.

## Workflow

1. **Review source material**: Read the design brief, product spec, or roadmap item. Identify all design deliverables required -- flows, wireframes, visual designs, prototypes, component specs, handoff documentation. Deliverable: deliverable inventory.
2. **Decompose into tasks**: Break each deliverable into discrete, estimable backlog items. Each item must have a clear definition of done, the target Figma file or page, and any dependencies on other design or product tasks. Deliverable: draft backlog items.
3. **Tag and categorize**: Apply labels for design phase (discovery, wireframe, visual, prototype, handoff), complexity, and design system impact (new component, variant, or existing reuse). Deliverable: tagged backlog items.
4. **Sequence and link**: Order items by dependency and phase. Link related items (e.g., wireframe precedes visual design for the same surface). Deliverable: sequenced backlog ready for sprint planning.

## Anti-Patterns

- **Vague tickets**: Creating backlog items like "design the feature" without specifying deliverable type, scope, or definition of done. *Why*: vague items cannot be estimated, assigned, or verified as complete, and they create ambiguity during sprint planning.
- **Skipping dependency mapping**: Adding items without identifying upstream blockers (pending research, missing content, unresolved spec questions). *Why*: designers pick up blocked tasks, stall, and switch context -- wasting capacity and disrupting flow.
- **One-shot population**: Populating the backlog once and never updating it as the brief evolves or scope changes. *Why*: stale backlogs misrepresent the true design workload and lead to missed deliverables.

## Output

**On success**: Produces a set of tagged, sequenced design backlog items with definitions of done, dependencies, and phase labels. Delivered in the team's backlog tool, ready for sprint planning.

**On failure**: Report which parts of the brief could not be decomposed (ambiguous requirements, missing content direction, undefined user flows), what partial items were created, and the questions that must be resolved.

## Related Skills

- [`spec-translator-design`](../../head-of-design/spec-translator-design/SKILL.md) -- Design briefs from spec translation are the primary input for backlog population.
- [`effort-estimator-design`](../../head-of-design/effort-estimator-design/SKILL.md) -- Backlog items are the unit of work that effort estimation operates on.
- [`wireframe-builder`](../wireframe-builder/SKILL.md) -- Wireframe tasks are a common output of backlog population.
