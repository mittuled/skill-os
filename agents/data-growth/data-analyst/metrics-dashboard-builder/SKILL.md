---
name: metrics-dashboard-builder
description: >
  This skill builds metrics dashboards that surface product and business KPIs. Use when asked to create a dashboard, visualize metrics, or set up a reporting view. Also consider when a new metric is defined without a visualization. Suggest when stakeholders rely on ad-hoc queries for recurring questions.
department: data-growth
agent: data-analyst
version: 1.0.0
complexity: medium
related-skills:
triggers:
  - "analytics dashboard"
  - "dashboard-builder"
  - "build dashboard"
  - "metrics dashboard"
---

# metrics-dashboard-builder

## Agent: Data Analyst

L2 data analyst (Nx) responsible for data modelling, instrumentation implementation, metrics dashboards, funnel analysis, and signal synthesis.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The metrics dashboard builder designs and implements dashboards that visualize product and business KPIs, enabling stakeholders to monitor health, detect regressions, and make data-informed decisions without writing SQL for recurring questions.

## When to Use

- When a new product initiative defines success metrics that need ongoing monitoring.
- When stakeholders request recurring metrics that are currently answered by ad-hoc SQL queries.
- When a quarterly goal framework is finalized and each metric needs a tracking visualization.
- When an existing dashboard is outdated, slow, or no longer reflects current KPIs.

## Workflow

1. **Gather requirements**: Identify the audience (executive, PM, engineering), the metrics to display, the required dimensions (time, cohort, segment), and the refresh cadence.
2. **Design layout**: Sketch the dashboard layout prioritizing the most critical metrics at the top. Group related metrics. Limit to 8-12 visualizations per dashboard to prevent cognitive overload.
3. **Write queries**: Build the SQL queries or BI tool calculations for each metric. Reference materialized views from the data model where available for performance.
4. **Select chart types**: Choose the appropriate visualization for each metric — time series for trends, bar charts for comparisons, scorecards for current values, funnels for conversion flows.
5. **Add context**: Include comparison baselines (prior period, target line), date filters, segment selectors, and metric definitions as tooltips or annotations.
6. **Validate accuracy**: Cross-check dashboard values against raw SQL queries for the same period. Confirm numbers match within acceptable rounding tolerance.
7. **Publish and document**: Deploy the dashboard, set access permissions, and write a one-page guide explaining each metric's definition, data source, and refresh cadence.

## Anti-Patterns

- **Dashboard sprawl**: Creating a new dashboard for every request instead of extending existing ones fragments metrics across dozens of views. *Why*: stakeholders stop checking dashboards when they can't find the one they need.
- **No metric definitions**: Displaying numbers without explaining the calculation leads to conflicting interpretations. *Why*: "active users" means different things to different teams; the dashboard must disambiguate.
- **Real-time when batch suffices**: Building real-time dashboards for metrics reviewed weekly wastes engineering resources on unnecessary pipeline complexity. *Why*: the refresh cadence should match the decision cadence, not the technical capability.

## Output

**Success:**
- A published dashboard with 8-12 visualizations covering the requested KPIs, comparison baselines, segment filters, and a documentation page with metric definitions and data sources.

**Failure:**
- Dashboard values do not match raw query results. Report the discrepancy, the affected metrics, the root cause (stale cache, wrong join, missing filter), and the correction applied.

## Related Skills

- [`data-model-designer-data`](../data-model-designer-data/SKILL.md) -- dashboards query the data model; schema changes may break dashboard queries.
- [`goal-framer-data`](../../../data-growth/analytics-lead/goal-framer-data/SKILL.md) -- the goal framework defines the metrics the dashboard must surface.
- [`alerting-configurator-data`](../../../data-growth/analytics-lead/alerting-configurator-data/SKILL.md) -- every dashboard metric should have corresponding alert coverage.
- [`metrics-dashboard-growth`](../../../data-growth/growth-engineer/metrics-dashboard-growth/SKILL.md) -- the growth dashboard focuses on acquisition/activation; this skill covers product and business KPIs broadly.
