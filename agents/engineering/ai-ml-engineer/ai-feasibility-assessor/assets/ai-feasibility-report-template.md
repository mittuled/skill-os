# AI Feasibility Assessment: [Use Case Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | AI/ML Engineer |
| Use Case | [Use case name] |
| Requester | [Team / Product Manager] |
| Skill | ai-feasibility-assessor |
| Status | [Draft / Final] |
| Recommendation | [Proceed / Proceed with conditions / Do not proceed] |

## Executive Summary

[3–4 sentences: the use case, the recommendation, the primary reason for the recommendation, and the single biggest risk or gap.
GUIDANCE: Lead with the recommendation — "AI FEASIBLE with conditions. Churn prediction meets data volume requirements and has a clear measurable outcome, but labeled training data covers only 12 months, limiting the model's ability to capture seasonal patterns. Recommend proceeding with a 6-month data enrichment sprint before model training begins."]

**Recommendation**: [Proceed / Proceed with conditions / Do not proceed]
**Confidence in recommendation**: [High / Medium / Low]

## Use Case Description

**Problem statement**: [What business problem is AI being asked to solve?]
**Proposed AI approach**: [Classification / Regression / Ranking / NLP / Generative / Computer Vision / Other]
**Success metric**: [Single, measurable metric that defines success, e.g., "Reduce customer churn rate from 8% to 6% within 6 months of deployment"]
**User of the AI output**: [Who acts on the model's prediction? How?]

## Feasibility Assessment

### Dimension 1: Problem Suitability for AI

| Question | Assessment | Score (1–5) |
|----------|-----------|------------|
| Is the problem well-defined with a clear outcome? | [Assessment] | [1–5] |
| Has this problem type been solved with AI before (proven use case)? | [Assessment] | [1–5] |
| Is the success metric measurable and attributable? | [Assessment] | [1–5] |
| Is the decision frequency high enough to justify AI automation? | [Assessment] | [1–5] |
| Could a simpler rule-based system solve 80% of the problem? | [Assessment] | [1–5] |

**Dimension score**: [X/25] — [Strong / Moderate / Weak suitability]

### Dimension 2: Data Availability and Quality

| Question | Assessment | Score (1–5) |
|----------|-----------|------------|
| Volume: Do we have enough labeled examples (≥ 10K for supervised, ≥ 1M for deep learning)? | [Assessment] | [1–5] |
| Label quality: Are labels accurate and consistently applied? | [Assessment] | [1–5] |
| Feature coverage: Are the predictive signals available as features? | [Assessment] | [1–5] |
| Data freshness: Is historical data representative of current behavior? | [Assessment] | [1–5] |
| PII and compliance: Can we legally use this data for training? | [Assessment] | [1–5] |

**Dimension score**: [X/25] — [Strong / Moderate / Weak data readiness]

**Data inventory**:

| Data Source | Records Available | Date Range | Label Quality | Access Status |
|------------|-----------------|-----------|--------------|--------------|
| [Source name] | [N records] | [YYYY–YYYY] | [High/Med/Low] | [Available / Requires approval] |

### Dimension 3: Technical Feasibility

| Question | Assessment | Score (1–5) |
|----------|-----------|------------|
| Does the team have ML expertise for this task type? | [Assessment] | [1–5] |
| Can the model meet latency requirements ([X ms])? | [Assessment] | [1–5] |
| Is a baseline model achievable within the proposed timeline? | [Assessment] | [1–5] |
| Do infrastructure capabilities support training and serving? | [Assessment] | [1–5] |
| Is model output explainable to the degree required (regulatory/UX)? | [Assessment] | [1–5] |

**Dimension score**: [X/25] — [Strong / Moderate / Weak technical readiness]

### Dimension 4: Business and Ethical Viability

| Question | Assessment | Score (1–5) |
|----------|-----------|------------|
| Does the business case justify the investment? | [Assessment] | [1–5] |
| Is the ROI measurable within 12 months? | [Assessment] | [1–5] |
| Are there fairness/bias risks that could harm users or the business? | [Assessment] | [1–5] |
| Is there a human-in-the-loop fallback for high-stakes decisions? | [Assessment] | [1–5] |
| Is the regulatory landscape clear for this use of AI? | [Assessment] | [1–5] |

**Dimension score**: [X/25] — [Strong / Moderate / Weak viability]

## Overall Feasibility Score

| Dimension | Score | Max | Weight | Weighted Score |
|-----------|-------|-----|--------|----------------|
| Problem suitability | [X] | 25 | 25% | [X] |
| Data availability | [X] | 25 | 35% | [X] |
| Technical feasibility | [X] | 25 | 25% | [X] |
| Business viability | [X] | 25 | 15% | [X] |
| **Total** | | | **100%** | **[X/25]** |

| Score | Recommendation |
|-------|---------------|
| 18–25 | Proceed — strong feasibility |
| 12–17 | Proceed with conditions — address gaps first |
| 7–11 | Do not proceed yet — significant gaps |
| < 7 | Do not proceed — use case not suitable for AI |

## Conditions and Prerequisites

[Required before proceeding:]

| # | Condition | Owner | Effort | Due |
|---|-----------|-------|--------|-----|
| 1 | [e.g., Collect 12 additional months of labeled training data] | [Data team] | [2 sprints] | [Date] |
| 2 | [e.g., Confirm PII handling approved by legal] | [Legal] | [1 week] | [Date] |

## Recommended Approach

**Proposed algorithm class**: [Gradient boosted trees / Transformer / Logistic regression / etc.]
**Recommended baseline**: [Simple heuristic or rule-based model as comparison point]
**Suggested initial experiment**: [1–2 sentence description of a low-risk first ML experiment]
**Timeline estimate**: [X weeks to first evaluation; Y weeks to production]

## Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| [Insufficient data quality] | [H/M/L] | [H/M/L] | [Data audit sprint] |
| [Model bias affecting protected groups] | | | [Fairness evaluation before deploy] |
| [Concept drift over time] | | | [Scheduled retraining + monitoring] |
