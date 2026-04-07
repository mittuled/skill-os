# Architecture Review — Event-Driven Payment Processing (ADR-042)

| Field | Value |
|---|---|
| Date | 2026-03-31 |
| Author | VP Engineering |
| Version | 1.0 |
| Status | CHANGES REQUESTED |
| Skill | architecture-reviewer |

## Executive Summary

ADR-042 proposes migrating the monolithic payment processing service to an event-driven microservices architecture using Kafka. The scalability design is strong and the observability plan is partially complete. However, missing required elements (threat model and rollback strategy) cap the composite score at 70/100. The verdict is **CHANGES REQUESTED** — 4 action items must be resolved before implementation begins.

---

## Review Verdict

**CHANGES REQUESTED — Architecture requires targeted improvements before approval**

Composite Score: **68.6 / 100** (capped at 70 due to missing required elements: threat_model, rollback_strategy)

The architecture's core Kafka-based design is sound. The implementation cannot begin until the rollback strategy for the 3-phase data migration and the threat model are submitted and reviewed.

---

## Criterion Scores

| Criterion | Score | Weight | Contribution | Assessment |
|---|---|---|---|---|
| Structural Soundness | 72 | 30% | 21.6 | Boundaries clear; consumer group isolation underspecified |
| Scalability | 85 | 25% | 21.3 | Kafka partition model supports 10x load with headroom |
| Standards Alignment | 68 | 25% | 17.0 | Observability partial; no threat model; tracing missing |
| Operational Risk | 55 | 20% | 11.0 | No rollback strategy; no on-call runbooks for consumer lag |
| **Total** | — | **100%** | **70.9 → capped at 68.6** | |

**Score capped at 70 due to 2 missing required elements:**
- `threat_model` — not submitted
- `rollback_strategy` — not documented

---

## Detailed Findings

### Structural Soundness (72/100)

The component boundaries between the payment orchestrator, ledger service, and notification service are well-defined. The failure domain design correctly isolates payment failures from notification failures using separate consumer groups.

**Finding:** Consumer group ownership is not documented. Multiple services reading from the same topic without defined partition ownership creates a latent race condition risk during partition rebalancing. Document a partition ownership registry before implementation.

### Scalability (85/100)

The Kafka partition model correctly anticipates 10x current load with documented headroom. Consumer group horizontal scaling is idiomatic and consistent with the tech radar. Capacity projections are present and credible.

**No blocking issues.** Minor recommendation: add a periodic partition rebalancing simulation to the load test suite.

### Standards Alignment (68/100)

Structured logging (JSON) and Prometheus metrics are specified correctly. **Missing:** distributed tracing integration — OpenTelemetry instrumentation must be specified per the observability standard. **Critical missing element:** no threat model has been submitted. Payment processing requires a documented threat model before architecture approval.

### Operational Risk (55/100)

**Critical gap:** The 3-phase data migration has no rollback strategy documented. If Phase 2 (dual-write) fails, the recovery path is undefined. This is a blocking risk for a payments system where data loss has regulatory consequences.

**Missing:** On-call runbooks for consumer lag, dead-letter queue monitoring, and partition leader failures. The team cannot go on-call for this system without runbooks.

---

## Required Action Items

| # | Action | Owner | Blocking |
|---|---|---|---|
| 1 | Submit threat model for payment processing attack surface | Security Engineer | YES |
| 2 | Document rollback strategy for each of the 3 migration phases | Tech Architect | YES |
| 3 | Specify OpenTelemetry distributed tracing integration | Sr. Backend Developer | YES |
| 4 | Write on-call runbooks: consumer lag, DLQ, partition leader failover | Sr. Backend Developer | NO |
| 5 | Document partition ownership and consumer group isolation policy | Tech Architect | NO |

**Blocking items (1–3) must be resolved before the VP Engineering issues final approval.**

---

## Re-Review Schedule

Submit updated ADR with action items 1–3 addressed by **2026-04-07**. Re-review will be completed within 48 hours of submission. Items 4–5 can be completed in parallel during implementation sprint Week 1.
