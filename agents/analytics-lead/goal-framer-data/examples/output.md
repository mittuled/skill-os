# Analytics Goals: Onboarding Improvement Initiative — Q2 2026

| Field | Value |
|-------|-------|
| Date | 2026-03-31 |
| Analytics Lead | Analytics Lead |
| Team | Growth |
| Objective | Improve user onboarding to increase activation rate and reduce time-to-first-value |
| Goal Period | Q2 2026 |
| Total Metrics | 2 |
| Skill | goal-framer-data |

## Goal 1: Onboarding Activation Rate

| Field | Value |
|-------|-------|
| Metric | onboarding_activation_rate |
| Type | Conversion Rate |
| Baseline | 34.0% |
| Target | 45.0% |
| Change Required | +32.4% (relative) |
| Timeframe | Quarterly |
| Measurement Frequency | Weekly |

**Key Result**: Improve onboarding_activation_rate from 0.34 to 0.45 (+32.4%) by end of Q2 2026.

**Query approach**:
```sql
SELECT COUNT(activated_users) / COUNT(registered_users)
FROM user_events
WHERE registration_date >= period_start
```

**Success criteria**: onboarding_activation_rate ≥ 0.45 sustained for the final 2 weeks of Q2.

**Failure threshold**: Rate < 0.323 triggers initiative review.

## Goal 2: Median Time to First Value

| Field | Value |
|-------|-------|
| Metric | median_time_to_first_value_days |
| Type | Efficiency |
| Baseline | 8.5 days |
| Target | 5.0 days |
| Change Required | -41.2% (reduction) |
| Timeframe | Monthly |
| Measurement Frequency | Weekly |

**Key Result**: Reduce median_time_to_first_value_days from 8.5 to 5.0 days (-41.2%) by end of monthly period.

**Query approach**:
```sql
SELECT MEDIAN(first_value_date - registration_date)
FROM user_journeys
WHERE cohort_month = period_month
```

**Success criteria**: median_time_to_first_value_days ≤ 5.0 for the measurement month.

**Failure threshold**: Days > 9.0 triggers initiative review.

## Anti-Patterns Checked

- All metrics have numeric baselines — no "improve engagement" without a number
- All targets are achievable from baseline — no moonshot without evidence
- Each metric has a query approach — no unqueryable goals
