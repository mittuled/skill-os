# Data Processing Agreement

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Product Counsel] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | data-processing-agreement-negotiator |

## Executive Summary

[2-3 sentences summarizing the parties, processing relationship, and key terms.
GUIDANCE: State the controller/processor designation, data categories, and any non-standard terms negotiated.]

## Processing Scope Document

[Define the personal data processing activities covered by this DPA.

GUIDANCE:
- Good: Table with Processing Activity, Data Categories, Data Subjects, Purpose, Legal Basis, Retention Period
- Bad: "Vendor processes our data"
- Format: Structured table per GDPR Article 28(3) requirements]

## Security Schedule

[Technical and organisational security measures required.

GUIDANCE:
- Good: "Encryption: AES-256 at rest, TLS 1.2+ in transit. Access control: RBAC with quarterly access reviews, MFA for all administrative access. Logging: all data access logged with 12-month retention. Incident response: 24/7 SOC with 4-hour initial response SLA."
- Bad: "Vendor will implement appropriate security"
- Format: Table with Security Domain, Requirement, Vendor Certification/Evidence, Compliance Status]

## Sub-Processor Terms

[Sub-processor management provisions.

GUIDANCE:
- Good: "General authorisation with 30-day advance notification of new sub-processors. Company may object within 15 days. Current sub-processor list attached as Annex. Flow-down of all DPA obligations to sub-processors."
- Bad: "Vendor may use sub-processors"
- Format: Authorisation type, notification mechanism, objection process, current sub-processor list, flow-down requirements]

## Cross-Border Transfer Documentation

[International data transfer mechanisms.

GUIDANCE:
- Good: "Data transferred to US. Mechanism: EU Commission SCCs (Module 2: Controller to Processor). Transfer Impact Assessment completed [date]. Supplementary measures: encryption in transit and at rest, access limited to authorised personnel in destination country."
- Bad: "Data may be transferred internationally"
- Format: Table with Transfer, Origin, Destination, Mechanism, TIA Date, Supplementary Measures]

## Deviation Log

[Non-standard terms negotiated and risk acceptance rationale.

GUIDANCE:
- Good: "Deviation 1: Breach notification extended from 24 to 48 hours at vendor request. Risk acceptance: 48-hour vendor notification still allows 72-hour GDPR reporting. Approved by [name]."
- Bad: "Some terms were changed"
- Format: Table with Deviation, Standard Term, Negotiated Term, Risk Assessment, Approver]

## Recommendations

[Post-execution actions and monitoring requirements.
GUIDANCE: Each recommendation should be:
- Specific (not "monitor vendor" but "schedule annual DPA compliance audit for Q2, verify sub-processor list currency quarterly")
- Actionable (assignable to a person/team)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[Negotiation framework applied per `references/dpa-negotiation-framework.md`. GDPR Article 28 compliance verified. Transfer mechanism assessed per Schrems II requirements.]

### B. Supporting Data

[Vendor security certifications, SOC 2 report summary, sub-processor list, Transfer Impact Assessment, SCC execution records.]
