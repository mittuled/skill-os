# Security Requirements Document

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Agent role / human name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | security-requirements-extractor |
| Source Specifications | [Links to PRD, design doc, architecture proposal] |
| Project | [Project or feature name] |

## Executive Summary

[2-3 sentences covering the data classification scope, applicable regulations, and the number and priority distribution of requirements derived.
GUIDANCE: Lead with the highest-impact regulatory obligation. Example: "This feature processes EU user PII and payment card data, triggering GDPR and PCI-DSS obligations. 14 security requirements were derived: 4 P1 (blocking launch to EU/regulated markets), 7 P2, and 3 P3. The most critical: PCI scope must be eliminated via Stripe hosted fields before any payment processing is coded."]

## Data Classification and Scope

[Identify all data types handled by this feature and their classification.

GUIDANCE:
- Good: "User email addresses: Confidential (GDPR PII). Payment card numbers: Restricted (PCI-DSS). User-generated content (public posts): Public. Session tokens: Restricted (credential)."
- Bad: "Handles user data and payments."
- Format: Table with data type, classification level, storage location, and retention period]

| Data Type | Classification | Storage Location | Retention | Applicable Regulation |
|-----------|---------------|-----------------|-----------|----------------------|
| [Data type] | [Public/Internal/Confidential/Restricted] | [Service/database] | [X days/years] | [GDPR/HIPAA/PCI/etc.] |

## Regulatory Applicability Matrix

[Identify which regulations apply and why.

GUIDANCE:
- Good: "GDPR: Applies — feature processes EU user email addresses and behavioral data. PCI-DSS: Applies — feature processes payment card interactions. HIPAA: Not applicable — no PHI processed."
- Bad: "Standard data protection regulations apply."
- Format: Table with each regulation, applicability decision, and trigger condition]

| Regulation | Applicable | Trigger Condition | Key Obligations |
|------------|-----------|------------------|----------------|
| GDPR | [Yes / No] | [Why it applies or doesn't] | [Key engineering obligations] |
| HIPAA | [Yes / No] | [Trigger condition] | [Obligations if applicable] |
| PCI-DSS | [Yes / No] | [Trigger condition] | [Obligations if applicable] |
| CCPA | [Yes / No] | [Trigger condition] | [Obligations if applicable] |
| SOC 2 | [Yes / No] | [Trigger condition] | [Obligations if applicable] |

## Security Requirements

[Derived, testable engineering requirements with traceability to source regulation or risk.

GUIDANCE:
- Good: "REQ-S-001 (P1): The `payments` service MUST NOT store full PAN (card numbers). All card interactions MUST use Stripe's hosted fields SDK to prevent card data entering application scope. Source: PCI-DSS 3.4. Test: Confirm no card number patterns (16-digit sequences) appear in application logs or database."
- Bad: "Payment data must be secured."
- Format: Numbered requirements with priority, source traceability, and test criteria]

### P1 — Blocking Requirements

| ID | Requirement | Source | Test Criteria | Owner |
|----|-------------|--------|---------------|-------|
| REQ-S-001 | [Actor] SHALL [action] [object] [constraint]. | [Regulation + article] | [How to verify compliance] | [Team] |
| REQ-S-002 | [Requirement] | [Source] | [Test] | [Team] |

### P2 — Required Requirements

| ID | Requirement | Source | Test Criteria | Owner |
|----|-------------|--------|---------------|-------|
| REQ-S-010 | [Requirement] | [Source / security best practice] | [Test] | [Team] |

### P3 — Recommended Requirements

| ID | Requirement | Source | Test Criteria | Owner |
|----|-------------|--------|---------------|-------|
| REQ-S-020 | [Requirement] | [Source] | [Test] | [Team] |

## Assumptions and Clarifications Needed

[Document assumptions made where specifications were incomplete.

GUIDANCE: Assumptions must be validated with the product or engineering team before requirements are finalized. Unvalidated assumptions create requirements that may be wrong.]

| Assumption | Impact If Wrong | Clarification Owner | Deadline |
|------------|----------------|---------------------|----------|
| [Assumption made] | [What changes if assumption is false] | [Who must confirm] | [YYYY-MM-DD] |

## Handoff Checklist

- [ ] Requirements reviewed with product manager for completeness
- [ ] Requirements reviewed with engineering lead for feasibility
- [ ] P1 requirements added to sprint backlog as must-have acceptance criteria
- [ ] P2 requirements added to engineering backlog with target sprint
- [ ] Requirements linked to architecture review task
- [ ] Requirements linked to QA test plan

## Recommendations

- **P1**: [Most critical security control to implement, owner, deadline]
- **P2**: [Required security control, owner, target sprint]
- **P3**: [Defense-in-depth enhancement, owner, backlog]

## Appendices

### A. Methodology

[How requirements were derived: which specification sections were reviewed, which regulatory texts were consulted, and what security frameworks were applied (OWASP ASVS level, NIST CSF).]

### B. Regulatory Reference Index

[Links to the specific regulatory articles and standards sections cited in the requirements.]
