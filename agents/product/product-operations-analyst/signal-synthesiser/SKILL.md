---
name: signal-synthesiser
description: >
  This skill synthesises signals from multiple sources (usage, support, sales, NPS) into actionable product insights.
  Use when the team has data from multiple channels but lacks a unified view of what it all means for the product.
  Also consider when conflicting signals from different sources are causing decision paralysis.
  Suggest when a planning cycle is starting and no cross-source signal summary exists for the current period.
department: product
agent: product-operations-analyst
version: 1.0.0
complexity: medium
related-skills: []
---

# signal-synthesiser

## Agent: Product Operations Analyst
L3 product operations analyst (multi-instance) responsible for rollout configuration, adoption tracking, revenue impact monitoring, support triage, and iteration prioritisation.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Synthesises signals from multiple sources (usage, support, sales, NPS) into actionable product insights.

## When to Use
- When the product team needs a unified view across usage analytics, support tickets, sales feedback, NPS results, and customer interviews
- When individual signal sources tell different stories and the team needs to reconcile conflicting data
- When a planning or prioritisation cycle requires an up-to-date synthesis of what customers are experiencing
- When leadership asks "what are customers telling us?" and the answer lives in five different systems

## Workflow
1. **Collect signals from all sources**: Gather data from each signal channel — usage analytics (adoption, engagement, drop-off), support tickets (themes, volume, severity), sales feedback (objections, feature requests, competitive mentions), NPS/CSAT scores and verbatims, and customer interview notes. Deliverable: raw signal inventory with source, date range, and volume per channel.
2. **Normalise and categorise**: Map signals from different sources to a common taxonomy — feature areas, user journey stages, or problem categories. This allows comparison across sources that use different vocabularies. Deliverable: categorised signal table with normalised labels across all sources.
3. **Identify convergent themes**: Find themes where multiple sources point in the same direction — e.g., usage drop-off in a feature area that also generates high support volume and negative NPS comments. Rank convergent themes by signal strength (number of sources, data volume, severity). Deliverable: convergent theme list ranked by signal strength with supporting evidence per theme.
4. **Flag divergent signals**: Identify areas where sources contradict — e.g., high usage but high complaints, or positive NPS but declining adoption. Investigate possible explanations (power users love it but new users struggle, or satisfaction is high but the feature is hard to discover). Deliverable: divergence report with hypotheses for each contradiction.
5. **Produce the synthesis**: Write a concise synthesis document covering the top 3-5 themes, supporting evidence from each source, signal strength assessment, and recommended product actions. Distinguish between signals that require immediate response and those that inform longer-term planning. Deliverable: signal synthesis report with executive summary, theme details, and prioritised action recommendations.

## Anti-Patterns
- **Cherry-picking signals that confirm existing plans**: Selecting data that supports what the team already wants to build while ignoring contradictory evidence. *Why*: Confirmation bias turns signal synthesis into a rubber stamp for predetermined decisions, negating its value as an objective input.
- **Treating all sources as equally reliable**: Weighting a single customer interview the same as usage data from 10,000 users. *Why*: Signal quality and statistical significance vary enormously across sources — synthesis must account for confidence levels.
- **Synthesising without making it actionable**: Producing a comprehensive data summary that describes what is happening without recommending what to do about it. *Why*: The purpose of synthesis is to inform decisions — a report that requires the reader to draw their own conclusions adds a step and risks misinterpretation.
- **Infrequent synthesis**: Running the synthesis quarterly when signals change weekly. *Why*: Stale synthesis means the product team operates on outdated information during the intervals, leading to delayed responses to emerging issues.

## Output
**On success**: A signal synthesis report containing the top 3-5 themes with multi-source evidence, signal strength rankings, divergence analysis with hypotheses, and prioritised action recommendations — formatted for product leadership and planning consumption.
**On failure**: Report which signal sources were unavailable or incomplete (e.g., NPS survey not yet closed, sales CRM data export delayed), what partial synthesis was produced, and recommend a timeline for completing the full synthesis once data gaps close.

## Related Skills
- (none yet — cross-references added in Phase 1.6)
