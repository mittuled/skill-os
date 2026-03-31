# North Star Metric Review: Monthly Active Users (MAU)

| Field | Value |
|-------|-------|
| Date | 2026-03-31 |
| Analytics Lead | Analytics Lead |
| Metric | Monthly Active Users (MAU) |
| Current Baseline | 12,400 |
| Overall Score | 5.95 / 10 |
| Verdict | WEAK — consider redefining the north star metric |
| Skill | north-star-metric-reviewer-data |

## Metric Definition

Count of unique users who performed at least one action in the product in the last 30 days.

## Criterion Scores

| Criterion | Level | Weighted Score | Weight |
|-----------|-------|---------------|--------|
| Value Reflection (25%) | Weak | 0.75 | 25% |
| Revenue Correlation (20%) | Assumed | 1.00 | 20% |
| Measurability (20%) | Fully Instrumented | 2.00 | 20% |
| Actionability (20%) | Directly Actionable | 2.00 | 20% |
| Leading Indicator (15%) | Mixed | 0.75 | 15% |
| **Total** | | **6.50 / 10** | |

## Weak Criteria (Score ≤ 3)

| Criterion | Problem |
|-----------|---------|
| Value Reflection | "One action in 30 days" does not reflect meaningful value delivery — a user who logs in once and leaves counts the same as a power user |
| Leading Indicator | MAU is partially a lagging indicator — churn is visible in MAU decline weeks after it begins |

## Recommendations

1. **Improve value_reflection**: Redefine the metric to capture meaningful engagement rather than any action. Consider "Weekly Active Users who completed at least one [core value action]" — this better reflects value delivery.
2. **Improve leading_indicator**: Replace or supplement MAU with a metric that detects engagement decline earlier, such as "Users who performed core value action in the last 7 days."

## Suggested Replacement Candidates

| Candidate | Why Better |
|-----------|-----------|
| Weekly Active Deployers (users who ran a deployment in last 7 days) | Ties directly to the product's core value; leading indicator of retention |
| Features Activated per New User in First 7 Days | Captures onboarding health; leads revenue by 30-60 days |

## Next Steps

1. Validate that "Weekly Active Deployers" correlates with 90-day retention — run cohort analysis
2. Verify instrumentation for core value action exists
3. Present replacement proposal to product leadership within 2 weeks
