# Architecture Document

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Tech Architect name] |
| Version | [1.0] |
| Status | [Draft / Review / Approved] |
| Skill | architecture-designer |
| System Name | [System or product name] |
| Review Date | [Date of last architecture review] |
| ADR Location | [Link to ADR directory] |

## Executive Summary

[2–3 sentences covering the system's purpose, the chosen granularity pattern, and the primary architectural trade-off made.

GUIDANCE: Good — "The payments service is a standalone modular monolith deployed on Kubernetes, separated from the core product to meet PCI-DSS isolation requirements; the primary trade-off is additional deployment overhead in exchange for audit compliance and independent scaling." Bad — "This document describes the system architecture."]

## Requirements

### Functional Requirements

| ID | Requirement | Priority | Source |
|----|-------------|----------|--------|
| FR-1 | [What the system must do] | Must-have / Should-have | [Spec / stakeholder] |

### Non-Functional Requirements

| ID | Requirement | Target | Source |
|----|-------------|--------|--------|
| NFR-1 | Availability | [e.g., 99.9% monthly] | [SLA document] |
| NFR-2 | Latency | [e.g., p99 < 200ms] | [Product requirement] |
| NFR-3 | Throughput | [e.g., 1K rps sustained] | [Scale projection] |
| NFR-4 | Data retention | [e.g., 7 years for financial records] | [Compliance requirement] |

### Constraints

| Constraint | Description | Impact on Design |
|------------|-------------|-----------------|
| Timeline | [Engineering weeks available] | [What it rules out] |
| Team | [Size and expertise] | [What it rules out] |
| Infrastructure | [Existing platform limits] | [What it rules out] |
| Regulatory | [Compliance requirements] | [What it mandates] |

## System Architecture

### Granularity Decision

**Pattern chosen**: [Monolith / Modular monolith / Service-oriented / Microservices]

**Rationale**: [Why this pattern fits the team size, operational maturity, and requirements — reference `references/framework.md` selection criteria]

### Component Diagram

```
[ASCII diagram or Mermaid / PlantUML diagram of components and their interactions]

Example:
┌─────────────┐     REST      ┌──────────────┐     Events    ┌──────────────┐
│  API Gateway │──────────────▶│ Core Service  │──────────────▶│  Worker      │
└─────────────┘               └──────┬───────┘               └──────────────┘
                                      │ SQL
                               ┌──────▼───────┐
                               │  PostgreSQL   │
                               └──────────────┘
```

### Component Responsibilities

| Component | Primary Responsibility | Data Owned | Interaction Pattern |
|-----------|----------------------|------------|---------------------|
| [Component] | [One sentence] | [Tables / entities] | [REST / Events / Batch / SDK] |

GUIDANCE: Each component gets exactly one primary responsibility. If you need "and", split the component.

## Data Architecture

### Storage Technologies

| Store | Technology | Purpose | Data Volume | Access Pattern |
|-------|-----------|---------|-------------|----------------|
| Primary DB | [PostgreSQL 16] | [Business objects] | [Estimated size] | [Read-heavy / Write-heavy] |
| Cache | [Redis 7] | [Session / hot data] | [Estimated size] | [High read, TTL-managed] |
| Search | [Optional] | [Full-text search] | [Estimated docs] | [Search queries] |
| Object storage | [S3 / GCS] | [Files / media] | [Estimated TB] | [CDN-fronted reads] |

### Data Flow

[Describe how data moves through the system for the primary use cases — which component creates, who reads, where it's replicated]

## Technology Selections

| Concern | Choice | Alternatives Considered | Rationale |
|---------|--------|------------------------|-----------|
| Language | [Language + version] | [Alt A, Alt B] | [Why this choice] |
| Web framework | [Framework] | [Alt A, Alt B] | [Why this choice] |
| Database | [Database] | [Alt A, Alt B] | [Why this choice] |
| Message broker | [Broker or N/A] | [Alt A, Alt B] | [Why this choice] |
| Container platform | [Platform] | [Alt A, Alt B] | [Why this choice] |

## Cross-Cutting Concerns

| Concern | Solution | Notes |
|---------|----------|-------|
| Authentication | [Protocol and token store] | [e.g., JWT, 1h TTL, Redis token store] |
| Authorization | [Model and enforcement point] | [e.g., RBAC enforced at API gateway] |
| Logging | [Aggregation platform] | [e.g., structured JSON → Datadog] |
| Metrics | [Platform] | [e.g., Prometheus → Grafana] |
| Tracing | [Platform] | [e.g., OpenTelemetry → Jaeger] |
| Error handling | [Retry + DLQ strategy] | [e.g., exponential backoff, 3 retries, SQS DLQ] |
| Secrets | [Storage] | [e.g., AWS Secrets Manager; rotated every 30 days] |
| Deployment | [Strategy] | [e.g., blue-green with automated rollback on error-rate spike] |
| Backup | [RTO / RPO] | [e.g., daily snapshot; RTO 4h; RPO 24h] |

## Key Architectural Trade-Offs

[Document each major decision where a meaningful alternative existed.]

### Trade-off 1: [Decision name]

**Decision**: [What was decided]
**Options considered**: [A] vs [B] vs [C]
**Rationale**: [Why this option was chosen]
**Consequences**: [What becomes easier / harder]
**Review trigger**: [Condition that would prompt reconsideration]

## Recommendations

**P1 — Required before development begins:**
- [Specific decision or prerequisite]

**P2 — Address in first sprint:**
- [Infrastructure or tooling setup needed]

**P3 — Architecture evolution milestones:**
- [Conditions that would trigger architecture revision — e.g., "Re-evaluate service split when team exceeds 15 engineers"]

## Appendices

### A. Methodology

Architecture designed using `architecture-designer` skill. Trade-off framework and cross-cutting checklist from `references/framework.md`. Reviewed with [names] on [date].

### B. Architecture Decision Records

[Links to individual ADR files for major technology and structural decisions]

### C. Diagrams

[Additional sequence diagrams, data flow diagrams, deployment diagrams]
