---
name: metrics-dashboard-growth
description: >
  This skill builds growth metrics dashboards covering acquisition, activation, retention, and revenue. Use when asked to create a growth dashboard, visualize AARRR metrics, or build an experiment results view. Also consider when growth metrics exist only in ad-hoc queries. Suggest when the growth team reviews metrics via spreadsheet instead of a live dashboard.
department: data-growth
agent: growth-engineer
version: 1.0.0
complexity: medium
related-skills:
  - metrics-dashboard-builder
  - growth-model-designer
  - funnel-analyser-growth
  - statistical-significance-tracker
triggers:
  - "build growth metrics dashboard"
  - "create growth KPI dashboard"
  - "growth dashboard setup"
  - "visualize growth metrics"
  - "growth reporting dashboard"
---

# metrics-dashboard-growth

## Agent: Growth Engineer

L2 growth engineer (Nx) responsible for growth instrumentation, metrics dashboards, funnel analysis, and growth loop activation.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The growth dashboard builder designs and implements dashboards that visualize the full AARRR funnel — acquisition volume and CAC by channel, activation rate by cohort, retention curves, revenue per user, and referral loop throughput — enabling the growth team to monitor performance and make experiment decisions from a single view.

## When to Use

- When the growth model is finalized and its metrics need a monitoring dashboard.
- When the growth team reviews metrics via ad-hoc queries or spreadsheets instead of a live view.
- When a new experiment launches and the team needs a results dashboard showing variant performance.
- When existing growth dashboards do not cover a new channel, loop, or funnel stage.

## Workflow

1. **Define dashboard scope**: Determine which AARRR stages, channels, experiments, and loops the dashboard must cover. Identify the primary audience (growth lead, growth engineer, leadership).
2. **Design layout**: Structure the dashboard in AARRR order — acquisition at the top, referral at the bottom. Include a summary scorecard with the 5 most important growth numbers.
3. **Build acquisition views**: Visualize daily signups by channel, CAC by channel, and channel-level conversion rates. Include UTM-based attribution breakdowns.
4. **Build activation and retention views**: Show activation rate by cohort, retention curves (Day 1/7/30/90), and time-to-activation distribution.
5. **Build experiment views**: Display active experiment status — variant sample sizes, conversion rates, confidence intervals, and days to significance. Link to the significance tracker.
6. **Build loop views**: Show loop throughput metrics — viral coefficient, referral conversion rate, cycle time, and loop-generated users as a percentage of total acquisition.
7. **Validate and publish**: Cross-check dashboard numbers against raw queries. Publish with access permissions and a documentation page explaining each metric.

## Anti-Patterns

- **Growth dashboard without experiment views**: Omitting experiment results from the growth dashboard forces the team to check a separate tool, reducing experiment visibility. *Why*: experiments are the primary mechanism of growth improvement; they should be front-and-centre on the growth dashboard.
- **No channel-level breakdown**: Showing aggregate acquisition without per-channel data prevents CAC optimization. *Why*: aggregate CAC hides that one channel may be 5x more expensive than another.
- **Stale retention curves**: Displaying retention curves that do not update with each new cohort gives the team outdated information. *Why*: retention changes with product updates and user mix; stale curves mask recent improvements or regressions.

## Output

**Success:**
- A growth dashboard with AARRR views, channel-level acquisition metrics, cohort retention curves, active experiment results, loop throughput metrics, and a documentation page.

**Failure:**
- Dashboard metrics do not match raw query results. Report the discrepancy, root cause, and corrective action.

## Related Skills

- [`metrics-dashboard-builder`](../../../data-growth/data-analyst/metrics-dashboard-builder/SKILL.md) -- the data analyst's dashboard builder covers product KPIs; this skill focuses on growth-specific AARRR metrics.
- [`growth-model-designer`](../../../data-growth/growth-lead/growth-model-designer/SKILL.md) -- the growth model defines the metrics this dashboard visualizes.
- [`funnel-analyser-growth`](../funnel-analyser-growth/SKILL.md) -- funnel analysis results are displayed on the growth dashboard.
- [`statistical-significance-tracker`](../../../data-growth/analytics-lead/statistical-significance-tracker/SKILL.md) -- experiment significance data feeds the experiment views on this dashboard.
