# Model Evaluation Report: [Model Name / Version]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | AI/ML Engineer |
| Model | [Model name and version, e.g., revenue-forecast-v2.1] |
| Task Type | [Classification / Regression / Ranking / Generation / Embedding] |
| Framework | [scikit-learn / PyTorch / TensorFlow / Hugging Face] |
| Skill | model-evaluation-runner |
| Evaluation Dataset | [Dataset name, version, and size] |
| Status | [Pass / Fail / Conditional Pass] |

## Executive Summary

[2–3 sentences covering the verdict, primary metric against threshold, and the key finding or concern.
GUIDANCE: Lead with verdict — "Model PASSES evaluation. Revenue forecast MAPE of 4.2% is within the 5% threshold with no evidence of data leakage or temporal drift. Model approved for A/B test deployment against v2.0 baseline."]

**Verdict**: [PASS / FAIL / CONDITIONAL PASS]
**Primary metric**: [MAPE 4.2% vs. 5.0% threshold]
**Baseline comparison**: [Better / Worse / Same vs. current production model]

## Model Summary

| Field | Value |
|-------|-------|
| Model architecture | [Random Forest / XGBoost / BERT / GPT / Custom NN] |
| Input features | [N features — see Appendix A] |
| Output | [Single value / Class probability / Top-k ranking] |
| Training data period | [YYYY-MM-DD to YYYY-MM-DD] |
| Evaluation data period | [YYYY-MM-DD to YYYY-MM-DD] |
| Temporal gap | [X days between training end and evaluation start] |

## Performance Metrics

### Primary Metrics

| Metric | Threshold | Model Score | Baseline (Prod) | Status |
|--------|-----------|-------------|----------------|--------|
| [MAPE / Accuracy / F1 / NDCG] | [≤ 5%] | [4.2%] | [4.8%] | [PASS] |

### Secondary Metrics

| Metric | Value | Notes |
|--------|-------|-------|
| [MAE] | [X] | |
| [RMSE] | [X] | |
| [R² / AUC / Precision@K] | [X] | |
| [Inference latency p50] | [X ms] | |
| [Inference latency p99] | [X ms] | |
| [Model size] | [X MB] | |

### Per-Segment Performance

[Evaluate across key segments to detect bias or performance gaps:]

| Segment | n | Primary Metric | vs. Overall | Notes |
|---------|---|----------------|-------------|-------|
| [Segment A, e.g., new users] | [N] | [X] | [+/-X%] | |
| [Segment B, e.g., high-value] | [N] | [X] | [+/-X%] | |
| [Segment C, e.g., mobile] | [N] | [X] | [+/-X%] | |

**Bias alert threshold**: Flag any segment with > 20% performance gap vs. overall metric.

## Data Quality Checks

| Check | Result | Notes |
|-------|--------|-------|
| Training/test data split is temporally ordered | [Pass/Fail] | [No future data leaked into training] |
| Evaluation set has no overlap with training set | [Pass/Fail] | |
| Missing value rate in evaluation features | [X%] | [Target: < 1% for required features] |
| Feature distribution shift (training vs. eval) | [None / Minor / Major] | [Use PSI or KS test] |
| Label quality check (sample review) | [Pass/Fail] | [N samples manually reviewed] |
| Class balance (classification only) | [Balanced / Imbalanced X:1] | |

### Population Stability Index (PSI) per Feature

| Feature | PSI | Stability |
|---------|-----|----------|
| [Feature 1] | [< 0.1] | Stable |
| [Feature 2] | [0.1–0.2] | Moderate shift |
| [Feature 3] | [> 0.2] | Major shift — investigate |

> PSI thresholds: < 0.1 = stable | 0.1–0.2 = moderate shift | > 0.2 = major shift (retrain recommended)

## Error Analysis

### Worst-Case Predictions

[Sample of highest-error predictions to identify failure modes:]

| Prediction | Actual | Error | Likely Cause |
|-----------|--------|-------|-------------|
| [Predicted value] | [Actual value] | [Absolute or relative error] | [Root cause hypothesis] |

### Error Distribution

| Error Range | Count | % of Eval Set |
|------------|-------|---------------|
| [Within 1%] | [N] | [%] |
| [1–5%] | [N] | [%] |
| [5–10%] | [N] | [%] |
| [> 10%] | [N] | [%] |

## Fairness and Bias Assessment

[Required for any model making decisions affecting people:]

| Protected Attribute | Group A | Group B | Disparity | Threshold | Status |
|--------------------|---------|---------|----------|-----------|--------|
| [e.g., Age group] | [Metric] | [Metric] | [X%] | [< 10%] | [Pass/Fail] |
| [e.g., Geography] | | | | | |

## Deployment Recommendation

**Deployment approval**: [Approved / Approved with conditions / Rejected]

**Conditions** (if applicable):
1. [e.g., "A/B test against production model for 2 weeks before full rollout"]
2. [e.g., "Monitor PSI on feature X weekly; retrain if PSI > 0.2"]

**Monitoring plan**:

| Signal | Alert Threshold | Action |
|--------|----------------|--------|
| Primary metric degradation | > [X%] worse than deployment baseline | Rollback to previous model |
| Feature PSI | > 0.2 on any top-10 feature | Trigger retraining |
| Prediction distribution shift | > [X%] shift in output distribution | Investigate + potential rollback |
| Inference latency p99 | > [X ms] | Scale inference fleet or rollback |

## Appendix A: Feature List

| Feature | Type | Description | Missing Rate |
|---------|------|-------------|-------------|
| [feature_name] | [numeric / categorical / text / embedding] | [What it represents] | [X%] |
