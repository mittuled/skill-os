---
name: brand-foundation
description: >
  This skill establishes the brand foundation including values, personality, tone, and visual
  principles. Use when asked to define brand values, create a brand personality framework, or
  establish tone-of-voice guidelines. Also consider when a new product needs its foundational
  brand pillars before any visual design begins. Suggest when the user is about to design a
  logo or identity system without documented brand principles.
department: design
agent: brand-designer
version: 1.0.0
complexity: medium
related-skills: []
---

# brand-foundation

## Agent: Brand Designer

L2 brand designer (1x) responsible for brand foundation, visual identity, and positioning expression through design.

Department ethos: [ideal-design.md](../../../departments/design/ideal-design.md)
Tool policy: [allowed-tools.yaml](../../../allowed-tools.yaml)

## Skill Description

Establishes the brand foundation including values, personality, tone, and visual principles that anchor all subsequent identity and communication decisions.

## When to Use

- When a new company or product needs its core brand pillars defined before visual identity work begins.
- When an existing brand lacks documented values, personality traits, or tone-of-voice guidelines and design decisions are made inconsistently.
- When a rebrand or brand evolution requires revisiting foundational principles to ensure the updated identity has strategic grounding.

## Workflow

1. **Stakeholder Discovery**: Conduct brand workshops or structured interviews with founders and key stakeholders to surface mission, vision, and aspirational qualities. Deliverable: raw workshop notes with verbatim quotes and recurring themes.
2. **Competitive Landscape Audit**: Map competitor brand positions across personality dimensions (e.g., formal vs. casual, premium vs. accessible) to identify whitespace. Deliverable: competitive positioning matrix.
3. **Values Distillation**: Synthesise workshop outputs into 3-5 core brand values, each with a one-sentence rationale and behavioural definition. Deliverable: brand values framework document.
4. **Personality & Tone Definition**: Define brand personality traits using a spectrum model (e.g., "confident, not arrogant") and translate into tone-of-voice guidelines with do/don't examples. Deliverable: personality and tone-of-voice guide.
5. **Visual Principles Articulation**: Derive 3-5 visual design principles from the brand values (e.g., "clarity over decoration") that will govern typography, colour, layout, and imagery choices. Deliverable: visual principles brief.
6. **Foundation Review**: Present the complete brand foundation to stakeholders for alignment and sign-off, iterating on any misalignments. Deliverable: approved brand foundation document.

## Anti-Patterns

- **Skipping stakeholder input**: Deriving brand values from competitor analysis alone without internal discovery. *Why*: brand values that don't reflect genuine organisational beliefs ring hollow and get ignored in practice.
- **Value inflation**: Defining more than 5 core values to avoid making hard choices. *Why*: too many values dilute focus and make them impossible to remember or apply consistently.
- **Tone without examples**: Stating tone attributes (e.g., "friendly") without concrete do/don't copy examples. *Why*: abstract tone descriptors are interpreted differently by every writer, defeating the purpose of standardisation.
- **Treating foundation as optional**: Jumping straight to logo design without documented principles. *Why*: visual identity built without foundational alignment produces designs that look good but don't communicate the right things.

## Output

**On success**: Produces a brand foundation document containing core values with definitions, brand personality spectrum, tone-of-voice guidelines with examples, and visual design principles. Delivered as a versioned markdown or PDF artifact shared with stakeholders and referenced by all downstream brand and content work.

**On failure**: Report which foundation elements could not be resolved (e.g., conflicting stakeholder visions), what was attempted to reconcile them, and recommend a follow-up workshop or decision-maker tiebreak to unblock.

## Related Skills

- [`brand-identity-v1`](../brand-identity-v1/SKILL.md) — Brand identity design depends on the foundation this skill produces.
- [`positioning-crafter-brand`](../positioning-crafter-brand/SKILL.md) — Visual positioning expression requires established brand values and personality as input.
- [`content-design-spec`](../../content-design-lead/content-design-spec/SKILL.md) — Content design specs operationalise the tone-of-voice guidelines created here.
