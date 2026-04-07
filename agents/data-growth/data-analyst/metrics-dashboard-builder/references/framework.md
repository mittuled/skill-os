# Framework: Metrics Dashboard Builder

Defines the design principles, layout standards, and chart selection guide for building actionable KPI dashboards.

## Dashboard Types

| Type | Audience | Purpose | Refresh Cadence | Max Visualizations |
|------|---------|---------|----------------|-------------------|
| Executive | C-level, board | Strategic health at a glance | Daily | 6 |
| Product | PM, growth lead | Feature and funnel performance | Daily / hourly | 10 |
| Engineering | Engineering team | System health, error rates, performance | Real-time | 12 |
| Analytics | Data team | Data quality, pipeline health, model validation | Daily | 10 |
| Campaign | Marketing, growth | Acquisition and conversion by campaign | Daily | 8 |

## Layout Principles

1. **Top-of-page = most critical**: The most important metric (north star or primary KPI) occupies the top-left position.
2. **Visual hierarchy**: Scorecards (current value vs. target) → trend lines → breakdowns → supporting detail. Move down the page as importance decreases.
3. **8–12 visualizations per dashboard**: Fewer visualizations force prioritization; more create cognitive overload.
4. **Group by theme, not type**: "Acquisition" section contains all acquisition metrics, not "all bar charts on this row."
5. **Every metric has a definition**: Include a tooltip or annotation explaining the calculation and data source for every metric.

## Chart Selection Guide

| Data Pattern | Recommended Chart | Avoid |
|-------------|------------------|-------|
| Trend over time (single metric) | Line chart with reference lines for targets | Pie chart |
| Comparison across categories | Horizontal bar chart | 3D charts |
| Current value vs. target | Scorecard with progress indicator | Area chart |
| Funnel step conversion | Funnel chart or waterfall | Stacked bar |
| Correlation between two metrics | Scatter plot | Dual-axis line (confusing scale) |
| Distribution of a metric | Histogram or box plot | Line chart |
| Cohort retention | Cohort table (retention grid) | Single-line retention curve |
| Geographic breakdown | Choropleth map | Bar chart (hard to compare regions) |

## Metric Definition Standards

Every metric displayed must have a documented definition covering:

| Field | Example |
|-------|---------|
| Metric name | "7-Day Active Users (WAU7)" |
| Business definition | "Unique users who performed a core action within any 7-day rolling window" |
| Technical definition | `COUNT(DISTINCT user_id) WHERE event = 'core_action' AND event_date >= CURRENT_DATE - 7` |
| Data source | analytics_warehouse.fct_events |
| Refresh cadence | Daily at 06:00 UTC |
| Owner | [name] |

## Comparison Baselines

Every metric on a dashboard must have at least one comparison baseline:

| Baseline Type | When to Use |
|--------------|------------|
| Prior period (WoW, MoM, QoQ) | Standard for all metrics — provides trend context |
| Target / goal line | When the metric has an OKR or quarterly goal |
| Cohort baseline | When comparing new cohort behaviour to historical cohorts |
| Segment benchmark | When the metric is segmented (show overall alongside segment) |

## Query Performance Standards

| Requirement | Standard |
|-------------|---------|
| Dashboard load time | < 5 seconds for all charts |
| Preferred data layer | Query materialized views, not raw event tables |
| Avoid | `SELECT *` or full table scans on event tables; joins across >3 tables in a single chart query |
| Large date ranges | Use pre-aggregated summary tables (daily/weekly grain) |
| Real-time charts | Only for metrics with a decision cadence < 1 hour; otherwise batch |

## Accuracy Validation Checklist

Before publishing any dashboard:
- [ ] All metric values cross-checked against raw SQL query for the same time window
- [ ] All segment filters tested (selecting a segment should change values appropriately)
- [ ] All date range pickers tested (changing range updates all charts)
- [ ] Target/goal lines confirmed against the current OKR document
- [ ] Metric definition tooltips present for all KPIs
