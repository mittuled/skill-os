---
name: mlops-pipeline-builder
description: >
  This skill builds MLOps pipelines for automated training, evaluation, and
  deployment of models. Use when asked to automate model retraining, set up CI/CD
  for ML, or build model deployment pipelines. Also consider when models are
  retrained and deployed manually. Suggest when the user deploys models without
  automated validation gates.
department: engineering
agent: ai-ml-engineer
version: 1.0.0
complexity: complex
related-skills:
  - ../ml-architecture-designer/SKILL.md
  - ../model-evaluation-runner/SKILL.md
  - ../model-trainer/SKILL.md
  - ../model-performance-monitor/SKILL.md
triggers:
  - "build MLOps pipeline"
  - "MLOps setup"
  - "ML deployment pipeline"
  - "model CI/CD"
  - "MLOps infrastructure"
---

# mlops-pipeline-builder

## Agent: AI/ML Engineer

L2 AI/ML engineer (Nx) responsible for feasibility assessment, model requirements, ML architecture design, model training, MLOps pipeline building, evaluation, and performance monitoring.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Builds MLOps pipelines for automated training, evaluation, validation, and deployment of models with reproducibility and audit trail guarantees.

## When to Use

- When a model moves from manual notebook-based training to production and requires automation.
- When model retraining frequency increases and manual deployment becomes a bottleneck.
- When regulatory or audit requirements mandate reproducible, traceable model deployments.

## Workflow

1. **Pipeline Orchestration Setup**: Select and configure the MLOps orchestrator (Kubeflow Pipelines, Vertex AI Pipelines, Airflow, or Metaflow). Define pipeline DAG structure: data validation, feature computation, training, evaluation, model registration, and deployment. Deliverable: pipeline DAG definition with orchestrator configuration.
2. **Data Validation Stage**: Implement data validation checks (schema validation, statistical distribution checks, data freshness verification) using tools like TensorFlow Data Validation (TFDV) or Great Expectations. Define data quality gates that halt the pipeline on failure. Deliverable: data validation stage with quality gates.
3. **Training Automation**: Automate model training with parameterized hyperparameters, reproducible random seeds, and experiment tracking integration (MLflow, W&B). Implement distributed training support where required. Deliverable: automated training stage with experiment tracking.
4. **Evaluation Gate**: Implement automated model evaluation against held-out test sets, fairness metrics (demographic parity, equalized odds), and regression tests against the current production model. Define promotion criteria (e.g., accuracy must exceed production model by 0.5%). Deliverable: evaluation gate with promotion criteria.
5. **Model Registry Integration**: Register validated models with metadata (training data version, hyperparameters, evaluation metrics, lineage hash) in the model registry (MLflow Model Registry, Vertex AI Model Registry). Deliverable: model registration stage with full metadata.
6. **Deployment Automation**: Implement automated deployment with canary rollout, shadow mode validation, and automated rollback on serving metric degradation. Deliverable: deployment stage with rollback triggers.
7. **Pipeline Monitoring**: Monitor pipeline execution health: stage durations, failure rates, data validation pass rates, and model promotion rates. Deliverable: pipeline health dashboard.

## Anti-Patterns

- **Notebooks in production**: Running Jupyter notebooks as production training jobs instead of parameterized pipeline stages. *Why*: notebooks lack reproducibility guarantees, are difficult to version, and cannot be reliably scheduled or monitored.
- **Skipping evaluation gates**: Deploying retrained models without automated comparison against the production model. *Why*: model regressions go live undetected, degrading user experience before anyone notices.
- **Non-reproducible training**: Training without pinned dependency versions, fixed random seeds, or data versioning. *Why*: non-reproducible training makes debugging model regressions impossible and fails audit requirements.

## Output

**On success**: Produces a fully automated MLOps pipeline comprising data validation, training automation, evaluation gates, model registry integration, deployment automation, and pipeline monitoring. Delivered as pipeline code and orchestrator configuration.

**On failure**: Report which pipeline stage could not be automated (e.g., manual approval required, infrastructure limitations), what partial automation exists, and recommended steps to close gaps.

## Related Skills

- [`ml-architecture-designer`](../ml-architecture-designer/SKILL.md) -- Provides the architecture this pipeline implements.
- [`model-evaluation-runner`](../model-evaluation-runner/SKILL.md) -- Defines the evaluation logic embedded in the pipeline's evaluation gate.
- [`model-trainer`](../model-trainer/SKILL.md) -- Provides the training procedure the pipeline automates.
