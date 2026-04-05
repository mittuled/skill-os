# Email Deliverability Health Report
## Metadata
| Field | Value |
|-------|-------|
| Report Period | [YYYY-MM-DD to YYYY-MM-DD] |
| Author | [Marketing Operations Manager] |
| Version | [1.0] |
| Status | [Draft / Final] |
| Skill | email-deliverability-manager |

## Executive Summary
[GUIDANCE: 2–3 sentences. State the overall health status (Healthy / At Risk / Critical), the most significant issue found, and the recommended action. Example: "Email deliverability is At Risk. Spam complaint rate reached 0.09% on the re-engagement campaign send on [date], approaching the 0.1% ISP threshold. Immediate list hygiene and campaign pause are recommended."]

## Overall Health Scorecard

| Metric | Current Value | Threshold | Status |
|--------|--------------|-----------|--------|
| Inbox placement rate | [X%] | ≥ 95% | 🟢 / 🟡 / 🔴 |
| Hard bounce rate | [X%] | < 0.5% | 🟢 / 🟡 / 🔴 |
| Soft bounce rate | [X%] | < 2% | 🟢 / 🟡 / 🔴 |
| Spam complaint rate | [X%] | < 0.08% | 🟢 / 🟡 / 🔴 |
| Unsubscribe rate | [X%] | < 0.5% | 🟢 / 🟡 / 🔴 |
| Avg. open rate (last 30 days) | [X%] | > 20% | 🟢 / 🟡 / 🔴 |
| Domain reputation (Postmaster) | [High/Medium/Low] | High | 🟢 / 🟡 / 🔴 |

**Overall Status**: [Healthy / At Risk / Critical]

## Authentication Compliance

| Record | Domain | Status | Last Verified | Notes |
|--------|--------|--------|--------------|-------|
| SPF | [domain.com] | [Pass / Fail / Missing] | [Date] | [Notes] |
| DKIM | [domain.com] | [Pass / Fail / Missing] | [Date] | [Selector] |
| DMARC | [domain.com] | [Pass / Fail / Missing] | [Date] | [Policy level] |

**Alignment check**: SPF aligns to From: domain — [Yes / No]. DKIM aligns to From: domain — [Yes / No].

## List Hygiene Summary

| Action | Contacts Before | Removed | Contacts After | Notes |
|--------|----------------|---------|----------------|-------|
| Hard bounce suppression | [N] | [N] | [N] | [Date of last action] |
| Spam trap removals | [N] | [N] | [N] | [Tool used] |
| Unengaged (90-day) suppression | [N] | [N] | [N] | [Re-engagement attempt Y/N] |
| Role-based addresses removed | [N] | [N] | [N] | — |

**Total active list size after hygiene**: [N] contacts

## Sender Reputation by ISP

| ISP | Tool | Reputation Score | Trend | Action Required |
|-----|------|-----------------|-------|----------------|
| Google (Gmail) | Postmaster | [High/Medium/Low/Bad] | [↑ / → / ↓] | [None / Monitor / Remediate] |
| Microsoft (Outlook) | SNDS | [Score] | [↑ / → / ↓] | [None / Monitor / Remediate] |
| Yahoo/AOL | Yahoo Postmaster | [OK / Issue] | [↑ / → / ↓] | [None / Monitor / Remediate] |

## Issues Identified and Remediation Plan

| Issue | Severity | Root Cause | Remediation Steps | Owner | Due Date |
|-------|----------|-----------|------------------|-------|----------|
| [Issue description] | [High/Med/Low] | [Root cause] | [Step 1, Step 2...] | [Name] | [Date] |

## Sending Best Practices Updates

| Practice | Current State | Recommended Change | Priority |
|----------|--------------|-------------------|---------|
| Send frequency | [Current] | [Recommended] | [H/M/L] |
| Segmentation | [Current] | [Recommended] | [H/M/L] |
| Send-time optimization | [Current] | [Recommended] | [H/M/L] |

## Appendices
### A. Blacklist Status
[Check MXToolbox for all sending domains/IPs and list results]

### B. Complaint Feedback Loop Registrations
[List active FBL registrations per ISP]
