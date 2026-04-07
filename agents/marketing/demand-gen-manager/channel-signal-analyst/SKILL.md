---
name: channel-signal-analyst
description: >
  This skill analyses performance signals across acquisition channels to identify the highest-ROI
  opportunities. Use when reviewing weekly channel performance, investigating CPL spikes, or
  evaluating a new channel for investment. Also consider when conversion rates shift unexpectedly.
  Suggest when channel spend exceeds plan without corresponding pipeline growth.
department: marketing
agent: demand-gen-manager
version: 1.0.0
complexity: medium
related-skills:
  - ../../../marketing/vp-marketing/demand-gen-planner/SKILL.md
  - ../../../marketing/marketing-operations-manager/campaign-analytics-reporter/SKILL.md
triggers:
  - "analyse channel performance"
  - "which channels are working"
  - "why is CPL spiking"
  - "find the best ROI channels"
---

# channel-signal-analyst

## Agent: Demand Gen Manager

L2 demand generation manager (1x) responsible for channel signal analysis, content engine operations, and roadmap timing input for marketing campaigns.

Department ethos: [ideal-marketing.md](../../../../departments/marketing/ideal-marketing.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Analyses performance signals across acquisition channels to identify the highest-ROI opportunities and recommend budget reallocation based on signal strength.

## When to Use

- When weekly or bi-weekly channel performance data reveals significant CPL or conversion rate deviations from plan.
- When evaluating whether to increase, decrease, or sunset investment in a specific acquisition channel.
- When a new channel is being tested and needs signal-based evaluation against established benchmarks.
- When pipeline velocity by channel diverges from historical norms, indicating audience fatigue or competitive pressure.

## Workflow

1. **Pull channel data**: Extract spend, impressions, clicks, form fills, MQLs, SQLs, and pipeline value by channel for the analysis period. Normalize to common timeframes. Deliverable: raw channel performance dataset.
2. **Calculate unit economics**: Compute CPL, cost-per-MQL, cost-per-SQL, and CAC for each channel using the unit economics table in [`assets/channel-signal-report-template.md`](assets/channel-signal-report-template.md). Compare against targets and prior period benchmarks. Deliverable: unit economics comparison table.
3. **Identify signal anomalies**: Flag channels where metrics deviate more than 15% from plan or prior period. Categorize as positive signal (outperformance) or negative signal (degradation). Deliverable: annotated anomaly report.
4. **Diagnose root causes**: For each anomaly, investigate causes from the root cause categories in the report template. Deliverable: root cause analysis per flagged channel.
5. **Recommend reallocation**: Propose specific budget shifts with projected MQL and pipeline impact using the reallocation table in [`assets/channel-signal-report-template.md`](assets/channel-signal-report-template.md). Score the analysis quality against [`references/scoring-rubric.md`](references/scoring-rubric.md) before delivery. Deliverable: channel signal report with reallocation recommendation.

## Anti-Patterns

- **Reacting to daily noise**: Making reallocation decisions based on single-day performance fluctuations. *Why*: daily data is too volatile for budget decisions; meaningful signals require at least one-week sample sizes.
- **Ignoring downstream conversion**: Optimizing for CPL without tracking MQL-to-SQL and SQL-to-close rates by channel. *Why*: cheap leads that never convert waste more budget than expensive leads that close.
- **Attribution tunnel vision**: Relying solely on last-touch attribution when evaluating channel contribution. *Why*: top-of-funnel channels that assist conversions get unfairly penalized, leading to underinvestment in awareness.

## Output

**On success**: Produces a channel signal report containing unit economics by channel, annotated anomalies with root causes, and specific reallocation recommendations with projected pipeline impact. Delivered to VP Marketing and demand gen team.

**On failure**: Report which data sources were unavailable or unreliable, what time period was covered, and recommend specific tracking fixes or data collection changes needed before the next analysis cycle.

## Related Skills

- [`demand-gen-planner`](../../../marketing/vp-marketing/demand-gen-planner/SKILL.md) — Sets the channel targets and budget allocations that this skill monitors and recommends adjusting.
- [`campaign-analytics-reporter`](../../../marketing/marketing-operations-manager/campaign-analytics-reporter/SKILL.md) — Provides the raw campaign performance data that feeds this analysis.
- [`marketing-attribution-modeller`](../../../marketing/marketing-operations-manager/marketing-attribution-modeller/SKILL.md) — Supplies the multi-touch attribution data needed for accurate channel contribution analysis.
