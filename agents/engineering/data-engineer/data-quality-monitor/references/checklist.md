# Checklist: Data Quality Monitor

Defines the complete set of quality dimensions, check types, and alerting standards for monitoring data pipeline outputs.

## Data Quality Dimensions

| Dimension | Definition | Example Failure |
|-----------|-----------|----------------|
| Completeness | Required fields are non-null; expected row volumes are present | `customer_id` is NULL in 15% of orders; daily row count drops 40% |
| Accuracy | Values are within expected domain and consistent with source | `revenue_usd` is negative; enum field contains undocumented value |
| Freshness | Data is updated within the defined latency SLA | Table `fct_events` last updated 26h ago; daily SLA is 8h |
| Uniqueness | Primary key columns contain no duplicate values | `event_id` has 1,200 duplicates in today's load |
| Consistency | Related tables are internally consistent (referential integrity, count reconciliation) | 3,400 orphaned foreign keys in `fct_orders` referencing deleted `dim_users` rows |
| Validity | Values conform to expected format or data type | `email` column contains 200 rows with no `@` symbol |

## Check Implementation Locations

| Location | Trigger | Checks to Place |
|---------|---------|----------------|
| Post-extraction | After raw data lands in staging | Schema conformance, null counts, row count floor |
| Post-transform | After business logic applied | Business rule assertions, referential integrity, deduplication |
| Post-load | After data written to mart/reporting | Row count match vs. source; uniqueness on primary key; freshness timestamp |
| Scheduled independent | Daily/hourly monitoring job | Cross-table consistency, long-term trend deviation |

## Mandatory Check Set

Every pipeline must implement at minimum:

### Completeness Checks
- [ ] Row count ≥ expected floor (absolute count, not just percentage): `ASSERT row_count >= {floor}` AND `ASSERT row_count >= {yesterday} * 0.8`
- [ ] Null rate on required columns ≤ 0.1%: `ASSERT null_count(required_column) / total_rows <= 0.001`

### Freshness Checks
- [ ] Table last loaded within SLA window: `ASSERT MAX(loaded_at) >= CURRENT_TIMESTAMP - INTERVAL '{sla_hours} hours'`

### Uniqueness Checks
- [ ] Primary key is unique: `ASSERT COUNT(DISTINCT pk) = COUNT(*)`

### Accuracy Checks
- [ ] Numeric measures within valid range: `ASSERT MIN(revenue_usd) >= 0`
- [ ] Enum fields contain only allowed values: `ASSERT COUNT(*) WHERE status NOT IN ('active','inactive','pending') = 0`

### Consistency Checks
- [ ] Foreign key integrity: `ASSERT COUNT(orphaned_fk) = 0`
- [ ] Cross-table row count reconciliation: `ASSERT ABS(source_count - target_count) / source_count <= 0.01`

## Alerting Configuration Standards

| Check Severity | Condition | Alert Channel | Response SLA |
|---------------|----------|--------------|-------------|
| Critical | Row count <80% of expected floor OR freshness SLA breached | PagerDuty + #data-incidents | 15 min |
| High | Null rate >1% on required columns OR uniqueness violation | #data-alerts + DM owner | 1 hour |
| Warning | Enum value outside allowed list; row count 80–95% of floor | #data-health | Next business day |

## Incident Runbook

### Freshness Failure
1. Check orchestrator for failed DAG runs.
2. Check pipeline logs for error message.
3. If source unavailable: wait for source recovery; set dashboard stale data banner.
4. If transform failure: review error, apply fix, re-trigger pipeline.
5. Notify data consumers in #data-incidents with estimated recovery time.

### Row Count Drop
1. Check source row count for same period — is the drop at source or in pipeline?
2. If at source: escalate to source system owner.
3. If in pipeline: check extract watermark (was the watermark updated correctly?).
4. If in transform: check deduplication logic for over-filtering.
5. Document root cause and resolution in incident log.

### Uniqueness Violation
1. Query duplicate rows to identify the key and timestamp.
2. Check if the pipeline has idempotent load semantics (merge vs. insert).
3. If insert-only pipeline: check for double-trigger or retry with duplicate data.
4. Apply deduplication patch; document the cause; add a pre-load deduplication step if recurring.

## Quality Dashboard Requirements

The quality dashboard must display:
- [ ] Pass/fail status per check per table (current run)
- [ ] 30-day trend of check pass rates per table
- [ ] SLA compliance % over last 30 days per pipeline
- [ ] Open incidents count and mean time to resolution
