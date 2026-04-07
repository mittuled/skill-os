# SOC 2 Readiness Tracker

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Security & Compliance Programme Manager] |
| Version | [1.0] |
| Status | [Draft / Approved] |
| Skill | soc2-programme-manager |
| Report Type | [SOC 2 Type I / SOC 2 Type II] |
| Audit Firm | [CPA firm name] |
| Observation Period | [MM/DD/YYYY] – [MM/DD/YYYY] (Type II only) |
| Target Report Date | [MM/DD/YYYY] |

## Programme Summary

[2-3 sentences describing the SOC 2 scope, trust criteria selected, and the business driver for certification.

GUIDANCE: Example: "This tracker covers SOC 2 Type II certification for the production SaaS platform, scoped to the Security and Availability criteria. The observation period runs January through December 2025 with fieldwork planned for Q1 2026. Certification is required to unblock enterprise sales engagements in the Fortune 500 pipeline."]

**Trust criteria in scope:** [Security (required) / Availability / Confidentiality / Processing Integrity / Privacy]
**Criteria excluded and rationale:** [e.g., Processing Integrity — not applicable; the platform does not process financial transactions]
**System description summary:** [Brief description of the system under assessment]

---

## Scope Document

| Scope Element | Included? | Justification |
|--------------|-----------|---------------|
| Production application (web / API) | [Yes / No] | |
| Production database | [Yes / No] | |
| Cloud infrastructure ([AWS / GCP / Azure] region: [us-east-1]) | [Yes / No] | |
| CI/CD pipeline | [Yes / No] | |
| Corporate IT / end-user devices | [Yes / No] | |
| Subprocessors: [Vendor 1, Vendor 2] | [Yes / No — disclosed as subservice organizations] | |
| Carve-out subservice organizations | [List any carved-out vendors] | |

---

## Control Matrix — Trust Services Criteria

### CC1 — Control Environment

| Control ID | Criterion | Control Description | Control Owner | Frequency | Evidence Type | Readiness | Gap? |
|------------|-----------|--------------------|--------------|-----------|--------------|---------|----|
| CC1.1 | CC1.1 | Board / management commitment to integrity and ethical values documented in Code of Conduct | [Legal / HR] | Annual | Code of Conduct + sign-off records | [Ready / Partial / Gap] | |
| CC1.2 | CC1.2 | Organizational structure with defined reporting lines and responsibilities | [HR] | Annual | Org chart + role descriptions | | |
| CC1.4 | CC1.4 | Security awareness training completed by all personnel | [HR / Compliance] | Annual (+ on-hire) | LMS completion report | | |

### CC2 — Communication & Information

| Control ID | Criterion | Control Description | Control Owner | Frequency | Evidence Type | Readiness | Gap? |
|------------|-----------|--------------------|--------------|-----------|--------------|---------|----|
| CC2.1 | CC2.1 | Information security policy communicated to all personnel | [Compliance] | Annual | Policy acknowledgement records | | |
| CC2.2 | CC2.2 | Internal communication of security responsibilities | [Compliance] | Annual | Policy + training records | | |

### CC6 — Logical and Physical Access Controls

| Control ID | Criterion | Control Description | Control Owner | Frequency | Evidence Type | Readiness | Gap? |
|------------|-----------|--------------------|--------------|-----------|--------------|---------|----|
| CC6.1 | CC6.1 | Access provisioning process — least privilege, role-based | [IT / Security] | Per event | Provisioning tickets, IAM config | | |
| CC6.2 | CC6.2 | Authentication — MFA enforced for production access | [Engineering] | Continuous | MFA enforcement config screenshot | | |
| CC6.3 | CC6.3 | Quarterly access reviews conducted and documented | [IT] | Quarterly | Access review sign-off records | | |
| CC6.6 | CC6.6 | Logical access restrictions for remote access (VPN / SSO) | [IT] | Continuous | VPN config, SSO policy | | |
| CC6.7 | CC6.7 | Encryption of data in transit and at rest | [Engineering] | Continuous | TLS cert inventory, KMS config | | |
| CC6.8 | CC6.8 | Malware / endpoint detection | [IT] | Continuous | EDR coverage report | | |

### CC7 — System Operations

| Control ID | Criterion | Control Description | Control Owner | Frequency | Evidence Type | Readiness | Gap? |
|------------|-----------|--------------------|--------------|-----------|--------------|---------|----|
| CC7.1 | CC7.1 | Security monitoring — SIEM / alerting configured | [Engineering] | Continuous | SIEM config + alert log sample | | |
| CC7.2 | CC7.2 | Anomaly detection and security event investigation | [Security] | Continuous | Incident log / alert review records | | |
| CC7.3 | CC7.3 | Incident response procedures documented and tested | [Security] | Annual (tabletop) | IR plan + test results | | |
| CC7.4 | CC7.4 | Incident response — containment, recovery, notification | [Security] | Per incident | Incident tickets with timeline | | |

### CC8 — Change Management

| Control ID | Criterion | Control Description | Control Owner | Frequency | Evidence Type | Readiness | Gap? |
|------------|-----------|--------------------|--------------|-----------|--------------|---------|----|
| CC8.1 | CC8.1 | Change management — approval, testing, deployment controls | [Engineering] | Per change | JIRA/GitHub PR records with approvals | | |

### CC9 — Risk Mitigation (Vendor / Third-Party)

| Control ID | Criterion | Control Description | Control Owner | Frequency | Evidence Type | Readiness | Gap? |
|------------|-----------|--------------------|--------------|-----------|--------------|---------|----|
| CC9.2 | CC9.2 | Vendor security assessments and DPAs in place | [Procurement / Legal] | Annual | Vendor assessment records, DPA list | | |

### A1 — Availability (if in scope)

| Control ID | Criterion | Control Description | Control Owner | Frequency | Evidence Type | Readiness | Gap? |
|------------|-----------|--------------------|--------------|-----------|--------------|---------|----|
| A1.1 | A1.1 | Capacity monitoring and planning | [Engineering] | Continuous | CloudWatch / monitoring dashboards | | |
| A1.2 | A1.2 | Disaster recovery plan documented and tested annually | [Operations] | Annual | DR plan + test results with RTO/RPO | | |
| A1.3 | A1.3 | Backup procedures and recovery testing | [Engineering] | Monthly | Backup logs, restore test records | | |

---

## Readiness Summary

**Scoring key:** Ready = control fully implemented and evidenced | Partial = control exists but evidence gaps | Gap = control not in place

| Trust Criterion | Total Controls | Ready | Partial | Gap | Readiness % |
|----------------|---------------|-------|---------|-----|------------|
| CC1 — Control Environment | [N] | [N] | [N] | [N] | [N]% |
| CC2 — Communication | [N] | | | | |
| CC6 — Logical Access | [N] | | | | |
| CC7 — System Operations | [N] | | | | |
| CC8 — Change Management | [N] | | | | |
| CC9 — Risk / Vendor | [N] | | | | |
| A1 — Availability | [N] | | | | |
| **Total** | **[N]** | **[N]** | **[N]** | **[N]** | **[N]%** |

**Audit go / no-go:** [Go — all critical controls ready / No-Go — [N] gaps must be remediated first]

---

## Audit Coordination Tracker

| Request ID | Auditor Request | Control / Criterion | Evidence Submitted | Status | Due Date | Owner |
|-----------|----------------|--------------------|--------------------|--------|----------|-------|
| REQ-001 | [Access review records for Q3] | CC6.3 | [GDrive link] | [Submitted / Pending] | [MM/DD] | [Name] |
| REQ-002 | | | | | | |

**Open auditor questions:** [N]
**Exception log:**

| Exception ID | Control | Finding Description | Management Response | Risk Accepted? |
|-------------|---------|--------------------|--------------------|---------------|
| EXC-001 | [CC6.3] | [Description] | [Response] | [Yes / No] |
