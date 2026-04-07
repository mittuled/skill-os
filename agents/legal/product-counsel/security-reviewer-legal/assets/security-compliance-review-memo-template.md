# Security Compliance Review Memo

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Product Counsel] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | security-reviewer-legal |

## Executive Summary

[2-3 sentences summarizing the system reviewed, overall compliance posture, and whether security representations are accurate.
GUIDANCE: Lead with the compliance verdict (compliant/non-compliant/partially compliant) and the most significant gap found.]

## Security Requirements Register

[All legal and contractual security requirements mapped to sources.

GUIDANCE:
- Good: Table with Requirement ID, Requirement Description, Legal Source (GDPR Art. 32 / SOC 2 CC6.1 / Customer DPA Section X), Priority (Critical/High/Medium), Implementation Status
- Bad: "Various security requirements apply"
- Format: Numbered register with legal source traceability]

## Architecture Compliance Gap Analysis

[Security architecture assessed against each requirement.

GUIDANCE:
- Good: "REQ-007 (Encryption at rest): GDPR Art. 32, SOC 2 CC6.1. Current: AES-256 for production databases, S3 server-side encryption. Gap: Development environment database unencrypted. Risk: Medium — dev environment contains anonymized data only. Remediation: Enable encryption on dev database."
- Bad: "Encryption is mostly in place"
- Format: Per-requirement assessment with current state, gap description, risk rating, and remediation]

## Contractual Representation Accuracy Report

[Verification of security claims against reality.

GUIDANCE:
- Good: "Customer Contract X, Section 7.2: 'Data encrypted at rest using AES-256.' Verification: TRUE for production. FALSE for development environment (see REQ-007 gap). Marketing page: '24/7 SOC monitoring.' Verification: TRUE — Datadog alerting with PagerDuty escalation."
- Bad: "Representations are accurate"
- Format: Table with Source Document, Claim, Verification Status (True/False/Partially True), Evidence, Gap Reference]

## Remediation Roadmap

[Prioritized gap remediation plan.

GUIDANCE:
- Good: Table with Gap ID, Remediation Action, Priority (based on regulatory exposure and contractual breach risk), Owner, Deadline, Success Criterion
- Bad: "Fix the gaps"
- Format: Roadmap sorted by priority with specific deadlines]

## Recommendations

[Post-review actions.
GUIDANCE: Each recommendation should be:
- Specific (not "improve security" but "enable AES-256 encryption on dev database and update SOC 2 evidence collection")
- Actionable (assignable to security/engineering)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[Scoring rubric applied per `references/scoring-rubric.md`. Requirements sources: GDPR Article 32, SOC 2 Trust Services Criteria, customer DPA security schedules, cyber insurance policy, PCI-DSS (if applicable), HIPAA Security Rule (if applicable).]

### B. Supporting Data

[Architecture diagrams, encryption configuration evidence, access control screenshots, SOC 2 control matrix, customer contract security schedules, penetration test results.]
