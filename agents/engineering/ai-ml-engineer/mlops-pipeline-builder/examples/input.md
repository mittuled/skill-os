# Scenario: Building MLOps Pipeline for Weekly Churn Model Retraining

The churn prediction model needs automated weekly retraining triggered on a schedule. The pipeline must include evaluation and staging gates before any production promotion. The team wants drift monitoring enabled.

## Input Parameters

```json
{
  "pipeline_name": "churn-prediction-weekly-retrain",
  "model_name": "churn-classifier-v2",
  "trigger_type": "schedule",
  "schedule": "0 2 * * 0",
  "stages_enabled": ["data_validation", "feature_engineering", "model_training", "model_evaluation", "model_registration", "staging_deployment", "production_promotion"],
  "drift_monitoring": true,
  "performance_metrics": ["auc_roc", "f1_score", "p99_latency_ms"]
}
```
