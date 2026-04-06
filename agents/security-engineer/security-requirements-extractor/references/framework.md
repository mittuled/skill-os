# Framework: Security Requirements Extractor

Defines the data classification model, regulatory mapping matrix, and requirement derivation methodology for extracting testable security requirements from product specifications.

## Data Classification Model

| Level | Definition | Examples | Default Controls Required |
|-------|-----------|----------|--------------------------|
| Public | Intentionally disclosed to the world | Marketing content, public APIs, open-source code | Integrity (no tampering) |
| Internal | Accessible to all employees; not for external sharing | Internal documentation, aggregate metrics | Access control, audit trail |
| Confidential | Sensitive business data; subset of employees | Business contracts, source code, employee data, user PII | Encryption at rest, access control, audit trail, DLP |
| Restricted | Highest sensitivity; regulatory or legal obligation | PHI, payment card data, credentials, encryption keys | Encryption at rest (AES-256), encryption in transit (TLS 1.2+), field-level encryption, strict access control, audit trail, data residency enforcement |

## Regulatory Applicability Matrix

Identify applicable regulations based on the data types and geographies present in the specification:

| Regulation | Trigger Condition | Key Engineering Obligations |
|------------|------------------|----------------------------|
| **GDPR** | EU/EEA personal data processed by any entity | Data subject rights API, consent management, data residency (EU), privacy by design, DPA with processors, breach notification within 72 hours |
| **HIPAA Security Rule** | PHI processed by a US covered entity or business associate | Administrative, physical, and technical safeguards; BAA; audit controls; transmission security; access controls |
| **PCI-DSS** | Payment card data stored, processed, or transmitted | Tokenization or scope elimination (preferred); cardholder data environment isolation; quarterly vulnerability scanning; annual penetration test |
| **CCPA** | California residents' personal data; revenue > $25M or 100K+ consumers | Right to know, right to delete, opt-out of sale, data inventory |
| **SOX ITGC** | Financial systems at public companies | Change management controls, access reviews, segregation of duties, audit trails |
| **SOC 2 Type II** | SaaS products sold to enterprise customers | CC6-CC9 trust service criteria; availability, confidentiality, processing integrity |

## Requirement Derivation Rules

For each regulatory obligation, derive requirements using this pattern:

```
[Actor] MUST/SHALL [Action] [Object] [Condition/Constraint] [Measurable Criterion]
```

| Regulation | Example Derived Requirement |
|------------|---------------------------|
| GDPR Art. 5(1)(e) | "The system SHALL automatically delete user personal data 30 days after account deletion, verified by deletion confirmation log entries" |
| GDPR Art. 32 | "All PII stored in the users database SHALL be encrypted at rest using AES-256 with keys stored in AWS KMS" |
| HIPAA § 164.312(a)(2)(i) | "All PHI access SHALL require individual user authentication with MFA for admin-role users" |
| SOC 2 CC6.1 | "All production IAM roles SHALL be reviewed quarterly; access not reaffirmed within 14 days of review deadline SHALL be automatically revoked" |
| PCI-DSS 3.4 | "The system SHALL NOT store full card numbers; payment processing SHALL route through Stripe's hosted fields to prevent card data entering application scope" |

## Testability Standards

Every requirement must be testable. Apply this validation before including a requirement:

| Testability Check | Pass Criteria |
|------------------|---------------|
| Observable | Can an engineer write an automated test or query to verify this requirement? |
| Measurable | Does the requirement include a numeric threshold, specific behavior, or definitive outcome? |
| Bounded | Is the scope of the requirement clear (which service, which data type, which user role)? |
| Attributable | Is it clear which team or component owns compliance? |

**Failing example**: "The system must be secure."
**Passing example**: "The `users` service MUST enforce HTTPS on all endpoints and MUST reject TLS versions < 1.2 with HTTP 400."

## Requirement Prioritization

| Priority | Criteria |
|----------|----------|
| P1 — Blocking | Compliance obligation with regulatory enforcement risk; absence blocks launch to regulated markets |
| P2 — Required | Security best practice with documented risk; absence creates known exploitable vulnerability |
| P3 — Recommended | Defense-in-depth enhancement; absence increases risk but does not create a specific exploitable condition |
