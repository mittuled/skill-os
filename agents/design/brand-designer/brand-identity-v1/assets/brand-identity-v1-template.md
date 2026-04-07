# Brand Identity V1 Guidelines

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Brand Designer name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | brand-identity-v1 |
| Brand Name | [Company / Product name] |
| Brand Architecture | [Monolithic / Endorsed / House of Brands] |

## Executive Summary

[2-3 sentences stating what the v1 identity system delivers, the visual direction chosen, and the primary brand architecture model adopted. Focus on what the identity expresses strategically, not a list of deliverables.]

GUIDANCE: Example — "The v1 identity for Helio adopts a monolithic architecture with a geometric wordmark that expresses technical precision through tight letterspacing and a single-weight construction. The cobalt and warm amber palette signals trustworthiness and energy without the cold associations of typical enterprise software. All identity components are WCAG 2.1 AA compliant and have been tested at favicon scale."

## Logo System

[Document all approved logo variants with their intended usage contexts.

GUIDANCE:
- Good: "Primary lockup (wordmark + icon): use on white and light backgrounds. Reversed lockup (white on brand colour): use on dark and photographic backgrounds. Isolated icon: use only at sizes below 80px where full lockup is illegible."
- Bad: "Here is our logo."
- Format: Table with variant name, preview description, minimum size, and approved backgrounds]

| Variant | Description | Minimum Size | Approved Backgrounds |
|---------|------------|-------------|---------------------|
| Primary lockup | [wordmark + icon, full colour] | [32px height] | White, light grey (#F5F5F5 or lighter) |
| Reversed lockup | [wordmark + icon, white] | [32px height] | Brand primary, dark photography |
| Isolated icon | [icon only, full colour] | [16px height] | White, brand primary |
| Wordmark only | [text only, full colour] | [24px height] | [Contexts] |

**Clear Space Rule**: Minimum clear space on all sides = [X]px / [descriptor, e.g., "the height of the 'o' in the wordmark"].

**Incorrect Usage** (prohibited actions):
- [ ] Do not stretch or distort the logo
- [ ] Do not recolour the logo outside approved variants
- [ ] Do not place the primary logo on a busy photographic background without a clear space buffer
- [ ] Do not reproduce the logo below minimum size

## Colour System

[Document the complete palette with technical values and accessibility annotations.

GUIDANCE:
- Good: "Primary Blue #1A6CF4 RGB(26,108,244) HSL(219,91%,53%). Passes AA on white (ratio 4.8:1). Do NOT use as background with white body text — use Primary Dark #0F4AC2 instead."
- Bad: "Our primary colour is blue."
- Format: Swatch table with hex, RGB, HSL, WCAG ratio on white, and usage notes]

### Primary Palette

| Name | Hex | RGB | HSL | WCAG on White | Approved Use |
|------|-----|-----|-----|--------------|-------------|
| [Primary] | [#000000] | [0,0,0] | [0°,0%,0%] | [ratio:1] | [CTAs, headings, key UI elements] |
| [Primary Dark] | | | | | [Text on light backgrounds] |

### Secondary Palette

| Name | Hex | RGB | HSL | WCAG on White | Approved Use |
|------|-----|-----|-----|--------------|-------------|
| [Secondary] | | | | | |

### Neutral Palette

| Name | Hex | Lightness | Approved Use |
|------|-----|-----------|-------------|
| White | #FFFFFF | 100% | Backgrounds |
| [Grey 50] | | | [Surface backgrounds] |
| [Grey 200] | | | [Dividers, borders] |
| [Grey 600] | | | [Secondary text] |
| [Grey 900] | | | [Primary text] |
| Black | #000000 | 0% | [Use cases] |

## Typography System

[Document the complete type scale with specifications.

GUIDANCE:
- Good: "H1: Neue Montreal Bold, 56px/64px line-height, -0.5px tracking, letter-spacing: -0.01em. Use for page heroes only, max 2 lines."
- Bad: "Use Neue Montreal for headings."
- Format: Table with role, typeface, weight, size, line-height, tracking, and usage note]

### Type Scale

| Role | Typeface | Weight | Size | Line Height | Tracking | Context |
|------|---------|--------|------|------------|---------|---------|
| Display | [Typeface] | [Bold] | [64px] | [72px] | [-0.02em] | [Hero headlines] |
| H1 | | | [48px] | | | |
| H2 | | | [36px] | | | |
| H3 | | | [28px] | | | |
| Body Large | | | [18px] | | | |
| Body | | | [16px] | | [0.01em] | [Default body text] |
| Caption | | | [13px] | | | |
| UI Label | | | [12px] | | | |

**Web Font Loading**: [Font file format, hosting location, font-display strategy]

## Supporting Elements

[Document iconography style, illustration direction, photography guidelines, and layout principles.

GUIDANCE:
- Good: "Iconography: 24px grid, 2px stroke, rounded line caps, no fill. Source: custom icon library at [link]. Never mix with other icon libraries."
- Bad: "Use nice icons."]

### Iconography

**Style**: [Outline / Filled / Duotone]
**Grid**: [16px / 24px / 32px]
**Stroke weight**: [1.5px / 2px]
**Corner radius**: [0 / 2px / 4px — rounded vs. sharp]
**Source**: [Library name + link]

### Photography

**Style direction**: [Candid vs. staged; documentary vs. aspirational; product-in-context vs. abstract]
**Subject**: [People: age range, activity, setting; Products: flat lay, lifestyle, technical]
**Post-processing**: [Colour grading notes, contrast treatment, brand colour overlays if any]
**Prohibited**: [Stock photo clichés to avoid, e.g., "handshake photos", "pointing at whiteboards"]

### Layout Principles

**Grid**: [12-column, 24px gutters, 80px margins desktop / 4-column, 16px gutters, 24px margins mobile]
**Spacing unit**: [8px base unit]
**Principle**: [e.g., "Signal through whitespace: generous spacing signals quality; crowding signals noise"]

## Recommendations

[Prioritised actions to maintain identity health post-launch.

GUIDANCE: Each recommendation must be specific and owned. Example: "P1: Create a Figma component library from these guidelines so all product designers use live-linked tokens (Brand Designer, within 2 weeks of approval)."]

| Priority | Recommendation | Owner | Deadline |
|----------|---------------|-------|---------|
| P1 | [Create Figma token library] | [Brand Designer] | [Date] |
| P2 | [Quarterly identity audit] | [Brand Designer] | [Recurring] |

## Appendices

### A. Methodology

[Foundation documents reviewed, concept directions explored, stakeholder review rounds, accessibility testing tools used (e.g., Stark, Colour Contrast Analyser).]

### B. File Package

[Asset library location, folder structure, file formats delivered (SVG, PNG, EPS, Sketch, Figma).]
