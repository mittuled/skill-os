---
name: data-model-designer
description: >
  This skill designs relational or document data models including schema, relationships, and indexing strategy. Use when asked to create a database schema, design entity relationships, or plan indexing. Also consider when migrating between database paradigms or when query performance degrades due to schema issues. Suggest when a new feature requires persistent storage or an existing model cannot support emerging access patterns.
department: engineering
agent: database-expert
version: 1.0.0
complexity: complex
related-skills:
  - ../../sr-backend-developer/builder/SKILL.md
  - ../../sr-backend-developer/instrumentation-planner-eng/SKILL.md
---

# data-model-designer

## Agent: Database Expert

L3 database specialist (1x) responsible for data model design and database architecture. Co-owns data modelling with the Data Engineer and Senior Backend Developer.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)
Tool policy: [allowed-tools.yaml](../../../allowed-tools.yaml)

## Skill Description

Designs the relational or document data model including schema definition, entity relationships, normalization decisions, and indexing strategy that supports application access patterns at target scale.

## When to Use

- A new product feature requires persistent storage and no existing schema covers the domain entities.
- Query latency exceeds SLOs and profiling points to missing indexes or suboptimal schema structure.
- The team is migrating between database paradigms (e.g., relational to document, monolith to polyglot persistence).
- A data engineer or backend developer requests a schema review before implementing a migration.
- Access pattern changes (new read-heavy dashboard, write-heavy event stream) demand schema evolution.

## Workflow

1. **Gather access patterns**: Collect all known read and write operations the application performs against the target domain. Deliverable: access-pattern inventory listing operation type, frequency, and latency requirements.
2. **Identify entities and relationships**: Extract domain entities, their attributes, and cardinality of relationships from requirements and existing code. Deliverable: entity-relationship diagram or document model map.
3. **Choose normalization level**: Decide normalization form (3NF for relational, embedding vs. referencing for document stores) based on read/write ratio and consistency requirements. Deliverable: normalization decision record with rationale.
4. **Define schema**: Write the DDL or schema definition including data types, constraints, foreign keys, and default values. Deliverable: migration-ready schema file.
5. **Design indexing strategy**: Identify columns or fields requiring indexes based on the access-pattern inventory. Include composite indexes, partial indexes, and covering indexes where beneficial. Deliverable: index specification with expected query-plan improvements.
6. **Validate against scale targets**: Estimate row counts, document sizes, and growth rates. Verify the schema handles projected load without partition hotspots or unbounded array growth. Deliverable: capacity projection table.
7. **Review with stakeholders**: Present the schema to the backend developer and data engineer for feedback on implementation feasibility and operational concerns. Deliverable: approved schema with sign-off or revision notes.
8. **Document decisions**: Record all schema and indexing decisions in an ADR including alternatives considered and reasons for rejection. Deliverable: architecture decision record.

## Anti-Patterns

- **Designing without access patterns.** Creating a schema from entity definitions alone ignores how data will actually be queried. *Why*: a normalized schema optimized for writes may cripple read-heavy dashboards with expensive joins.
- **Over-indexing.** Adding indexes on every column to "be safe" degrades write throughput and increases storage costs. *Why*: each index adds overhead to every insert, update, and delete operation.
- **Premature denormalization.** Flattening data before measuring actual query performance introduces update anomalies without proven benefit. *Why*: denormalization trades write complexity for read speed and should be evidence-driven.
- **Ignoring growth projections.** Designing for current data volume without considering 12-month growth leads to emergency migrations. *Why*: schema changes under load are the most dangerous operations in production.
- **Schema-only thinking.** Delivering a schema without migration scripts or rollback plans leaves the backend developer to improvise. *Why*: the gap between a design and a deployed schema is where data loss occurs.

## Output

**On success**: Produces a migration-ready schema definition (DDL or equivalent), an entity-relationship diagram, an index specification, and an architecture decision record. Delivered to the backend developer and data engineer for implementation.

**On failure**: Report which access patterns could not be satisfied by the proposed schema, what normalization tradeoffs were attempted, and recommended next steps (e.g., prototype benchmarking, alternative database engine evaluation). Every gap must include a concrete resolution path.

## Related Skills

- [`builder`](../../sr-backend-developer/builder/SKILL.md) -- implements the backend services that consume the data model.
- [`instrumentation-planner-eng`](../../sr-backend-developer/instrumentation-planner-eng/SKILL.md) -- plans observability for database query performance and connection pool health.
