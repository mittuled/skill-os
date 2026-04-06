# Framework: Data Pipeline Designer

Defines the architectural patterns and design standards for ETL/ELT data pipeline design.

## Architecture Decision: ETL vs. ELT vs. Streaming

| Pattern | When to Choose | Tradeoffs |
|---------|---------------|---------|
| ETL (transform before load) | Strict data governance; on-premise warehouse; limited warehouse compute | Less warehouse cost; harder to reprocess; tightly coupled to transform logic |
| ELT (load raw, transform in warehouse) | Cloud warehouse (Snowflake/BigQuery/Redshift); need raw data for re-processing | Raw data always available; transform logic in SQL; warehouse costs for raw storage |
| Micro-batch | Latency 1–15 min; event-driven use cases | Middle ground; more complex orchestration than batch |
| Streaming (Kafka/Kinesis) | Latency < 1 min; real-time dashboards; event-driven workflows | Most complex; highest infrastructure cost; use only when batch cannot meet SLA |

## Pipeline Layer Definitions

| Layer | Responsibility | Idempotency Requirement | Retry Semantics |
|-------|--------------|------------------------|----------------|
| Extract | Connect to source; paginate; apply watermark; write raw to staging | Idempotent: re-extracting the same window produces the same staging files | Retry up to 3× with exponential backoff; alert on 3rd failure |
| Stage | Land raw data without transformation; schema validation only | Idempotent: overwrite staging partition on re-run | No retry needed; re-run extraction |
| Transform | Apply business logic; deduplicate; join dimensions | Idempotent: re-running produces identical output (upsert or overwrite) | Retry up to 3× after fixing transform issue |
| Load | Write to target warehouse table; update metadata | Idempotent: re-loading the same partition produces no duplicates (upsert/merge) | Retry up to 3×; alert on failure |

## DAG Design Principles

1. **One task per layer**: Extract, Stage, Transform, Load are separate DAG tasks. No monolithic tasks.
2. **Parameterize by date partition**: Every task accepts a date parameter for backfill capability.
3. **Dependency arrows are data dependencies**: Only add a dependency edge when one task's output is another's input.
4. **Timeout every task**: No task runs indefinitely. Set a timeout of 2× the P95 historical duration.
5. **SLA monitor on the final load task**: Alert if the load does not complete by the freshness commitment time.

## Source-to-Target Mapping Standards

Every field in the mapping sheet must document:

| Column | Description | Example |
|--------|------------|---------|
| Source table | Source system and table/endpoint name | `salesforce.opportunity` |
| Source field | Exact source field name | `CloseDate` |
| Source type | Source data type | `date` |
| Target table | Warehouse target table | `stg_salesforce.opportunity` |
| Target field | Target column name (snake_case) | `close_date` |
| Target type | Warehouse data type | `DATE` |
| Transform rule | Any coercion or business logic | `CAST(CloseDate AS DATE)` |
| Null handling | What to do if source value is null | `COALESCE(close_date, '1900-01-01')` or `ALLOW NULL` |
| PII | Whether the field contains PII | `Yes — masked in transform layer` / `No` |

## Idempotency Design Patterns

| Pattern | Use Case | Implementation |
|---------|---------|---------------|
| Overwrite partition | Batch pipeline loading date-partitioned facts | DELETE WHERE event_date = {{ ds }}; INSERT | 
| Upsert / Merge | Slowly changing records (e.g., user attributes) | MERGE ON primary_key; update changed rows, insert new |
| Insert-only with deduplication view | Append-only pipeline with downstream dedup | Deduplicate in the mart layer using ROW_NUMBER() OVER (PARTITION BY key ORDER BY load_ts DESC) |

## SLA Framework

| Metric | Definition | Typical Targets |
|--------|-----------|----------------|
| Freshness SLA | Maximum age of data in target table when dashboards open | Hourly: < 2h lag; Daily: by 08:00 local time |
| Completeness SLA | Minimum row count as % of expected source volume | > 99% of expected rows |
| Latency SLA | Maximum pipeline execution duration | Hourly: < 45 min; Daily: < 2 hours |
| Retry SLA | Maximum time to recover from a transient failure | < 2× pipeline duration |
