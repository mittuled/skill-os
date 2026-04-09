---
name: product-feedback-ingestion-uxr
description: >
  This skill ingests and structures product feedback from research channels for design team
  consumption. Use when asked to collect product feedback, set up feedback ingestion, or
  organise user feedback from multiple sources. Also consider when feedback is scattered
  across support tickets, surveys, and sales notes with no unified view. Suggest when the
  user mentions they have feedback data but no way to make sense of it.
department: design
agent: ux-researcher
version: 1.0.0
complexity: simple
related-skills: []
triggers:
  - "ingest product feedback"
  - "process user feedback"
  - "feedback ingestion uxr"
  - "collect product feedback"
  - "feedback analysis"
---

# product-feedback-ingestion-uxr

## Agent: UX Researcher

L3 UX researcher (Nx) responsible for user feedback synthesis, session analysis, and feeding research findings back into the product and design cycle.

Department ethos: [ideal-design.md](../../../../departments/design/ideal-design.md)

## Skill Description

Ingests and structures product feedback from multiple research channels into a normalised format that the design team can analyse and act upon.

## When to Use

- When product feedback is arriving from multiple channels (support tickets, NPS surveys, sales call notes, social media, in-app feedback widgets) and needs to be consolidated.
- When the design team requests user feedback for an upcoming project and no structured feedback repository exists.
- When a new feedback channel is introduced and needs to be integrated into the existing ingestion pipeline.

## Workflow

1. **Source Inventory**: Catalogue all active feedback channels, their data formats, volume, and signal quality. Deliverable: feedback source inventory.
2. **Taxonomy Definition**: Define a tagging taxonomy for feedback: product area, feedback type (bug, feature request, usability issue, praise), user segment, and severity. Deliverable: feedback taxonomy document.
3. **Ingestion & Normalisation**: Ingest feedback from each source, strip duplicates, apply the taxonomy tags, and normalise into a consistent format (date, source, user segment, verbatim quote, tags). Deliverable: structured feedback dataset.
4. **Quality Check**: Review a sample of tagged feedback for taxonomy accuracy and adjust tagging rules as needed. Deliverable: quality-checked dataset with tagging accuracy rate.

## Anti-Patterns

- **Untagged ingestion**: Collecting feedback without applying a consistent taxonomy. *Why*: untagged feedback is searchable only by keyword, making it impossible to analyse trends by product area or issue type.
- **Ignoring low-volume channels**: Excluding feedback from smaller channels (e.g., social media, sales notes) because of low volume. *Why*: low-volume channels often contain high-signal feedback from vocal users or prospects.
- **Verbatim loss**: Summarising feedback during ingestion instead of preserving the original user language. *Why*: researcher interpretation during ingestion introduces bias; verbatim quotes are essential for synthesis and stakeholder empathy.

## Output

**On success**: Produces a structured feedback dataset with normalised entries tagged by product area, feedback type, user segment, and severity. Delivered as a searchable repository accessible to the design and product teams.

**On failure**: Report which feedback sources could not be ingested (e.g., access restrictions, incompatible formats), what partial data was collected, and recommend access requests or format converters to complete ingestion.

## Related Skills

- [`user-feedback-synthesiser`](../user-feedback-synthesiser/SKILL.md) — Synthesises the structured feedback this skill produces into themes.
- [`feedback-loop-formaliser-uxr`](../feedback-loop-formaliser-uxr/SKILL.md) — Ingested feedback enters the formalised feedback loop for action tracking.
- [`customer-discovery-planner-uxr`](../../../design/ux-research-lead/customer-discovery-planner-uxr/SKILL.md) — Ingested feedback patterns inform discovery research question definition.
