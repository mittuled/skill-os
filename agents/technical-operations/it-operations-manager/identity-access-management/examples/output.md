# IAM Compliance Audit — Meridian AI

| Field | Value |
|---|---|
| Company | Meridian AI |
| Tier | Startup (<25 employees) |
| Security Posture | ACCEPTABLE |
| Compliance Rate | 33% (3/9 active users fully compliant) |
| MFA Missing | 2 users |
| SSO Not Enrolled | 2 users |
| Stale Accounts | 1 (>90 days) |
| Privileged Access Review Overdue | 3 |
| Skill | identity-access-management |

## Compliance Issues by User

| User | Department | Access Level | Risk | MFA | SSO | Stale | Review Overdue |
|---|---|---|---|---|---|---|---|
| Alex Chen | Executive | Admin | High | OK | OK | — | — |
| Priya Nair | Engineering | Admin | High | OK | OK | — | — |
| Jordan Lee | Product | Standard | Low | OK | OK | — | Review (120d / 365d limit) |
| Marcus Webb | Engineering | Production | High | OK | OK | — | OVERDUE (200d > 180d) |
| Diana Torres | Design | Standard | Low | OK | OK | — | Review (120d / 365d limit) |
| Sarah Chen | Engineering | Production | High | **MISSING** | OK | — | — |
| New Hire 2 | Sales | Standard | Low | **MISSING** | **NOT ENROLLED** | — | — |
| External Contractor | Engineering | Staging | Medium | OK | **NOT ENROLLED** | **95 days** | OVERDUE (180d > 180d) |
| Kevin Park | Operations | Billing | High | OK | OK | — | OVERDUE (195d > 180d) |

## MFA Missing (Immediate Action Required)

1. **Sarah Chen** — Production access, MFA not enabled. **High risk.** Block production access until MFA is configured (today).
2. **New Hire 2** — Standard access, MFA and SSO not set up. Send onboarding completion reminder with 48-hour deadline.

## SSO Not Enrolled

1. **New Hire 2** — Not enrolled in SSO. Complete as part of onboarding.
2. **External Contractor** — Not enrolled in SSO; using direct credentials. Enforce SSO enrollment or suspend access.

## Stale Accounts

1. **External Contractor** — 95 days since last login. Verify whether engagement is still active; if not, deprovision immediately.

## Privileged Access Reviews Overdue

| User | Access Level | Days Since Review | Review Required Every |
|---|---|---|---|
| Marcus Webb | Production | 200 days | 180 days |
| Kevin Park | Billing | 195 days | 180 days |
| External Contractor | Staging | 180 days | 180 days |

**Action:** Schedule access reviews for all three users this week. Document review outcomes for SOC 2 evidence.

## Remediation Priority

| Priority | Action | Owner | Deadline |
|---|---|---|---|
| P0 | Enable MFA for Sarah Chen — production access | Sarah Chen + IT | Today |
| P1 | Verify External Contractor engagement status | Manager + IT | 48 hours |
| P1 | Complete SSO and MFA for New Hire 2 | New Hire 2 + IT | 48 hours |
| P2 | Enroll External Contractor in SSO | IT | This week |
| P2 | Access review: Marcus Webb (Production) | IT + CTO | This week |
| P2 | Access review: Kevin Park (Billing) | IT + CFO | This week |
| P3 | Access review: External Contractor | IT + CTO | This week |

## SOC 2 Readiness Note

Current IAM posture (33% compliant) is below the 90% threshold typically expected for SOC 2 Type II audit evidence. Resolve P0/P1 issues immediately and conduct all overdue access reviews before Q3 audit window opens.
