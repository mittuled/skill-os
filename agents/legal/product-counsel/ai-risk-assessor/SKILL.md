---
name: ai-risk-assessor
description: >
  This skill assesses legal and regulatory risks of AI features and models. Use when
  asked to evaluate AI compliance, assess algorithmic bias risk, or review AI features
  for regulatory exposure. Also consider when the product introduces automated
  decision-making affecting users. Suggest when the user is launching an AI feature
  without a legal risk review.
department: legal
agent: product-counsel
version: 1.0.0
complexity: complex
related-skills:
  - ../privacy-impact-assessor/SKILL.md
  - ../product-legal-reviewer/SKILL.md
---

# ai-risk-assessor

## Agent: Product Counsel

L2 product counsel (1x) responsible for legal review of business models, positioning, pricing, product compliance, and security audit oversight.

Department ethos: [ideal-legal.md](../../../../departments/legal/ideal-legal.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Assesses the legal and regulatory risks of AI-powered features by evaluating compliance with emerging AI regulations, identifying bias and fairness exposure, and recommending mitigations before launch.

## When to Use

- When the product introduces a new AI or machine learning feature that makes predictions, recommendations, or automated decisions affecting users.
- When regulatory developments (EU AI Act, state-level AI laws, sector-specific AI guidance) require re-assessment of existing AI features.
- When an AI feature processes sensitive data categories (health, finance, employment) where algorithmic decision-making carries heightened legal scrutiny.

## Workflow

1. **Feature Scoping**: Document the AI feature's purpose, input data, model type, output decisions, and affected user populations. Classify the feature's risk tier under applicable frameworks (EU AI Act Annex III risk categories, NIST AI RMF). Deliverable: AI feature risk classification document.
2. **Regulatory Mapping**: Map the feature against applicable AI regulations by jurisdiction — EU AI Act, NIST AI RMF, state-level AI laws (Illinois AI Video Interview Act, Colorado AI Act, NYC Local Law 144), and sector-specific guidance (EEOC, CFPB, FDA). Deliverable: regulatory applicability matrix.
3. **Bias and Fairness Assessment**: Evaluate the feature for discriminatory impact across protected classes. Review training data composition, model performance across demographic groups, and calculate fairness metrics (demographic parity, equalized odds, calibration). Identify proxy discrimination risks. Deliverable: bias and fairness risk assessment.
4. **Transparency and Explainability Review**: Assess whether the feature meets transparency requirements using appropriate explainability methods (SHAP, LIME). Verify users can understand decisions, contest them, and that the model is sufficiently explainable for the regulatory context. Deliverable: transparency gap analysis.
5. **Mitigation Recommendations**: For each risk, recommend mitigations spanning technical controls (bias testing pipelines, human-in-the-loop), legal controls (disclosures, consent, appeal processes), and operational controls (monitoring, audit trails). Deliverable: risk mitigation plan with implementation priorities.
6. **Scoring and Reporting**: Apply scoring rubric at `references/scoring-rubric.md` to evaluate assessment completeness. Produce report using template at `assets/ai-risk-assessment-report-template.md`. Deliverable: scored AI risk assessment report.
7. **Ongoing Monitoring Framework**: Define ongoing monitoring: model drift detection, fairness metric tracking, regulatory change alerts, and re-assessment triggers. Deliverable: AI risk monitoring plan.

## Anti-Patterns

- **One-time assessment**: Assessing AI risk only at launch without ongoing monitoring for model drift, data distribution changes, or regulatory updates. *Why*: AI systems change over time; a model that was fair at launch can become discriminatory as data distributions shift.
- **Regulation-only focus**: Evaluating only explicit regulatory requirements while ignoring ethical risks and reputational exposure. *Why*: AI regulations lag AI capabilities; a feature can be technically legal but create significant reputational and user trust damage.
- **Treating all AI equally**: Applying the same risk assessment to a content recommendation system and an automated lending decision. *Why*: risk is proportional to impact; risk-tiered assessment allocates review effort where it matters most.
- **Ignoring training data provenance**: Assessing the model output without reviewing how training data was collected, labelled, and consented. *Why*: biased or non-consensually collected training data creates legal liability regardless of model performance metrics.

## Output

**On success**: Produces an AI risk assessment containing risk classification, regulatory matrix, bias assessment, transparency analysis, mitigation plan, and monitoring framework. Delivered before feature launch with periodic re-assessments.

**On failure**: Report which risk dimensions could not be assessed (e.g., training data documentation unavailable, model not explainable), what partial assessment was completed, and what must be resolved before launch can proceed.

## Related Skills

- [`privacy-impact-assessor`](../privacy-impact-assessor/SKILL.md) -- AI features often process personal data requiring coordinated privacy and AI risk assessment.
- [`product-legal-reviewer`](../product-legal-reviewer/SKILL.md) -- AI risk assessment is a specialized input to the broader product legal review.
