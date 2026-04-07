---
name: community-signal-extractor
description: >
  This skill extracts product and market signals from community conversations.
  Use when asked to mine community feedback, identify feature requests from discussions, or detect emerging trends.
  Also consider when product teams need qualitative input beyond support tickets.
  Suggest when the user is about to make product decisions without consulting community conversation data.
department: marketing
agent: community-manager
version: 1.0.0
complexity: medium
related-skills: []
---

# community-signal-extractor

## Agent: Community Manager

L2 community manager responsible for extracting community signals, designing community-led growth, building the early community, and maintaining community health.

Department ethos: [ideal-marketing.md](../../../../departments/marketing/ideal-marketing.md)

## Skill Description

Extracts product and market signals from community conversations to surface feature requests, sentiment shifts, and competitive intelligence.

## When to Use

- When the product team needs qualitative user feedback beyond structured surveys and support tickets.
- When community conversation volume has grown and manual monitoring no longer catches important signals.
- When preparing for a product planning cycle and needing community-sourced input.
- When a competitor announcement triggers community discussion that contains strategic intelligence.

## Workflow

1. **Define signal categories**: Use the signal taxonomy in [framework.md](references/framework.md) to select the categories relevant to this extraction cycle (feature requests, pain points, competitor mentions, praise, churn indicators, use-case discoveries). Deliverable: signal taxonomy document.
2. **Select data sources**: Inventory all relevant channels per the source inventory model in the framework (public channels, DMs with consent, event feedback, social mentions). Deliverable: source inventory with access status.
3. **Extract and tag signals**: Review conversations and tag each signal using the tagging protocol in the framework (category, severity P0–P3, frequency, source attribution, verbatim quote). Deliverable: tagged signal database or spreadsheet.
4. **Cluster and prioritize**: Group signals with > 60% semantic overlap into themes per the clustering method in the framework. Rank P0/P1 signals for immediate routing. Deliverable: prioritized signal report with theme clusters.
5. **Synthesize insights**: Write a narrative summary using [signal-report-template.md](assets/signal-report-template.md) connecting signal themes to product and market implications. Deliverable: signal report for product and leadership teams.
6. **Distribute and close loop**: Route signals to the appropriate team per the routing matrix in the framework. Post community acknowledgments for signals that led to action per the closing-the-loop protocol. Deliverable: routing log and community acknowledgment posts.

## Anti-Patterns

- **Cherry-picking signals**: Selecting only signals that confirm existing product direction while ignoring contradictory feedback. *Why*: Confirmation bias wastes the unique value of community data, which is its ability to surface surprises and blind spots.
- **Extracting without attribution**: Reporting signal themes without linking back to specific conversations or members. *Why*: Stakeholders cannot verify signal validity or follow up for deeper understanding without source attribution.
- **Signal hoarding**: Collecting signals but never distributing them to the teams that can act on them. *Why*: Unreported signals have zero value and erode community trust when members see their feedback disappear without response.

## Output

**On success**: Produces a prioritized signal report and insight memo containing tagged signals, theme clusters, and strategic implications. Delivered to product, marketing, and community leadership.

**On failure**: Report which data sources were inaccessible, what time periods could not be covered, and recommend alternative extraction methods. Every error must be actionable.

## Related Skills

- [`community-health-grower`](../community-health-grower/SKILL.md) — Sentiment signals extracted here feed into health metric tracking.
- [`community-led-growth-designer`](../community-led-growth-designer/SKILL.md) — Signals about what motivates members inform growth programme design.
- [`developer-community-signal-extractor`](../../../marketing/developer-relations-lead/developer-community-signal-extractor/SKILL.md) — Parallel skill for developer-specific community signal extraction.
