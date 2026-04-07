# Data Model Design Document

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Database Expert name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | data-model-designer |
| System | [System / feature name] |
| Database | [PostgreSQL / MySQL / MongoDB / Firestore / ...] |
| Stakeholders | [Backend Developer, Data Engineer, Product Lead] |

## Executive Summary

[2-3 sentences summarizing the domain being modeled, the primary design decision made, and the key tradeoff.
GUIDANCE: Lead with the most important design choice. Example: "This document defines the data model for the subscription billing domain, covering plans, subscriptions, invoices, and payment events. The primary design decision is to use 3NF with a separate invoice_line_items table rather than embedding line items in a JSON column, enabling future analytics queries without JSON parsing overhead. The main tradeoff accepted is an additional join for invoice rendering, mitigated by a covering index."]

## Access Pattern Inventory

[All known read and write operations the application performs. This drives every design decision below.

GUIDANCE:
- Good: List each operation with frequency estimate and latency requirement — this is the source of truth for all indexing and normalization decisions
- Bad: "Standard CRUD operations on all entities"
- Format: Table grouped by entity]

| # | Operation | Type | Frequency | Latency SLO | Key Columns |
|---|-----------|------|-----------|------------|-------------|
| 1 | [e.g., Fetch user subscription by user_id] | Read | [High — every auth request] | [< 5ms] | [user_id, status] |
| 2 | [e.g., List active invoices for billing run] | Read | [Low — nightly batch] | [< 2s] | [status, billing_date] |
| 3 | [e.g., Insert payment event] | Write | [Medium — per transaction] | [< 50ms] | [subscription_id, occurred_at] |

## Entity-Relationship Diagram

[Visual or textual representation of entities and relationships.

GUIDANCE:
- Good: Include cardinality (1:1, 1:N, M:N) and the foreign key direction for each relationship
- Bad: A list of table names without relationships
- Format: Mermaid ER diagram or textual description]

```
[Entity A] 1 ──── N [Entity B]
[Entity B] M ──── N [Entity C] (via junction table entity_b_c)
```

## Schema Definition

[Complete DDL or document schema definitions.

GUIDANCE:
- Good: Include all constraints (NOT NULL, UNIQUE, FK, CHECK), default values, and index definitions
- Bad: Column names and types only without constraints
- Format: SQL DDL for relational; field spec table for document stores]

```sql
-- Example table definition
CREATE TABLE [table_name] (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    [field]     [TYPE] NOT NULL,
    [fk_field]  UUID NOT NULL REFERENCES [other_table](id) ON DELETE [CASCADE/RESTRICT],
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

## Normalization Decision Record

[Explanation of normalization choices made for each entity or relationship group.

GUIDANCE:
- Good: "Invoice line items are in a separate table (3NF) rather than a JSON array because: (1) analytics queries need to aggregate by product_sku, (2) future schema changes to line item fields must be migrations not JSON schema changes"
- Bad: "Used 3NF because it's best practice"]

| Entity / Relationship | Normalization Choice | Rationale | Alternative Considered |
|----------------------|---------------------|-----------|----------------------|
| [e.g., invoice_line_items] | [Separate table (3NF)] | [Analytics queries aggregate by product_sku] | [Embedded JSON array — rejected: unqueryable] |

## Indexing Strategy

[Index specification with query-plan improvement rationale.

GUIDANCE:
- Good: Show which access patterns from the inventory each index serves, and whether it eliminates a full-table scan
- Bad: "We added indexes on foreign key columns"]

| Index Name | Table | Columns | Type | Access Patterns Served | Expected Improvement |
|-----------|-------|---------|------|----------------------|---------------------|
| [idx_subscriptions_user_status] | subscriptions | [user_id, status] | Composite B-tree | [#1, #3] | [Eliminates full-table scan; query cost from O(n) to O(log n)] |

## Capacity Projections

[Scale validation ensuring the schema handles 12-month growth.

GUIDANCE:
- Good: Base projections on current data volume + observed growth rate, not product manager estimates
- Bad: "The database can handle this"]

| Table | Current Row Count | Monthly Growth Rate | 12-Month Projection | Largest Index Size | Partitioning Required? |
|-------|------------------|--------------------|--------------------|-------------------|----------------------|
| [table_name] | [N rows] | [X% / month] | [N × (1+X)^12] | [~Y MB] | [Yes/No — rationale] |

## Recommendations

[Prioritized recommendations for implementation and future schema evolution.

GUIDANCE: Focus on migration risks, query performance concerns, and growth-related risks.]

- **P1**: [Critical risk — e.g., "Table X will exceed 100M rows within 6 months; partition by created_at must be added before 50M rows to avoid locking"]
- **P2**: [Important improvement — e.g., "Add covering index on users(email) INCLUDE (name) to eliminate table heap access for auth queries"]
- **P3**: [Long-term consideration — e.g., "Consider read replica or materialized view for invoice analytics at 10M+ rows"]

## Appendices

### A. Architecture Decision Record (ADR)

[Formal record of the most significant design decisions, alternatives considered, and reasons for rejection.]

**Decision**: [Schema design choice]
**Status**: Accepted
**Context**: [What problem this solves]
**Decision details**: [The choice made]
**Alternatives rejected**: [Options considered and why they were rejected]
**Consequences**: [Tradeoffs accepted]

### B. Migration Strategy

[How this schema will be applied in production, including rollback plan.]

| Migration Step | Operation | Downtime Required? | Rollback Steps |
|---------------|-----------|-------------------|---------------|
| [Step 1] | [ADD COLUMN / CREATE TABLE / CREATE INDEX CONCURRENTLY] | [Yes/No] | [DROP COLUMN etc.] |
