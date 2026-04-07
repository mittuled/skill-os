# AI Risk Assessment Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Product Counsel] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | ai-risk-assessor |

## Executive Summary

[2-3 sentences summarizing the AI feature assessed, the overall risk tier classification, and the primary recommendation (approve/conditional/block).
GUIDANCE: Lead with the risk classification and most critical finding. State the regulatory frameworks that apply.]

## Feature Classification

[Document the AI feature's purpose, input data, model type, output decisions, and affected user populations.

GUIDANCE:
- Good: "The recommendation engine uses collaborative filtering on purchase history to suggest products. It processes 50K daily active users' behavioural data and outputs ranked product lists. Classified as Limited Risk under EU AI Act Annex III."
- Bad: "We use AI to recommend things to users."
- Format: Table with Feature Name, Model Type, Input Data Categories, Output Type, Affected Population, EU AI Act Risk Tier, NIST AI RMF Category]

## Regulatory Applicability Matrix

[Map the feature against applicable AI regulations by jurisdiction.

GUIDANCE:
- Good: Table with columns for Regulation, Jurisdiction, Applicable (Y/N), Specific Requirements, Compliance Status
- Bad: "GDPR and EU AI Act apply"
- Format: Table covering EU AI Act, NIST AI RMF, state-level AI laws (IL AI Video Interview Act, CO AI Act), sector-specific (EEOC, CFPB, FDA)]

## Bias and Fairness Assessment

[Evaluate discriminatory impact across protected classes with quantitative evidence.

GUIDANCE:
- Good: "Model accuracy varies by age group: 18-25 (94.2%), 26-40 (95.1%), 41-60 (91.3%), 60+ (87.4%). The 7.7pp gap for 60+ users exceeds the 5pp threshold and requires mitigation."
- Bad: "We checked for bias and it looks fine."
- Format: Performance metrics table by demographic group, proxy variable analysis, training data composition breakdown]

## Transparency and Explainability Analysis

[Assess user-facing explanation quality and contestability mechanisms.

GUIDANCE:
- Good: "Users see 'Recommended because you purchased X' explanations. SHAP values confirm top-3 features align with displayed reasons in 89% of cases. Appeal mechanism allows users to flag incorrect recommendations."
- Bad: "The model is explainable."
- Format: Explainability method, user explanation design, contestation process, regulatory requirement mapping]

## Risk Mitigation Plan

[Prioritized mitigations for each identified risk.

GUIDANCE:
- Each recommendation should be:
  - Specific (not "reduce bias" but "implement demographic parity constraint in model training pipeline")
  - Actionable (assigned to ML Engineering / Product / Legal)
  - Prioritized (P1: pre-launch blocker, P2: 30-day post-launch, P3: next quarter)
- Format: Table with Risk, Mitigation, Control Type (technical/legal/operational), Owner, Priority, Deadline]

## Monitoring Framework

[Ongoing monitoring requirements for the AI feature.

GUIDANCE:
- Good: "Monthly fairness metric review, quarterly model drift assessment, regulatory change alerts via compliance scanner, annual full re-assessment"
- Bad: "We will monitor the model"
- Format: Table with Metric, Threshold, Frequency, Owner, Escalation Trigger]

## Recommendations

[Prioritized list of recommendations based on findings.
GUIDANCE: Each recommendation should be:
- Specific (not "improve X" but "implement Y to achieve Z")
- Actionable (assignable to a person/team)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[Scoring rubric applied per `references/scoring-rubric.md`. Regulatory frameworks consulted: EU AI Act, NIST AI RMF 1.0, applicable state AI laws. Bias testing methodology: demographic parity, equalized odds, calibration across protected classes.]

### B. Supporting Data

[Model performance metrics by demographic group, training data composition statistics, SHAP/LIME explainability outputs, regulatory applicability research.]
