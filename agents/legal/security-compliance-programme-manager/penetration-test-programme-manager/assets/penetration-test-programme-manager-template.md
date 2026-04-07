# Penetration Test Scope & Results Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Security & Compliance Programme Manager] |
| Version | [1.0] |
| Status | [Draft / Final] |
| Skill | penetration-test-programme-manager |
| Engagement Type | [Annual compliance / Post-release / Customer-requested] |
| Testing Firm | [Firm name] |
| Testers | [Lead tester name(s), certifications: CREST / OSCP / CEH] |

---

## Engagement Summary

[2-3 sentences summarising the test type, scope, key findings, and overall risk posture.

GUIDANCE: Example: "A grey-box external penetration test was conducted against the production web application and public API surface from [MM/DD] to [MM/DD/YYYY]. The engagement identified 2 High and 4 Medium findings, all of which have been remediated or have active remediation tickets. No critical vulnerabilities were identified; overall risk posture is assessed as Medium."]

**Test methodology:** [Black-box / Grey-box / White-box]
**Testing window:** [MM/DD/YYYY] to [MM/DD/YYYY]
**Overall risk rating:** [Critical / High / Medium / Low]
**Total findings:** [N] Critical, [N] High, [N] Medium, [N] Low, [N] Informational

---

## Scope Definition

### In-Scope Targets

| # | Target | Type | URL / IP Range | Testing Approach |
|---|--------|------|---------------|-----------------|
| 1 | [Production web application] | Web app | [https://app.company.com] | Authenticated + unauthenticated |
| 2 | [Public API] | REST/GraphQL API | [https://api.company.com] | Authenticated with test credentials |
| 3 | [Admin portal] | Web app | [https://admin.company.com] | Authenticated (admin role) |
| 4 | [Mobile application] | iOS / Android | [App Store / Play Store build] | [Grey-box] |
| 5 | [Cloud configuration] | AWS / GCP / Azure | [Account ID] | [Config review] |

### Out-of-Scope Systems

| System | Reason for Exclusion |
|--------|----------------------|
| [Production database direct access] | [Risk to data integrity — covered by config review] |
| [Third-party SSO provider] | [Provider-managed; separate vendor assessment] |
| [Dev/staging environments] | [Isolated from production; separate engagement] |

### Credentials Provided (Grey-box)

| Role | Username | Access Level |
|------|----------|--------------|
| Standard user | [testuser@company.com] | Standard authenticated user |
| Admin user | [testadmin@company.com] | Admin role — [specific permissions] |

---

## Rules of Engagement

| Parameter | Agreed Value |
|-----------|-------------|
| Authorized testing start | [MM/DD/YYYY HH:MM UTC] |
| Authorized testing end | [MM/DD/YYYY HH:MM UTC] |
| Emergency stop contact | [Name, mobile number] |
| Critical finding escalation | Notify [security@company.com] within [2 hours] of discovery |
| DoS/DDoS testing | [Permitted / Prohibited] |
| Social engineering | [Permitted / Prohibited] |
| Production data handling | Tester must not exfiltrate real user data; use test accounts only |
| Evidence retention by tester | [30 days post-report] |
| Report classification | [Confidential — Not for distribution] |

**Engagement agreement signed:** [Yes / Pending] — Date: [MM/DD/YYYY]
**NDA executed:** [Yes / Pending] — Date: [MM/DD/YYYY]

---

## Findings Summary

| Finding ID | Title | Severity | CVSS Score | CWE / OWASP | Status | Owner | SLA Due | Closed Date |
|------------|-------|----------|------------|-------------|--------|-------|---------|-------------|
| PT-001 | [Broken access control — horizontal privilege escalation] | High | [8.1] | CWE-284 / OWASP A01 | [Open / In Progress / Closed] | [Engineering] | [MM/DD] | [MM/DD] |
| PT-002 | [SQL injection in search parameter] | High | [7.5] | CWE-89 / OWASP A03 | | | | |
| PT-003 | [CSRF on account settings endpoint] | Medium | [6.5] | CWE-352 / OWASP A01 | | | | |
| PT-004 | [Sensitive data in API response — PII over-exposure] | Medium | [5.4] | CWE-200 / OWASP A02 | | | | |
| PT-005 | [Missing security headers (HSTS, CSP, X-Frame-Options)] | Low | [3.1] | CWE-693 | | | | |
| PT-006 | [Verbose error messages exposing stack traces] | Informational | [N/A] | CWE-209 | | | | |

**Remediation SLAs:**
- Critical: 7 days
- High: 30 days
- Medium: 90 days
- Low: Next scheduled release cycle

---

## Detailed Finding Template

*Repeat this section for each finding.*

### PT-00[N]: [Finding Title]

**Severity:** [Critical / High / Medium / Low / Informational]
**CVSS 3.1 Score:** [N.N] — [Vector string]
**CWE:** [CWE-NNN — Name]
**OWASP Top 10:** [OWASP A0N:2021 — Category]

**Description:**
[Clear, non-technical description of the vulnerability and what it allows an attacker to do.]

**Evidence / Steps to Reproduce:**
1. [Step 1]
2. [Step 2]
3. [Observed outcome]

**Request / Response (redacted):**
```
[HTTP request snippet or command — redact any sensitive data]
```

**Business Impact:**
[What an attacker could achieve if this finding were exploited — confidentiality, integrity, availability impact.]

**Recommended Remediation:**
[Specific, actionable fix recommendation referencing the relevant framework or OWASP guidance.]

**Management Response:**
[Agreed remediation action, owner, and target date.]

---

## Remediation Tracker

| Finding ID | Severity | Remediation Action | Engineering Ticket | Owner | SLA Due | Verified By | Verification Date | Status |
|------------|----------|-------------------|--------------------|-------|---------|-------------|------------------|--------|
| PT-001 | High | [Fix description] | [JIRA-NNN] | [Name] | [MM/DD] | [Security] | [MM/DD] | [Closed] |
| PT-002 | High | | | | | | | |
| PT-003 | Medium | | | | | | | |
| PT-004 | Medium | | | | | | | |
| PT-005 | Low | | | | | | | |

**Remediation completion summary:**
- Critical: [N/N] closed ([N] open)
- High: [N/N] closed ([N] open)
- Medium: [N/N] closed ([N] open)
- Low: [N/N] closed ([N] open)

---

## Compliance Evidence Package Checklist

This package is submitted to SOC 2 auditors and for customer security questionnaires.

- [ ] Executed engagement agreement (SOW + NDA)
- [ ] Signed rules of engagement document
- [ ] Final penetration test report (this document)
- [ ] Remediation tracker with current status
- [ ] Closure evidence for Critical and High findings (screenshots / commit links / ticket resolutions)
- [ ] Management response letter summarising risk acceptance for any open items
- [ ] Next scheduled test date confirmed

**Package prepared by:** [Name]
**Package date:** [MM/DD/YYYY]
**Approved for distribution by:** [CISO / Security Lead]
