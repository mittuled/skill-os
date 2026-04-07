# Framework: architecture-designer

Defines the methodology for producing system architecture designs that are decisions-first, constraint-grounded, and reviewable.

## Architecture Decision Model

### Granularity Selection

Choose system granularity based on team size and operational maturity:

| Granularity | Team Size | Operational Maturity | When to Choose |
|-------------|-----------|---------------------|----------------|
| Monolith | 1–8 engineers | Any | Greenfield, < 12 months runway, unclear domain boundaries |
| Modular monolith | 5–20 engineers | Medium | Clear domain boundaries; deployment complexity not yet justified |
| Service-oriented (2–6 services) | 8–30 engineers | Medium-High | 2+ teams working on distinct domains; independent deployment valuable |
| Microservices (> 6 services) | 20+ engineers | High | Large teams with dedicated platform/SRE; operational tooling in place |

**Rule**: Default to the simpler option. Only increase granularity when a specific requirement — independent scaling, team autonomy, isolation of failure domain — cannot be met with the simpler architecture.

## Component Responsibility Model

Every component in the architecture must have:
1. A single primary responsibility (one sentence: "This service owns X")
2. An explicit data ownership boundary (what data it creates, reads, updates, deletes)
3. Defined interaction pattern with each consumer (sync REST, async event, batch, SDK)

## Data Architecture Patterns

| Use Case | Recommended Pattern | When to Avoid |
|----------|--------------------|----|
| Single source of truth for business objects | Single PostgreSQL database per domain | When data volume > 1TB or write throughput > 5K req/s |
| Cross-service reads | Materialized view / read replica | When consistency must be < 1 second |
| Real-time updates | Event streaming (Kafka / SQS + fanout) | Simple CRUD with low traffic |
| Full-text search | Elasticsearch / OpenSearch as search layer | If PostgreSQL full-text suffices (< 10M documents) |
| User sessions | Redis with TTL | Sticky sessions on load balancer (anti-pattern) |
| File / media storage | Object storage (S3 / GCS) behind CDN | Storing binary in relational DB |

## Technology Selection Criteria

Evaluate technology choices on five factors:

| Factor | Questions to Answer | Weight |
|--------|--------------------|----|
| Fit | Does it solve the stated requirement without over-engineering? | High |
| Team familiarity | Does the team have production experience with this tech? | High |
| Ecosystem maturity | Active maintenance, large community, >3 years production history? | Medium |
| Operational cost | What does monitoring, debugging, and operating it require? | Medium |
| Vendor lock-in risk | Can we migrate if the vendor changes pricing or terms? | Low |

## Cross-Cutting Concerns Checklist

Architecture is incomplete without these cross-cutting decisions:

| Concern | Decision Required |
|---------|------------------|
| Authentication | Protocol (JWT / session / API key), token store, refresh strategy |
| Authorization | Model (RBAC / ABAC / ACL), enforcement point (API gateway / service / DB) |
| Observability | Log aggregation tool, metrics platform, distributed tracing |
| Error handling | Retry strategy, dead-letter queues, circuit breaker placement |
| Configuration | Secret storage (Vault / AWS Secrets Manager), feature flags platform |
| Deployment | Container orchestration, zero-downtime deployment strategy, rollback mechanism |
| Data backup | Backup frequency, recovery time objective (RTO), recovery point objective (RPO) |

## Trade-Off Documentation Format

For each major architecture decision, document the trade-off explicitly:

```
Decision: [What was decided]
Context: [Why a decision was needed]
Options considered:
  A) [Option A] — Pros: ... Cons: ...
  B) [Option B] — Pros: ... Cons: ...
  C) [Option C] — Pros: ... Cons: ...
Decision rationale: [Why option X was chosen over alternatives]
Consequences: [What becomes easier / harder with this choice]
Review trigger: [What condition would prompt reconsideration]
```

## Architecture Review Checklist

Before presenting the architecture for approval:

- [ ] Every component has a single-sentence responsibility statement
- [ ] Data ownership is explicit for each component (no shared mutable state between services)
- [ ] All interaction patterns are documented (sync/async/batch)
- [ ] Technology selections have documented rationale and alternatives considered
- [ ] All cross-cutting concerns have a defined solution
- [ ] No single point of failure exists without a documented mitigation
- [ ] Architecture can be operated by the current team without new tooling expertise
- [ ] Cost estimate at target scale is documented
