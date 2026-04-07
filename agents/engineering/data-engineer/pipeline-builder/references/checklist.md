# Checklist: Data Pipeline Build

Comprehensive checklist for implementing production-grade data pipelines covering extraction, transformation, orchestration, testing, and deployment. Aligned with Lambda/Kappa architecture patterns and modern orchestration practices (Airflow, Dagster, Prefect).

## How to Use

Work through each section in sequence. Mark items `[x]` when verified. Items marked `[REQUIRED]` are non-negotiable for production pipelines. Items marked `[RECOMMENDED]` are best practices that prevent common operational failures.

---

## Section 1: Environment Setup

- [ ] `[REQUIRED]` Development environment provisioned with all required connectors and credentials
- [ ] `[REQUIRED]` Connectivity to all source systems verified in dev environment (not just assumed)
- [ ] `[REQUIRED]` Connectivity to all target systems (warehouse, data lake) verified
- [ ] `[REQUIRED]` Target sandbox schemas created in development/staging warehouse
- [ ] `[REQUIRED]` Secrets stored in secrets manager — no credentials in code, config files, or environment variables committed to version control
- [ ] `[RECOMMENDED]` Docker/container environment used for reproducibility across dev, staging, and production

---

## Section 2: Extraction Implementation

- [ ] `[REQUIRED]` Incremental extraction strategy implemented (CDC, watermark columns, or cursor-based — NOT full table scan on every run)
- [ ] `[REQUIRED]` Pagination handling implemented for API sources (handle all page sizes and edge cases)
- [ ] `[REQUIRED]` Rate limit handling implemented: exponential backoff with jitter on 429 responses
- [ ] `[REQUIRED]` Connection timeout and retry logic implemented with maximum retry count
- [ ] `[REQUIRED]` Source schema validation: fail-fast if upstream schema changes break the expected contract
- [ ] `[REQUIRED]` Unit tests written for extraction logic with mocked API responses
- [ ] `[RECOMMENDED]` Delta/checkpoint state persisted so pipeline can resume from last successful position after failure
- [ ] `[RECOMMENDED]` Source extraction rate monitored and logged for performance visibility

---

## Section 3: Transformation Implementation

- [ ] `[REQUIRED]` Transformation logic matches the source-to-target mapping specification exactly
- [ ] `[REQUIRED]` Idempotent upsert semantics implemented: re-running the transformation produces the same result (no duplicate rows)
- [ ] `[REQUIRED]` NULL handling defined for all nullable source fields
- [ ] `[REQUIRED]` Data type casting validated: no silent truncation or precision loss
- [ ] `[REQUIRED]` Business logic transformations unit tested with representative test fixtures
- [ ] `[REQUIRED]` dbt models (if used) have schema tests: `not_null`, `unique`, `accepted_values` for critical columns
- [ ] `[RECOMMENDED]` Transformation written as SQL (dbt) or Spark — avoid row-by-row Python loops for large datasets
- [ ] `[RECOMMENDED]` Soft deletes handled: deleted source records marked as inactive rather than physically deleted in target

---

## Section 4: Orchestration Wiring

- [ ] `[REQUIRED]` DAG defined in the orchestrator (Airflow, Dagster, or Prefect) with explicit task dependencies
- [ ] `[REQUIRED]` Retry policy configured per task: max 3 retries with exponential backoff
- [ ] `[REQUIRED]` Timeout limit configured per task and per DAG run
- [ ] `[REQUIRED]` SLA monitor configured: alert if pipeline does not complete within freshness SLA window
- [ ] `[REQUIRED]` Trigger schedule documented and reviewed: cron expression matches business freshness requirement
- [ ] `[REQUIRED]` Backfill behavior defined and tested: can the pipeline re-process historical date ranges?
- [ ] `[RECOMMENDED]` DAG tagged with owner, data domain, and SLA tier for operational triage
- [ ] `[RECOMMENDED]` Sensor tasks used to check source availability before extraction begins
- [ ] `[RECOMMENDED]` Concurrency limits configured to prevent resource exhaustion on parallel runs

---

## Section 5: Integration Testing

- [ ] `[REQUIRED]` Full end-to-end pipeline run completed in staging against representative data
- [ ] `[REQUIRED]` Row count validation: target table row count matches expected count from source
- [ ] `[REQUIRED]` Schema conformance validated: all columns present, correct types, no unexpected nulls
- [ ] `[REQUIRED]` Idempotency test: pipeline re-run produces identical results (same row counts, same values)
- [ ] `[REQUIRED]` Incremental extraction test: only new/modified records since last run are processed
- [ ] `[REQUIRED]` Failure recovery test: pipeline interrupted mid-run resumes correctly from checkpoint
- [ ] `[RECOMMENDED]` Data freshness validated: target data reflects source data within freshness SLA
- [ ] `[RECOMMENDED]` Performance test: pipeline completes within 80% of SLA time window under realistic data volume

---

## Section 6: Deployment

- [ ] `[REQUIRED]` Pipeline deployed using blue-green or shadow deployment (old pipeline runs in parallel until new one is verified)
- [ ] `[REQUIRED]` Monitoring hooks enabled: pipeline metrics (duration, row counts, error rates) sent to monitoring backend
- [ ] `[REQUIRED]` Alerting configured: notify on-call data engineer on DAG failure or SLA breach
- [ ] `[REQUIRED]` Runbook documented: steps to investigate and recover from each failure type
- [ ] `[REQUIRED]` Old pipeline decommissioned only after new pipeline has run successfully for ≥ 3 consecutive cycles
- [ ] `[RECOMMENDED]` Pipeline configuration stored as code (DAG definition + secrets reference) — not manual orchestrator UI configuration

---

## Pipeline Completion Sign-Off

| Section | Status | Evidence | Reviewer |
|---------|--------|----------|---------|
| 1. Environment Setup | [ ] Complete / [ ] Partial | | |
| 2. Extraction | [ ] Complete / [ ] Partial | | |
| 3. Transformation | [ ] Complete / [ ] Partial | | |
| 4. Orchestration | [ ] Complete / [ ] Partial | | |
| 5. Integration Testing | [ ] Complete / [ ] Partial | | |
| 6. Deployment | [ ] Complete / [ ] Partial | | |

**Pipeline Status**: `[ ] PRODUCTION DEPLOYED` `[ ] PARTIAL — see remediation` `[ ] FAILED — needs rework`

**Data Engineer**: _________________________ Date: _________
