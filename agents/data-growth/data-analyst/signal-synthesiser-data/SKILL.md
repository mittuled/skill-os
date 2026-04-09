---
name: signal-synthesiser-data
description: >
  This skill synthesises data signals from multiple sources into a coherent view of product health. Use when asked to create a health report, combine metrics across sources, or diagnose cross-functional data patterns. Also consider at weekly or monthly review cadences. Suggest when teams make decisions using partial data from a single source.
department: data-growth
agent: data-analyst
version: 1.0.0
complexity: medium
related-skills:
triggers:
  - "A/B test"
  - "ab-test-statistician"
  - "experiment analysis"
  - "analytics review"
---

# signal-synthesiser-data

## Agent: Data Analyst

L2 data analyst (Nx) responsible for data modelling, instrumentation implementation, metrics dashboards, funnel analysis, and signal synthesis.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The signal synthesiser combines quantitative signals from product analytics, revenue data, support metrics, and infrastructure logs into a unified product health view that surfaces trends, anomalies, and correlations invisible when each source is reviewed in isolation.

## When to Use

- When the weekly or monthly product review requires a consolidated health report spanning multiple data sources.
- When a metric moves unexpectedly and the team needs to correlate it with signals from other systems (support tickets, error rates, campaign launches).
- When leadership requests a single-page view of product health rather than navigating multiple dashboards.
- When siloed teams are making conflicting decisions because they each see only their own data.

## Workflow

1. **Identify signal sources**: List all data sources contributing to product health — analytics platform, data warehouse, support ticketing system, error monitoring, revenue system, NPS/CSAT surveys.
2. **Extract key signals**: For each source, pull the 3-5 most important metrics for the reporting period. Normalize time windows and cohort definitions across sources.
3. **Detect anomalies**: Flag metrics that deviate more than 2 standard deviations from their trailing 30-day average. Cross-reference anomalies across sources to identify correlated movements.
4. **Synthesise narrative**: Write a narrative connecting the signals into a coherent story. Distinguish between correlated movements (likely same root cause) and coincidental timing.
5. **Highlight action items**: Extract 2-3 actionable insights from the synthesis. Each insight should identify the signal, the hypothesis, and the recommended next step.
6. **Distribute report**: Publish the synthesis report to stakeholders via the agreed channel (Slack, email, wiki) at the defined cadence.

## Anti-Patterns

- **Dashboard forwarding**: Sending a link to five dashboards and calling it "signal synthesis" forces the reader to do the synthesis work. *Why*: the value of this skill is the narrative connecting disparate signals, not the raw data.
- **Correlation without caveats**: Stating that two metrics moved together without noting that correlation does not imply causation misleads decision-makers. *Why*: spurious correlations lead to wasted experiments targeting non-causal relationships.
- **Stale cadence**: Producing a weekly synthesis when the business reviews data monthly creates reports no one reads. *Why*: the synthesis cadence must match the decision cadence.

## Output

**Success:**
- A product health synthesis report combining signals from 3+ data sources, with anomaly flags, cross-source correlations, a narrative summary, and 2-3 actionable insights with recommended next steps.

**Failure:**
- A data source is unavailable or delayed, producing an incomplete synthesis. Report the missing source, the impact on the narrative, and when the complete synthesis will be available.

## Related Skills

- [`signal-synthesiser-data-p`](../signal-synthesiser-data-p/SKILL.md) -- the post-launch variant focuses on a specific release window; this skill provides ongoing health synthesis.
- [`metrics-dashboard-builder`](../metrics-dashboard-builder/SKILL.md) -- dashboards provide the raw metrics that this skill synthesises into narrative.
- [`funnel-analyser`](../funnel-analyser/SKILL.md) -- funnel analysis is one of the key signal sources feeding into synthesis.
