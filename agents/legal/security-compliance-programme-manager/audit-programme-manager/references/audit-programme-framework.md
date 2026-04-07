# Audit Programme Management Framework

Reference framework for managing security and compliance audit programmes covering scheduling, preparation, evidence management, and continuous improvement.

## Annual Audit Calendar Planning

### Common Audit Types and Cadences

| Audit Type | Typical Cadence | Planning Lead Time | Key Dependencies |
|-----------|----------------|-------------------|-----------------|
| SOC 2 Type II | Annual (12-month observation period) | 3-6 months | Control design, evidence automation, auditor engagement |
| ISO 27001 Surveillance | Annual (certification every 3 years) | 2-3 months | ISMS maintenance, internal audit completion |
| ISO 27001 Recertification | Every 3 years | 4-6 months | Full ISMS review, management review |
| Customer Audit | Per contract (typically annual) | 1-2 months | Customer scope agreement, evidence preparation |
| Penetration Test | Annual + after major changes | 1-2 months | Scope definition, vendor engagement |
| Internal Audit | Semi-annual or quarterly | 2-4 weeks | Audit plan, control owner availability |
| Regulatory Examination | As required by regulator | Varies | Regulatory notification, evidence compilation |

### Calendar Coordination Principles

1. Schedule SOC 2 observation period to align with fiscal year when possible
2. Complete internal audits 2-3 months before external audits to identify and remediate gaps
3. Stagger audits to avoid evidence collection bottlenecks (no more than 2 audits in the same month)
4. Schedule penetration tests to complete before SOC 2 observation period ends
5. Align customer audit windows with post-SOC 2 report issuance for evidence reuse

## Readiness Assessment Checklist

| Category | Assessment Item | Evidence Source |
|----------|----------------|----------------|
| Access Controls | Access reviews completed for audit period | IAM platform export, review sign-offs |
| Change Management | All changes documented with approval records | Ticketing system (Jira, Linear), deployment logs |
| Incident Response | IR plan tested, incidents documented and resolved | IR tabletop exercise records, incident tickets |
| Risk Assessment | Annual risk assessment completed | Risk register, risk review meeting notes |
| Vendor Management | Vendor assessments current, DPAs executed | Vendor tracker, DPA log |
| Training | Security awareness training completed | LMS completion reports |
| DR/BCP | DR drill conducted within audit period | DR drill report |
| Logging | Audit logs retained for required period | Log retention configuration evidence |
| Encryption | Encryption at rest and in transit verified | Configuration screenshots, certificate records |
| Policies | All policies reviewed within 12 months | Policy inventory with review dates |

## Evidence Collection Best Practices

### Automation Priority Matrix

| Evidence Type | Automation Feasibility | Recommended Approach |
|--------------|----------------------|---------------------|
| Access review completion | High | IAM platform scheduled exports |
| Change management tickets | High | Ticketing system API integration |
| Training completion | High | LMS API integration |
| Vulnerability scan results | High | Scanner scheduled reports |
| Encryption configuration | Medium | Infrastructure-as-code review |
| Policy acknowledgements | Medium | HR system integration |
| Incident response records | Medium | Incident platform export |
| Risk assessment documentation | Low | Manual collection, template standardization |
| Vendor assessment records | Low | Vendor management platform or manual |

### Evidence Quality Standards

1. **Timestamped**: Every piece of evidence must include a date or date range
2. **Scoped**: Evidence must cover the entire audit period, not just a point in time
3. **Attributable**: Evidence must show who performed the control activity
4. **Complete**: Population evidence must demonstrate completeness (all users, all systems, all changes)
5. **Current**: Evidence must be from the audit period, not a prior period

## Finding Remediation SLA Framework

| Severity | Definition | Remediation SLA | Escalation |
|----------|-----------|----------------|-----------|
| Critical | Control failure with active data exposure or regulatory breach | 7 days | CISO + General Counsel immediately |
| High | Material control gap likely to result in audit exception | 30 days | CISO within 48 hours |
| Medium | Control weakness that could develop into a material gap | 90 days | Security team lead within 1 week |
| Low | Improvement opportunity or best practice gap | Next audit cycle | Track in remediation backlog |
| Observation | Auditor recommendation, not a finding | Evaluate and plan | Include in programme retrospective |
