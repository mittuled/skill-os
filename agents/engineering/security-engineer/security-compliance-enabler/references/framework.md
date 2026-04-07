# Framework: Security Compliance Enabler

Defines the control framework mapping, implementation strategy, and evidence automation approach for achieving SOC 2, GDPR, HIPAA, and PCI-DSS compliance.

## Control Framework Mapping

### SOC 2 Trust Service Criteria (TSC)

| TSC | Category | Key Technical Controls |
|-----|----------|----------------------|
| CC6.1 | Logical access | IAM, MFA, RBAC, access provisioning and de-provisioning |
| CC6.2 | User access authentication | Password policy, MFA enforcement, SSO integration |
| CC6.3 | Role-based authorization | RBAC definition, privilege review, least-privilege enforcement |
| CC6.6 | External system boundaries | WAF, network segmentation, API authentication |
| CC7.1 | Vulnerability detection | SAST, DAST, dependency scanning, container scanning |
| CC7.2 | Monitoring | SIEM, log aggregation, anomaly detection, alert management |
| CC8.1 | Change management | CI/CD pipeline controls, peer review enforcement, deployment approval |
| CC9.2 | Vendor risk | Third-party security assessments, DPA management, SOC 2 report collection |
| A1.1 | Availability | SLO monitoring, capacity planning, incident response procedures |

### GDPR Key Technical Obligations

| Article | Obligation | Technical Implementation |
|---------|-----------|-------------------------|
| Art. 5 | Data minimization | Field-level audit of all collected data; delete unused fields |
| Art. 15-21 | Data subject rights | Rights API (access, rectification, erasure, portability) |
| Art. 25 | Privacy by design | Default opt-out; minimal data collection; pseudonymization |
| Art. 32 | Appropriate security | Encryption at rest and in transit; access controls; regular testing |
| Art. 33 | Breach notification | Incident response procedure with 72-hour notification workflow |
| Art. 44 | Data transfers | EU data residency or Standard Contractual Clauses for transfer |

### PCI-DSS v4.0 Key Controls

| Requirement | Description | Implementation |
|-------------|-------------|----------------|
| Req. 1 | Install and maintain network security | Firewall rules, network segmentation, DMZ |
| Req. 2 | No vendor defaults | Change all default credentials; harden all systems |
| Req. 3 | Protect stored card data | Tokenization (preferred); if stored: AES-256, masked PAN |
| Req. 4 | Encrypt transmission of card data | TLS 1.2+ on all card data paths |
| Req. 6 | Secure systems and software | Patch management SLAs; SAST/DAST in CI/CD |
| Req. 7 | Restrict access to card data | Role-based access; least privilege; access reviews |
| Req. 10 | Log and monitor all access | Audit logging; SIEM; log retention ≥ 12 months |
| Req. 11 | Test security of systems | Quarterly vulnerability scans; annual pen test |

## Control Gap Analysis Method

### Priority Classification

| Gap Severity | Definition | Remediation Timeline |
|-------------|-----------|---------------------|
| Audit Blocker | Absence causes automatic audit failure or immediate regulatory enforcement | Must resolve before audit; cannot ship to regulated markets |
| High | Absence results in significant audit finding or known exploitable risk | Resolve within 30 days; document exception if not possible |
| Medium | Absence results in minor finding or partial control credit | Resolve within 90 days |
| Low | Enhancement recommended by framework but not strictly required | Address in next planning cycle |

## Evidence Automation Architecture

Manual evidence collection is an anti-pattern. Build automated collection for:

| Evidence Type | Automation Method | Collection Frequency |
|--------------|------------------|---------------------|
| Access review completion | Export from IdP (Okta, Azure AD) of access reviews | Monthly |
| Vulnerability scan results | API export from scanner (Nessus, Qualys, Snyk) | Weekly |
| Security training completion | Export from training platform (KnowBe4, Curricula) | Monthly |
| Change management records | CI/CD pipeline metadata export | On each deployment |
| Incident response records | Export from incident management tool (PagerDuty, OpsGenie) | Monthly |
| Backup verification | Automated restore test result export | Weekly |
| Configuration compliance | Prowler / ScoutSuite scan export | Daily |

## Compliance Readiness Gates

Before external audit engagement, all gates must be green:

| Gate | Readiness Criterion |
|------|---------------------|
| Control inventory | 100% of required controls documented with owner and evidence link |
| Evidence collection | Automated for ≥ 80% of controls; manual for ≤ 20% with documented process |
| Policy library | All required policies written, approved, and signed |
| Audit blocker gaps | Zero open audit blockers |
| Mock audit | Internal mock audit completed within 90 days of real audit date |
| Remediation tracking | All open findings have owner and deadline |
