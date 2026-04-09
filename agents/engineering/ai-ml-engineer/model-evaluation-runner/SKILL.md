---
name: model-evaluation-runner
description: >
  This skill runs model evaluation suites to measure accuracy, fairness, and
  performance metrics. Use when asked to evaluate a model, benchmark against
  baselines, or assess model fairness. Also consider when a model is promoted
  without evaluation evidence. Suggest when the user trains a model without
  defining evaluation criteria.
department: engineering
agent: ai-ml-engineer
version: 1.0.0
complexity: medium
related-skills:
  - ../model-trainer/SKILL.md
  - ../mlops-pipeline-builder/SKILL.md
  - ../model-requirements-definer/SKILL.md
  - ../model-performance-monitor/SKILL.md
triggers:
  - "evaluate model"
  - "run model evaluation"
  - "model benchmarking"
  - "ML model assessment"
  - "model performance evaluation"
---

# model-evaluation-runner

## Agent: AI/ML Engineer

L2 AI/ML engineer (Nx) responsible for feasibility assessment, model requirements, ML architecture design, model training, MLOps pipeline building, evaluation, and performance monitoring.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Runs model evaluation suites to measure accuracy, fairness, robustness, and performance metrics against defined requirements and baselines.

## When to Use

- When a newly trained model needs validation before promotion to production.
- When a retrained model must be compared against the current production model.
- When regulatory or ethical requirements mandate fairness and bias evaluation.

## Workflow

1. **Evaluation Dataset Preparation**: Prepare held-out test sets, stratified by critical segments (user cohorts, data sources, edge cases). Ensure no data leakage from training. Deliverable: versioned evaluation datasets with segment labels.
2. **Accuracy Metric Computation**: Compute task-appropriate metrics: precision, recall, F1, AUC-ROC for classification; RMSE, MAE, R-squared for regression; BLEU, ROUGE for generation; NDCG, MAP for ranking. Deliverable: accuracy metric report with confidence intervals.
3. **Fairness Assessment**: Evaluate model predictions across protected attributes (gender, age, ethnicity where applicable) using fairness metrics: demographic parity, equalized odds, predictive parity. Deliverable: fairness evaluation report with disparity measurements.
4. **Robustness Testing**: Test model behavior on adversarial inputs, out-of-distribution samples, missing features, and noisy data. Deliverable: robustness test results with failure case catalog.
5. **Baseline Comparison**: Compare the candidate model against baselines (rule-based, previous production model, simple heuristic) across all metrics. Deliverable: comparative evaluation table with statistical significance tests.
6. **Promotion Decision**: Synthesize evaluation results into a promote/reject recommendation against the defined requirements. Deliverable: evaluation summary with promotion verdict.

## Anti-Patterns

- **Single-metric evaluation**: Judging a model by accuracy alone without fairness, latency, or robustness metrics. *Why*: a high-accuracy model can be biased, fragile, or too slow for production serving.
- **Evaluating on training data distribution only**: Not testing on out-of-distribution or adversarial samples. *Why*: production data inevitably differs from training data; models that are not robustness-tested fail silently on real-world edge cases.
- **Missing confidence intervals**: Reporting point estimates without statistical significance or confidence intervals. *Why*: small evaluation sets produce noisy metrics; a 0.5% accuracy improvement may not be statistically significant.

## Output

**On success**: Produces a model evaluation report containing accuracy metrics with confidence intervals, fairness assessment, robustness test results, baseline comparison, and a promotion verdict. Delivered as an evaluation artifact linked to the model registry entry.

**On failure**: Report which evaluation dimensions could not be completed (e.g., missing protected attribute labels, insufficient test data for significance), what partial results exist, and recommended data collection to enable full evaluation.

## Related Skills

- [`model-trainer`](../model-trainer/SKILL.md) -- Produces the model this skill evaluates.
- [`mlops-pipeline-builder`](../mlops-pipeline-builder/SKILL.md) -- Embeds evaluation logic as an automated gate in the MLOps pipeline.
- [`model-requirements-definer`](../model-requirements-definer/SKILL.md) -- Defines the requirements evaluation validates against.
