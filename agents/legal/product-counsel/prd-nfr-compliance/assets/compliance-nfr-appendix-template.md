# Compliance NFR Appendix

**Product / Feature:** [FEATURE NAME]
**PRD Version:** [VERSION]
**PRD Author:** [PM NAME]
**Compliance Review By:** [PRODUCT COUNSEL NAME]
**Review Date:** [DATE]
**Legal Sign-Off:** ✅ Signed-Off / ❌ Pending Resolution of Items Below

---

## Overview

This appendix documents the non-functional compliance requirements (NFRs) for [FEATURE NAME]. Each requirement is testable, traceable to a regulatory source, and assigned to an engineering owner. Requirements must be accepted by the PM and Engineering Lead before the PRD is considered complete.

**PM Acknowledgment:** _____________________________ Date: ___________

**Engineering Lead Acknowledgment:** _____________________________ Date: ___________

---

## Compliance Coverage Summary

| Area | Applicable? | NFR Count | Status |
|---|---|---|---|
| Data Privacy (GDPR / CCPA) | Yes / No | [N] | ✅ Specified / ❌ Pending |
| Accessibility (WCAG 2.1 AA) | Yes / No | [N] | ✅ Specified / ❌ Pending |
| Security (encryption, auth) | Yes / No | [N] | ✅ Specified / ❌ Pending |
| Regulatory Disclosures | Yes / No | [N] | ✅ Specified / ❌ Pending |
| Audit Logging | Yes / No | [N] | ✅ Specified / ❌ Pending |
| Sector-Specific (HIPAA / PCI / COPPA) | Yes / No | [N] | ✅ Specified / ❌ Pending |
| Data Retention and Deletion | Yes / No | [N] | ✅ Specified / ❌ Pending |

---

## 1. Data Privacy Requirements

### NFR-PRIV-01: User Consent — GDPR Lawful Basis

- **Requirement:** The feature must establish and record a lawful basis for processing personal data before collection begins. Where consent is the chosen basis, an explicit opt-in mechanism must be presented prior to data collection.
- **Acceptance Criterion:** Consent records are stored with timestamp, version of consent text, and user identifier. Consent is re-solicited if consent text changes materially.
- **Regulatory Source:** GDPR Art. 6 (lawful basis), Art. 7 (conditions for consent)
- **Engineering Owner:** [OWNER]
- **Priority:** P0 — blocking

### NFR-PRIV-02: CCPA Opt-Out

- **Requirement:** California residents must be able to opt out of the sale or sharing of their personal information. The "Do Not Sell or Share My Personal Information" link must appear on the data collection surface.
- **Acceptance Criterion:** Opt-out preference is persisted within 15 business days of request and propagated to all downstream data processors.
- **Regulatory Source:** CCPA § 1798.120, CPRA amendment
- **Engineering Owner:** [OWNER]
- **Priority:** P0 — blocking

### NFR-PRIV-03: Data Minimisation

- **Requirement:** The feature must collect only personal data fields that are strictly necessary for the stated purpose. Fields not required for the core function must not be collected by default.
- **Acceptance Criterion:** Data model reviewed and signed off by Product Counsel. Each collected field is documented with its purpose and retention period.
- **Regulatory Source:** GDPR Art. 5(1)(c)
- **Engineering Owner:** [OWNER]
- **Priority:** P1

### NFR-PRIV-04: Data Export (Subject Access Request)

- **Requirement:** Users must be able to export all personal data held about them in a machine-readable format (JSON or CSV).
- **Acceptance Criterion:** Export endpoint available. Export delivered within 30 days of request. Export includes all personal data fields as documented in the data inventory.
- **Regulatory Source:** GDPR Art. 20 (right to data portability)
- **Engineering Owner:** [OWNER]
- **Priority:** P1

### NFR-PRIV-05: Right to Erasure (Deletion Endpoint)

- **Requirement:** Users must be able to request deletion of their personal data. The feature must support a deletion endpoint that removes or anonymises all personal data within 30 days.
- **Acceptance Criterion:** Deletion endpoint tested. Personal data confirmed absent from primary store, backups, and downstream systems within 30-day SLA. Deletion audit log retained for compliance verification.
- **Regulatory Source:** GDPR Art. 17, CCPA § 1798.105
- **Engineering Owner:** [OWNER]
- **Priority:** P1

### NFR-PRIV-06: Retention Policy

- **Requirement:** Personal data must not be retained beyond [X] days / [stated purpose completion] unless required by law.
- **Acceptance Criterion:** Automated purge job runs [daily / weekly] and deletes personal data records older than [RETENTION PERIOD]. Purge verified by automated test.
- **Regulatory Source:** GDPR Art. 5(1)(e)
- **Engineering Owner:** [OWNER]
- **Priority:** P1

---

## 2. Accessibility Requirements

### NFR-A11Y-01: WCAG 2.1 Level AA Compliance

- **Requirement:** All UI components introduced by this feature must meet WCAG 2.1 Level AA success criteria.
- **Acceptance Criterion:** Automated accessibility scan (axe-core or equivalent) returns 0 critical / 0 serious violations. Manual screen reader test (NVDA + Chrome / VoiceOver + Safari) passes for primary user flows.
- **Regulatory Source:** ADA Title III (digital accessibility), EU Web Accessibility Directive
- **Engineering Owner:** [OWNER]
- **Priority:** P1

### NFR-A11Y-02: Keyboard Navigation

- **Requirement:** All interactive elements must be reachable and operable via keyboard alone. Focus order must be logical and visible.
- **Acceptance Criterion:** Tab order audit passes. No keyboard trap introduced. All actions achievable without mouse.
- **Regulatory Source:** WCAG 2.1 SC 2.1.1, 2.4.3
- **Engineering Owner:** [OWNER]
- **Priority:** P1

---

## 3. Security Requirements

### NFR-SEC-01: Encryption at Rest

- **Requirement:** All personal data stored by this feature must be encrypted at rest using AES-256.
- **Acceptance Criterion:** Infrastructure configuration reviewed and confirmed. Data verified encrypted in storage layer audit.
- **Regulatory Source:** GDPR Art. 32, SOC 2 CC6.1
- **Engineering Owner:** [OWNER]
- **Priority:** P0 — blocking

### NFR-SEC-02: Encryption in Transit

- **Requirement:** All data transmitted by this feature must use TLS 1.2 or higher. TLS 1.0 and 1.1 must be disabled.
- **Acceptance Criterion:** TLS configuration scan (e.g., SSL Labs) returns A rating. No downgrade attacks possible.
- **Regulatory Source:** GDPR Art. 32, PCI DSS 4.2.1
- **Engineering Owner:** [OWNER]
- **Priority:** P0 — blocking

### NFR-SEC-03: Multi-Factor Authentication (MFA)

- **Requirement:** [If applicable] Access to [sensitive data / admin functions] must require MFA.
- **Acceptance Criterion:** MFA enforced for [user segment / admin roles]. Bypass not possible through API calls.
- **Regulatory Source:** [GDPR / SOC 2 / HIPAA — select applicable]
- **Engineering Owner:** [OWNER]
- **Priority:** P1

---

## 4. Regulatory Disclosures

### NFR-DISC-01: Terms of Service Acceptance

- **Requirement:** Users must explicitly accept the [COMPANY NAME] Terms of Service and Privacy Policy before accessing the feature. Acceptance must be recorded.
- **Acceptance Criterion:** Checkbox or explicit affirmation required. Acceptance timestamp, ToS version, and user ID stored. Pre-checked boxes not permitted.
- **Regulatory Source:** GDPR Art. 7, COPPA (if applicable)
- **Engineering Owner:** [OWNER]
- **Priority:** P0 — blocking

### NFR-DISC-02: Cookie Consent

- **Requirement:** Cookie consent banner must be displayed to users in jurisdictions requiring it (EU, UK, CA). Non-essential cookies must not be set until consent is granted.
- **Acceptance Criterion:** Consent management platform integrated. Non-essential cookies blocked prior to consent. Consent state persisted across sessions.
- **Regulatory Source:** EU ePrivacy Directive, GDPR, CCPA
- **Engineering Owner:** [OWNER]
- **Priority:** P0 — blocking

---

## 5. Audit Logging

### NFR-AUDIT-01: User Action Audit Log

- **Requirement:** All user actions on [sensitive data / PII / financial records] must be logged with actor, action type, resource ID, and timestamp.
- **Acceptance Criterion:** Audit log immutable (append-only). Log retained for [X] years per [REGULATORY REQUIREMENT]. Log queryable by compliance team within 48 hours of request.
- **Regulatory Source:** [GDPR Art. 30 / HIPAA / SOC 2 CC7.2 — select applicable]
- **Engineering Owner:** [OWNER]
- **Priority:** P1

---

## 6. Sector-Specific Requirements

### NFR-SECTOR-01: [HIPAA / PCI / COPPA — select applicable]

- **Requirement:** [SPECIFIC REQUIREMENT FOR REGULATED SECTOR]
- **Acceptance Criterion:** [CONCRETE TESTABLE CRITERION]
- **Regulatory Source:** [SPECIFIC REGULATION CITATION]
- **Engineering Owner:** [OWNER]
- **Priority:** P0 / P1

---

## 7. Unresolved Items

| Item | Area | Blocker Reason | Owner | Resolution Due |
|---|---|---|---|---|
| [ITEM 1] | [AREA] | [WHY UNRESOLVED — e.g., regulatory framework under analysis] | [OWNER] | [DATE] |
| [ITEM 2] | [AREA] | [WHY UNRESOLVED] | [OWNER] | [DATE] |

**PRD completeness:** ✅ All NFRs specified — PRD is complete / ❌ [N] unresolved items above must be closed before PRD sign-off

---

*Appendix prepared by [PRODUCT COUNSEL NAME] | Reviewed by [GENERAL COUNSEL NAME] | [DATE]*
