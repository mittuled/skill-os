---
name: campaign-analytics-reporter
description: >
  This skill produces the weekly campaign performance report with spend, leads, and CAC by channel.
  Use when generating the weekly marketing performance report, when leadership requests ad hoc
  campaign analysis, or when a campaign underperforms and needs diagnostic reporting.
  Also consider when a new channel launches and needs baseline reporting.
  Suggest when a campaign has been running for a week without a performance report.
department: marketing
agent: marketing-operations-manager
version: 1.0.0
complexity: medium
related-skills:
  - ../marketing-attribution-modeller/SKILL.md
  - ../../demand-gen-manager/channel-signal-analyst/SKILL.md
---

# campaign-analytics-reporter

## Agent: Marketing Operations Manager

L2 marketing operations manager (1x) responsible for martech stack, lead scoring, campaign analytics, attribution modelling, and email deliverability.

Department ethos: [ideal-marketing.md](../../../departments/marketing/ideal-marketing.md)

## Skill Description

Produces the weekly campaign performance report with spend, leads, MQLs, pipeline contribution, and CAC by channel, enabling data-driven budget and strategy decisions.

## When to Use

- When the weekly reporting cadence requires the standard campaign performance report.
- When leadership requests an ad hoc deep-dive into a specific campaign or channel's performance.
- When a campaign is underperforming targets and needs diagnostic analysis to identify the breakdown point.
- When a new channel or campaign type launches and needs baseline reporting established.

## Workflow

1. **Extract campaign data**: Pull spend, impressions, clicks, form fills, MQLs, SQLs, and pipeline data from ad platforms, CRM, and marketing automation. Reconcile cross-platform discrepancies. Deliverable: unified campaign dataset for the reporting period.
2. **Calculate performance metrics**: Compute CPL, cost-per-MQL, cost-per-SQL, CAC, and ROAS by channel and campaign. Compare against targets, prior period, and benchmarks. Deliverable: metrics table with variance analysis.
3. **Identify trends and outliers**: Flag campaigns or channels with significant positive or negative deviations. Annotate with known context (budget changes, creative refreshes, seasonal factors). Deliverable: annotated trend analysis.
4. **Build the report**: Assemble the performance report with executive summary, channel-by-channel breakdown, trend charts, and recommended actions. Keep the executive summary to one paragraph. Deliverable: formatted weekly campaign report.
5. **Distribute and brief**: Send the report to VP Marketing, demand gen, and channel owners. Brief stakeholders on key findings and recommended actions in the weekly marketing standup. Deliverable: distributed report with briefing notes.

## Anti-Patterns

- **Metric overload**: Filling reports with every available metric instead of focusing on the 5-7 that drive decisions. *Why*: dense reports go unread; decision-makers need signal, not noise.
- **Reporting without recommendations**: Presenting data without interpreting what it means or what actions to take. *Why*: reports that describe without prescribing shift the analysis burden to non-analysts and delay action.
- **Manual data reconciliation**: Spending hours manually reconciling platform data instead of building automated pipelines. *Why*: manual processes introduce errors and make reporting unsustainable at scale.

## Output

**On success**: Produces a weekly campaign performance report with executive summary, channel metrics with variance analysis, trend charts, and action recommendations. Delivered to VP Marketing, demand gen team, and channel owners.

**On failure**: Report which data sources were unavailable or inconsistent, what partial reporting is possible, and recommend data pipeline fixes to prevent recurrence.

## Related Skills

- [`marketing-attribution-modeller`](../marketing-attribution-modeller/SKILL.md) — Supplies the attribution data that determines how pipeline credit is allocated across channels in this report.
- [`channel-signal-analyst`](../../demand-gen-manager/channel-signal-analyst/SKILL.md) — Consumes this report's data to perform deeper channel-level analysis and reallocation recommendations.
- [`demand-gen-planner`](../../vp-marketing/demand-gen-planner/SKILL.md) — Sets the targets that this report measures performance against.
