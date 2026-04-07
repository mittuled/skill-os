# Phase Plan — Search Infrastructure Rebuild

| Field | Value |
|---|---|
| Date | 2026-03-31 |
| Author | VP Engineering |
| Version | 1.0 |
| Status | Draft — pending milestone alignment |
| Skill | phase-planner-eng |

## Executive Summary

The Search Infrastructure Rebuild spans 2 phases across 5 sprints at 80% effective capacity (32 points/sprint). Phase 1 covers index architecture and runs 2 sprints (39 points). Phase 2 covers query layer migration and runs 2 sprints (27 points). Total timeline: approximately 10 weeks at 2-week sprints.

---

## Phase Summary

| Phase | Story Points | Sprints | Sprint Range | Critical Path Tasks |
|---|---|---|---|---|
| Phase 1 — Index Architecture | 39 | 2 | Sprints 1–2 | 4 of 5 tasks |
| Phase 2 — Query Layer Migration | 27 | 2 | Sprints 3–4 | 4 of 5 tasks |
| **Total** | **66** | **4** | | |

---

## Phase 1 — Index Architecture

**Entry criteria:** Architecture ADR approved by VP Engineering
**Exit criteria:** New index serving read traffic in staging with <200ms p95 latency
**Sprint range:** Sprints 1–2 (4 weeks)

### Sprint Allocation

| Task | Points | Critical Path |
|---|---|---|
| Design Elasticsearch cluster topology | 5 | YES |
| Provision staging index | 8 | YES |
| Implement indexing pipeline | 13 | YES |
| Write index health monitoring | 5 | No |
| Load test to 3x expected query volume | 8 | YES |

**Critical path:** Cluster design → Staging provision → Indexing pipeline → Load test. All 4 must complete for exit criteria.

**Phase risks:** Elasticsearch version compatibility with existing query DSL — evaluate in Sprint 1; resolve before indexing pipeline work begins.

---

## Phase 2 — Query Layer Migration

**Entry criteria:** Phase 1 exit criteria met; staging performance validated
**Exit criteria:** 100% of query traffic routing to new index in production with zero regression
**Sprint range:** Sprints 3–4 (4 weeks)

### Sprint Allocation

| Task | Points | Critical Path |
|---|---|---|
| Migrate query service to new client | 8 | YES |
| Implement dual-read shadow mode | 5 | YES |
| Validate result parity (old vs. new index) | 8 | YES |
| Cutover traffic with feature flag | 3 | YES |
| Decommission old index | 3 | No |

**Critical path:** Client migration → Shadow mode → Parity validation → Feature flag cutover. Decommission runs post-cutover.

**Phase risks:** Result parity gaps may require index re-configuration — build 3-point contingency buffer in Sprint 4.

---

## Assumptions

1. Sprint capacity set to 80% of total (32 points) to preserve unplanned-work buffer
2. All dependencies resolved before phase start unless noted in risk section
3. 2-week sprint cadence assumed; adjust sprint count for 1-week sprints

---

## Milestone Dates (at 2-week sprints)

| Milestone | Sprint | Target Date |
|---|---|---|
| Phase 1 kickoff | Sprint 1 | 2026-04-07 |
| Staging index live | Sprint 2 | 2026-05-02 |
| Phase 2 kickoff | Sprint 3 | 2026-05-05 |
| Production cutover | Sprint 4 | 2026-05-30 |
| Old index decommissioned | Sprint 5 (buffer) | 2026-06-13 |
