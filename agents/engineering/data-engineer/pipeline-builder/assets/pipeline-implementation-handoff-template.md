# Pipeline Implementation Handoff

**Pipeline Name:** [PIPELINE NAME]
**Design Document:** [LINK TO DESIGN DOC]
**Implementation Completed:** [DATE]
**Implemented By:** [DATA ENGINEER NAME]
**Reviewed By:** [TECH LEAD / PEER NAME]
**Environment:** Production
**Orchestrator:** [Airflow / Dagster / Prefect]

---

## Overview

| Attribute | Value |
|---|---|
| Source systems | [SOURCE 1], [SOURCE 2] |
| Target system | [DATA WAREHOUSE / DATABASE] |
| Target schema | `[SCHEMA].[TABLE]` |
| Extraction mode | Full / Incremental (CDC / Watermark / Cursor) |
| Trigger schedule | `[CRON EXPRESSION]` — e.g., `0 3 * * *` (daily at 03:00 UTC) |
| SLA — completion by | [HH:MM UTC] |
| DAG ID | `[DAG_ID]` |
| Repository path | `[REPO_PATH]` |

---

## 1. Environment and Connectivity

### Credentials and Secrets

| Secret | Storage Location | Access Method | Rotated By |
|---|---|---|---|
| [SOURCE 1] API key | [Vault / AWS Secrets Manager / GCP Secret Manager] | Environment variable `[VAR_NAME]` | [OWNER] |
| [DATABASE] password | [Vault / AWS Secrets Manager / GCP Secret Manager] | Environment variable `[VAR_NAME]` | [OWNER] |
| [SERVICE ACCOUNT] | [Vault / GCP IAM] | Mounted credential file | [OWNER] |

### Target Sandbox Schema (Staging)

- Staging schema: `[SCHEMA_STAGING].[TABLE]`
- Staging warehouse: `[WAREHOUSE / PROJECT]`
- Teardown required after: [DATE] / Not required

---

## 2. Extraction Implementation

### Connector Details

| Source | Connector Type | Library / Version | Pagination Strategy | Rate Limit Handling |
|---|---|---|---|---|
| [SOURCE 1] | REST / JDBC / File / CDC | [library] v[X.Y.Z] | Cursor / Offset / Token | Exponential backoff, max [N] retries |
| [SOURCE 2] | REST / JDBC / File / CDC | [library] v[X.Y.Z] | Cursor / Offset / Token | Exponential backoff, max [N] retries |

### Incremental Strategy

- **Mode:** [CDC / Watermark column / Cursor-based / Full load]
- **Watermark column:** `[TABLE].[COLUMN]` (e.g., `updated_at`)
- **State storage:** [Airflow XCom / Dagster IO Manager / Redis / DynamoDB]
- **Backfill procedure:** `[COMMAND OR RUNBOOK LINK]`

### Unit Test Coverage

| Module | Test File | Scenarios Covered |
|---|---|---|
| `[extractor_module].py` | `tests/test_[extractor].py` | Auth failure, rate limit retry, empty response, pagination |
| `[connector_module].py` | `tests/test_[connector].py` | Connection timeout, schema mismatch, partial response |

---

## 3. Transformation Implementation

### Source-to-Target Mapping Summary

| Source Column | Source Table | Target Column | Target Table | Transform Logic |
|---|---|---|---|---|
| `[src_col_1]` | `[src_table]` | `[tgt_col_1]` | `[tgt_table]` | Direct copy |
| `[src_col_2]` | `[src_table]` | `[tgt_col_2]` | `[tgt_table]` | `COALESCE([src_col_2], 'UNKNOWN')` |
| `[src_col_3]` | `[src_table]` | `[tgt_col_3]` | `[tgt_table]` | `CAST(... AS TIMESTAMP)` |
| _(derived)_ | — | `[derived_col]` | `[tgt_table]` | `[src_a] / [src_b]` |

### Idempotency Approach

- **Upsert key:** `[PRIMARY_KEY_COLUMN(S)]`
- **Upsert strategy:** MERGE / DELETE+INSERT / INSERT OVERWRITE partition
- **Idempotency verified:** Yes — re-run produces identical output (see integration test results)

### Test Fixtures

- Fixture location: `tests/fixtures/[pipeline_name]/`
- Fixture description: [N] representative input records covering happy path, nulls, type edge cases, and schema drift simulation.

---

## 4. Orchestration Configuration

### DAG Summary

| Property | Value |
|---|---|
| DAG ID | `[DAG_ID]` |
| Schedule | `[CRON]` |
| Start date | [DATE] |
| Catchup | False / True |
| Max active runs | [N] |
| Default retries | [N] |
| Retry delay | [X] minutes |
| Timeout (task) | [X] minutes |
| SLA miss callback | `[CALLBACK_FUNCTION]` |

### Task Dependency Graph

```
[extract_source_1] ──┐
                      ├──▶ [validate_raw] ──▶ [transform] ──▶ [load_target] ──▶ [notify_success]
[extract_source_2] ──┘
```

### Monitoring Hooks

- SLA miss alert: Slack `#[CHANNEL]` + PagerDuty `[SERVICE_NAME]`
- Task failure alert: Slack `#[CHANNEL]`
- Data quality gate: Integrated at `[validate_raw]` task — fails DAG on threshold breach

---

## 5. Integration Test Results

**Test run date:** [DATE]
**Environment:** Staging
**Dataset:** [Description of staging dataset used]

| Test Scenario | Expected | Actual | Result |
|---|---|---|---|
| Full pipeline end-to-end | [N] rows loaded | [N] rows | ✅ Pass / ❌ Fail |
| Schema conformance | All columns present, correct types | [ACTUAL] | ✅ Pass / ❌ Fail |
| Idempotency (re-run) | Identical row count, no duplicates | [ACTUAL] | ✅ Pass / ❌ Fail |
| Source 1 timeout simulation | Pipeline retries and completes | [ACTUAL] | ✅ Pass / ❌ Fail |
| Empty source response | No rows loaded, no failure | [ACTUAL] | ✅ Pass / ❌ Fail |
| Row count source vs target | Counts match ±0.1% | [ACTUAL] | ✅ Pass / ❌ Fail |

**Overall integration test result:** ✅ All passing / ❌ [N] failures — see notes below

**Failure notes:** [DESCRIPTION OF ANY FAILURES AND RESOLUTION]

---

## 6. Deployment

- **Deployment method:** Blue-green / Shadow / Direct promotion
- **Deployed at:** [DATETIME UTC]
- **Promoted by:** [NAME]
- **First production run:** [DATETIME UTC]
- **First production run result:** ✅ Success / ❌ Failure

### Monitoring Active

- [ ] DAG visible in orchestrator UI
- [ ] SLA alerts wired and tested
- [ ] Data quality checks integrated and running
- [ ] Runbook published at [LINK]
- [ ] On-call rotation updated with pipeline ownership

---

## 7. Handoff Checklist

- [ ] Design document reviewed and approved before implementation
- [ ] No hardcoded credentials — all secrets in secret manager
- [ ] Unit tests passing with ≥ 80% coverage
- [ ] Integration tests passing
- [ ] Idempotency verified
- [ ] Monitoring active
- [ ] Runbook published
- [ ] Data quality monitor configured (see data-quality-monitor skill)
- [ ] Reliability test scheduled (see pipeline-reliability-tester skill)

---

*Handoff prepared by [DATA ENGINEER NAME] | [DATE]*
