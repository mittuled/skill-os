# Pipeline Reliability Test Report

**Pipeline Name:** [PIPELINE NAME]
**Test Executed By:** [DATA ENGINEER NAME]
**Test Date:** [DATE]
**Environment:** [Staging / Pre-production]
**Pipeline Version / Commit:** [GIT SHA or VERSION TAG]
**Overall Verdict:** ✅ PASS — Ready for production / ❌ FAIL — [N] blocking failures

---

## Executive Summary

[One paragraph describing the scope of reliability testing, what scenarios were exercised, whether the pipeline met reliability requirements, and any blocking issues that must be resolved before production promotion.]

---

## 1. Failure Mode Inventory

| ID | Failure Scenario | Category | Tested | Severity |
|---|---|---|---|---|
| FM-01 | Source API unavailable (connection refused) | Source | ✅ / ❌ | Critical |
| FM-02 | Source API timeout (> [X]s) | Source | ✅ / ❌ | Critical |
| FM-03 | Schema drift — new column added | Source | ✅ / ❌ | High |
| FM-04 | Schema drift — column removed | Source | ✅ / ❌ | Critical |
| FM-05 | Schema drift — column type changed | Source | ✅ / ❌ | High |
| FM-06 | Network partition mid-extraction | Network | ✅ / ❌ | Critical |
| FM-07 | Out-of-order event delivery | Data | ✅ / ❌ | High |
| FM-08 | Partial write to target (task killed mid-load) | Pipeline | ✅ / ❌ | Critical |
| FM-09 | Orchestrator worker crash during transformation | Pipeline | ✅ / ❌ | Critical |
| FM-10 | Duplicate records injected at source | Data | ✅ / ❌ | High |
| FM-11 | Bad records with invalid types injected | Data | ✅ / ❌ | Medium |
| FM-12 | Target write throttled / quota exceeded | Target | ✅ / ❌ | High |

---

## 2. Idempotency Verification

**Test objective:** Execute the pipeline twice with identical input and confirm outputs are identical — no duplicate rows, no missing records, identical aggregations.

| Check | Run 1 | Run 2 | Match? |
|---|---|---|---|
| Row count in `[TARGET_TABLE]` | [N] rows | [N] rows | ✅ / ❌ |
| Sum of `[METRIC_COLUMN]` | [VALUE] | [VALUE] | ✅ / ❌ |
| Distinct `[KEY_COLUMN]` count | [N] | [N] | ✅ / ❌ |
| `MAX(updated_at)` in target | [TIMESTAMP] | [TIMESTAMP] | ✅ / ❌ |
| Duplicate row count after 2nd run | — | [N] | ✅ 0 / ❌ [N] |

**Idempotency result:** ✅ PASS — re-run produces identical output / ❌ FAIL — [describe discrepancy]

**Upsert key used:** `[PRIMARY_KEY_COLUMN(S)]`
**Upsert strategy:** MERGE / DELETE+INSERT / INSERT OVERWRITE partition

---

## 3. Fault Injection Results

### Source Failures

| Scenario | Failure Injected | Expected Behaviour | Observed Behaviour | Result |
|---|---|---|---|---|
| FM-01: Source unavailable | Blocked connection at network layer | Retry [N] times, then alert | [OBSERVED] | ✅ / ❌ |
| FM-02: Source timeout | Injected [X]s latency | Timeout after [Y]s, retry | [OBSERVED] | ✅ / ❌ |
| FM-03: New column at source | Added `new_field` to source payload | Pipeline ignores unknown fields | [OBSERVED] | ✅ / ❌ |
| FM-04: Column removed at source | Removed required `[COLUMN]` | Pipeline fails with schema error, sends alert | [OBSERVED] | ✅ / ❌ |

### Network Failures

| Scenario | Failure Injected | Expected Behaviour | Observed Behaviour | Result |
|---|---|---|---|---|
| FM-06: Network partition | Dropped connection mid-extraction | Retry from last checkpoint | [OBSERVED] | ✅ / ❌ |

### Pipeline Execution Failures

| Scenario | Failure Injected | Expected Behaviour | Observed Behaviour | Result |
|---|---|---|---|---|
| FM-08: Partial write (task killed) | Killed task at [X]% completion | Target left in clean state on retry | [OBSERVED] | ✅ / ❌ |
| FM-09: Worker crash during transform | Killed orchestrator worker | Task retried on different worker | [OBSERVED] | ✅ / ❌ |

### Data Quality Failures

| Scenario | Failure Injected | Expected Behaviour | Observed Behaviour | Result |
|---|---|---|---|---|
| FM-07: Out-of-order events | Injected events with past timestamps | Handled by watermark logic | [OBSERVED] | ✅ / ❌ |
| FM-10: Duplicate records | Injected 10% duplicate rows at source | Deduplication eliminates all dupes | [OBSERVED] | ✅ / ❌ |
| FM-11: Bad records | Injected [N] rows with invalid types | Bad records quarantined, pipeline continues | [OBSERVED] | ✅ / ❌ |

**Fault injection summary:** [N] / [TOTAL] scenarios passed

---

## 4. Data Consistency Validation

| Check | Table | Expected | Actual | Result |
|---|---|---|---|---|
| Row count — source vs target | `[SOURCE]` vs `[TARGET]` | Match ±0.1% | [SOURCE N] vs [TARGET M] | ✅ / ❌ |
| Referential integrity — fact → dim | `[FACT].[FK]` → `[DIM].[PK]` | 0 orphans | [N] orphans | ✅ / ❌ |
| Orphaned foreign keys | `[TABLE].[FK_COLUMN]` | 0 | [N] | ✅ / ❌ |
| Aggregation match | `SUM([METRIC])` source vs target | < 0.01% deviation | [X]% deviation | ✅ / ❌ |
| Null foreign keys | `[TABLE].[FK]` | 0 | [N] | ✅ / ❌ |

**Consistency result:** ✅ All checks pass / ❌ [N] failures — see details below

[DETAIL OF ANY CONSISTENCY FAILURES]

---

## 5. SLA Stress Test

**Test scenario:** Pipeline run at [X]× peak volume ([N] rows, [Y] GB)
**SLA requirement:** Complete by [HH:MM UTC] — must finish within [X] minutes of trigger

| Run | Input Volume | Start Time | End Time | Duration | SLA Met? |
|---|---|---|---|---|---|
| Baseline | [N] rows / [Y] GB | [HH:MM] | [HH:MM] | [X] min | ✅ / ❌ |
| Peak (1×) | [N] rows / [Y] GB | [HH:MM] | [HH:MM] | [X] min | ✅ / ❌ |
| Peak (2×) | [N] rows / [Y] GB | [HH:MM] | [HH:MM] | [X] min | ✅ / ❌ |
| Peak (5×) | [N] rows / [Y] GB | [HH:MM] | [HH:MM] | [X] min | ✅ / ❌ |

**SLA stress test result:** ✅ PASS — SLA met under all load conditions / ❌ FAIL — SLA breached at [X]× load
**Bottleneck identified at:** [TASK / STEP] under peak load — [DESCRIPTION]

---

## 6. Summary and Sign-Off

| Test Area | Result | Blocking? |
|---|---|---|
| Idempotency | ✅ Pass / ❌ Fail | Yes / No |
| Fault injection | ✅ Pass / ❌ Fail | Yes / No |
| Data consistency | ✅ Pass / ❌ Fail | Yes / No |
| SLA stress test | ✅ Pass / ❌ Fail | Yes / No |

### Blocking Issues (must resolve before production promotion)

| Issue | Test Area | Failure Mode | Root Cause | Recommended Fix |
|---|---|---|---|---|
| [ISSUE 1] | [AREA] | FM-[XX] | [ROOT CAUSE] | [RECOMMENDED FIX] |

### Non-Blocking Issues (monitor in production)

| Issue | Test Area | Risk | Recommended Action |
|---|---|---|---|
| [ISSUE 1] | [AREA] | Low / Medium | [ACTION] |

---

**Production promotion approved:** ✅ Yes / ❌ No — pending resolution of blocking issues above

*Report prepared by [DATA ENGINEER NAME] | Reviewed by [TECH LEAD] | [DATE]*
