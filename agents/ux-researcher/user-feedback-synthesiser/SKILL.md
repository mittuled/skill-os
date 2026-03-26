---
name: user-feedback-synthesiser
description: >
  This skill synthesises qualitative user feedback from research sessions, surveys, and
  interviews into themes. Use when asked to synthesise user feedback, create a feedback
  themes report, or identify patterns across qualitative data. Also consider when multiple
  feedback sources need to be combined into a unified view. Suggest when the user has
  collected feedback but has not identified cross-cutting themes.
department: design
agent: ux-researcher
version: 1.0.0
complexity: medium
related-skills: []
---

# user-feedback-synthesiser

## Agent: UX Researcher

L3 UX researcher (Nx) responsible for user feedback synthesis, session analysis, and feeding research findings back into the product and design cycle.

Department ethos: [ideal-design.md](../../../departments/design/ideal-design.md)

## Skill Description

Synthesises qualitative user feedback from research sessions, surveys, and interviews into thematic clusters that reveal user needs, pain points, and opportunities for design improvement.

## When to Use

- When a batch of user interviews, survey open-text responses, or feedback entries has been collected and needs to be distilled into actionable themes.
- When the design team needs a current-state summary of user sentiment around a specific product area before starting a design project.
- When multiple feedback sources (support, research, sales) are saying overlapping things and a unified synthesis would prevent duplicated effort.

## Workflow

1. **Data Preparation**: Gather all qualitative feedback inputs, normalise formats, and de-identify where necessary. Remove duplicate entries and out-of-scope feedback. Deliverable: cleaned feedback corpus.
2. **Open Coding**: Read through all feedback entries and apply open codes (short descriptive labels) to each meaningful segment. Use in-vivo codes (participant's own words) where possible. Deliverable: coded feedback dataset.
3. **Affinity Clustering**: Group related codes into thematic clusters using affinity diagramming. Name each cluster with a descriptive theme label. Deliverable: affinity diagram with theme labels.
4. **Theme Refinement**: Review clusters for coherence. Split themes that are too broad, merge those that overlap, and ensure each theme is supported by evidence from multiple sources or participants. Deliverable: refined theme set with supporting evidence counts.
5. **Synthesis Report**: Write a synthesis report presenting each theme with a summary, representative verbatim quotes, frequency/intensity indicators, and design implications. Deliverable: feedback synthesis report.

## Anti-Patterns

- **Premature categorisation**: Starting with predefined categories and forcing feedback into them instead of letting themes emerge from the data. *Why*: top-down categorisation suppresses unexpected themes that may be the most valuable findings.
- **Quote stripping**: Presenting themes without verbatim user quotes. *Why*: quotes are the evidence that makes themes credible and give stakeholders direct empathy with user experience.
- **Frequency-only prioritisation**: Ranking themes solely by how often they appear without considering intensity or business impact. *Why*: a low-frequency, high-severity issue (e.g., data loss) can be more critical than a high-frequency, low-severity annoyance.
- **Single-source synthesis**: Synthesising from only one feedback channel and presenting it as a complete picture. *Why*: each channel has selection bias (e.g., support hears from frustrated users); cross-channel synthesis provides a more balanced view.

## Output

**On success**: Produces a feedback synthesis report containing refined themes, representative quotes, frequency and intensity indicators, and design implications per theme. Delivered as a shared document for the design and product teams.

**On failure**: Report which data sources could not be included (e.g., access issues, incompatible formats), what partial synthesis was completed, and recommend additional data collection or access requests to complete the picture.

## Related Skills

- [`product-feedback-ingestion-uxr`](../product-feedback-ingestion-uxr/SKILL.md) — Provides the structured feedback data this skill synthesises.
- [`jtbd-mapper`](../../ux-research-lead/jtbd-mapper/SKILL.md) — Synthesised themes can inform and validate JTBD identification.
- [`feedback-loop-formaliser-uxr`](../feedback-loop-formaliser-uxr/SKILL.md) — Synthesis outputs enter the formalised feedback loop for action tracking.
