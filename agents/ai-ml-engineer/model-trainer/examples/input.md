# Scenario: Training a Churn Classifier with Hyperparameter Search

The churn prediction model is ready for its first full training run after data preparation. The team will use gradient boosted trees with 5-fold cross-validation and a Bayesian hyperparameter search across 20 trials.

## Input Parameters

```json
{
  "experiment_name": "churn-classifier-v2-training",
  "model_family": "gradient_boosted_trees",
  "dataset_version": "v3-2026-03-31",
  "target_column": "churned_within_90_days",
  "feature_columns": ["tenure_days", "weekly_active_days", "feature_adoption_score", "plan_tier_encoded", "support_ticket_count"],
  "train_split": 0.70,
  "validation_split": 0.15,
  "run_hyperparameter_search": true,
  "n_trials": 20,
  "cross_validation": true,
  "cv_folds": 5,
  "random_seed": 42,
  "metrics_to_log": ["auc_roc", "f1_score", "train_loss", "val_loss"],
  "early_stopping_patience": 15,
  "max_training_time_minutes": 90,
  "framework_versions": {"xgboost": "2.0.3", "scikit-learn": "1.4.0", "python": "3.11.8"}
}
```
