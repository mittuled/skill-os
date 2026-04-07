# Framework: Revenue Impact Monitoring

## Core Model

Revenue impact monitoring attributes changes in revenue metrics to specific product releases, using pre/post cohort analysis and controlled comparisons to distinguish feature effect from baseline trends and external factors.

## Revenue Metrics Hierarchy

| Tier | Metric | Definition | Measurement Window |
|------|--------|-----------|-------------------|
| Primary | MRR change | Net change in monthly recurring revenue for affected cohort | 30, 60, 90 days post-launch |
| Primary | Upgrade rate | % of eligible users who upgraded to a higher plan | 30 days post-launch |
| Secondary | Feature-to-revenue conversion | % of feature activators who convert to paid or upgrade | 30 days post-activation |
| Secondary | Expansion ARR | ARR added via upsell/cross-sell attributable to the feature | Quarterly |
| Guardrail | Churn rate | % of monthly churns for cohort exposed to the change | 30, 60 days post-launch |
| Guardrail | Downgrade rate | % of users who downgraded after feature activation | 30 days post-launch |

## Attribution Methodology

Use difference-in-differences (DiD) where possible:

1. **Treatment group**: Users who received the feature change
2. **Control group**: Comparable users who did not (holdout cohort, matched by plan tier + usage intensity + tenure)
3. **Pre-period**: 30 days before launch
4. **Post-period**: 30 days after launch
5. **Impact estimate**: (Post-treatment revenue change) − (Post-control revenue change)

When a control group is not available, use a trend-adjusted pre/post comparison (compare actual post-launch revenue to the trendline extrapolated from pre-launch data).

## Confounding Factor Checklist

Before attributing revenue change to the feature, rule out:
- [ ] Seasonal trend (compare to same period prior year)
- [ ] Concurrent marketing campaign (check campaign calendar)
- [ ] Pricing change in the same window (check pricing log)
- [ ] Sales team activity spike (check CRM pipeline)
- [ ] Platform incident (check incident log for the period)

Any unruled confounding factor must be noted as a caveat in the report.

## Statistical Significance Threshold

- Report results as **confirmed** only at p < 0.05 (95% confidence)
- Report results as **directional** at p < 0.10 (90% confidence)
- Report results as **inconclusive** if p >= 0.10 or sample size < 100 per group
- Never headline an "inconclusive" result as positive — report what the data supports

## Reporting Cadence

| Phase | Cadence | Audience | Purpose |
|-------|---------|---------|---------|
| Day 7 | Quick pulse | PM only | Early signal; flag anomalies |
| Day 30 | Full report | PM + Finance + Leadership | Primary attribution window |
| Day 90 | Follow-up | Finance + Leadership | Sustained impact confirmation |
