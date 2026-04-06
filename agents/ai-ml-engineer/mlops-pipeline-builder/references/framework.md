# Framework: MLOps Pipeline Architecture

Defines the structural framework for building MLOps pipelines aligned with the MLOps Maturity Model, CRISP-DM phases, and production ML lifecycle requirements.

## MLOps Maturity Levels

| Level | Description | Pipeline Automation |
|-------|-------------|---------------------|
| 0 — Manual | Notebook-based training, manual deployment | None |
| 1 — ML Pipeline | Automated training and evaluation; manual deployment trigger | Training + Evaluation |
| 2 — Full MLOps | Automated training, evaluation, deployment, and monitoring with CI/CD | End-to-end |

This framework targets Level 2 MLOps maturity.

## Pipeline Stage Architecture

### Stage 1: Data Validation

**Purpose**: Prevent training on schema-invalid or statistically anomalous data.

| Check Type | Implementation | Gate Action on Failure |
|------------|---------------|----------------------|
| Schema validation | TFDV or Great Expectations schema spec | Halt pipeline, alert data engineering |
| Statistical drift | KS test or PSI against baseline statistics | Halt if PSI > 0.2 (large drift) |
| Data freshness | Assert max_age of latest record ≤ SLA window | Halt if stale beyond SLA |
| Null rate check | Assert null rate ≤ threshold per critical feature | Halt if exceeds threshold |
| Row count check | Assert row count within expected range ± 20% | Halt if outside range |

### Stage 2: Training Automation

**Purpose**: Reproducible, tracked model training from versioned data.

| Requirement | Implementation |
|-------------|---------------|
| Versioned data | Data registered in feature store or DVC-tracked snapshot |
| Experiment tracking | MLflow or W&B run with hyperparameters, metrics, artifacts |
| Reproducible seeds | Fixed random seeds in training code; logged as hyperparameter |
| Dependency pinning | requirements.txt or conda env locked to exact versions |
| Distributed training | Horovod, PyTorch DDP, or Vertex AI distributed training |

**MLflow Experiment Schema** (minimum required fields):

```
mlflow.log_param("model_type", ...)
mlflow.log_param("learning_rate", ...)
mlflow.log_param("batch_size", ...)
mlflow.log_param("training_data_version", ...)
mlflow.log_metric("val_f1", ...)
mlflow.log_metric("val_auc_roc", ...)
mlflow.log_artifact("model_artifact")
```

### Stage 3: Evaluation Gate

**Purpose**: Automated promotion decision based on defined criteria.

| Metric Type | Required Metrics | Promotion Threshold Example |
|-------------|-----------------|----------------------------|
| Accuracy | F1, AUC-ROC, Precision/Recall | Candidate F1 ≥ production F1 - 0.01 (no regression) |
| Fairness | Demographic parity difference, equalized odds | Disparity ≤ 0.05 across protected groups |
| Robustness | OOD performance, adversarial accuracy | OOD accuracy ≥ 0.80 × in-distribution accuracy |
| Latency | p50 and p99 inference time | p99 ≤ latency budget from model requirements |

Gate outcome: `PROMOTE | REJECT | FLAG_FOR_REVIEW`

### Stage 4: Model Registry

**Purpose**: Traceable artifact management with full lineage.

**Required Registry Metadata**:

| Field | Value Format |
|-------|-------------|
| `model_name` | `<service>-<task>-v<semver>` |
| `training_data_version` | Dataset hash or versioned URI |
| `feature_pipeline_version` | Feature store snapshot ID |
| `hyperparameters` | JSON blob from MLflow run |
| `evaluation_metrics` | JSON blob with all gate metrics |
| `training_environment` | Docker image SHA + GPU type |
| `lineage_hash` | SHA256 of training data + code + config |
| `stage` | `Staging` → `Production` on promotion |

### Stage 5: Deployment Automation

**Purpose**: Safe, observable model rollout with automated rollback.

| Deployment Pattern | Use Case | Rollback Trigger |
|-------------------|----------|-----------------|
| Canary (5% → 25% → 100%) | Standard production rollout | Serving error rate > 1% or latency p99 > SLA |
| Shadow mode | High-stakes use cases (fraud, medical) | Never auto-promotes; requires human review |
| Blue-green | Batch prediction replacement | Old version retained for 24h post-switch |

### Stage 6: Pipeline Monitoring

| Metric | Threshold | Alert Severity |
|--------|-----------|---------------|
| Pipeline run duration | > 2× historical average | Warning |
| Data validation pass rate | < 95% over 7 days | Critical |
| Model promotion rate | < 50% over 30 days (models failing evaluation) | Warning |
| Stage failure rate | > 10% in any 24h window | Critical |

## CRISP-DM Alignment

| CRISP-DM Phase | MLOps Pipeline Stage |
|---------------|---------------------|
| Business Understanding | Model requirements (pre-pipeline) |
| Data Understanding | Data validation stage |
| Data Preparation | Feature computation (pre-pipeline) |
| Modeling | Training automation stage |
| Evaluation | Evaluation gate |
| Deployment | Model registry + deployment automation |
| (Monitoring) | Pipeline monitoring + model monitoring |
