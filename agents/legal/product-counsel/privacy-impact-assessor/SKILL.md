---
name: privacy-impact-assessor
description: >
  This skill conducts privacy impact assessments for new features and data processing
  activities. Use when asked to evaluate privacy risk, conduct a PIA or DPIA, or
  assess a feature's data collection practices. Also consider when the product
  introduces new data collection or changes processing purposes. Suggest when the
  user is launching a feature that collects personal data without a privacy review.
department: legal
agent: product-counsel
version: 1.0.0
complexity: complex
related-skills:
  - ../data-processing-agreement-negotiator/SKILL.md
  - ../ai-risk-assessor/SKILL.md
---

# privacy-impact-assessor

## Agent: Product Counsel

L2 product counsel (1x) responsible for legal review of business models, positioning, pricing, product compliance, and security audit oversight.

Department ethos: [ideal-legal.md](../../../../departments/legal/ideal-legal.md)

## Skill Description

Conducts privacy impact assessments for new features and data processing activities by mapping data flows, evaluating necessity and proportionality, identifying privacy risks, and recommending mitigations to ensure regulatory compliance and user trust.

## When to Use

- When a new feature collects, processes, or shares personal data in ways not covered by existing privacy assessments.
- When GDPR Article 35 triggers are met (large-scale profiling, systematic monitoring, sensitive data processing) requiring a mandatory DPIA.
- When the company enters a new market or jurisdiction with different privacy requirements than currently addressed.

## Workflow

1. **Data Flow Mapping**: Map the complete data lifecycle: collection points, processing activities, storage locations with retention periods, all third-party recipients, and deletion mechanisms. Link to Records of Processing Activities (ROPA) per GDPR Article 30. Deliverable: data flow diagram with processing inventory.
2. **Legal Basis Assessment**: Determine legal basis per processing activity per GDPR Article 6. For consent-based processing, verify GDPR requirements (freely given, specific, informed, unambiguous). For legitimate interest, document the balancing test. Assess CCPA sale/sharing opt-out. Deliverable: legal basis analysis per activity.
3. **Necessity and Proportionality**: Evaluate each data element's necessity for the stated purpose. Systematically evaluate less privacy-invasive alternatives. Apply data minimization, pseudonymization, and anonymization where possible. Deliverable: necessity and proportionality analysis.
4. **Risk Identification**: Identify risks across all dimensions: unauthorized access, function creep, re-identification, cross-border transfer, data subject rights compliance, and processor chain risks. Rate per ISO 29134 privacy risk framework. Deliverable: privacy risk register.
5. **Mitigation Design**: For each risk, design mitigations spanning technical (encryption, pseudonymization, k-anonymity, access controls), organizational (policies, training, DPO oversight), and legal measures (consent mechanisms, privacy notices, DPAs). Assign owners and timelines. Deliverable: mitigation plan.
6. **Scoring and Reporting**: Apply scoring rubric at `references/scoring-rubric.md`. Produce report using template at `assets/privacy-impact-assessment-report-template.md`. Deliverable: scored PIA report.
7. **DPO/Authority Consultation**: Consult with DPO. For high-risk processing per GDPR Article 35, consider prior consultation with the supervisory authority (Article 36). Document outcome and conditions. Deliverable: consultation record.

## Anti-Patterns

- **Retroactive PIA**: Conducting the privacy assessment after the feature has launched rather than during design. *Why*: privacy by design requires assessment before implementation; retroactive changes are more expensive and may require user notification or consent re-collection.
- **Checklist-only assessment**: Completing a privacy checklist without analysing actual data flows and risks. *Why*: checklists miss context-specific risks; a PIA must reflect the actual processing, not generic categories.
- **No follow-up**: Completing the PIA without tracking whether recommended mitigations are implemented. *Why*: an unimplemented PIA provides documentation but no actual privacy protection; regulators evaluate outcomes, not paperwork.
- **Ignoring data subject rights**: Assessing data collection without evaluating whether the system can fulfill access, deletion, portability, and correction requests. *Why*: data subject rights are not optional; systems that cannot fulfill requests create regulatory liability.

## Output

**On success**: Produces a privacy impact assessment containing data flow maps, legal basis analysis, necessity evaluation, risk register, mitigation plan, and consultation records. Delivered before feature launch with periodic re-assessments.

**On failure**: Report which processing activities could not be assessed (unclear data flows, undetermined legal basis), what risks are known but unmitigated, and what must be resolved before launch. Escalate to the DPO.

## Related Skills

- [`data-processing-agreement-negotiator`](../data-processing-agreement-negotiator/SKILL.md) -- PIAs identify processing activities that require DPAs with vendors.
- [`ai-risk-assessor`](../ai-risk-assessor/SKILL.md) -- AI features often require coordinated privacy and AI risk assessment.
