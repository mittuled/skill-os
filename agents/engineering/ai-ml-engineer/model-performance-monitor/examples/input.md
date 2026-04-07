# Scenario: Weekly Health Check on Production Churn Classifier

The churn prediction model has been running in production for 6 weeks. This week's monitoring run detects elevated feature PSI and a small accuracy drop. The ML engineer runs the health check to determine if action is needed.

## Input Parameters

```json
{
  "model_name": "churn-classifier-v2",
  "monitoring_window": "2026-03-24 to 2026-03-31",
  "current_metrics": {
    "accuracy": 0.78,
    "feature_psi": 0.15,
    "p99_latency_ms": 162
  },
  "baseline_metrics": {
    "accuracy": 0.82,
    "feature_psi": 0.02,
    "p99_latency_ms": 145
  }
}
```
