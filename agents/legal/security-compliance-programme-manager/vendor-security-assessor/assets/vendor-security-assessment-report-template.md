# Vendor Security Assessment Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Security & Compliance Programme Manager] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | vendor-security-assessor |

## Executive Summary

[2-3 sentences summarizing the vendor assessed, risk tier, and security decision.
GUIDANCE: Lead with the approve/conditional/reject decision and the most significant finding.]

## Vendor Risk Tier Classification

[Risk tier determination based on structured criteria.

GUIDANCE:
- Good: "Vendor: Acme Analytics. Data Access: PII (user behaviour data with email addresses). System Access: Read-only API access to production database replica. Business Criticality: Important (product analytics, 30-day replacement timeline). Risk Tier: Tier 2 (Standard)."
- Bad: "High-risk vendor"
- Format: Table with Dimension (Data Access, System Access, Business Criticality), Classification, Rationale, resulting Risk Tier]

## Security Posture Review

[Detailed review of vendor's security practices and certifications.

GUIDANCE:
- Good: "SOC 2 Type II: Valid through 2026-12-31. Scope: Analytics platform (covers our use case). Exceptions: 1 (access review delay in Q2 — remediated). Complementary user entity controls: IP allowlisting required (implemented). Penetration test: Annual, last conducted 2026-01. No critical/high findings open."
- Bad: "Vendor has SOC 2"
- Format: Per-certification review (scope, validity, exceptions) plus questionnaire domain-by-domain analysis]

## Gap Analysis

[Vendor posture compared against organizational security requirements.

GUIDANCE:
- Good: Table with Security Domain, Organizational Requirement, Vendor Status, Gap (Y/N), Gap Description, Risk Level, Compensating Control
- Bad: "A few gaps were found"
- Format: Domain-by-domain comparison covering encryption, access controls, incident response, BCP, data handling, sub-processors]

## Security Decision

[Formal approve/conditional/reject recommendation.

GUIDANCE:
- Good: "Decision: APPROVE WITH CONDITIONS. Conditions: (1) Vendor must implement IP allowlisting for API access within 30 days. (2) Vendor must provide updated penetration test report annually. (3) DPA must be executed before data sharing begins. Rationale: Security posture meets Tier 2 requirements with conditions addressing API access control gap."
- Bad: "Approved"
- Format: Decision, conditions (if any) with deadlines, rationale, contractual requirements]

## Monitoring Plan

[Ongoing vendor security monitoring.

GUIDANCE:
- Good: Table with Monitoring Activity, Frequency, Trigger, Owner. Including: annual reassessment, certification renewal tracking, breach notification monitoring, scope change review.
- Bad: "We will monitor the vendor"
- Format: Monitoring activity table with specific cadence and triggers]

## Recommendations

[Post-assessment actions.
GUIDANCE: Each recommendation should be:
- Specific (not "monitor vendor" but "add Acme Analytics to breach notification monitoring service and configure alert for security advisories")
- Actionable (assignable to security/procurement)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[Scoring rubric applied per `references/scoring-rubric.md`. Assessment performed per vendor tiering criteria. SOC 2 report reviewed per AICPA guidance. Gap analysis against organizational vendor security requirements.]

### B. Supporting Data

[Security questionnaire responses, SOC 2 report summary, ISO 27001 certificate, penetration test executive summary, insurance certificate, sub-processor list.]
