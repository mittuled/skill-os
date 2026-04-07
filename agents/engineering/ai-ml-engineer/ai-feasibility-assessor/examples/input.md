# Scenario: Evaluating ML Feasibility for Churn Prediction Feature

A product team wants to build an ML-powered churn prediction feature. The engineering team has access to 3 years of user activity logs (approximately 50,000 labelled churn/retain examples), but label quality is uncertain (sourced from cancellation logs with known gaps). Compute budget is moderate. The feature needs to score users once daily — latency is not strict.

## Input Parameters

```json
{
  "problem_name": "User Churn Prediction",
  "task_type": "classification",
  "estimated_timeline_weeks": 10,
  "criteria_ratings": {
    "data_volume": "medium",
    "label_quality": "medium",
    "compute_budget": "sufficient",
    "latency_feasibility": "relaxed",
    "problem_complexity": "ml_adds_value"
  },
  "risks": [
    "Label quality depends on cancellation logs — cancellations may not capture silent churners",
    "Class imbalance expected: ~5% churn rate",
    "Distribution shift possible as product evolves"
  ]
}
```
