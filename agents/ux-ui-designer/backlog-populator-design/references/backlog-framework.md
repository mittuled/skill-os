# Design Backlog Population Framework

A guide for converting design briefs into well-formed, sequenced, estimable backlog items.

---

## Core Methodology

A backlog item is atomic when it can be independently designed, reviewed, and handed off. Decompose until each item has a single, testable deliverable.

---

## Deliverable-to-Ticket Mapping

| Design Deliverable | Backlog Item Type | Definition of Done |
|-------------------|------------------|-------------------|
| User flow (per flow) | Flow design ticket | All paths (happy, error, edge case) diagrammed; stakeholder sign-off |
| Wireframe (per screen set) | Wireframe ticket | All breakpoints; annotated; review complete |
| Visual design (per screen set) | Visual design ticket | All states; tokens applied; design review complete |
| Prototype (per flow) | Prototype ticket | Interactive paths tested; shareable link |
| Component (new) | DS component ticket | Figma component published; usage documented |
| Component (variant) | DS variant ticket | Variant added to existing component; named per convention |
| Handoff spec | Handoff ticket | Redlines, tokens, interactions annotated; engineering walkthrough done |
| Copy / microcopy | Content ticket | All strings authored; content review complete |
| Accessibility audit | A11y ticket | Checked against WCAG AA; issues filed |

---

## Ticket Template

Each backlog item must include:

```
Title:          [Deliverable type] — [Feature name] — [Screen / scope]
Phase:          Discovery / Definition / Production / Handoff
Description:    [What needs to be created and why]
Design file:    [Figma file link or page reference]
Definition of Done:
  - [ ] [Specific, verifiable completion condition]
  - [ ] [Review completed]
  - [ ] [Dependencies confirmed resolved]
Estimate:       [XS / S / M / L / XL]
Dependencies:   [Upstream tickets that must complete first]
Design system impact: [None / New variant / New component / Token update]
```

---

## Phase Labels

| Label | When to Apply |
|-------|--------------|
| `phase:discovery` | Flow mapping, problem space exploration, research review |
| `phase:wireframe` | Lo-fi layout, content hierarchy, interaction skeleton |
| `phase:visual` | Hi-fi design with tokens, typography, colour |
| `phase:prototype` | Interactive Figma prototype for testing or review |
| `phase:handoff` | Redlines, specs, DS updates, engineering walkthrough |
| `phase:iteration` | Post-launch fix or improvement to shipped feature |

---

## Design System Impact Labels

| Label | When to Apply |
|-------|--------------|
| `ds:none` | Uses existing components and tokens without modification |
| `ds:new-variant` | Requires a new variant of an existing component |
| `ds:new-component` | Requires a net-new component in the design system |
| `ds:token-update` | Requires a new or modified design token |

---

## Sequencing Rules

1. **Flow before wireframe** — User flows must be approved before wireframes start
2. **Wireframe before visual** — Visual design must have an approved wireframe to build on
3. **Visual before prototype** — Interactive prototypes use finished visual frames
4. **All states before handoff** — Every state (empty, error, loading, disabled) must be designed before a handoff ticket is opened
5. **DS components before implementation** — New or updated design system components must be published before engineering implements features that use them

---

## Dependency Flags

Use these flags in ticket descriptions to surface blocked items during planning:

| Flag | Meaning |
|------|---------|
| `BLOCKED: research` | Cannot proceed until research output is available |
| `BLOCKED: content` | Cannot proceed until copy is written |
| `BLOCKED: product` | Cannot proceed until a product decision is made |
| `BLOCKED: engineering` | Cannot proceed until a technical constraint is resolved |
| `BLOCKED: DS` | Cannot proceed until a design system component is ready |
