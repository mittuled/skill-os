# Instrumentation Plan: MVP Product Launch

| Field | Value |
|-------|-------|
| Date | 2026-03-31 |
| Analytics Lead | Analytics Lead |
| Plan | MVP Product Launch Instrumentation Plan |
| SDK | Segment |
| Platforms | Web + Server |
| Total Events | 30 |
| Total Estimate | 22 days |
| Skill | instrumentation-planner-data |

## SDK Selection

| Attribute | Value |
|-----------|-------|
| SDK | Segment |
| Best for | Multi-destination event routing |
| Strengths | Unified customer data platform; 300+ integrations |

## Routing Architecture

| Layer | Implementation |
|-------|---------------|
| Client to SDK | Segment SDK on web, server |
| SDK to Warehouse | Event stream → S3/GCS → BigQuery via Segment connector |
| Identity Resolution | Anonymous ID → User ID on login/signup; server-side identity calls |

## Rollout Phases

| Phase | Name | Days | Description |
|-------|------|------|-------------|
| 1 | Foundation | 3 | SDK installation, identity, and session setup |
| 2 | Core Events | 6 | High-priority events for primary user journeys (~12 events) |
| 3 | Feature Events | 10 | Feature-specific event instrumentation (~18 events) |
| 4 | QA and Validation | 4 | Verify data quality in staging and production |
| **Total** | | **23 days** | |

## Sequencing Notes

1. Always instrument server-side events before client-side for critical business events (payments, signups) — server-side events cannot be blocked by ad blockers
2. Deploy to staging first; run QA validation against spec before production rollout
3. Backfill historical events is not possible — start instrumentation before the feature launches, not after

## Phase 1 Checklist: Foundation

- [ ] Install Segment analytics.js on all web pages
- [ ] Install Segment Node.js SDK on server
- [ ] Implement anonymous ID generation and persistence
- [ ] Implement identify() call on user login and signup
- [ ] Implement session tracking
- [ ] Validate events reach Segment debugger before proceeding to Phase 2
