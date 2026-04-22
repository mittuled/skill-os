---
name: developer-community-signal-extractor
description: >
  This skill extracts product and market signals from developer community forums and feedback.
  Use when asked to analyze developer forum discussions, surface SDK pain points, or detect API adoption trends.
  Also consider when engineering needs developer-sourced input for roadmap prioritization.
  Suggest when the user is about to plan a developer product cycle without community signal data.
department: marketing
agent: developer-relations-lead
version: 1.0.0
complexity: medium
related-skills:
  - developer-feedback-synthesiser
  - developer-experience-reviewer
  - community-signal-extractor
triggers:
  - "extract dev community signals"
  - "analyze developer feedback"
  - "developer sentiment analysis"
  - "community signal report"
  - "dev forum signal mining"
---

# developer-community-signal-extractor

## Agent: Developer Relations Lead

L2 developer relations lead responsible for developer community signal extraction, developer GTM, experience review, feedback synthesis, and community growth.

Department ethos: [ideal-marketing.md](../../../../departments/marketing/ideal-marketing.md)

## Skill Description

Extracts product and market signals from developer community forums and feedback channels to surface SDK pain points, API gaps, and adoption trends.

## When to Use

- When engineering or product teams need developer-sourced qualitative data for roadmap planning.
- When developer forum or Discord activity has grown beyond what can be manually monitored.
- When a new SDK or API version launches and early developer reactions need rapid capture.
- When Stack Overflow questions, GitHub issues, or forum threads reveal patterns that indicate systemic problems.

## Workflow

1. **Define signal taxonomy**: Use the developer signal taxonomy in [framework.md](references/framework.md) to select the relevant categories for this extraction cycle (API pain points, SDK bugs, missing features, documentation gaps, performance complaints, migration friction, praise signals). Deliverable: developer signal taxonomy.
2. **Map data sources**: Inventory all developer touchpoints using the source map in the framework (forums, Discord/Slack, GitHub issues, Stack Overflow, Twitter/X, conference feedback, support tickets). Deliverable: source map with access and volume notes.
3. **Extract and classify**: Review developer conversations and classify each signal using the classification protocol in the framework (category, severity P0–P3, product area, developer segment, frequency, verbatim quote). Deliverable: classified signal log.
4. **Identify patterns**: Cluster signals using the pattern analysis method from the framework — semantic clustering, product timeline correlation, segment weighting, and velocity tracking. Deliverable: pattern analysis with timeline correlation.
5. **Write signal brief**: Produce a concise brief connecting developer signal themes to product and engineering implications with specific recommendations ranked by severity and business impact. Deliverable: developer signal brief.
6. **Route and track**: Distribute signals per the routing matrix in the framework. Track which signals lead to action and report outcomes back to the community. Deliverable: signal routing tracker.

## Anti-Patterns

- **Platform myopia**: Monitoring only one channel (e.g., only GitHub issues) while ignoring where developers actually discuss problems (e.g., Twitter, Discord). *Why*: Developers fragment across platforms; single-channel monitoring creates blind spots on the most vocal or frustrated segments.
- **Volume as importance**: Treating the most-mentioned signal as the most important without weighting by developer segment or business impact. *Why*: A niche signal from enterprise developers may have higher revenue impact than a frequently mentioned issue from hobbyists.
- **Delayed reporting**: Collecting signals over weeks before reporting, missing the window when engineering could act. *Why*: Developer frustration compounds rapidly; signals reported after a sprint planning cycle waste a full iteration.

## Output

**On success**: Produces a developer signal brief containing classified signals, pattern analysis, and routed recommendations. Delivered to engineering, product, and developer relations teams.

**On failure**: Report which data sources were inaccessible, what time window was missed, and recommend alternative monitoring approaches. Every error must be actionable.

## Related Skills

- [`developer-feedback-synthesiser`](../developer-feedback-synthesiser/SKILL.md) — Synthesiser consumes signal outputs to produce actionable improvement plans.
- [`developer-experience-reviewer`](../developer-experience-reviewer/SKILL.md) — Signals about developer friction inform targeted experience reviews.
- [`community-signal-extractor`](../../../marketing/community-manager/community-signal-extractor/SKILL.md) — Parallel skill for general community signals; developer version focuses on technical channels.
