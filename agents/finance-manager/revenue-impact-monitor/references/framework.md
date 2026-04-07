# Framework: revenue-impact-monitor

Defines the methodology for monitoring and attributing revenue impact of product, pricing, and operational changes.

## Attribution Methodology Selection

Choose the appropriate method based on the initiative type and available data:

| Method | When to Use | Strengths | Limitations |
|--------|------------|-----------|-------------|
| Before/After Comparison | Single rollout with no concurrent changes | Simple; requires little data | Cannot isolate concurrent effects |
| Cohort Analysis | New customer acquisition; changes affecting onboarding | Controls for customer vintage | Requires time to accumulate cohort data |
| A/B Test (Holdout) | Pricing tests; feature rollouts with control group | Strongest causal attribution | Requires engineering to implement hold-out group |
| Segment Comparison | Changes affecting only one customer segment | Controls for external factors | Assumes unchanged segments are valid controls |
| Regression-Based | Multiple concurrent changes; mature data environment | Handles confounders statistically | Requires statistical expertise; data-intensive |

## Baseline Establishment Protocol

Before any change ships, capture:

1. **Trailing 3-month average**: MRR, ARR, ARPU, expansion rate, contraction rate, churn rate
2. **Expected impact range**: Point estimate and ±20% range from the financial model
3. **Confounders to monitor**: Seasonality factors, concurrent product changes, market events
4. **Measurement window**: Define the post-change observation period (e.g., 90 days for pricing; 30 days for feature)
5. **Attribution boundary**: Define what counts as change-attributed vs. organic movement

## Metric Decomposition Framework

Decompose total revenue movement into components:

```
Total MRR Change = New MRR + Expansion MRR − Contraction MRR − Churned MRR
                   ↑              ↑                   ↑                ↑
              New bookings  Upsells/usage        Downgrades         Cancellations
```

For each component, separate:
- **Change-attributed**: Movement directly traceable to the initiative (e.g., cohorts exposed to new pricing)
- **Organic**: Movement in unexposed cohorts or channels unaffected by the change

## Measurement Cadence

| Time Horizon | Frequency | Focus |
|-------------|-----------|-------|
| Week 1–4 | Weekly | Adoption rate; early signal; anomaly detection |
| Month 2–3 | Monthly | Revenue impact quantification; cohort behavior |
| Month 4+ | Quarterly | Durability assessment; annualized ARR impact |

## Variance Investigation Triggers

Investigate when actual impact deviates from expected by:
- **More than 10%** on any individual metric for two consecutive measurement periods
- **More than 20%** in total ARR impact vs. the expected range (outside ±20% band)
- **Sign reversal**: Expected positive impact but actuals show negative movement

Investigation steps:
1. Decompose the variance by metric component (new vs. expansion vs. contraction vs. churn)
2. Check for timing effects (recognition lag, billing cycle misalignment)
3. Check for confounders (concurrent changes, external market events)
4. Interview sales, CS, and product teams for qualitative signal
5. Classify as: timing effect / structural effect / measurement error / external factor

## Intervention Decision Framework

| Impact vs. Expected | Action |
|--------------------|--------|
| > 20% above expected, sustained | Scale the initiative; increase investment |
| Within 20% of expected | Continue monitoring; no immediate action |
| 10–20% below expected | Investigate; iterate on the initiative design |
| > 20% below expected | Pause; root cause analysis; consider rollback |
| Negative impact confirmed | Escalate to leadership; rollback decision required |
