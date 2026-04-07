# Go-Live Decision — Payments v2 Billing Model Migration

| Field | Value |
|---|---|
| Date | 2026-03-31 |
| Author | VP Engineering |
| Version | 1.0 |
| Status | BLOCKED — critical risk unmitigated |
| Skill | go-live-approver-lead |

## Executive Summary

Payments v2 go-live is **BLOCKED**. The release has two unresolved blockers: an unmitigated critical risk (RISK-018: migration script not dry-run in production) and a missing on-call rotation. Quality gates are substantially met but test coverage is below threshold. The release cannot proceed until RISK-018 is mitigated and on-call is confirmed.

---

## Go-Live Decision

**BLOCKED**

**Rationale:** Blocking criteria not met: (1) Unmitigated critical risk RISK-018 — migration script not dry-run in production environment; (2) On-call rotation not staffed for a payments release.

**Approved by:** VP Engineering
**Decision Date:** 2026-03-31

---

## Quality Gate Status

| Gate | Status |
|---|---|
| Tech Lead Approval Complete | PASSED |
| CI/CD Pipeline Green | PASSED |
| No Open P0/P1 Bugs | PASSED |
| Regression Suite Passed | PASSED |
| Test Coverage Meets Threshold | **FAILED** |

**4/5 quality gates passed.** Test coverage gap is a concern but not a standalone blocker if RISK-018 is resolved and coverage is tracked as a post-launch item.

---

## Operational Readiness

| Check | Status |
|---|---|
| Runbooks Exist | READY |
| Alerting Configured to SLOs | READY |
| Rollback Procedure Documented and Tested | READY |
| On-Call Rotation Staffed | **NOT READY** |

**3/4 operational checks ready.** Missing on-call rotation for a payments release is a hard blocker — billing incidents require an available engineer within 15 minutes.

---

## Risk Assessment

### RISK-014 — Stripe Webhook Retry Under Load (HIGH)
**Status: MITIGATED / ACCEPTED**
Idempotency keys implemented and rate limiter in place. Accepted risk. No blocking action required.

### RISK-018 — Migration Script Not Dry-Run in Production (CRITICAL)
**Status: UNMITIGATED / NOT ACCEPTED — BLOCKING**
The legacy billing records migration script has not been executed in the production environment. A failed migration on live billing data could corrupt active customer records and create regulatory exposure. This release cannot proceed until the script has been successfully dry-run in production.

**Resolution required:** Execute migration script in production with `--dry-run` flag and review output for errors. VP Engineering must confirm results before release is re-submitted.

---

## Path to Approval

To convert this decision from BLOCKED to APPROVED:

| Action | Owner | Deadline |
|---|---|---|
| Dry-run migration script in production environment and review output | Tech Lead (Payments) | 2026-04-01 |
| Confirm on-call rotation is staffed for release window | Engineering Manager | 2026-04-01 |
| Resolve test coverage gap (minimum 80%) | Sr. Backend Developer | 2026-04-02 |

**Re-review:** Submit updated checklist after above items are resolved. VP Engineering will complete re-review within 4 hours of resubmission.
