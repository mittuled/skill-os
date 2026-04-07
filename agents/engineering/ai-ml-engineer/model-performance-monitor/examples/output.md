# Model Health Report: churn-classifier-v2

| Field | Value |
|-------|-------|
| Date | 2026-03-31 |
| Engineer | AI/ML Engineer |
| Model | churn-classifier-v2 |
| Monitoring Window | 2026-03-24 to 2026-03-31 |
| Overall Health | DEGRADED — review within 24 hours |
| Skill | model-performance-monitor |

## Health Summary

| Dimension | Current | Baseline | Change | Status |
|-----------|---------|----------|--------|--------|
| Accuracy | 0.78 | 0.82 | -4.9% | WARNING |
| Feature PSI | 0.15 | 0.02 | +0.13 | WARNING |
| p99 Latency | 162ms | 145ms | +11.7% | OK |

## Alerts

| Severity | Dimension | Message |
|----------|-----------|---------|
| WARNING | Accuracy | Accuracy dropped 4.9% — monitor closely |
| WARNING | Feature Drift | Feature PSI 0.150 — moderate drift detected, schedule model review |

## Root Cause Analysis

The accuracy drop (4.9%) correlates with the elevated feature PSI (0.15), suggesting that the input data distribution has shifted since the model was trained. This is consistent with recent product changes or seasonal patterns in user behaviour. Feature PSI of 0.15 is above the warning threshold (0.1) but below critical (0.2).

## Recommended Actions

| Priority | Action | Timeline |
|----------|--------|----------|
| 1 | Identify which features are driving the PSI increase (review per-feature PSI breakdown) | Within 24 hours |
| 2 | Schedule model retraining if PSI continues to increase next week | Within 1 week |
| 3 | Review recent product changes that may have altered feature distributions | This week |
| 4 | If accuracy drops below 0.75 before next weekly check, trigger emergency retraining | Threshold-based |

## Monitoring Thresholds Reference

| Dimension | Warning | Critical |
|-----------|---------|---------|
| Accuracy drop | > 3% | > 7% |
| Feature PSI | > 0.10 | > 0.20 |
| Latency increase | > 20% | > 50% |

## Next Monitoring Run

Scheduled: 2026-04-07. If PSI exceeds 0.20 before then, emergency retraining pipeline will be triggered automatically.
