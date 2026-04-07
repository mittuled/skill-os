# Security Alert Triage: [Alert Name / Incident ID]

## Metadata

| Field | Value |
|-------|-------|
| Alert ID | [SIEM alert ID or incident ticket] |
| Date / Time | [YYYY-MM-DD HH:MM UTC] |
| Triaged By | Security Engineer |
| Alert Source | [SIEM / IDS / WAF / CSP Report / Manual] |
| Severity | [Critical / High / Medium / Low / Informational] |
| Status | [Open / Investigating / Contained / Closed] |
| Skill | continuous-security-monitoring |

## Alert Summary

**Alert name**: [Exact alert name from monitoring system]
**Triggered rule**: [Rule ID and description]
**Asset affected**: [Service, hostname, IP, or user account]
**First occurrence**: [YYYY-MM-DD HH:MM UTC]
**Occurrence count**: [N occurrences in last [X] hours]

## Initial Assessment

**Is this a true positive?**
- [ ] True positive — confirmed malicious or anomalous activity
- [ ] False positive — benign activity matching rule signature
- [ ] Indeterminate — further investigation required

**Verdict basis**: [Evidence or reasoning for the above classification]

## Timeline

| Time (UTC) | Event | Source |
|-----------|-------|--------|
| [HH:MM] | [Alert fired] | [SIEM] |
| [HH:MM] | [Analyst began triage] | [Manual] |
| [HH:MM] | [Finding or action] | [Log source / tool] |
| [HH:MM] | [Containment action taken] | [Manual / Automated] |

## Evidence

### Log Samples

```
[Raw log lines supporting the finding — include timestamp, source IP, user, action, and outcome]
```

### Indicators of Compromise (IoCs)

| Type | Value | Confidence | Source |
|------|-------|-----------|--------|
| IP Address | [IP] | [High/Med/Low] | [Log / Threat intel feed] |
| Domain | [domain] | | |
| File Hash | [SHA-256] | | |
| User Account | [username] | | |
| URL | [full URL] | | |

### MITRE ATT&CK Mapping

| Tactic | Technique | ID | Observed Behavior |
|--------|-----------|----|--------------------|
| [Initial Access] | [Phishing] | [T1566] | [Description] |
| [Execution] | | | |
| [Persistence] | | | |
| [Exfiltration] | | | |

## Impact Assessment

**Blast radius**: [One sentence — which systems, data, or users are affected or at risk]

| Impact Dimension | Assessment |
|-----------------|------------|
| Confidentiality | [None / Potential / Confirmed breach] |
| Integrity | [None / Potential / Confirmed tampering] |
| Availability | [None / Degraded / Service down] |
| Compliance scope | [None / PII / PCI / HIPAA / SOC2] |

## Containment Actions

| Action | Status | Performed By | Time |
|--------|--------|-------------|------|
| [Block IP at WAF] | [Completed / Pending] | [Role] | [HH:MM] |
| [Revoke compromised credential] | | | |
| [Isolate affected host] | | | |
| [Disable user account] | | | |

## Root Cause (if true positive)

**Root cause**: [Specific technical explanation — not "insufficient monitoring" but "API endpoint /admin/export lacked authentication check introduced in commit abc123"]

**Contributing factors**:
1. [Factor 1]
2. [Factor 2]

## Remediation Plan

| # | Action | Owner | Due | Ticket |
|---|--------|-------|-----|--------|
| 1 | [Immediate fix] | [Role] | [Date] | [Link] |
| 2 | [Long-term hardening] | [Role] | [Date] | [Link] |

## Escalation

| Threshold | Action Taken |
|-----------|-------------|
| Confirmed breach of PII | [Notified CISO at HH:MM] |
| Lateral movement detected | [Escalated to incident commander] |
| Data exfiltration suspected | [Engaged legal counsel] |

## Close / Disposition

**Final status**: [True Positive — Remediated / False Positive — Rule Tuned / True Positive — Accepted Risk]

**Tuning action (if false positive)**: [Rule adjustment or exception added — specify exact change]

**Lessons learned**: [One specific improvement to detection, response, or hardening derived from this incident]
