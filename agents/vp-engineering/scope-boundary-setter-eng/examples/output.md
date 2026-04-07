# Scope Boundary Document — Notification System Overhaul v2

| Field | Value |
|---|---|
| Date | 2026-03-31 |
| Author | VP Engineering |
| Version | 1.0 |
| Status | Active — 1 change request pending |
| Skill | scope-boundary-setter-eng |

## Scope Boundary Definition

### In Scope

1. Replace legacy pub/sub library with Kafka-based event bus
2. Email and in-app notification delivery
3. Notification preferences UI (basic on/off per category)
4. Delivery status tracking (sent/delivered/read)

### Out of Scope

1. SMS and push notification channels
2. AI-based notification scheduling optimization
3. Multi-language notification templates
4. Analytics dashboard for notification performance

---

## Change Control Process

| Request Size | Approver | Timeline | Requirements |
|---|---|---|---|
| Minor | Tech Lead | 24 hours | No timeline adjustment |
| Medium | VP Engineering | 48 hours | Timeline impact assessment required |
| Major | VP Engineering + CTO | 1 week | Formal scope change document required |

---

## Change Request Log

### CHANGE-001 — Slack Notification Channel (PENDING)

**Requester:** VP Product
**Size:** Medium
**Description:** Add Slack notification channel for internal operational alerts
**Status:** PENDING REVIEW — VP Engineering approval required
**Impact assessment:** Completed
**Decision:** VP Engineering has not approved. Schedule review session with VP Product to evaluate: (1) is this critical path for any committed product milestone? (2) can Slack notifications be deferred to v3 without business impact? If deferral is not acceptable, a 1-sprint timeline extension must be negotiated.

### CHANGE-002 — Broken Unsubscribe Link Fix (APPROVED)

**Requester:** Legal
**Size:** Minor
**Description:** Fix broken unsubscribe link in current email templates
**Status:** APPROVED
**Decision:** Approved — this is a pre-existing compliance bug (GDPR/CAN-SPAM requirement), not a scope addition. Tech Lead to add to Sprint 1 backlog as a P1 bug fix. Zero timeline impact.

---

## Scope Health

**Status: 1 change request awaiting approval**

CHANGE-001 must be resolved (approved or deferred) before Sprint 2 planning. Recommend decision by 2026-04-03 to avoid planning uncertainty.
