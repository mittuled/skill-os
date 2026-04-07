---
name: wireframe-builder
description: >
  This skill builds low-fidelity wireframes to communicate layout, content hierarchy, and
  interaction concepts. Use when asked to wireframe a screen, sketch a layout for a new
  feature, or create a structural mockup before visual design. Also consider when a user
  flow has been approved and the next step is spatial layout. Suggest when a designer jumps
  straight to high-fidelity visual design without validating layout structure first.
department: design
agent: ux-ui-designer
version: 1.0.0
complexity: simple
related-skills: []
triggers:
  - "wireframe this screen"
  - "sketch the layout"
  - "create a lo-fi mockup"
  - "build wireframes for this feature"
---

# wireframe-builder

## Agent: UX/UI Designer

L2 UX/UI designer (Nx) responsible for user flow design, wireframing, prototyping, and component mapping.

Department ethos: [ideal-design.md](../../../../departments/design/ideal-design.md)

## Skill Description

Builds low-fidelity wireframes that communicate layout structure, content hierarchy, and interaction zones for screens within a defined user flow.

## When to Use

- When a user flow has been approved and the spatial layout of each screen needs to be defined before visual design.
- When a feature concept needs rapid structural exploration across multiple layout options.
- When product and design need to align on content priority and information hierarchy before investing in visual polish.

## Workflow

1. **Gather inputs**: Collect the user flow, content inventory, component mapping (if available), and responsive breakpoint requirements. Deliverable: input checklist confirming readiness.
2. **Define content hierarchy**: For each screen, rank content elements by importance to the user's task. Determine what is primary, secondary, and tertiary. Deliverable: content hierarchy per screen.
3. **Build wireframes**: Create grey-box layouts in Figma using placeholder content and structural annotations. Show layout grid, content zones, interactive element placement, and scroll behavior. Cover all specified breakpoints. Deliverable: wireframe set for all in-scope screens and breakpoints.
4. **Annotate interactions**: Mark interactive elements with expected behavior (tap targets, expandable regions, scroll containers, modals). Note navigation connections between screens. Deliverable: annotated wireframes with interaction callouts.

## Anti-Patterns

- **Wireframe as visual design**: Adding colour, branded typography, or detailed imagery to wireframes. *Why*: visual detail at the wireframe stage anchors stakeholders on aesthetics instead of layout and hierarchy, making structural feedback harder to extract.
- **Single-breakpoint wireframes**: Building wireframes for only one screen size when the feature targets multiple platforms. *Why*: layout decisions made for desktop often do not transfer to mobile; content priority must be validated at every breakpoint.
- **Skipping content hierarchy**: Laying out elements by spatial convenience rather than user task priority. *Why*: wireframes that do not reflect content hierarchy produce visual designs where important information is buried below the fold or lost in visual noise.

## Output

**On success**: Produces a set of annotated low-fidelity wireframes covering all in-scope screens and breakpoints, with content hierarchy documentation and interaction annotations. Delivered as a Figma page linked to the project file.

**On failure**: Report which screens could not be wireframed (missing user flow, undefined content, unresolved layout constraints), what partial wireframes were created, and what is needed to complete the set.

## Related Skills

- [`ux-flow-designer`](../ux-flow-designer/SKILL.md) -- User flows are the prerequisite input that wireframes spatialize.
- [`component-mapper-design`](../component-mapper-design/SKILL.md) -- Component mapping identifies reusable elements that inform wireframe structure.
- [`prototype-creator`](../prototype-creator/SKILL.md) -- Wireframes may be connected into low-fidelity interactive prototypes for early testing.
