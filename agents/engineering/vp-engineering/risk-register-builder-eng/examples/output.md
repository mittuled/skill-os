# Engineering Risk Register — Real-Time Data Pipeline Migration

| Field | Value |
|---|---|
| Date | 2026-03-31 |
| Author | VP Engineering |
| Version | 1.0 |
| Phase | Phase 1 — Core Streaming Infrastructure |
| Next Review | 2026-04-30 |
| Skill | risk-register-builder-eng |

## Executive Summary

Phase 1 risk register identifies 4 risks: 1 critical, 2 high, 1 medium. The critical risk (downstream consumer breakage) and key engineer availability risk are the primary threats to Phase 1 delivery. Both have mitigation plans in place with assigned owners. Register must be reviewed at the April 30 phase boundary.

---

## Risk Summary

| Level | Count |
|---|---|
| Critical | 1 |
| High | 2 |
| Medium | 1 |
| Low / Minimal | 0 |
| **Total** | **4** |

---

## Risk Register

| ID | Description | Category | Likelihood | Impact | Score | Level | Strategy | Owner | Status | Resolution Date |
|---|---|---|---|---|---|---|---|---|---|---|
| RISK-002 | Downstream consumers break from real-time migration | External | High | Critical | 12 | CRITICAL | Reduce | Tech Lead | Open | 2026-05-15 |
| RISK-004 | Key engineer on leave during Phase 1 critical path | Resource | High | High | 9 | HIGH | Reduce | Engineering Manager | Open | 2026-04-05 |
| RISK-001 | Team lacks Kafka operational experience | Technical | Medium | High | 6 | HIGH | Reduce | Staff Engineer | Open | 2026-04-07 |
| RISK-003 | Infrastructure cost overrun from partition misconfiguration | Operational | Low | Medium | 2 | MINIMAL | Reduce | DevOps Engineer | Open | 2026-04-21 |

---

## Risk Detail

### RISK-002 — Downstream Consumer Breakage (CRITICAL)

**Description:** All downstream consumers depend on batch data ingestion schedule. Migration to real-time streaming changes the data contract without a grace period, potentially breaking 12+ consuming services.

**Mitigation:** Run dual-write mode for 4 weeks post-migration — batch pipeline continues alongside streaming pipeline. All consumer teams notified with 6-week lead time with migration guide and test environment access.

**Owner:** Tech Lead
**Resolution Date:** 2026-05-15 (after dual-write validation period)
**Status:** OPEN — notification to consumer teams must go out by 2026-04-04

---

### RISK-004 — Key Engineer Availability (HIGH)

**Description:** The engineer with primary Kafka implementation ownership is on approved leave for 3 weeks starting 2026-04-14 — overlapping with Phase 1 critical path.

**Mitigation:** Cross-train backup engineer on all critical Kafka configuration decisions. Require documentation of all implementation decisions before leave begins (2026-04-11 deadline).

**Owner:** Engineering Manager
**Resolution Date:** 2026-04-05 (cross-training schedule confirmed)
**Status:** OPEN — backup engineer not yet assigned

---

### RISK-001 — Limited Kafka Operational Experience (HIGH)

**Description:** No team member has operated a production Kafka cluster at scale. Incident response time may be 3–5x longer than expected if cluster issues arise.

**Mitigation:** 2-day Kafka operations training workshop scheduled for 2026-04-07. Contractor with 3+ years Kafka production experience engaged to pair on implementation.

**Owner:** Staff Engineer
**Resolution Date:** 2026-04-07 (post-training)
**Status:** OPEN

---

### RISK-003 — Infrastructure Cost Overrun (MINIMAL)

**Description:** Kafka partition count misconfiguration could lead to over-provisioning and budget overrun.

**Mitigation:** Load test at 3x expected peak before production cutover. Budget alerts at 80% of allocation in cloud console.

**Owner:** DevOps Engineer
**Resolution Date:** 2026-04-21
**Status:** OPEN — low priority

---

## Maintenance Schedule

| Trigger | Action |
|---|---|
| Phase boundary (2026-04-30) | Full register review; close resolved risks, add new ones |
| After any P1/P2 incident | Add incident-identified risks within 24h of resolution |
| Scope change > 20% | Immediate risk re-assessment |
| Risk status change | Owner updates status field in register |
