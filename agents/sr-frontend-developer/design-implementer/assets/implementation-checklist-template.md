# Design Implementation Checklist

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Agent role / human name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | design-implementer |

## Executive Summary

[2-3 sentences summarizing implementation scope: number of components, design fidelity status, and remaining work.
GUIDANCE: Lead with the overall fidelity verdict. Flag any design ambiguities that blocked implementation.]

## State Coverage

[Verify every component state from the design spec is implemented.

GUIDANCE:
- Good: "AddressForm: default (empty fields), filled (valid data), error (field-level validation messages), loading (submit spinner), disabled (during payment processing). All 5 states implemented and screenshot-verified."
- Bad: "AddressForm works."
- Format: Table with component, state, implemented (Y/N), screenshot link]

| Component | State | Implemented | Screenshot | Notes |
|-----------|-------|-------------|------------|-------|
| [Name] | [default/hover/active/disabled/error/loading/empty] | [Y/N] | [link] | [Any deviation from spec] |

## Responsive Verification

[Confirm layout matches design at each breakpoint.

GUIDANCE:
- Good: "CheckoutLayout at 320px: single column, payment form stacks below shipping. At 768px: side-by-side layout. At 1280px: centered with max-width 960px. All verified against Figma breakpoint frames."
- Bad: "Looks good on mobile."
- Format: Table with breakpoint, expected layout, actual layout, match status]

| Breakpoint | Expected Layout | Match Status | Deviation Notes |
|-----------|----------------|-------------|----------------|
| [320px / 768px / 1024px / 1280px] | [Description from spec] | [Match / Minor deviation / Major deviation] | [Details] |

## Design Token Compliance

[Verify all visual values use design tokens, not hardcoded values.

GUIDANCE:
- Good: "Color: all backgrounds use `var(--color-surface-primary)`. Typography: headings use `var(--font-heading-lg)`. Spacing: all padding uses `var(--space-4)` scale."
- Bad: "Uses the design system."
- Format: Checklist with token category and compliance status]

## Fidelity Comparison

[Overlay implementation against design file to confirm pixel-level alignment.

GUIDANCE:
- Good: "Overlay at 1x: header height matches within 1px. Button padding 2px wider than spec — accepted as rounding difference. Card shadow uses `elevation-2` token matching Figma shadow exactly."
- Bad: "Looks close enough."
- Format: Table with screen, deviation measurement, acceptable (Y/N)]

## Recommendations

[Prioritized list of remaining work or design clarifications needed.
GUIDANCE: Each recommendation should be:
- Specific (not "fix responsive" but "add max-width constraint to .checkout-grid at 1440px+ viewports")
- Actionable (assignable to a person/team)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[Design file version, comparison tools used (Percy, manual overlay), breakpoints tested, browsers used for verification]

### B. Supporting Data

[Full screenshot comparison gallery, design file links, component documentation links]
