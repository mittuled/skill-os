# MLOps Pipeline: churn-prediction-weekly-retrain

| Field | Value |
|-------|-------|
| Date | 2026-03-31 |
| Engineer | AI/ML Engineer |
| Pipeline | churn-prediction-weekly-retrain |
| Model | churn-classifier-v2 |
| Trigger | Schedule: Every Sunday at 02:00 UTC |
| Skill | mlops-pipeline-builder |

## Executive Summary

A fully automated weekly retraining pipeline for the churn classifier with all 4 required gates configured. No warnings — the pipeline is safe for production use. Every stage is gated: models that fail evaluation are rejected before registration; production promotion requires explicit approval.

## Pipeline Stages

| Stage | Type | Gate | Requires Approval |
|-------|------|------|------------------|
| data_validation | Processing | No | No |
| feature_engineering | Processing | No | No |
| model_training | Processing | No | No |
| model_evaluation | Validation | Yes | Yes |
| model_registration | Artifact | Yes | Yes |
| staging_deployment | Deployment | Yes | Yes |
| production_promotion | Deployment | Yes | Yes |

## Gate Specifications

### model_evaluation gate
- Must pass AUC-ROC ≥ baseline, F1 ≥ baseline, p99 latency ≤ requirement
- Compares candidate against current production model
- Automatic reject if primary metric drops > 5%

### staging_deployment gate
- Deploy to staging environment; run shadow traffic for 24 hours
- Compare prediction distributions between staging and production model
- Human approval required before proceeding

### production_promotion gate
- Canary rollout: 5% → 25% → 100% traffic over 48 hours
- Automatic rollback if error rate or latency exceeds thresholds
- Requires ML engineer sign-off at each traffic increment

## Monitoring Configuration

| Dimension | Configuration |
|-----------|---------------|
| Drift detection | PSI on input features, weekly, threshold 0.2 |
| Drift action | Alert only (manual trigger for retraining on detection) |
| Metrics tracked | auc_roc, f1_score, p99_latency_ms |
| Performance alert | 5% drop in primary metric triggers PagerDuty |

## Reproducibility Guarantees

| Guarantee | Implementation |
|-----------|----------------|
| Data versioning | All training datasets versioned with SHA hash |
| Code versioning | Git commit SHA pinned to every pipeline run |
| Artefact storage | Model artefacts stored in versioned S3/GCS with immutable keys |
| Experiment tracking | MLflow run ID linked to every model registry entry |

## Warnings

None — all required gates are configured.
