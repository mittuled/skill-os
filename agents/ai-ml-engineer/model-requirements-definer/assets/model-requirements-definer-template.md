# Model Requirements Document

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [AI/ML Engineer name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | model-requirements-definer |
| Project | [ML project name] |
| Stakeholders | [Product Lead, ML Lead, Data Lead] |

## Executive Summary

[2-3 sentences summarizing the model's purpose, the primary success metric, and the most important constraint.
GUIDANCE: Lead with the prediction task and business outcome. Example: "This document defines requirements for a churn prediction model that must achieve F1 ≥ 0.82 at inference latency ≤ 150ms p99, replacing the current rule-based system. The primary constraint is fairness: predictions must not vary by more than 5% in true positive rate across customer tenure segments."]

## Business Objective Mapping

[Table translating each business goal into a measurable model metric.

GUIDANCE:
- Good: "Business goal: reduce manual review queue by 40% → Model metric: recall ≥ 0.88 for flagged transactions at precision ≥ 0.70"
- Bad: "The model should be accurate and fast"]

| Business Objective | Owner | Model Metric | Target Value | Measurement Method |
|-------------------|-------|-------------|--------------|-------------------|
| [e.g., Reduce false positives in fraud detection by 30%] | [@product-lead] | [Precision for fraud class] | [≥ 0.85] | [Held-out test set, n=10,000] |
| [e.g., Maintain fraud catch rate] | [@product-lead] | [Recall for fraud class] | [≥ 0.75] | [Same test set] |

## Input/Output Schema

[Complete specification of model inputs and outputs.

GUIDANCE:
- Good: Define every feature with name, type, range/domain, nullability, and freshness requirement
- Bad: "The model takes user features as input"
- Format: Tables for inputs and outputs]

### Input Features

| Feature Name | Data Type | Range / Domain | Nullable? | Max Staleness | Source |
|-------------|-----------|---------------|-----------|--------------|--------|
| [feature_name] | [float / int / string / bool] | [e.g., 0–1 or ["A","B","C"]] | [Yes / No] | [e.g., 1 hour] | [e.g., user_events table] |

### Output Schema

| Field | Type | Description | Range |
|-------|------|-------------|-------|
| [prediction] | [float / int / string] | [e.g., Probability of churn in next 30 days] | [0.0–1.0] |
| [confidence] | [float] | [Model confidence score] | [0.0–1.0] |
| [explanation] | [JSON] | [SHAP feature contributions for top 5 features] | [Optional] |

## Performance Constraints

[Numeric performance requirements for accuracy and serving.

GUIDANCE:
- Good: Specify p50 AND p99 latency, with hard limits
- Bad: "The model should be fast enough for production"]

### Accuracy Requirements

| Metric | Minimum Acceptable | Target | Baseline to Beat |
|--------|-------------------|--------|-----------------|
| [Primary metric, e.g., F1] | [e.g., ≥ 0.80] | [e.g., ≥ 0.85] | [e.g., Rule-based F1 = 0.71] |
| [Secondary metric, e.g., Precision] | [e.g., ≥ 0.82] | [e.g., ≥ 0.88] | |

### Serving Requirements

| Requirement | Target | Hard Limit |
|-------------|--------|-----------|
| Inference latency p50 | [≤ X ms] | [≤ Y ms — fail eval if exceeded] |
| Inference latency p99 | [≤ X ms] | [≤ Y ms — fail eval if exceeded] |
| Throughput | [≥ N predictions/second] | |
| Model size (edge only) | [≤ X MB] | |
| Availability SLA | [e.g., 99.9%] | |

## Fairness and Safety Constraints

[Fairness metrics and safety boundaries.

GUIDANCE:
- Good: Specify which protected attributes apply with regulatory basis, and numeric disparity thresholds
- Bad: "The model should be fair"]

### Protected Attributes

| Attribute | In Scope? | Regulatory Basis | Fairness Metric | Max Disparity |
|-----------|-----------|-----------------|----------------|--------------|
| [e.g., Age] | [Yes / No] | [e.g., ADEA] | [e.g., Equalized odds] | [e.g., ≤ 0.05] |

### Safety Boundaries

| Boundary | Specification |
|----------|--------------|
| Confidence threshold for automated action | [e.g., Predictions with confidence < 0.70 route to human review] |
| Human review rate cap | [e.g., ≤ 15% of decisions require human review] |
| Explainability requirement | [e.g., SHAP feature importance required for all audit decisions] |
| Regulatory explainability | [e.g., Right to explanation per GDPR Article 22 — decision rationale must be retrievable] |

## Recommendations

[Prioritized recommendations for stakeholders or the ML architecture team.

GUIDANCE: Focus on decisions that need stakeholder input, tradeoffs between metrics, and known risks.]

- **P1**: [Critical decision or risk that must be resolved before architecture begins]
- **P2**: [Important tradeoff or clarification needed]
- **P3**: [Nice-to-have enhancement for future iterations]

## Appendices

### A. Methodology

[How requirements were gathered — interviews, existing data analysis, regulatory review, stakeholder workshops.]

### B. Rejected Requirements

[Requirements that were proposed but rejected, with rationale. Prevents future re-litigation of decisions.]

| Proposed Requirement | Reason for Rejection | Alternative Adopted |
|---------------------|---------------------|---------------------|
