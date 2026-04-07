# Compliance Gap Analysis: [Framework / Standard]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | Security Engineer |
| Framework | [SOC 2 Type II / ISO 27001 / PCI DSS v4 / HIPAA / GDPR] |
| Audit Target Date | [YYYY-MM-DD] |
| Skill | security-compliance-enabler |
| Status | [In Progress / Complete] |
| Overall Readiness | [X% of controls met] |

## Summary

| Status | Control Count | % of Total |
|--------|-------------|-----------|
| Met — evidence available | [N] | [%] |
| Partially met — gaps exist | [N] | [%] |
| Not met — remediation required | [N] | [%] |
| Not applicable | [N] | [%] |
| **Total in scope** | **[N]** | **100%** |

**Estimated readiness for audit**: [X%]
**Critical gaps (will likely result in audit failure if not remediated)**: [N]
**Target readiness date**: [YYYY-MM-DD]

## Control Gap Detail

### Critical Gaps (Audit Blockers)

| Control ID | Control Name | Gap Description | Remediation | Owner | Due Date | Evidence Required |
|-----------|-------------|----------------|-------------|-------|----------|-----------------|
| [CC6.1] | [Logical and physical access controls] | [MFA not enforced for all users with admin access] | [Enable MFA enforcement at IdP level] | [IT / Security] | [Date] | [Screenshot of MFA enforcement policy] |
| [A.9.2.3] | [Management of privileged access] | [No quarterly privileged access review conducted] | [Schedule quarterly access review; document first review] | [Security] | [Date] | [Access review records] |

### Partial Gaps (Needs Strengthening)

| Control ID | Control Name | Current State | Gap | Remediation | Owner | Due |
|-----------|-------------|--------------|-----|-------------|-------|-----|
| [CC7.2] | [System monitoring] | [Monitoring in place but no documented alert response SLAs] | [Missing SLA documentation] | [Document alert response times in runbooks] | [DevOps] | [Date] |

### Met Controls (Evidence Available)

| Control ID | Control Name | Evidence Location | Last Verified |
|-----------|-------------|------------------|--------------|
| [CC6.6] | [Encryption in transit] | [TLS configuration screenshots in [wiki link]] | [YYYY-MM-DD] |
| [CC8.1] | [Change management] | [Git history + PR review policy in CLAUDE.md] | [YYYY-MM-DD] |

## Evidence Collection Status

| Evidence Type | Required For | Status | Location |
|--------------|-------------|--------|----------|
| MFA enforcement screenshot | [CC6.1, CC6.2] | [Collected / Pending] | [Link] |
| Penetration test report | [CC4.1] | [Collected / Pending] | [Link] |
| Vulnerability scan results (last 90 days) | [CC7.1] | [Collected / Pending] | [Link] |
| Access review records | [CC6.3] | [Collected / Pending] | [Link] |
| Incident response log | [CC7.3] | [Collected / Pending] | [Link] |
| Vendor security assessments | [CC9.1] | [Collected / Pending] | [Link] |
| Security training completion records | [CC1.4] | [Collected / Pending] | [Link] |
| Business continuity test results | [A.17.1.3] | [Collected / Pending] | [Link] |

## Remediation Roadmap

### Phase 1 (Critical gaps — complete before audit)

| # | Control | Action | Owner | Due | Estimated Effort |
|---|---------|--------|-------|-----|-----------------|
| 1 | [Control ID] | [Specific action] | [Role] | [Date] | [X days] |

### Phase 2 (Partial gaps — strengthen before audit)

| # | Control | Action | Owner | Due | Estimated Effort |
|---|---------|--------|-------|-----|-----------------|
| 1 | [Control ID] | [Specific action] | [Role] | [Date] | [X days] |

### Phase 3 (Evidence gathering — ongoing)

| # | Evidence Item | Owner | Collection Method | Due |
|---|--------------|-------|------------------|-----|
| 1 | [Evidence] | [Role] | [How to collect] | [Date] |

## Audit Preparation Checklist

- [ ] All critical gaps remediated
- [ ] All evidence collected and organized in audit folder
- [ ] Evidence reviewed by a second person for completeness
- [ ] Auditor briefing document prepared
- [ ] Key personnel briefed on their roles during audit
- [ ] Customer data access request procedure tested
- [ ] Incident response simulation completed in last 12 months
