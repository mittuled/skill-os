# Scenario: Defining Requirements for a Content Recommendation Model

The product team wants a content recommendation model to increase feature adoption. The model will rank 20 content items per user. Latency must be under 100ms at p99. Fairness across age groups is required per policy.

## Input Parameters

```json
{
  "model_name": "content-recommender-v1",
  "task_type": "ranking",
  "business_objective": "Increase feature adoption by surfacing relevant content to users during onboarding",
  "input_features": ["user_tenure_days", "plan_tier", "last_active_features", "content_category", "user_cohort"],
  "input_data_types": {"user_tenure_days": "int", "plan_tier": "string", "last_active_features": "list", "content_category": "string", "user_cohort": "string"},
  "required_input_fields": ["user_tenure_days", "plan_tier"],
  "serving_mode": "synchronous",
  "fairness_required": true,
  "protected_attributes": ["age_group", "geographic_region"],
  "retraining_frequency": "weekly",
  "interpretability_required": false,
  "success_criteria": {
    "min_accuracy": 0.45,
    "target_accuracy": 0.60,
    "p50_latency_ms": 30,
    "p99_latency_ms": 100,
    "max_fairness_disparity": 0.05
  }
}
```
