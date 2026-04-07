# Product Legal Review Memo

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Product Counsel] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | product-legal-reviewer |

## Executive Summary

[2-3 sentences summarizing the feature reviewed, overall legal risk level, and clearance decision.
GUIDANCE: Lead with the clearance status (cleared/conditional/blocked) and the most significant legal risk.]

## Feature Intake Summary

[Feature understanding documentation.

GUIDANCE:
- Good: "Feature: AI-powered job matching for enterprise HR. Users: enterprise HR managers and job candidates. Data: resumes (PII, potentially sensitive categories), job descriptions, matching scores. Monetization: per-seat SaaS subscription. Geographic reach: US and EU."
- Bad: "New feature for matching"
- Format: Table with Feature Name, Purpose, Target Users, Data Processed, Monetization, Geographic Reach]

## Regulatory Applicability Matrix

[All applicable regulations mapped by jurisdiction.

GUIDANCE:
- Good: Table with Regulation, Jurisdiction, Applicable Section, Requirement, Feature Impact, Compliance Status
- Bad: "GDPR and employment law apply"
- Format: Matrix covering privacy, consumer protection, accessibility, employment, AI regulation, sector-specific rules]

## Legal Risk Assessment

[Compliance gap identification with classification.

GUIDANCE:
- Good: "Gap: AI matching algorithm processes protected class data (age, gender from resumes) without bias testing. Regulation: EEOC guidance on AI in employment, IL AI Video Interview Act, NYC Local Law 144. Classification: Blocking. Likelihood: High. Severity: High."
- Bad: "Some employment law issues"
- Format: Table with Gap ID, Description, Applicable Regulation, Classification (Blocking/Recommended/Advisory), Likelihood, Severity]

## Clearance Decision

[Formal legal clearance with conditions.

GUIDANCE:
- Good: "Clearance: CONDITIONAL. Blocking items: (1) Complete bias audit per NYC LL 144 before NY market launch. (2) Implement GDPR Article 22 human review mechanism for automated decisions. Advisory: Consider WCAG 2.1 AA compliance for candidate-facing interface."
- Bad: "Approved with some items"
- Format: Clearance status, blocking items, recommended items, advisory items, scope and assumptions]

## Recommendations

[Prioritized post-review actions.
GUIDANCE: Each recommendation should be:
- Specific (not "address bias" but "engage third-party auditor to complete NYC LL 144 bias audit before NY market launch in Q3")
- Actionable (assignable to a person/team)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[Scoring rubric applied per `references/scoring-rubric.md`. Regulatory frameworks consulted per jurisdiction. Risk classification criteria: Blocking = must fix pre-launch, Recommended = fix within 90 days, Advisory = best practice.]

### B. Supporting Data

[Feature specification, user flow documentation, data flow diagrams, regulatory research, comparable product legal precedents.]
