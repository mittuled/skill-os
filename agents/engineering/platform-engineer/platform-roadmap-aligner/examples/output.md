# Platform Roadmap Alignment — Meridian AI Q2 2026

| Field | Value |
|---|---|
| Team | Meridian AI Engineering |
| Planning Period | Q2 2026 |
| Product Items Reviewed | 4 |
| Platform Items | 4 |
| Conflicts (Platform Misses Product) | 2 |
| At Risk | 0 |
| Skill | platform-roadmap-aligner |

## Alignment Summary

| Product Feature | Target Sprint | Platform Deps | Has Conflict | Risk |
|---|---|---|---|---|
| Multi-tenant workspace support | Q2-S3 | PLAT-101, PLAT-102 | YES (PLAT-102) | HIGH |
| AI workflow v2 — streaming responses | Q2-S1 | PLAT-103 | YES (PLAT-103) | HIGH |
| Compliance report exporter | Q2-S2 | None | No | LOW |
| Real-time collaboration (beta) | Q2-S4 | PLAT-104 | No | MEDIUM |

## Conflicts (Platform Delivers After Product Needs It)

### Conflict 1: AI Workflow v2 Streaming — CRITICAL
**Product feature:** PROD-202 — AI workflow v2 (streaming responses) | Target: **Q2-S1**
**Platform dependency:** PLAT-103 — WebSocket support at API gateway | Delivers: **Q2-S2**

**Gap:** Product team needs WebSocket support in Sprint 1 but platform delivers in Sprint 2.
**Impact:** Squad Nova cannot ship streaming responses in Q2-S1 without WebSocket support. Either the feature slips to Q2-S2 or platform must expedite.

**Options:**
1. Platform team accelerates PLAT-103 to Q2-S1 (is this achievable in 2-week sprint?)
2. Product team scopes a non-streaming v2 for Q2-S1 and adds streaming in Q2-S2 patch
3. Accept Q2-S2 as the ship date for streaming feature

---

### Conflict 2: Multi-Tenant Workspace — Row-Level Security (PLAT-102)
**Product feature:** PROD-201 — Multi-tenant workspace | Target: **Q2-S3**
**Platform dependency (partial):** PLAT-102 — Row-level security | Delivers: **Q2-S4**

**Gap:** Product needs row-level security in Sprint 3; platform delivers in Sprint 4.
**Note:** PLAT-101 (SSO tenant isolation) delivers Q2-S2 and is on time.

**Options:**
1. Scope Q2-S3 multi-tenant to SSO isolation only (PLAT-101); defer RLS to Q2-S4 patch
2. Platform team prioritizes PLAT-102 to Q2-S3 (requires scope reduction elsewhere)
3. Product team launches multi-tenant without RLS and adds a feature flag gate for customers until RLS ships

## No Conflict Items

### Compliance Report Exporter (PROD-203)
No platform dependencies. Fully self-contained. Ship Q2-S2 as planned.

### Real-Time Collaboration Beta (PROD-204)
PLAT-104 (event bus) delivers Q2-S3, one sprint before PROD-204 needs it in Q2-S4. **On track.** Note: platform team is still deciding between Kafka and EventBridge — product team should be consulted on the decision as it may affect the beta API surface.

## Recommended Actions

| Priority | Action | Owner | Deadline |
|---|---|---|---|
| P0 | Discuss PLAT-103 acceleration with platform team — can WebSocket support land Q2-S1? | CTO + Platform | This week |
| P0 | Product team to define scope fallback for streaming (non-streaming v2 for Q2-S1) | Squad Nova CPM | This week |
| P1 | Decide whether to launch multi-tenant in Q2-S3 with SSO only or wait for RLS | Product + Platform | Sprint planning |
| P2 | Decide Kafka vs. EventBridge for PLAT-104 — loop in Squad Nova | Platform + Nova | Next sprint |
