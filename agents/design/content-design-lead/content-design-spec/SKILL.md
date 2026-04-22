---
name: content-design-spec
description: >
  This skill writes the content design specification defining voice, tone, and copy standards
  for the product. Use when asked to create a voice and tone guide, define copy standards, or
  write a content style guide. Also consider when multiple writers are producing inconsistent
  copy across product surfaces. Suggest when the user is about to scale the content team
  without documented standards.
department: design
agent: content-design-lead
version: 1.0.0
complexity: complex
related-skills:
  - brand-foundation
  - ux-copy-writer
  - copy-implementation-reviewer
triggers:
  - "content design spec"
  - "content spec"
  - "write content spec"
  - "content design document"
  - "content guidelines"
---

# content-design-spec

## Agent: Content Design Lead

L2 content design lead (1x) (moved from Product, now reports to Head of Design) responsible for microcopy, voice standards, UX copy, and help content architecture.

Department ethos: [ideal-design.md](../../../../departments/design/ideal-design.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Writes the content design specification defining voice, tone, and copy standards that ensure every word in the product reinforces the brand and helps users accomplish their goals.

## When to Use

- When a product has no documented voice and tone guidelines and copy decisions are made ad hoc by individual writers or designers.
- When the brand foundation has been established and voice attributes need to be operationalised into concrete writing rules for product surfaces.
- When copy inconsistencies across the product (different terminology for the same concept, conflicting tone in error messages vs. onboarding) signal the need for standardisation.

## Workflow

1. **Brand Voice Intake**: Review the brand foundation document, particularly personality traits and tone-of-voice guidelines. Interview stakeholders on any product-specific voice nuances not covered in brand docs. Deliverable: voice input summary.
2. **Content Audit**: Audit existing product copy across key surfaces (onboarding, empty states, error messages, settings, notifications) to catalogue inconsistencies and identify existing patterns worth preserving. Deliverable: content audit findings.
3. **Voice Definition**: Define the product voice as 3-5 attributes, each with a spectrum (e.g., "direct, not blunt"), do/don't copy examples, and guidance on when to modulate tone (e.g., error states require more empathy than confirmation dialogs). Deliverable: voice and tone framework.
4. **Terminology Glossary**: Create a glossary of product-specific terms with approved usage, capitalisation, and any deprecated alternatives. Include terms users encounter in the UI, help content, and marketing. Deliverable: terminology glossary.
5. **Copy Pattern Library**: Document reusable copy patterns for common UI elements: button labels, form validation messages, empty states, success confirmations, destructive action warnings, and loading states. Include the structural formula and 2-3 examples per pattern. Deliverable: copy pattern library.
6. **Grammar & Mechanics Rules**: Define rules for capitalisation (sentence case vs. title case), punctuation in UI, number formatting, date/time formatting, and abbreviation use. Deliverable: grammar and mechanics section.
7. **Accessibility Copy Standards**: Document standards for writing accessible copy: alt text conventions, ARIA label patterns, screen-reader-friendly link text, and error message association. Deliverable: accessibility copy guidelines.
8. **Review & Approval**: Present the complete spec to design, product, and engineering leads. Iterate on contested decisions. Deliverable: approved content design specification.

## Anti-Patterns

- **Voice without examples**: Describing voice attributes abstractly without showing real product copy examples in do/don't format. *Why*: writers interpret abstract guidance differently; concrete examples are the only way to transmit voice consistently.
- **Spec without pattern library**: Defining voice and tone but not providing reusable copy patterns for common UI elements. *Why*: writers must reinvent copy for every button and error message, producing inconsistency despite having a voice guide.
- **Ignoring tone modulation**: Defining a single tone for all contexts instead of specifying how tone shifts across situations (celebration vs. error vs. destructive action). *Why*: a chirpy tone in an error state or a formal tone in a success moment both feel wrong; context-aware tone guidance prevents this.
- **One-time document**: Treating the spec as a finished artifact rather than a living document that evolves with the product. *Why*: products evolve, new surfaces appear, and terminology changes; a static spec becomes irrelevant and ignored.
- **Skipping accessibility**: Omitting guidance on accessible copy patterns (alt text, ARIA labels, screen-reader link text). *Why*: inaccessible copy excludes users who rely on assistive technology and may violate compliance requirements.

## Output

**On success**: Produces a content design specification containing voice and tone framework with examples, terminology glossary, copy pattern library, grammar and mechanics rules, and accessibility copy standards. Delivered as a living document (wiki, shared doc, or design system page) accessible to all writers, designers, and engineers.

**On failure**: Report which spec sections could not be completed (e.g., unresolved terminology disputes, missing brand foundation inputs), what was drafted, and recommend specific decisions or inputs needed to finalise.

## Related Skills

- [`brand-foundation`](../../../design/brand-designer/brand-foundation/SKILL.md) — Brand personality and tone guidelines are the upstream input for this spec.
- [`ux-copy-writer`](../ux-copy-writer/SKILL.md) — UX copy writing executes against the standards defined in this spec.
- [`copy-implementation-reviewer`](../copy-implementation-reviewer/SKILL.md) — Implementation review validates that shipped copy conforms to this spec.
