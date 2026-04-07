# Scoring Rubric: pipeline-reliability-tester

Evaluates the reliability of a data pipeline under failure conditions, covering idempotency, fault recovery, data consistency, and SLA compliance under load.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Idempotency | 30% | Re-running the pipeline with identical input produces identical output with no duplicates and no missing records |
| 2 | Fault Recovery | 30% | Pipeline recovers correctly from injected failures (source unavailability, network partition, schema drift, partial writes) |
| 3 | Data Consistency | 25% | Referential integrity between tables is maintained after recovery; row counts match source after any failure mode |
| 4 | SLA Compliance Under Load | 15% | Pipeline completes within the defined SLA window when run against peak-volume data |
| **Total** | | **100%** | |

## Scale

Each criterion is scored **0–10**:
- **0**: No evidence / completely absent
- **5**: Partially present with significant gaps
- **10**: Fully present, comprehensive, no gaps

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 – 10.0 | Production-ready | Fully idempotent; recovers from all cataloged failure modes; data consistent post-recovery; SLA met at 3× peak volume | Approve for production deployment |
| A | 8.0 – 8.9 | Ready with monitoring | Idempotent; recovers from all critical failure modes; 1 edge case with manual intervention needed; SLA met at 2× peak | Deploy with enhanced alerting on the edge case |
| B | 7.0 – 7.9 | Conditionally ready | Idempotent; 1 non-critical fault mode requires manual restart; data consistent after recovery; SLA meets at 1.5× peak | Document manual recovery procedure; deploy with caution; fix fault mode in next sprint |
| C | 5.0 – 6.9 | Not production-ready | Duplicate rows detected on re-run; 1–2 fault modes cause data corruption; SLA breached at 1.5× peak | Block production deployment; significant reliability work required |
| D | 3.0 – 4.9 | Significant failures | Multiple idempotency failures; majority of fault modes cause pipeline to hang or produce corrupt data | Architectural rework required before production promotion |
| F | 0.0 – 2.9 | Critical failures | Pipeline produces different results on identical re-runs; catastrophic data loss on fault injection; SLA breached even at baseline volume | Do not promote; complete re-implementation of reliability mechanisms required |

## Signal Tables

### Idempotency

| Score | Evidence |
|-------|----------|
| 9–10 | Pipeline run twice with same date parameter: row counts identical, no duplicate primary keys, all aggregates (sum, count, distinct) match to 100% precision |
| 7–8 | Idempotent for full re-runs; 1 edge case (e.g., late-arriving records in a 5-minute window) produces minor variance documented and bounded to <0.01% |
| 5–6 | Idempotent for clean re-runs; non-idempotent when source data changes between runs (expected behavior but not handled with a version/snapshot strategy) |
| 3–4 | Re-run with identical input produces 1–5% duplicate rows; no deduplication logic at load step; duplicate detection only present as a downstream fix |
| 0–2 | Re-run produces a meaningfully different result (>5% row count difference); no idempotency mechanism exists; each run appends without deduplication |

### Fault Recovery

| Score | Evidence |
|-------|----------|
| 9–10 | All cataloged failures tested: source killed mid-run → pipeline retries and completes; bad record injected → pipeline quarantines bad record and continues; schema column added → pipeline handles gracefully with no failure |
| 7–8 | All P0/P1 failures tested and recovered automatically; 1 P2 failure (e.g., rare schema drift scenario) requires manual restart, documented in runbook |
| 5–6 | Network partition and source unavailability tested; schema drift not tested; partial write scenario untested; 2+ fault modes require manual intervention |
| 3–4 | Only source unavailability tested (happy-path fault); schema drift causes pipeline to fail with unhandled exception; partial write scenario produces duplicates |
| 0–2 | No fault injection testing performed; "testing" consists only of a successful end-to-end run with clean data; no recovery mechanism documented |

### Data Consistency

| Score | Evidence |
|-------|----------|
| 9–10 | Post-recovery: zero orphaned foreign keys; row counts in target match source reconciliation within 0.01%; no referential integrity violations; all downstream tables consistent |
| 7–8 | Post-recovery: <5 orphaned FK rows (late-arriving data pattern); row count delta < 0.1%; consistency verified with automated assertions |
| 5–6 | Post-recovery: row counts match but 1 table has orphaned FKs that resolve on next full sync; no automated consistency check implemented |
| 3–4 | Post-recovery: row count discrepancy 1–5% between source and target; referential integrity violations present; requires manual SQL repair |
| 0–2 | Post-recovery: significant data loss or corruption; row count discrepancy >5%; referential integrity violations across multiple tables; manual repair infeasible |

### SLA Compliance Under Load

| Score | Evidence |
|-------|----------|
| 9–10 | Pipeline completes within SLA window at 3× current peak volume; no OOM errors; no task timeouts; P99 duration < SLA window |
| 7–8 | Completes within SLA at 2× peak volume; 1 task approaches timeout limit at 2× but does not breach; P95 duration < SLA |
| 5–6 | Completes within SLA at 1.5× peak; 1 task times out at 2× requiring a configuration change; P95 at SLA boundary |
| 3–4 | Completes within SLA at current volume only; 1.5× peak causes SLA breach; scaling bottleneck identified but not addressed |
| 0–2 | SLA breached at current volume; pipeline not tested under any load condition above baseline |
