# Technical Onboarding Status — Acme Corp

| Field | Value |
|---|---|
| Date | 2026-03-31 |
| Customer | Acme Corp |
| Engineer | Jordan Lee |
| Target Go-Live | 2026-04-18 |
| Overall Status | BLOCKED |
| Progress | 17% (1/6 phases complete) |
| Skill | technical-onboarding-runner |

## Executive Summary

The Acme Corp implementation is blocked at the integration configuration phase. Environment setup is complete and the customer is provisioned. However, the Salesforce API credentials have not been provided by the customer's admin, preventing integration configuration from proceeding. Data migration, acceptance testing, training, and go-live are all downstream and cannot start until integration is unblocked. The go-live date of April 18 is at risk if credentials are not received by April 3.

## Phase Status

| Phase | Status | Issue |
|---|---|---|
| Environment Setup | ✅ Complete | |
| Integration Configuration | 🔴 Blocked | Salesforce API credentials not provided by customer |
| Data Migration | ⏳ Pending | Cannot start until integrations are configured |
| Acceptance Testing | ⏳ Pending | |
| Customer Training | ⏳ Pending | |
| Go-Live and Hypercare | ⏳ Pending | |

## Blocked Phases

### Integration Configuration — Salesforce API Credentials

**Blocker:** Acme Corp's Salesforce admin has not provided the API credentials required to configure the CRM integration. Follow-up email sent 2026-03-28 — no response as of 2026-03-31.

**Impact:** Data migration cannot begin until the Salesforce sync is operational. All downstream phases are blocked.

**Escalation path:**
1. Implementation Engineer to send second follow-up today with explicit deadline (April 3)
2. If no response by April 3 → escalate to Acme Corp's executive sponsor and copy the implementation lead
3. If go-live date is not recoverable → propose revised timeline with customer

**Owner:** Jordan Lee (implementation), Acme Salesforce Admin (customer action required)

## Timeline Risk Assessment

| Scenario | Go-Live Date |
|---|---|
| Credentials received by April 3 | April 18 (on track) |
| Credentials received April 4–7 | April 21–25 (1 week slip) |
| Credentials not received by April 7 | May 2+ (significant slip, escalation required) |

## Next Steps

| Action | Owner | Due |
|---|---|---|
| Send second follow-up to Acme Salesforce admin | Jordan Lee | Today (2026-03-31) |
| Escalate to Acme executive sponsor if no response | Jordan Lee | 2026-04-03 |
| Update implementation lead on status | Jordan Lee | 2026-04-01 |
| Prepare migration mapping document in parallel (unblocked work) | Jordan Lee | 2026-04-05 |
