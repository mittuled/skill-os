# Scenario: Evaluating Churn Classifier v2 Against Production Model

The newly trained churn classifier v2 needs evaluation before promotion. The requirements specify AUC-ROC ≥ 0.78, max fairness disparity ≤ 0.05, robustness ≥ 0.70, and p99 latency ≤ 200ms. The current production baseline has AUC-ROC of 0.74.

## Input Parameters

```json
{
  "model_name": "churn-classifier-v2",
  "task_type": "classification",
  "metrics": {
    "primary_accuracy": 0.82,
    "baseline_accuracy": 0.74,
    "max_fairness_disparity": 0.03,
    "robustness_score": 0.76,
    "p99_latency_ms": 145
  },
  "requirements": {
    "min_accuracy": 0.78,
    "max_fairness_disparity": 0.05,
    "min_robustness": 0.70,
    "max_p99_latency_ms": 200
  }
}
```
