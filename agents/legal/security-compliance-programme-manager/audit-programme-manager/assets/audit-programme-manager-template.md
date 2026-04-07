# Annual Audit Programme Schedule

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Security & Compliance Programme Manager] |
| Version | [1.0] |
| Status | [Draft / Approved] |
| Skill | audit-programme-manager |
| Audit Year | [YYYY] |

## Programme Overview

[2-3 sentences summarising the audit scope, frameworks in scope, and key compliance drivers for the year.

GUIDANCE: Example: "This programme covers SOC 2 Type II, ISO 27001 surveillance, and two customer-initiated audits for FY2025. Internal control reviews are staggered to precede each external engagement by at least 60 days. The programme is designed to avoid overlapping evidence requests across all audits."]

**Frameworks in scope:** [SOC 2 / ISO 27001 / HIPAA / PCI DSS / Customer audit / Regulatory examination]
**Audit firm(s):** [Firm name(s) and audit type]
**Programme sponsor:** [CISO / General Counsel / VP Engineering]

---

## Annual Audit Calendar

| # | Audit Name | Framework | Type | Start Date | End Date | Lead Owner | Audit Firm | Status |
|---|-----------|-----------|------|------------|----------|------------|------------|--------|
| 1 | Internal Control Review — Q1 | All frameworks | Internal | [MM/DD] | [MM/DD] | [Name] | Internal | [Planned] |
| 2 | SOC 2 Type II Observation Period Begins | SOC 2 | External | [MM/DD] | [MM/DD] | [Name] | [CPA Firm] | [Planned] |
| 3 | ISO 27001 Surveillance Audit | ISO 27001 | External | [MM/DD] | [MM/DD] | [Name] | [CB Firm] | [Planned] |
| 4 | Internal Control Review — Q3 | All frameworks | Internal | [MM/DD] | [MM/DD] | [Name] | Internal | [Planned] |
| 5 | SOC 2 Type II Observation Period Ends | SOC 2 | External | [MM/DD] | [MM/DD] | [Name] | [CPA Firm] | [Planned] |
| 6 | SOC 2 Type II Fieldwork | SOC 2 | External | [MM/DD] | [MM/DD] | [Name] | [CPA Firm] | [Planned] |
| 7 | Customer Security Audit — [Customer Name] | Customer contract | External | [MM/DD] | [MM/DD] | [Name] | Customer | [Planned] |
| 8 | Annual Penetration Test | Policy / SOC 2 | External | [MM/DD] | [MM/DD] | [Name] | [Pentest Firm] | [Planned] |

**Staggering rule:** No more than 2 active audits in any calendar month.
**Internal-before-external buffer:** Internal reviews must complete ≥ 60 days before each external audit start.

---

## Control Domain Matrix

| Control Domain | Framework Mapping | Internal Review Frequency | Evidence Owner | Last Reviewed | Next Review |
|---------------|-------------------|--------------------------|----------------|---------------|-------------|
| Access Management | SOC 2 CC6.1-6.8, ISO A.9 | Quarterly | [IT/Security] | [MM/DD/YYYY] | [MM/DD/YYYY] |
| Change Management | SOC 2 CC8.1, ISO A.12.1 | Monthly | [Engineering] | [MM/DD/YYYY] | [MM/DD/YYYY] |
| Incident Response | SOC 2 CC7.3-7.5, ISO A.16 | Quarterly | [Security] | [MM/DD/YYYY] | [MM/DD/YYYY] |
| Risk Assessment | SOC 2 CC3.1-3.4, ISO A.6.1 | Semi-annual | [Compliance] | [MM/DD/YYYY] | [MM/DD/YYYY] |
| Vendor Management | SOC 2 CC9.2, ISO A.15 | Annual | [Procurement] | [MM/DD/YYYY] | [MM/DD/YYYY] |
| Security Awareness Training | SOC 2 CC1.4, ISO A.7.2 | Annual | [HR/Compliance] | [MM/DD/YYYY] | [MM/DD/YYYY] |
| Logging & Monitoring | SOC 2 CC7.1-7.2, ISO A.12.4 | Monthly | [Engineering] | [MM/DD/YYYY] | [MM/DD/YYYY] |
| Encryption | SOC 2 CC6.7, ISO A.10 | Annual | [Engineering] | [MM/DD/YYYY] | [MM/DD/YYYY] |
| Disaster Recovery / BCP | SOC 2 A1.2, ISO A.17 | Annual | [Operations] | [MM/DD/YYYY] | [MM/DD/YYYY] |
| Physical Security | SOC 2 CC6.4, ISO A.11 | Annual | [Facilities] | [MM/DD/YYYY] | [MM/DD/YYYY] |
| Policy & Procedure | SOC 2 CC1.2, ISO A.5 | Annual | [Compliance] | [MM/DD/YYYY] | [MM/DD/YYYY] |

---

## Finding Remediation Tracker

| Finding ID | Audit Source | Control Domain | Severity | Description | Root Cause | Owner | SLA Due Date | Status | Closed Date |
|------------|-------------|----------------|----------|-------------|------------|-------|--------------|--------|-------------|
| [AUD-001] | [SOC 2 / Internal] | [Domain] | Critical | [Finding description] | [Root cause] | [Name] | [MM/DD/YYYY] | [Open / In Progress / Closed] | [MM/DD/YYYY] |
| [AUD-002] | | | High | | | | | | |
| [AUD-003] | | | Medium | | | | | | |
| [AUD-004] | | | Low | | | | | | |

**Remediation SLAs:**
- Critical: 7 days
- High: 30 days
- Medium: 90 days
- Low: Next audit cycle

---

## Readiness Assessment Summary

| Readiness Area | Score (1-5) | Gaps Identified | Remediation Required Before Audit | Owner |
|----------------|------------|-----------------|-----------------------------------|-------|
| Access Controls | [N] | [Yes / No] | [Description or N/A] | [Name] |
| Change Management | [N] | | | |
| Incident Response | [N] | | | |
| Risk Assessment | [N] | | | |
| Vendor Management | [N] | | | |
| Security Training | [N] | | | |
| DR/BCP | [N] | | | |
| Logging & Monitoring | [N] | | | |
| Encryption | [N] | | | |
| Policies | [N] | | | |

**Scoring key:** 1 = No control, 2 = Partial/undocumented, 3 = Documented but untested, 4 = Documented and tested, 5 = Automated and continuously monitored

**Overall readiness score:** [Weighted average] / 5
**Audit go / no-go decision:** [Go / No-Go — rationale]

---

## Programme Retrospective Notes

[Recurring findings from prior cycles that must be addressed:]
- [Finding pattern + resolution approach]

[Evidence bottlenecks identified:]
- [Domain/control + bottleneck description + automation opportunity]

[Process improvements for next cycle:]
- [Improvement + owner + target date]
