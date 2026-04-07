# Security Findings Legal Review Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Product Counsel] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | security-auditor-legal |

## Executive Summary

[2-3 sentences summarizing the security findings reviewed, whether breach notification is triggered, and immediate actions required.
GUIDANCE: Lead with the disclosure determination (notification required/not required) and the earliest deadline. State the scope of exposure.]

## Classified Findings Register

[Security findings classified for legal assessment.

GUIDANCE:
- Good: Table with Finding ID, Description, Data Type Affected (PII/PHI/Financial), Records Exposed (count/estimate), Duration of Exposure, Actual vs. Potential Access, Legal Risk Rating (Critical/High/Medium/Low)
- Bad: "Several vulnerabilities were found"
- Format: Classified register with legal risk rating per finding]

## Disclosure Obligation Matrix

[Notification requirements mapped per finding per jurisdiction.

GUIDANCE:
- Good: Table with Finding ID, Statute, Jurisdiction, Trigger Met (Y/N), Deadline, Required Content, Recipient, Encryption Safe Harbor Applicable
- Bad: "We may need to notify regulators"
- Format: Matrix covering GDPR Art. 33/34, state breach statutes, HIPAA, contractual DPAs, SEC materiality]

## Notification Package

[Draft notifications for required disclosures.

GUIDANCE:
- Good: Separate notification drafts for: supervisory authority (GDPR Art. 33), affected individuals (GDPR Art. 34 / state statutes), contractual counterparties (DPA notification clauses). Each with required statutory content.
- Bad: "We will send a notification"
- Format: Per-recipient notification draft with statutory content mapping, timing, and distribution plan]

## Privilege-Protected Remediation Memo

[ATTORNEY-CLIENT PRIVILEGED documentation of remediation.

GUIDANCE:
- Good: "Remediation actions documented under privilege: root cause analysis, remediation steps, evidence preservation. Privilege markers on all internal communications. Outside counsel [firm] engaged for litigation assessment."
- Bad: Detailed technical findings in an unprotected document
- Format: Privileged memo with root cause, remediation actions, litigation risk assessment, evidence preservation]

## Recommendations

[Immediate and follow-up actions.
GUIDANCE: Each recommendation should be:
- Specific (not "notify regulators" but "file GDPR Art. 33 notification with Irish DPC within 72 hours of discovery, using draft at Appendix C")
- Actionable (assignable to a person/team)
- Prioritized (P1: immediate / P2: within 1 week / P3: within 30 days)]

## Appendices

### A. Methodology

[Scoring rubric applied per `references/scoring-rubric.md`. Breach definitions analysed per GDPR, per-state statutes (50-state survey), HIPAA, contractual terms. Encryption safe harbor analysis per state statute.]

### B. Supporting Data

[Security audit report, vulnerability scan results, access logs, encryption status verification, DPA notification clause extracts, state breach notification statute summaries.]
