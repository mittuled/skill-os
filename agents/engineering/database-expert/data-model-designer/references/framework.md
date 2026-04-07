# Framework: Data Model Design

Defines the structured approach for designing relational and document data models, covering access pattern analysis, normalization decisions, indexing strategy, and schema validation.

## Design Process

```
Access Pattern Inventory
         │
         ▼
Entity-Relationship Analysis
         │
         ▼
Normalization Decision (3NF vs. denormalized)
         │
         ▼
Schema Definition (DDL / Document Schema)
         │
         ▼
Indexing Strategy
         │
         ▼
Scale Validation (capacity projections)
         │
         ▼
Stakeholder Review → ADR
```

## Access Pattern Classification

Before defining any schema, classify all access patterns:

| Pattern Type | Examples | Schema Implication |
|-------------|----------|-------------------|
| Point lookup by PK | `SELECT * WHERE id = ?` | Primary key index sufficient |
| Range query on ordered field | `SELECT * WHERE created_at BETWEEN ? AND ?` | Sorted index on the range field |
| Filter by low-cardinality column | `SELECT * WHERE status = 'active'` | Partial index on status |
| Join-heavy reporting | `SELECT ... FROM orders JOIN users JOIN products` | Consider denormalization or materialized view |
| Write-heavy, read-rarely | Event log, audit trail | Append-only; no indexes on non-query fields |
| Full-text search | `WHERE body CONTAINS ?` | Full-text index or external search engine (Elasticsearch) |
| Geospatial | `WHERE location WITHIN radius` | GiST index (PostgreSQL) |

## Normalization Decision Guide

| Scenario | Recommended Form | Rationale |
|----------|-----------------|-----------|
| OLTP system with complex writes, moderate reads | 3NF | Prevents update anomalies; writes are efficient |
| Read-heavy dashboard / reporting | 2NF or denormalized | Reduces joins; improves read performance |
| Document store (MongoDB/Firestore) | Embed when < 1:N bound; reference when unbounded | Embedding bounds document growth; referencing prevents unbounded arrays |
| Event sourcing | Append-only flat schema | Never update; only insert events; reconstruct state by replay |
| Time-series data | Hypertable (TimescaleDB) or partition by time | Efficient range queries and data retention management |

## Indexing Strategy Matrix

| Query Pattern | Index Type | Notes |
|--------------|-----------|-------|
| Single-column equality filter | B-tree on column | Default; covers most filters |
| Multi-column filter with equality | Composite B-tree (most selective column first) | Column order matters; only leftmost prefix used |
| Range query on ordered column | B-tree on range column | Works for BETWEEN, >, < |
| Low-cardinality column filter (e.g., status) | Partial index with WHERE clause | `CREATE INDEX ON orders(id) WHERE status = 'pending'` — much smaller, faster |
| Covering index (no table heap access) | Include non-filtered columns in index | `CREATE INDEX ON users(email) INCLUDE (name, avatar_url)` |
| Full-text search | GIN index on tsvector | PostgreSQL full-text; use Elasticsearch for advanced search |
| JSON/JSONB field queries | GIN index on JSONB | Efficient for `@>` and `->>` operators |
| UUID primary key (random inserts) | B-tree (default) | Consider UUIDv7 (time-ordered) to reduce index fragmentation |

### Index Anti-Patterns

| Anti-Pattern | Impact | Alternative |
|-------------|--------|-------------|
| Index on every column | Write performance degradation; storage waste | Index only query-critical columns |
| Index on unbounded array field (document stores) | Index size explosion | Reference instead of embed for unbounded arrays |
| Composite index with wrong column order | Index not used for single-column queries on non-leftmost column | Lead with the most selective column |
| Index on low-read, high-write tables | High write overhead with little read benefit | Defer index creation until read patterns are established |

## Schema Definition Standards

### Relational (PostgreSQL)

```sql
-- Required constraints
id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),

-- Always use TIMESTAMPTZ (not TIMESTAMP) for timezone correctness
-- Always use TEXT (not VARCHAR(255)) unless length enforcement is required
-- Always define NOT NULL on required fields
-- Always define foreign key constraints
-- Always add updated_at trigger for mutable entities
```

### Document Store (MongoDB/Firestore)

```
Embedding rules:
- Embed when the related data is ALWAYS read with the parent (1:1 or bounded 1:N)
- Embed when document size stays below 16MB (MongoDB) or 1MB (Firestore)
- Reference when the relationship is many-to-many
- Reference when the sub-document is accessed independently
- Reference when the array is unbounded
```

## Scale Validation Checklist

Before finalizing schema:

- [ ] Row count estimated for 12 months at P90 growth rate
- [ ] Largest table checked for partition hotspot risk (sequential UUID vs. time-based partition)
- [ ] Estimated index size calculated and within storage budget
- [ ] Unbounded array fields or JSON blobs bounded with documented limits
- [ ] Migration strategy defined for each schema change (backwards-compatible vs. requires downtime)
- [ ] Rollback plan documented for each migration (DROP COLUMN only after deployment confirmed)
