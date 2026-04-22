# Data Quality Monitoring Report

**Pipeline / Dataset:** [PIPELINE NAME]
**Reporting Period:** [DATE] to [DATE]
**Report Generated:** [DATE]
**Owner:** [DATA ENGINEER NAME]
**Environment:** [Production / Staging]

---

## Executive Summary

| Overall Quality Score | SLA Status | Open Incidents | Tables Monitored |
|---|---|---|---|
| [X]% | ✅ Met / ❌ Breached | [N] | [N] |

[One paragraph summarising the health of data quality this period. Call out any SLA breaches, significant degradations, or resolved incidents. Note any dimensions that improved or worsened relative to the prior period.]

---

## 1. Quality Dimension Summary

| Dimension | Target | Actual | Status | Trend vs Prior Period |
|---|---|---|---|---|
| Completeness | ≥ [X]% | [Y]% | ✅ / ⚠️ / ❌ | ↑ [+X%] / ↓ [-X%] / → Stable |
| Accuracy | ≥ [X]% | [Y]% | ✅ / ⚠️ / ❌ | ↑ [+X%] / ↓ [-X%] / → Stable |
| Freshness | ≤ [X] min lag | [Y] min avg | ✅ / ⚠️ / ❌ | ↑ Improved / ↓ Degraded / → Stable |
| Uniqueness | 0 duplicates | [N] dupes | ✅ / ⚠️ / ❌ | ↑ Improved / ↓ Degraded / → Stable |
| Consistency | ≥ [X]% | [Y]% | ✅ / ⚠️ / ❌ | ↑ / ↓ / → |

---

## 2. Table-Level Quality Scorecard

| Table | Completeness | Accuracy | Freshness | Uniqueness | Consistency | Overall |
|---|---|---|---|---|---|---|
| `[schema].[table_1]` | [X]% | [X]% | [X] min | [N] dupes | [X]% | ✅ / ⚠️ / ❌ |
| `[schema].[table_2]` | [X]% | [X]% | [X] min | [N] dupes | [X]% | ✅ / ⚠️ / ❌ |
| `[schema].[table_3]` | [X]% | [X]% | [X] min | [N] dupes | [X]% | ✅ / ⚠️ / ❌ |
| `[schema].[table_4]` | [X]% | [X]% | [X] min | [N] dupes | [X]% | ✅ / ⚠️ / ❌ |

---

## 3. Check Results — Pass / Fail Breakdown

### Completeness Checks

| Check | Table | Column | Expected | Actual | Result |
|---|---|---|---|---|---|
| Non-null [COLUMN] | `[TABLE]` | `[COLUMN]` | 0 nulls | [N] nulls | ✅ / ❌ |
| Row count floor | `[TABLE]` | — | ≥ [N] rows | [M] rows | ✅ / ❌ |
| Required fields populated | `[TABLE]` | `[COLUMN_LIST]` | 100% | [X]% | ✅ / ❌ |

### Freshness Checks

| Check | Table | SLA | Actual Lag | Result |
|---|---|---|---|---|
| Ingestion lag | `[TABLE]` | ≤ [X] min | [Y] min | ✅ / ❌ |
| Last updated timestamp | `[TABLE]` | ≤ [X] hours ago | [Y] hours ago | ✅ / ❌ |

### Uniqueness Checks

| Check | Table | Column(s) | Duplicate Count | Result |
|---|---|---|---|---|
| Primary key uniqueness | `[TABLE]` | `[PK_COLUMN]` | [N] | ✅ / ❌ |
| Business key uniqueness | `[TABLE]` | `[BIZ_KEY]` | [N] | ✅ / ❌ |

### Accuracy and Consistency Checks

| Check | Table | Description | Expected | Actual | Result |
|---|---|---|---|---|---|
| Referential integrity | `[FACT]` → `[DIM]` | FK exists in dim | 0 orphans | [N] orphans | ✅ / ❌ |
| Value range | `[TABLE].[COLUMN]` | Values in [MIN, MAX] | 0 violations | [N] violations | ✅ / ❌ |
| Cross-table row count match | `[SOURCE]` vs `[TARGET]` | Counts match ±1% | [N] source | [M] target | ✅ / ❌ |

---

## 4. Alerts and Incidents

### Alerts Fired This Period

| Alert ID | Severity | Dimension | Table | Fired At | Resolved At | Duration |
|---|---|---|---|---|---|---|
| [ALERT-001] | Critical / Warning | [DIMENSION] | `[TABLE]` | [DATETIME] | [DATETIME] | [X] min |
| [ALERT-002] | Critical / Warning | [DIMENSION] | `[TABLE]` | [DATETIME] | [DATETIME] | [X] min |

### Open Incidents

| Incident | Severity | Table | Root Cause | Owner | Status | Due |
|---|---|---|---|---|---|---|
| [INC-001] | Critical | `[TABLE]` | [ROOT CAUSE SUMMARY] | [OWNER] | In Progress | [DATE] |
| [INC-002] | Warning | `[TABLE]` | [ROOT CAUSE SUMMARY] | [OWNER] | Monitoring | [DATE] |

### Resolved Incidents

| Incident | Table | Root Cause | Resolution | Resolved At |
|---|---|---|---|---|
| [INC-003] | `[TABLE]` | [ROOT CAUSE] | [RESOLUTION APPLIED] | [DATETIME] |

---

## 5. SLA Compliance

| SLA | Target | Actual | Compliance |
|---|---|---|---|
| Daily ingestion completeness | ≥ [X]% | [Y]% | ✅ / ❌ |
| Freshness SLA | ≤ [X] min | [Y] min avg | ✅ / ❌ |
| Zero-duplicate guarantee | 0 dupes/day | [N] dupes | ✅ / ❌ |
| Alert response time | ≤ [X] min | [Y] min avg | ✅ / ❌ |

---

## 6. Trend Analysis

### Quality Score Trend (Last 8 Weeks)

| Week | Completeness | Freshness | Uniqueness | Accuracy | Consistency |
|---|---|---|---|---|---|
| [WEEK -7] | [X]% | [X] min | [N] dupes | [X]% | [X]% |
| [WEEK -6] | [X]% | [X] min | [N] dupes | [X]% | [X]% |
| [WEEK -5] | [X]% | [X] min | [N] dupes | [X]% | [X]% |
| [WEEK -4] | [X]% | [X] min | [N] dupes | [X]% | [X]% |
| [WEEK -3] | [X]% | [X] min | [N] dupes | [X]% | [X]% |
| [WEEK -2] | [X]% | [X] min | [N] dupes | [X]% | [X]% |
| [WEEK -1] | [X]% | [X] min | [N] dupes | [X]% | [X]% |
| **This week** | **[X]%** | **[X] min** | **[N] dupes** | **[X]%** | **[X]%** |

---

## 7. Recommended Actions

| Priority | Action | Owner | Due | Impact |
|---|---|---|---|---|
| P1 | [ACTION DESCRIPTION] | [OWNER] | [DATE] | Resolves [INC-00X] / Prevents SLA breach |
| P2 | [ACTION DESCRIPTION] | [OWNER] | [DATE] | Improves [DIMENSION] by ~[X]% |
| P3 | [ACTION DESCRIPTION] | [OWNER] | [DATE] | Reduces alert noise |

---

*Report prepared by [DATA ENGINEER NAME] | Distribution: [VP ENGINEERING, DATA TEAM, ANALYTICS TEAM] | [DATE]*
