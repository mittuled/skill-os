# Component Map

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Agent role / human name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | component-mapper-eng |

## Executive Summary

[2-3 sentences summarizing the mapping results: how many components identified, how many are new vs. existing, and the recommended build order.
GUIDANCE: Lead with the ratio of reuse to new build. Highlight any components that block multiple features.]

## Component Inventory

[List every distinct visual and interactive element from the design file.

GUIDANCE:
- Good: "SearchInput — text field with debounced autocomplete dropdown, clear button, keyboard navigation. Design ref: Frame 42"
- Bad: "Search component"
- Format: Table with columns: Name, Description, Design Reference, States (list all states)]

| Name | Description | Design Reference | States |
|------|-------------|-----------------|--------|
| [ComponentName] | [What it does, interaction model] | [Frame/artboard ref] | [default, hover, active, disabled, error, loading, empty] |

## Existing Library Match

[Map each inventoried component against the current component library.

GUIDANCE:
- Good: "SearchInput → Exact match: `<Autocomplete>` in design-system v2.4. Props: `onSearch`, `suggestions`, `loading`."
- Bad: "We have a search thing already."
- Format: Table with match status: Exact / Partial / New]

| Component | Match Status | Existing Component | Gap Notes |
|-----------|-------------|-------------------|-----------|
| [Name] | [Exact / Partial / New] | [Existing component path or N/A] | [What's missing for partial matches] |

## Reuse Analysis

[Group components sharing structure, behaviour, or styling into candidate abstractions.

GUIDANCE:
- Good: "FilterChip, TagBadge, and StatusPill share the same pill shape, padding, and dismiss interaction. Propose: `<Pill variant='filter|tag|status'>` with shared base styles."
- Bad: "Some components look similar."
- Format: Table grouping candidates with shared pattern description]

## Component Hierarchy

[Define parent-child relationships and prop interfaces.

GUIDANCE:
- Good: Tree diagram showing `<CheckoutForm>` → `<ShippingSection>` → `<AddressInput>`, with prop flow annotations (e.g., `onAddressChange: (addr: Address) => void`)
- Bad: "CheckoutForm contains ShippingSection"
- Format: Indented tree with prop annotations]

## Build Plan

[Sequence components for implementation: leaf nodes and shared primitives first, then composites.

GUIDANCE:
- Good: "Phase 1: Pill, TextInput, IconButton (leaf). Phase 2: SearchInput, FilterBar (composite). Phase 3: SearchPanel (page-level)."
- Bad: "Build everything."
- Format: Phased table with complexity and dependency notes]

| Phase | Component | Complexity | Dependencies | Estimated Effort |
|-------|-----------|-----------|-------------|-----------------|
| [1/2/3] | [Name] | [Simple/Medium/Complex] | [List deps] | [Hours/points] |

## Recommendations

[Prioritized list of recommendations based on the mapping.
GUIDANCE: Each recommendation should be:
- Specific (not "improve reuse" but "extract Pill base component to reduce 3 duplicate implementations")
- Actionable (assignable to a person/team)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[How this mapping was produced: design file format, component library version audited, classification criteria for reuse analysis]

### B. Supporting Data

[Full component inventory spreadsheet, design file links, existing library audit results]
