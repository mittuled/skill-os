# Training Run Plan: churn-classifier-v2-training

| Field | Value |
|-------|-------|
| Date | 2026-03-31 |
| Engineer | AI/ML Engineer |
| Experiment | churn-classifier-v2-training |
| Model Family | Gradient Boosted Trees |
| Dataset Version | v3-2026-03-31 |
| Skill | model-trainer |

## Dataset Configuration

| Split | Proportion | Purpose |
|-------|-----------|---------|
| Training | 70% | Model fitting |
| Validation | 15% | Hyperparameter selection |
| Test | 15% | Final held-out evaluation |

**Features**: tenure_days, weekly_active_days, feature_adoption_score, plan_tier_encoded, support_ticket_count
**Target**: churned_within_90_days

## Hyperparameter Configuration

**Default configuration** (before search):

| Hyperparameter | Default Value |
|---------------|---------------|
| n_estimators | 500 |
| max_depth | 6 |
| learning_rate | 0.05 |
| subsample | 0.8 |

**Hyperparameter search**: Bayesian optimisation, 20 trials

| Hyperparameter | Search Space |
|---------------|-------------|
| n_estimators | [200, 500, 1000] |
| max_depth | [4, 6, 8] |
| learning_rate | [0.01, 0.05, 0.1] |

## Cross-Validation

- **Strategy**: 5-fold stratified cross-validation
- **Stratification**: By target column (churned_within_90_days) to preserve class ratio

## Experiment Tracking

**Backend**: MLflow

**Metrics logged per run**: auc_roc, f1_score, train_loss, val_loss

**Artefacts logged**: model_weights, feature_importance, confusion_matrix, hyperparameter_config

## Stopping Criteria

| Criterion | Value |
|-----------|-------|
| Early stopping patience | 15 rounds without improvement |
| Max training time | 90 minutes |

## Reproducibility

| Guarantee | Value |
|-----------|-------|
| Random seed | 42 |
| Data hash | sha256:v3-2026-03-31 |
| XGBoost version | 2.0.3 |
| scikit-learn version | 1.4.0 |
| Python version | 3.11.8 |

## Post-Training Actions

1. Register best model in MLflow Registry with `staging` tag
2. Run model-evaluation-runner against held-out test set
3. If evaluation passes all requirements, submit for model-performance-monitor baseline capture
4. Link this MLflow run ID to the model registry entry for full audit trail
