# Scenario: Framing Q2 Analytics Goals for Onboarding Improvement Initiative

The product team wants to improve onboarding in Q2. The analytics lead needs to translate the objective into measurable goals with baselines, targets, and query approaches.

## Input Parameters

```json
{
  "objective": "Improve user onboarding to increase activation rate and reduce time-to-first-value",
  "goal_period": "Q2 2026",
  "team": "Growth",
  "metrics": [
    {
      "name": "onboarding_activation_rate",
      "metric_type": "conversion_rate",
      "baseline": 0.34,
      "target": 0.45,
      "timeframe": "quarterly",
      "measurement_frequency": "weekly",
      "query_approach": "SELECT COUNT(activated_users) / COUNT(registered_users) FROM user_events WHERE registration_date >= period_start"
    },
    {
      "name": "median_time_to_first_value_days",
      "metric_type": "efficiency",
      "baseline": 8.5,
      "target": 5.0,
      "timeframe": "monthly",
      "measurement_frequency": "weekly",
      "query_approach": "SELECT MEDIAN(first_value_date - registration_date) FROM user_journeys WHERE cohort_month = period_month"
    }
  ]
}
```
