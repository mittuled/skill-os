# SOC 2 Control Framework Reference

Reference framework for managing SOC 2 certification covering Trust Services Criteria, control design, and evidence collection.

## Trust Services Criteria Overview

| Category | Required | Common Controls | When to Include |
|----------|----------|----------------|----------------|
| Security (CC) | Yes (always) | Access control, change management, risk assessment, incident response, logging, encryption | Always included |
| Availability (A) | Optional | DR/BCP, capacity management, SLA monitoring, failover | When uptime SLAs are in customer contracts |
| Processing Integrity (PI) | Optional | Data validation, error handling, reconciliation, completeness checks | When accuracy of data processing is critical |
| Confidentiality (C) | Optional | Data classification, encryption, access restrictions, disposal | When handling confidential business data |
| Privacy (P) | Optional | Consent, DSR processing, retention, disclosure | When processing personal data (often overlaps GDPR) |

## Common Controls by Trust Services Criterion

### Security (CC) — Required Controls

| Criterion | Control Area | Typical Controls |
|-----------|-------------|-----------------|
| CC1.1-1.5 | Control Environment | Security policies, organisational structure, board oversight, personnel standards |
| CC2.1-2.3 | Communication | Internal/external security communication, reporting channels |
| CC3.1-3.4 | Risk Assessment | Annual risk assessment, risk register, change-triggered reassessment |
| CC4.1-4.2 | Monitoring | Continuous monitoring, deficiency evaluation and remediation |
| CC5.1-5.3 | Control Activities | Control selection, technology controls, policy deployment |
| CC6.1-6.8 | Logical/Physical Access | Authentication, MFA, RBAC, access provisioning/deprovisioning, physical access |
| CC7.1-7.5 | System Operations | Vulnerability management, change detection, incident response, recovery |
| CC8.1 | Change Management | Change authorization, testing, approval, deployment |
| CC9.1-9.2 | Risk Mitigation | Vendor management, business disruption risk |

### Availability (A) — Common Controls

| Criterion | Control Area | Typical Controls |
|-----------|-------------|-----------------|
| A1.1 | Capacity Management | Capacity monitoring, auto-scaling, threshold alerts |
| A1.2 | Recovery Planning | DR plan, BCP plan, RTO/RPO targets |
| A1.3 | Recovery Testing | Annual DR drill, backup restoration testing |

## Evidence Collection Matrix

| Control | Evidence Type | Collection Frequency | Automation |
|---------|--------------|---------------------|-----------|
| Access Reviews | Access review completion records | Quarterly | IAM platform export |
| MFA Enforcement | MFA configuration screenshot | Observation period start + end | IdP configuration export |
| Change Management | Change tickets with approvals | Per change (continuous) | Ticketing system API |
| Vulnerability Scanning | Scan results and remediation | Monthly or continuous | Scanner scheduled reports |
| Incident Response | IR plan + incident records | Per incident + annual plan review | Incident platform export |
| Security Training | Completion reports | Annual + per hire | LMS API |
| Risk Assessment | Risk register + review notes | Annual + per change | Manual (standardized template) |
| Encryption | Configuration evidence | Observation period start + end | Infrastructure-as-code review |
| Backup/DR | DR drill report, backup logs | Annual drill + continuous backup | Backup platform logs |
| Vendor Management | Vendor assessments, DPAs | Per vendor + annual review | Vendor management platform |

## SOC 2 Type I vs. Type II Decision Matrix

| Factor | Type I | Type II |
|--------|--------|---------|
| Timeline | 1-3 months preparation | 6-12 months observation period |
| What it proves | Controls designed appropriately at a point in time | Controls operating effectively over a period |
| Customer acceptance | Acceptable for initial procurement, not for renewals | Required by most enterprise customers for ongoing |
| Cost | Lower (shorter audit) | Higher (longer observation + ongoing evidence) |
| When to choose | First SOC 2, need certification quickly | Mature programme, enterprise customer requirements |

## Audit Timeline Template

| Phase | Duration | Activities |
|-------|----------|-----------|
| Scoping | 2-4 weeks | Define criteria, system boundaries, auditor selection |
| Gap Assessment | 4-8 weeks | Internal assessment, remediation of critical gaps |
| Observation Period (Type II) | 6-12 months | Continuous evidence collection, control operation |
| Fieldwork | 4-8 weeks | Auditor testing, walkthroughs, evidence review |
| Report Drafting | 2-4 weeks | Auditor drafts report, management review |
| Report Issuance | 1-2 weeks | Final report, management response, distribution |
