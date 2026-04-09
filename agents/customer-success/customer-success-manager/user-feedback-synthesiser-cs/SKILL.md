---
name: user-feedback-synthesiser-cs
description: >
  This skill synthesises qualitative customer feedback from CS interactions into
  themes for product and support. Use when asked to aggregate feedback, identify
  feedback themes, or produce voice-of-customer reports. Also consider when
  product planning needs structured customer input. Suggest when the user makes
  roadmap decisions without synthesized customer feedback.
department: customer-success
agent: customer-success-manager
version: 1.0.0
complexity: simple
related-skills: []
triggers:
  - "synthesise user feedback"
  - "synthesize feedback cs"
  - "summarize customer feedback"
  - "user feedback synthesis"
  - "feedback analysis cs"
---

# user-feedback-synthesiser-cs

## Agent: Customer Success Manager

L3 customer success manager (Nx) responsible for signal extraction, feedback synthesis, early adopter success, and customer activation.

Department ethos: [ideal-customer-success.md](../../../../departments/customer-success/ideal-customer-success.md)

## Skill Description

Synthesises qualitative customer feedback from CS interactions into thematic insights for product, support, and leadership teams.

## When to Use

- When accumulated CS signals and feedback need to be aggregated into themes for product planning.
- When product or leadership teams request a voice-of-customer summary for decision-making.
- When a feedback synthesis cycle is due (monthly, quarterly) to maintain a current view of customer sentiment.

## Workflow

1. **Aggregate Feedback**: Collect all customer feedback from the period: CS signal logs, NPS verbatims, support ticket themes, QBR notes, and CSM observations. Deliverable: raw feedback corpus.
2. **Identify Themes**: Group feedback into recurring themes using affinity clustering. Quantify each theme by frequency and customer count. Deliverable: theme list with frequency data.
3. **Assess Impact**: For each theme, estimate business impact -- revenue at risk, expansion blocked, or satisfaction affected. Deliverable: impact-rated theme list.
4. **Produce Synthesis Report**: Write the voice-of-customer report with themes ranked by impact, representative quotes, and recommended actions. Deliverable: feedback synthesis report.

## Anti-Patterns

- **Cherry-picking feedback**: Selecting feedback that supports a predetermined narrative rather than representing the full spectrum. *Why*: biased synthesis leads to product decisions that address the wrong problems.
- **Themes without evidence**: Claiming feedback themes without backing them with specific customer examples and frequency data. *Why*: unsupported themes are easily dismissed; evidence makes them actionable.
- **Synthesis without routing**: Producing reports that are not delivered to the teams who can act on them. *Why*: feedback that sits in a document creates no value; routing ensures accountability.

## Output

**On success**: Produces a feedback synthesis report containing impact-rated themes, representative quotes, frequency data, and recommended actions. Delivered to product, support, and leadership.

**On failure**: Report which feedback sources could not be accessed (missing logs, incomplete data), what partial synthesis was achieved, and what data gaps should be addressed.

## Related Skills

- [`cs-signal-extractor`](../cs-signal-extractor/SKILL.md) -- Individual signals that feed into thematic synthesis.
- [`nps-programme-manager`](../../../customer-success/customer-programs-manager/nps-programme-manager/SKILL.md) -- NPS verbatims are a key feedback source for synthesis.
- [`cs-health-monitor`](../../../customer-success/cs-manager/cs-health-monitor/SKILL.md) -- Feedback themes may explain health score trends.
