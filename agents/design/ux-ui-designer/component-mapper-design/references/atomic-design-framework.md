# Atomic Design & Component Mapping Framework

A guide for mapping UI requirements to design system components using atomic design taxonomy, and for planning gap resolution.

---

## Core Methodology

Atomic design organises components from most primitive to most composed:

```
Atoms → Molecules → Organisms → Templates → Pages
```

Map every UI element to the appropriate atomic level before checking the component library. This prevents semantic mismatches where visually similar components serve different purposes.

---

## Atomic Levels Reference

| Level | Definition | Examples |
|-------|-----------|---------|
| **Atom** | Indivisible UI primitive | Button, Input, Icon, Badge, Avatar, Label, Divider |
| **Molecule** | Atoms combined into a functional unit | Search bar (Input + Button), Form field (Label + Input + Error), Card header (Avatar + Text) |
| **Organism** | Molecules/atoms forming a distinct UI section | Navigation bar, Data table, Modal, Feature card |
| **Template** | Wireframe-level page layout | Dashboard layout, Settings page, List + Detail layout |
| **Page** | Template with real content | Specific product page instances |

---

## Component Mapping Table Format

For each UI element identified in the design brief or wireframe:

| # | UI Element | Screen / Context | Atomic Level | Library Match | Component Name | Variant / State | Coverage Status | Gap Type |
|---|-----------|-----------------|--------------|--------------|----------------|-----------------|-----------------|---------|
| 1 | | | | Yes / Partial / No | | | Covered / Gap | — / New variant / New component / Token |

**Coverage Status definitions:**
- **Covered** — Existing component matches exactly (semantic role + visual + behaviour)
- **Partial** — Existing component matches visually but needs a new variant, state, or token
- **Gap** — No component match; new component required or one-off usage needed

---

## Semantic Matching Rules

Before marking a component as "covered", verify all three dimensions match:

1. **Semantic role** — Does the component mean the same thing in both contexts? (A `Card` used as a selectable list item is semantically a `SelectableCard`, not a `Card`)
2. **Interaction behaviour** — Does it behave the same way? (A toggle vs. a checkbox may look similar but have different ARIA roles and keyboard behaviour)
3. **Visual variants available** — Do the required states (error, disabled, loading, selected) exist in the library component?

---

## Gap Resolution Decision Tree

For each identified gap, choose the resolution path:

```
Is the gap a missing state on an existing component?
  └─ YES → Add state variant to existing component (small effort, high reuse)
  └─ NO → Is this a pattern that will appear in 3+ places?
            └─ YES → Create a new component (invest in the system)
            └─ NO → Is the pattern consistent with system principles?
                      └─ YES → One-off usage with documented rationale (low-risk exception)
                      └─ NO → Escalate to design system maintainer for direction
```

---

## Token Coverage Check

For every component mapping, verify token coverage for the target context:

| Token Category | Check |
|---------------|-------|
| Colour (fill, stroke, text) | Semantic tokens exist for the component's role and state? |
| Spacing (padding, gap, margin) | Spacing scale values cover the needed densities? |
| Typography | Type styles available for the component's text roles? |
| Elevation / shadow | Shadow tokens available for the component's depth level? |
| Border radius | Radius tokens cover the needed curvature? |
| Motion | Duration and easing tokens available for transitions? |

If a required token does not exist, flag it as a token gap alongside the component gap.

---

## Gap Severity Classification

| Severity | Definition | Impact on Design Progress |
|---------|-----------|--------------------------|
| **Blocking** | Gap is on a critical-path screen or interaction; cannot design without it | Design cannot proceed for this surface until resolved |
| **Non-blocking** | Gap is on a secondary screen or optional variant; design can continue with a placeholder | Note the gap; design with a placeholder; file a DS ticket |

---

## Effort Estimates for Gap Resolution

| Resolution Type | Estimated Design Effort | Who Resolves |
|----------------|------------------------|-------------|
| New component state / variant | S (4–8 h) | UX/UI Designer + DS review |
| New Figma-only component | M (8–16 h) | UX/UI Designer, DS maintainer publishes |
| New full system component (Figma + code) | L–XL (24–80 h) | DS Designer + Engineer |
| Token addition | XS (1–2 h) | DS maintainer |
