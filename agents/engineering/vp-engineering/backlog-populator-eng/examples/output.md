# Engineering Backlog — Webhook Delivery System

| Field | Value |
|---|---|
| Date | 2026-03-31 |
| Author | VP Engineering |
| Spec | PRD-2026-047 |
| Total Tasks | 5 |
| Total Points | 21 |
| Skill | backlog-populator-eng |

## Summary

5 tasks, 21 story points total. 3 tasks are on the critical path. 1 external blocker requires security team approval before HMAC implementation begins.

---

## Engineering Backlog

| Task ID | Title | Size | Points | Priority | Critical Path | Status |
|---|---|---|---|---|---|---|
| ENG-001 | Webhook endpoint registration API | M | 5 | P1-critical | YES | Ready |
| ENG-002 | Event fan-out queue worker | L | 8 | P1-critical | YES | Ready |
| ENG-004 | HMAC signature verification | S | 2 | P1-critical | YES | **Blocked** |
| ENG-003 | Webhook delivery logs API | M | 5 | P2-high | No | Ready |
| ENG-005 | Webhook admin UI | M | 5 | P3-medium | No | Ready |

---

## External Blockers

| Task | Blocker | Action Required |
|---|---|---|
| ENG-004 — HMAC signature verification | Security team must approve HMAC implementation approach | Schedule security review before Sprint 1; target 2026-04-03 |

---

## Task Detail

### ENG-001 — Webhook Endpoint Registration API
**Priority:** P1-critical | **Critical Path:** Yes | **Points:** 5
**Acceptance Criteria:** POST /webhooks creates a registration, returns 201 with id; duplicate URL returns 409
**Dependencies:** None
**Spec:** PRD-2026-047

### ENG-002 — Event Fan-Out Queue Worker
**Priority:** P1-critical | **Critical Path:** Yes | **Points:** 8
**Acceptance Criteria:** Worker dequeues events, delivers to all registered endpoints within 5 seconds of event, retries up to 3 times on failure
**Dependencies:** ENG-001 (registration API must be complete before worker can route events)
**Spec:** PRD-2026-047

### ENG-004 — HMAC Signature Verification
**Priority:** P1-critical | **Critical Path:** Yes | **Points:** 2
**Acceptance Criteria:** All outgoing webhooks include X-Signature header signed with customer secret; verification guide in docs
**External Blocker:** Security team approval required
**Spec:** PRD-2026-047

### ENG-003 — Webhook Delivery Logs API
**Priority:** P2-high | **Critical Path:** No | **Points:** 5
**Acceptance Criteria:** GET /webhooks/:id/deliveries returns last 100 attempts with status, timestamp, and response code
**Dependencies:** ENG-002 (requires delivery records to exist)
**Spec:** PRD-2026-047

### ENG-005 — Webhook Admin UI
**Priority:** P3-medium | **Critical Path:** No | **Points:** 5
**Acceptance Criteria:** Dashboard lists all registrations with endpoint URL and status; allows delete with confirmation
**Dependencies:** ENG-001
**Spec:** PRD-2026-047

---

## Warnings

- ENG-004 has an external blocker — resolve security team approval before Sprint 1 planning to avoid blocking critical path
