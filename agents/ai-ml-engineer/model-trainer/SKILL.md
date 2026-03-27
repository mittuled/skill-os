---
name: model-trainer
description: >
  This skill trains ML models using defined datasets, features, and training
  procedures. Use when asked to train a model, run experiments, or tune
  hyperparameters. Also consider when a model needs retraining due to data drift.
  Suggest when the user attempts model training without a reproducible procedure.
department: engineering
agent: ai-ml-engineer
version: 1.0.0
complexity: medium
related-skills:
  - ../model-requirements-definer/SKILL.md
  - ../model-evaluation-runner/SKILL.md
  - ../ml-architecture-designer/SKILL.md
---

# model-trainer

## Agent: AI/ML Engineer

L2 AI/ML engineer (Nx) responsible for feasibility assessment, model requirements, ML architecture design, model training, MLOps pipeline building, evaluation, and performance monitoring.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

Trains ML models using defined datasets, feature pipelines, and training procedures with experiment tracking and reproducibility guarantees.

## When to Use

- When model requirements and architecture are defined and a model needs to be trained.
- When model performance has degraded due to data drift and retraining is required.
- When a new model architecture or algorithm needs experimentation against the current approach.

## Workflow

1. **Training Data Preparation**: Load versioned training data from the feature store or data pipeline. Apply preprocessing (normalization, encoding, imputation) and create train/validation/test splits with stratification. Verify no data leakage across splits. Deliverable: versioned training dataset with split metadata.
2. **Experiment Configuration**: Configure the training experiment: model architecture, hyperparameter search space, optimization algorithm (Adam, SGD, learning rate schedule), regularization strategy, and early stopping criteria. Register the experiment in the tracking system (MLflow, W&B). Deliverable: experiment configuration with tracking run ID.
3. **Training Execution**: Execute model training with checkpointing, gradient monitoring, and resource utilization tracking. For large models, configure distributed training (data parallelism, model parallelism) as specified in the architecture. Deliverable: trained model checkpoint with training logs.
4. **Hyperparameter Tuning**: Run hyperparameter optimization (Bayesian optimization, grid search, or random search) across the defined search space. Track all trials with metrics. Deliverable: hyperparameter tuning results with best configuration.
5. **Artifact Registration**: Register the best model artifact with full lineage: training data version, feature pipeline version, hyperparameters, training metrics, and environment specification (dependency versions, GPU type). Deliverable: registered model artifact with complete lineage metadata.

## Anti-Patterns

- **Training without experiment tracking**: Running training jobs without logging hyperparameters, metrics, and artifacts to a tracking system. *Why*: without tracking, reproducing results is impossible and comparing experiments relies on memory or scattered notes.
- **Overfitting to validation set**: Tuning hyperparameters extensively against the validation set without a held-out test set. *Why*: the validation set effectively becomes a second training set, and the model's true generalization ability is unknown until production.
- **Ignoring training data versioning**: Training on "latest data" without snapshotting the exact dataset version. *Why*: non-versioned data makes it impossible to reproduce a model or diagnose performance changes.

## Output

**On success**: Produces a trained model artifact with experiment tracking records, hyperparameter tuning results, training metrics, and full lineage metadata registered in the model registry. Delivered as a registered model ready for evaluation.

**On failure**: Report which training phase failed (e.g., OOM during training, divergent loss, data loading errors), what was attempted, and recommended fixes (reduce batch size, adjust learning rate, fix data pipeline).

## Related Skills

- [`model-requirements-definer`](../model-requirements-definer/SKILL.md) -- Provides the requirements that guide training targets.
- [`model-evaluation-runner`](../model-evaluation-runner/SKILL.md) -- Evaluates the trained model before production promotion.
- [`ml-architecture-designer`](../ml-architecture-designer/SKILL.md) -- Specifies the training infrastructure and architecture this skill uses.
