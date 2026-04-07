# Compliance Framework Implementation Roadmap

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Security & Compliance Programme Manager] |
| Version | [1.0] |
| Status | [Draft / Approved] |
| Skill | compliance-framework-implementer |
| Framework | [SOC 2 / ISO 27001 / HIPAA / PCI DSS] |
| Target Certification Date | [MM/DD/YYYY] |

## Programme Summary

[2-3 sentences describing the framework, the business driver for implementation, and the organisational scope.

GUIDANCE: Example: "This roadmap implements SOC 2 Type II for the core SaaS platform to satisfy enterprise procurement requirements. The scope covers the production infrastructure, application tier, and all supporting engineering processes. The target observation period begins Q2 and fieldwork is scheduled for Q4."]

**Business driver:** [Enterprise sales requirement / Investor diligence / Regulatory mandate / Internal maturity]
**Systems in scope:** [Production environment / Data warehouse / [Specific systems]]
**Systems out of scope:** [Dev/test environments / [Specific exclusions]]

---

## Framework Scope Document

| Scope Element | In Scope | Justification / Exclusion Reason |
|--------------|----------|----------------------------------|
| Production web application | [Yes / No] | |
| Production database | [Yes / No] | |
| Cloud infrastructure ([AWS / GCP / Azure]) | [Yes / No] | |
| Third-party SaaS tools ([List]) | [Yes / No] | |
| Mobile application | [Yes / No] | |
| Corporate IT / end-user devices | [Yes / No] | |
| Subprocessors / vendors | [Yes / No] | |

**Applicable criteria / control domains:**
- [SOC 2: Security (CC), Availability (A), Confidentiality (C), Processing Integrity (PI), Privacy (P)]
- [ISO 27001: Annex A control categories selected]
- [HIPAA: Administrative / Physical / Technical safeguards]
- [PCI DSS: Requirements 1-12 in scope]

---

## Control Mapping Matrix

| Control ID | Framework Requirement | Control Description | Control Type | Owner | Existing Control? | Gap? | Shared With |
|------------|----------------------|--------------------|--------------|---------|--------------------|------|-------------|
| CTRL-001 | SOC 2 CC6.1 / ISO A.9.2 | User access provisioning policy and process | Administrative | [IT/Security] | [Yes / Partial / No] | [Yes / No] | ISO 27001 |
| CTRL-002 | SOC 2 CC6.2 | Multi-factor authentication enforcement | Technical | [Engineering] | [Yes / Partial / No] | | |
| CTRL-003 | SOC 2 CC6.3 | Quarterly access reviews | Administrative | [IT] | | | |
| CTRL-004 | SOC 2 CC8.1 / ISO A.12.1 | Change management — approval and testing | Administrative | [Engineering] | | | |
| CTRL-005 | SOC 2 CC7.3 / ISO A.16 | Incident response plan and testing | Administrative | [Security] | | | |
| CTRL-006 | SOC 2 CC3.2 / ISO A.6.1 | Annual risk assessment | Administrative | [Compliance] | | | |
| CTRL-007 | SOC 2 CC9.2 / ISO A.15 | Vendor security assessment process | Administrative | [Procurement] | | | |
| CTRL-008 | SOC 2 CC1.4 / ISO A.7.2 | Annual security awareness training | Administrative | [HR/Compliance] | | | |
| CTRL-009 | SOC 2 CC6.7 / ISO A.10 | Encryption at rest and in transit | Technical | [Engineering] | | | |
| CTRL-010 | SOC 2 A1.2 / ISO A.17 | Disaster recovery plan and annual test | Administrative | [Operations] | | | |
| [Add rows per framework requirements] | | | | | | | |

**Control types:** Technical (system-enforced), Administrative (policy/process), Physical (facility/hardware)
**Shared controls reduce total implementation effort by [N]% across frameworks.**

---

## Gap Remediation Plan

| Gap ID | Control ID | Gap Description | Remediation Action | Control Type | Effort (S/M/L) | Owner | Target Date | Status |
|--------|------------|----------------|--------------------|-------------|----------------|-------|-------------|--------|
| GAP-001 | CTRL-001 | Access provisioning process undocumented | Draft access management policy and procedure | Administrative | S | [Name] | [MM/DD] | [Not Started] |
| GAP-002 | CTRL-002 | MFA not enforced on all production systems | Enable MFA in [IAM system] for all production roles | Technical | M | [Name] | [MM/DD] | |
| GAP-003 | CTRL-003 | No recurring access review process | Configure quarterly access review in [tool] | Administrative | M | [Name] | [MM/DD] | |
| GAP-004 | CTRL-006 | Risk register not maintained | Create risk register and annual review cycle | Administrative | L | [Name] | [MM/DD] | |
| [Add rows per gap] | | | | | | | | |

**Effort key:** S = < 1 week, M = 1-4 weeks, L = > 4 weeks

---

## Implementation Phases

### Phase 1 — Foundation (Weeks 1–[N])

**Goal:** Scope finalized, critical-path gaps remediated, policies drafted.

| Milestone | Owner | Target Date | Done? |
|-----------|-------|-------------|-------|
| Framework scope document approved | [Name] | [MM/DD] | [ ] |
| Control mapping matrix v1 complete | [Name] | [MM/DD] | [ ] |
| Gap analysis complete | [Name] | [MM/DD] | [ ] |
| Critical and High gaps remediated | [Name] | [MM/DD] | [ ] |
| Core policies drafted and approved | [Name] | [MM/DD] | [ ] |

### Phase 2 — Implementation (Weeks [N]–[N])

**Goal:** All controls implemented and operational; evidence collection running.

| Milestone | Owner | Target Date | Done? |
|-----------|-------|-------------|-------|
| Technical controls deployed | [Engineering] | [MM/DD] | [ ] |
| Administrative controls in operation | [Compliance] | [MM/DD] | [ ] |
| Evidence collection automated where possible | [Engineering] | [MM/DD] | [ ] |
| Training programme deployed | [HR] | [MM/DD] | [ ] |

### Phase 3 — Readiness Validation (Weeks [N]–[N])

**Goal:** Internal audit confirms certification readiness; external auditor engaged.

| Milestone | Owner | Target Date | Done? |
|-----------|-------|-------------|-------|
| Internal pre-audit completed | [Compliance] | [MM/DD] | [ ] |
| Remaining gaps remediated | [Owners] | [MM/DD] | [ ] |
| Auditor engaged and engagement letter signed | [Compliance] | [MM/DD] | [ ] |
| Evidence package organised and submitted | [Compliance] | [MM/DD] | [ ] |

---

## Evidence Requirements by Control Domain

| Control Domain | Evidence Type | Collection Method | Frequency | Storage Location | Responsible |
|---------------|---------------|------------------|-----------|-----------------|-------------|
| Access Management | IAM user export, access review sign-offs | Automated export + manual sign-off | Quarterly | [GDrive / Confluence / GRC tool] | [IT] |
| Change Management | Ticket export with approval records | JIRA/GitHub API export | Per change | | [Engineering] |
| Incident Response | Incident log, tabletop test results | Manual log + test documentation | Quarterly | | [Security] |
| Risk Assessment | Risk register, review meeting minutes | Manual | Annual | | [Compliance] |
| Vendor Management | Vendor list, SOC 2 reports, DPAs | Manual registry | Annual | | [Procurement] |
| Security Training | LMS completion report | LMS export | Annual + on-hire | | [HR] |
| Logging & Monitoring | SIEM alert log, anomaly review | Automated | Continuous | | [Engineering] |
| Encryption | Config screenshots, certificate inventory | Manual + automated scan | Annual | | [Engineering] |
| DR/BCP | DR test results, RTO/RPO measurements | Manual test documentation | Annual | | [Operations] |

---

## Certification Readiness Summary

[Complete at end of Phase 3 internal audit]

**Overall readiness:** [N]% of controls fully implemented and evidenced
**Gaps remaining:** [N] gaps — [N] Critical, [N] High, [N] Medium
**Recommendation:** [Proceed to external audit / Defer — rationale]
**Auditor engagement date:** [MM/DD/YYYY]
