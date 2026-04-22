---
name: prototype-creator
description: >
  This skill creates interactive prototypes for usability testing and stakeholder review. Use
  when asked to build a clickable prototype, prepare a test-ready prototype for research, or
  create an interactive demo for stakeholder alignment. Also consider when a static design
  needs to be validated with real user interaction. Suggest when usability testing is scheduled
  but no interactive prototype exists.
department: design
agent: ux-ui-designer
version: 1.0.0
complexity: medium
related-skills:
  - flow-designer
  - wireframe-builder
  - design-review-runner
triggers:
  - "prototype"
  - "prototype-builder"
  - "interactive prototype"
  - "build prototype"
---

# prototype-creator

## Agent: UX/UI Designer

L2 UX/UI designer (Nx) responsible for user flow design, wireframing, prototyping, and component mapping.

Department ethos: [ideal-design.md](../../../../departments/design/ideal-design.md)

## Skill Description

Creates interactive prototypes in Figma that simulate real user interactions for usability testing, stakeholder review, and engineering specification.

## When to Use

- When usability testing is planned and an interactive prototype is needed to simulate task flows with real users.
- When stakeholders need to experience an interaction pattern before committing to implementation.
- When a complex flow (multi-step form, conditional navigation, drag-and-drop) cannot be evaluated from static screens alone.
- When engineering needs an interactive reference to understand transition behavior, timing, and state sequences.

## Workflow

1. **Define prototype scope**: Identify which user flows and interaction paths the prototype must cover. Distinguish between paths that need full interactivity and those where a static screen or placeholder is sufficient. Deliverable: prototype scope document with flow paths marked as interactive or static.
2. **Set fidelity level**: Determine whether the prototype should be low-fidelity (grey-box, focused on flow logic), mid-fidelity (styled components, no real content), or high-fidelity (production-ready visuals, real content). Match fidelity to the testing or review objective. Deliverable: fidelity decision with rationale.
3. **Build interactive frames**: Construct the prototype in Figma using Smart Animate, overlays, and component interactions. Wire up navigation, state changes, conditional paths, and micro-interactions per the flow designer's specification. Deliverable: functional Figma prototype.
4. **Add realistic content**: Replace placeholder text and images with realistic (not production) content that matches the target use case. Ensure content length variations are represented. Deliverable: content-populated prototype.
5. **Test internally**: Walk through every interactive path to verify transitions, hotspot accuracy, and state correctness. Fix dead ends, broken links, and unresponsive interactions. Deliverable: QA-passed prototype ready for external use.
6. **Prepare sharing artifacts**: Generate a shareable prototype link with appropriate permissions. Write a brief usage guide noting entry points, supported flows, and known limitations. Deliverable: prototype link and usage guide.

## Anti-Patterns

- **Over-scoping interactivity**: Making every element in every screen interactive when only the test flows require it. *Why*: over-scoped prototypes take disproportionately long to build and maintain, and testers interact with elements outside the test scenario, generating noise data.
- **Mismatched fidelity**: Building a high-fidelity prototype for a concept validation test where low-fidelity would suffice, or vice versa. *Why*: high fidelity in concept tests anchors participants on visual polish instead of flow logic; low fidelity in usability tests misses interaction and content issues.
- **Prototype as specification**: Treating the prototype as the sole design deliverable without separate interaction specs and redlines. *Why*: engineers cannot extract spacing, token, and timing values from a prototype; they need explicit documentation.

## Output

**On success**: Produces a functional Figma prototype with specified interactive paths, a shareable link, and a usage guide noting entry points and known limitations. Delivered to the usability researcher, stakeholder, or engineering lead depending on the use case.

**On failure**: Report which flows could not be prototyped (missing visual designs, undefined interaction specs, Figma performance limitations), what partial prototype was built, and what is needed to complete it.

## Related Skills

- [`flow-designer`](../flow-designer/SKILL.md) -- Interaction flow specifications are the blueprint the prototype implements.
- [`wireframe-builder`](../wireframe-builder/SKILL.md) -- Low-fidelity wireframes may be promoted into interactive wireframe prototypes.
- [`design-review-runner`](../../../design/head-of-design/design-review-runner/SKILL.md) -- Prototypes are a key artifact in design review sessions.
