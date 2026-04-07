# AI/ML Feasibility Assessment: User Churn Prediction

| Field | Value |
|-------|-------|
| Date | 2026-03-31 |
| Engineer | AI/ML Engineer |
| Problem | User Churn Prediction |
| Task Type | Classification |
| Feasibility Score | 7.35 / 10 |
| Verdict | CONDITIONAL GO — feasible if specified conditions are met |
| Skill | ai-feasibility-assessor |

## Executive Summary

The churn prediction ML project is conditionally feasible. Data volume (50k labelled examples) clears the minimum viable threshold for a binary classifier. The primary risk is label quality — cancellation-log-derived labels may miss silent churners, inflating the apparent training set quality. Addressing this gap and implementing class imbalance handling are pre-conditions for GO.

## Feasibility Scorecard

| Dimension | Level | Weighted Score | Weight |
|-----------|-------|---------------|--------|
| Data Volume | Medium (10k–100k) | 1.75 | 25% |
| Label Quality | Medium (5-15% noise) | 1.20 | 20% |
| Compute Budget | Sufficient | 1.50 | 15% |
| Latency Feasibility | Relaxed (daily batch) | 2.00 | 20% |
| Problem Complexity | ML adds value over heuristics | 1.40 | 20% |
| **Total** | | **7.35 / 10** | |

## Baseline Performance Benchmark

Before training, the team must beat these baselines:

| Baseline | Expected AUC-ROC | Notes |
|----------|-----------------|-------|
| Majority class (predict no churn) | 0.50 | Useless but common mistake |
| Recency-frequency heuristic | 0.68 | Login frequency + days since last action |
| Gradient boosted trees (shallow) | 0.74 | Quick to train, strong on tabular features |

**ML must achieve AUC-ROC > 0.78** to justify the infrastructure investment over the heuristic baseline.

## Risk Register

| Risk | Severity | Mitigation |
|------|----------|------------|
| Silent churners missing from labels | HIGH | Audit cancellation log coverage; supplement with proxy labels (90-day inactivity) |
| Class imbalance (~5% churn rate) | MEDIUM | Use SMOTE oversampling or class-weighted loss; evaluate on F1 not accuracy |
| Distribution shift as product evolves | MEDIUM | Schedule monthly model retraining; monitor feature drift in production |

## Pre-Conditions for GO

1. Audit label coverage: confirm what % of actual churners are captured in the training labels
2. Agree on churn definition with the product team (cancellation vs inactivity vs downgrade)
3. Implement class imbalance strategy before first training run

## Recommended Timeline

| Phase | Duration | Key Deliverable |
|-------|----------|-----------------|
| Data audit and label quality review | 2 weeks | Data readiness report |
| Feature engineering and baseline training | 3 weeks | Baseline model with AUC-ROC benchmark |
| Model development and evaluation | 3 weeks | Candidate model with evaluation report |
| MLOps setup and shadow mode deployment | 2 weeks | Production-ready model pipeline |
| **Total** | **10 weeks** | |
