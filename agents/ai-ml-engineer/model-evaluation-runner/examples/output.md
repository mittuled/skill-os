# Model Evaluation Report: churn-classifier-v2

| Field | Value |
|-------|-------|
| Date | 2026-03-31 |
| Engineer | AI/ML Engineer |
| Model | churn-classifier-v2 |
| Task Type | Classification |
| Overall Score | 8.74 / 10 |
| Verdict | PROMOTE — all requirements met |
| Skill | model-evaluation-runner |

## Executive Summary

churn-classifier-v2 passes all required evaluation dimensions and achieves an overall score of 8.74/10. The model shows a 10.8% improvement in AUC-ROC over the production baseline (0.82 vs 0.74). Fairness disparity is well within threshold at 0.03 (limit 0.05). Latency at p99 is 145ms against a 200ms budget. Recommend promotion to staging with 24-hour shadow testing.

## Dimension Scores

| Dimension | Achieved | Required | Passes | Weighted Score |
|-----------|---------|----------|--------|---------------|
| Accuracy (35%) | AUC-ROC 0.82 | ≥ 0.78 | Yes | 3.28 |
| Fairness (20%) | Max disparity 0.03 | ≤ 0.05 | Yes | 1.70 |
| Robustness (20%) | Score 0.76 | ≥ 0.70 | Yes | 1.52 |
| Latency (15%) | p99 145ms | ≤ 200ms | Yes | 1.24 |
| Baseline Improvement (10%) | +10.8% over baseline | Positive | Yes | 1.00 |
| **Total** | | | | **8.74 / 10** |

## Baseline Comparison

| Metric | v2 (Candidate) | Production Baseline | Improvement |
|--------|---------------|---------------------|-------------|
| AUC-ROC | 0.82 | 0.74 | +10.8% |
| Max Fairness Disparity | 0.03 | Not measured | N/A |
| p99 Latency | 145ms | Not measured | N/A |

## Fairness Assessment

| Protected Attribute | Demographic Parity Gap | Equalized Odds Gap | Status |
|--------------------|----------------------|---------------------|--------|
| Age group | 0.02 | 0.03 | Pass |
| Geographic region | 0.01 | 0.02 | Pass |
| Plan tier | 0.03 | 0.02 | Pass |

**Maximum disparity: 0.03 (threshold: 0.05)** — Well within acceptable range.

## Hard Fails

None — all dimensions pass.

## Promotion Recommendation

1. Promote to staging environment
2. Run 24-hour shadow traffic (compare prediction distributions against production model)
3. If shadow results are consistent, proceed with canary rollout: 5% → 25% → 100% over 48 hours
4. Monitor AUC-ROC and p99 latency on live traffic; rollback if either degrades > 3%
