# Pipeline Design Document

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Data Engineer name] |
| Version | [1.0] |
| Status | [Draft / Review / Approved] |
| Skill | data-pipeline-designer |
| Pipeline Name | [pipeline-name] |
| Ticket | [JIRA / Linear ticket link] |

## Executive Summary

[2-3 sentences describing the pipeline purpose, architecture pattern chosen, and the top design tradeoff resolved.

GUIDANCE: Example: "This pipeline ingests Stripe subscription events into the data warehouse using an ELT pattern with incremental extraction (cursor-based on updated_at). The primary design tradeoff resolved was real-time vs. daily batch — daily batch was chosen because the consuming dashboard is reviewed once per day, avoiding unnecessary Stripe API quota consumption."]

## Source Inventory

[All data sources involved.

GUIDANCE:
- Good: Table with source name, type, connection method, schema snapshot, estimated volume, and SLA metadata.
- Bad: Just naming the source system.
- Format: Table.]

| Source Name | Type | Connection | Schema Version | Daily Volume (rows) | Source SLA | Notes |
|------------|------|-----------|---------------|--------------------|-----------|----|
| [Source] | [API / DB / File / Stream] | [Connector / JDBC / S3 / Kafka] | [v1.x] | [N rows] | [SLA or "best effort"] | [Rate limits, auth method] |

## Pipeline Requirements

[Stakeholder requirements with acceptance criteria.

GUIDANCE:
- Good: Each requirement is a testable statement with a threshold.
- Bad: "Pipeline should be fast and reliable."
- Format: Table.]

| Requirement | Acceptance Criterion | Priority |
|------------|--------------------|----|
| Freshness | Data available by [HH:MM] UTC daily | P0 |
| Completeness | ≥ [99%] of source rows present in target within [N] minutes of SLA | P0 |
| Latency | Full pipeline execution ≤ [N] minutes | P1 |
| Schema evolution | Pipeline does not break when source adds nullable columns | P1 |

## Architecture Decision Record (ADR)

[Rationale for the chosen architecture pattern.

GUIDANCE:
- Good: Document the options considered, why each was rejected, and why the chosen pattern was selected. Include volume and latency data.
- Bad: "We chose ELT because it's modern."
- Format: Structured ADR.]

**Decision:** [ETL / ELT / Streaming / Micro-batch]

**Options considered:**
1. [Option A] — rejected because [reason with data]
2. [Option B] — rejected because [reason]
3. [Chosen option] — selected because [reason with data]

**Consequences:** [Known tradeoffs of the chosen approach]

## DAG Specification

[Step-by-step pipeline flow with task-level SLAs.

GUIDANCE:
- Good: Every task has a name, type, inputs, outputs, expected duration, timeout, retry policy, and failure alert.
- Bad: A diagram without task-level SLA documentation.
- Format: Table.]

| Task Name | Type | Depends On | Expected Duration | Timeout | Retries | Failure Alert |
|-----------|------|-----------|------------------|---------|---------|--------------|
| `extract_[source]` | Extract | (start) | [N min] | [N min] | 3× exponential | [Channel] |
| `stage_[source]` | Stage | `extract_[source]` | [N min] | [N min] | 1× | [Channel] |
| `transform_[model]` | Transform | `stage_[source]` | [N min] | [N min] | 3× | [Channel] |
| `load_[target]` | Load | `transform_[model]` | [N min] | [N min] | 3× | [Channel] |

**Backfill strategy:** [How to re-run the pipeline for historical date ranges]

## Source-to-Target Mapping

[Field-level mapping from source to warehouse target.

GUIDANCE:
- Good: Every field mapped with transform rule, null handling, and PII flag.
- Bad: Only column names without types or business logic.
- Format: Table.]

| Source Field | Source Type | Target Field | Target Type | Transform Rule | Null Handling | PII |
|-------------|------------|-------------|------------|---------------|--------------|-----|
| [field_name] | [type] | [field_name] | [type] | [CAST / COALESCE / custom] | [ALLOW NULL / default value] | [Yes/No] |

## SLA Targets

| Dimension | Target | Monitoring Method |
|-----------|--------|-----------------|
| Freshness | Data in target by [HH:MM] UTC | SLA monitor on final load task |
| Completeness | ≥ [99%] of expected rows | Row count assertion post-load |
| Pipeline duration | ≤ [N] minutes end-to-end | DAG execution time tracking |

## Recommendations

[Prioritized design risks and next steps.

GUIDANCE:
- P1: Unresolved design issues that must be addressed before implementation begins.
- P2: Architectural improvements deferred to a future iteration.
- P3: Monitoring enhancements to add after initial production deployment.]

## Appendices

### A. Methodology

[Data profiling results used to estimate volumes, rate limit documentation from source API, and schema snapshots used during design.]

### B. Supporting Data

[Source API documentation links, schema ERD, volume growth projections, and comparable pipeline designs referenced.]
