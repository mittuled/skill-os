# Framework: Growth Dashboard Design

Defines the AARRR metric hierarchy, dashboard structure, and data quality requirements for growth metrics dashboards.

## AARRR Metric Hierarchy

Structure the dashboard in this order (most strategic at top):

| Stage | Primary KPI | Secondary Metrics | Refresh Cadence |
|-------|------------|-----------------|----------------|
| Acquisition | New signups by channel (daily) | CAC by channel, landing page CVR, organic vs. paid split | Daily |
| Activation | Activation rate (D7 cohort) | Time-to-activation (median), onboarding funnel by step | Daily |
| Retention | Day-1/7/30 retention curves | Retention by cohort, feature-level engagement | Weekly |
| Revenue | MRR, MRR growth rate | ARPU, trial-to-paid conversion, expansion MRR | Weekly |
| Referral | Viral coefficient (k) | Referral volume, invite-to-signup CVR, cycle time | Weekly |

## Summary Scorecard (Top of Dashboard)

The dashboard's first view must show the 5 most important numbers with trend vs. prior period:

| Metric | Comparison Period | Alert Threshold |
|--------|-----------------|----------------|
| Weekly signups | vs. prior week | Alert if >15% drop week-over-week |
| Activation rate (D7) | vs. prior 4-week average | Alert if >3 pp drop |
| D30 retention | vs. prior cohort | Alert if >5 pp drop |
| MRR | vs. prior week | Alert if growth rate turns negative |
| Active experiments | Count | Alert if 0 active (team not experimenting) |

## Retention Curve Requirements

Retention curves are the most misused chart in growth dashboards. Requirements:

1. **Cohort-based, never aggregate**: Show the retention curve for each weekly cohort separately, not an average across all users.
2. **Rolling update**: Every new week, append the latest data point for in-progress cohorts. Do not show incomplete cohorts as if they are finished.
3. **Mark D1, D7, D30, D90**: These are the standard checkpoints for retention analysis.
4. **Benchmark line**: Overlay the product category benchmark (e.g., consumer app D30 ≥ 20%) as a reference line.

## Experiment Results View Requirements

For each active experiment, show:
- Experiment name and hypothesis
- Variant labels and sample sizes (both arms)
- Primary metric: conversion rate per variant with 95% confidence interval
- Days to significance (estimated) or significance achieved (p-value)
- Status: Running / Significant / Inconclusive

**Never**: Show a winner/loser designation before statistical significance is achieved (p < 0.05 at 80% power).

## Data Validation Requirements

Before publishing any metric on the dashboard:
1. Cross-check against the source query — dashboard value must match raw query within 1%
2. Verify date filters are consistent (all metrics use the same timezone and week boundary)
3. Confirm NULLs are handled correctly (NULLs in user_id break cohort counts)
4. Add a "last updated" timestamp to each dashboard section

## Dashboard Documentation Page

Every growth dashboard must have a documentation page (linked from the dashboard) containing:
- Metric definitions (exact SQL or description for each KPI)
- Data freshness SLA (how often each metric updates)
- Known limitations (e.g., "Mobile app data lags by 4 hours due to batch ingestion")
- Escalation contact for data questions
