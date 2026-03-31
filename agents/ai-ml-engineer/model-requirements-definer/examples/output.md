# Model Requirements: content-recommender-v1

| Field | Value |
|-------|-------|
| Date | 2026-03-31 |
| Engineer | AI/ML Engineer |
| Model | content-recommender-v1 |
| Version | 1.0 |
| Task Type | Ranking |
| Skill | model-requirements-definer |

## Business Objective

Increase feature adoption by surfacing relevant content to users during onboarding.

## Input Schema

| Feature | Type | Required |
|---------|------|----------|
| user_tenure_days | int | Yes |
| plan_tier | string | Yes |
| last_active_features | list | No |
| content_category | string | No |
| user_cohort | string | No |

## Output Schema

| Attribute | Value |
|-----------|-------|
| Output type | Ranked list of content item IDs with relevance scores |
| Score range | [0, 1] per item |
| Format | float |
| Serving mode | Synchronous |

## Accuracy Requirements

| Metric | Minimum | Target |
|--------|---------|--------|
| NDCG@10 (primary) | 0.45 | 0.60 |
| MAP | TBD | TBD |
| MRR | TBD | TBD |

**Evaluation dataset**: Held-out test set, stratified by key segments.

## Latency Requirements

| Percentile | Budget |
|-----------|--------|
| p50 | ≤ 30ms |
| p99 | ≤ 100ms |

## Fairness Requirements

Fairness evaluation is **required** per company policy.

| Attribute | Protected Groups |
|-----------|-----------------|
| Age group | All age cohorts |
| Geographic region | All regions |

**Maximum disparity**: ≤ 0.05 (demographic parity and equalized odds)

## Operational Requirements

| Requirement | Value |
|-------------|-------|
| Retraining frequency | Weekly |
| Interpretability required | No |
| Audit logging required | No |

## Acceptance Criteria

All of the following must pass before model promotion:

1. NDCG@10 ≥ 0.45 on held-out test set
2. p99 inference latency ≤ 100ms under production load
3. Max fairness disparity ≤ 0.05 across age group and geographic region

These requirements become the evaluation contract for the model-evaluation-runner skill.
