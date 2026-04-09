---
name: brand-identity-v1
description: >
  This skill designs the v1 brand identity including logo, colour palette, typography, and
  usage guidelines. Use when asked to create a visual identity system, design a logo, or
  build a brand style guide. Also consider when a product has brand foundations but no
  visual system. Suggest when the user is about to create marketing assets without an
  established identity kit.
department: design
agent: brand-designer
version: 1.0.0
complexity: complex
related-skills: []
triggers:
  - "brand identity"
  - "create brand identity"
  - "brand v1"
  - "initial brand design"
  - "brand guidelines"
---

# brand-identity-v1

## Agent: Brand Designer

L2 brand designer (1x) responsible for brand foundation, visual identity, and positioning expression through design.

Department ethos: [ideal-design.md](../../../../departments/design/ideal-design.md)

## Skill Description

Designs the v1 brand identity including logo, colour palette, typography, and usage guidelines that translate brand foundations into a cohesive visual system.

## When to Use

- When brand foundations are approved and the product needs its first visual identity system before any marketing or product design begins.
- When a startup is preparing for public launch and needs a logo, colour palette, typography, and brand guidelines to ensure consistent visual output.
- When existing visual assets were created ad hoc without a systematic identity and need to be replaced with a coherent v1 system.

## Workflow

1. **Foundation Review**: Read the approved brand foundation document and extract the visual principles, personality traits, and tone attributes that must be expressed visually. Deliverable: design brief summarising visual constraints and aspirations.
2. **Moodboard & Direction Exploration**: Create 2-3 visual direction moodboards exploring different aesthetic interpretations of the brand personality (e.g., geometric vs. organic, high-contrast vs. muted). Deliverable: moodboard deck with rationale per direction.
3. **Logo Concept Development**: Design 3-5 logo concepts across the selected direction(s), exploring wordmarks, lettermarks, and combination marks as appropriate. Test each at minimum viable sizes (16px favicon, 32px app icon). Deliverable: logo concept presentation with usage rationale.
4. **Colour Palette Definition**: Define primary, secondary, and neutral colour palettes with hex/RGB/HSL values. Validate all foreground/background combinations against WCAG 2.1 AA contrast ratios (4.5:1 for body text, 3:1 for large text). Deliverable: colour system with accessibility annotations.
5. **Typography Selection**: Select primary and secondary typefaces with a clear hierarchy (headings, body, captions, UI labels). Specify weights, sizes, and line-height scales. Verify web font availability and performance impact. Deliverable: type scale specification.
6. **Supporting Elements**: Define supplementary identity elements: iconography style, illustration direction, photography guidelines, and spacing/layout principles. Deliverable: supporting elements reference sheet.
7. **Brand Guidelines Assembly**: Compile all identity elements into a brand guidelines document with correct/incorrect usage examples, minimum clear space rules, and file format specifications (SVG, PNG, EPS). Deliverable: v1 brand guidelines document.
8. **Stakeholder Review & Iteration**: Present the complete identity system to stakeholders, collect structured feedback, and iterate. Resolve conflicts by referring back to brand foundation principles. Deliverable: approved v1 brand identity.
9. **Asset Export & Handoff**: Export all final assets in required formats and organise into a shared asset library. Deliverable: brand asset package with naming conventions and folder structure.

## Anti-Patterns

- **Designing without foundations**: Starting logo exploration before brand values and personality are documented. *Why*: visual choices become arbitrary preference debates instead of strategic decisions traceable to brand principles.
- **Single-concept presentation**: Showing only one logo direction to stakeholders. *Why*: it frames the conversation as accept/reject rather than comparative evaluation, producing weaker outcomes and more revision cycles.
- **Ignoring accessibility in colour**: Selecting palette colours based on aesthetics alone without checking contrast ratios. *Why*: inaccessible colour combinations exclude users and require costly retrofits once caught in product development.
- **Missing usage constraints**: Delivering logo files without clear-space rules, minimum sizes, or incorrect-usage examples. *Why*: without constraints, the identity degrades as different teams stretch, recolour, or crowd the logo.
- **Skipping small-size testing**: Designing logos only at presentation scale without verifying legibility at favicon and app-icon sizes. *Why*: most real-world logo encounters happen at small sizes; a logo that fails there fails in practice.

## Output

**On success**: Produces a v1 brand identity package containing logo files (SVG, PNG, EPS), colour palette with accessibility annotations, type scale specification, supporting element guidelines, and a comprehensive brand guidelines document. Delivered as an organised asset library with a guidelines PDF or markdown document.

**On failure**: Report which identity elements could not be finalised (e.g., stakeholder disagreement on logo direction), what alternatives were explored, and recommend a structured decision process (e.g., user preference testing, executive tiebreak) to resolve.

## Related Skills

- [`brand-foundation`](../brand-foundation/SKILL.md) — This skill consumes the brand values and visual principles defined during foundation work.
- [`launch-narrative-brand`](../launch-narrative-brand/SKILL.md) — Launch visual storytelling assets depend on the identity system created here.
- [`positioning-crafter-brand`](../positioning-crafter-brand/SKILL.md) — Visual positioning expression uses the identity toolkit as its design vocabulary.
