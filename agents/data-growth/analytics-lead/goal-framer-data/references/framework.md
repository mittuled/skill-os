# Framework: Goal Framer Data

Defines the structure for translating product and business objectives into measurable analytics goals using OKR-aligned metric hierarchies.

## Goal Hierarchy

```
Company Objective
  └── Product OKR (Key Result with numeric target)
        └── Analytics Goal (metric + baseline + target + measurement plan)
              └── Leading Indicators (early signals)
              └── Lagging Indicators (outcome confirmation)
```

## Metric Definition Standard

Every analytics goal must specify all six elements:

| Element | Description | Example |
|---------|-------------|---------|
| **Metric name** | Plain-language label | "7-day feature activation rate" |
| **Formula** | Exact numerator / denominator | Users who completed `feature_used` ≥ 1 within 7 days of signup / users who signed up in the cohort window |
| **Time window** | Measurement period and cohort definition | Rolling 30-day cohort; measured at Day 7 after signup |
| **Data source** | Table, query, or dashboard reference | `events.user_actions` WHERE event_type = 'feature_used' |
| **Baseline** | Current measured value (not estimated) | 24% (trailing 30 days, as of [date]) |
| **Target** | Threshold with stretch and minimum | Minimum: 28%; Target: 35%; Stretch: 42% |

## Leading vs. Lagging Indicator Pairing

For every analytics goal, pair a lagging outcome metric with a leading signal:

| Goal Type | Lagging (outcome) | Leading (early signal) |
|-----------|------------------|------------------------|
| Activation | 7-day activation rate | Day-1 onboarding completion rate |
| Retention | Day-30 retention | Day-7 feature engagement rate |
| Conversion | Trial-to-paid rate | Trial users reaching 3 core actions |
| Revenue | MRR growth | Expansion revenue from upgrades |
| Engagement | DAU/MAU ratio | Weekly session count per user |

## Target-Setting Methods

Choose the method appropriate to data availability:

| Method | When to Use | Calculation |
|--------|------------|-------------|
| **Historical trend extrapolation** | 6+ months of baseline data | Apply recent growth rate to the planning window |
| **Benchmark comparison** | Industry benchmarks available | Set target at median for growth stage / category |
| **Model-based forecast** | Cohort or regression model exists | Use model output ± confidence interval |
| **Negotiated commitment** | New metric with no history | Set minimum = current estimated value + 10%; stretch = + 30% |

Always provide **three scenario targets**: minimum acceptable, primary target, and stretch.

## Goal Framework Table Format

The output goal framework document must include one row per metric:

| Objective | Metric | Formula | Baseline | Min Target | Primary Target | Stretch Target | Data Source | Dashboard | Owner | Review Cadence |
|-----------|--------|---------|---------|-----------|---------------|---------------|------------|-----------|-------|---------------|

## Anti-Patterns: Common Definition Errors

| Ambiguous Definition | Corrected Definition |
|----------------------|---------------------|
| "Active users" | "Users who triggered ≥ 1 core action event (`checkout_started`, `report_viewed`, or `export_completed`) within a rolling 7-day window" |
| "Engagement" | "Average session count per user per week among users active in the trailing 30 days" |
| "Conversion rate" | "Trial users who upgraded to a paid plan within 30 days of trial start, divided by all trial starts in the same cohort window" |
| "Retention" | "Percentage of users first seen in Week 0 who returned and triggered ≥ 1 session in Week 4 (Day 22–28)" |

## Goal Conflict Resolution

When two teams define the same metric differently:
1. Identify each team's formula in writing.
2. Compute both versions against the same dataset — quantify the divergence.
3. Propose the canonical definition using the more complete formula.
4. Update all dashboards and lock the definition for the planning period.
5. Document the resolution decision and the date it was locked.
