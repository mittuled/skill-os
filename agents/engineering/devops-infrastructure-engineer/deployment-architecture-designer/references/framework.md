# Framework: deployment-architecture-designer

Defines architecture patterns, evaluation criteria, and decision frameworks for designing deployment topologies.

## Deployment Model Selection

| Model | Best For | Operational Maturity Required | Cost Profile |
|-------|---------|-------------------------------|-------------|
| Kubernetes (managed: EKS/GKE/AKS) | Microservices, large teams, complex traffic management | High | Medium-High (savings with spot/preemptible nodes) |
| Serverless (Lambda/Cloud Functions) | Event-driven workloads, unpredictable traffic, low ops overhead | Low | Pay-per-invocation (can be high at scale) |
| Container platform (ECS/Cloud Run) | Teams transitioning from VMs, moderate complexity | Medium | Medium |
| VMs (EC2/GCE with ASG) | Stateful workloads, legacy apps, simple horizontal scaling | Low-Medium | Medium |
| Hybrid | Mixed workloads, gradual migration | Varies | Varies |

**Decision rule**: Choose the model matching team operational maturity first, performance second, cost third. A Kubernetes cluster operated by a team without Kubernetes expertise is a reliability liability.

## Environment Topology Standards

| Environment | Required | Scale | Data Isolation |
|-------------|---------|-------|----------------|
| Development | Yes | Minimal (single replicas) | Isolated dev data only |
| Staging | Yes | 30–50% of production | Synthetic or anonymized production data |
| Production | Yes | Full scale with auto-scaling | Live user data |
| DR (disaster recovery) | For SLO ≥ 99.9% | Active-passive or active-active | Replicated from production |
| Canary | When canary deployments used | Proportional to canary % | Shared with production |

## Service Communication Patterns

| Pattern | Use When | Protocol | Failure Mode |
|---------|---------|---------|-------------|
| Synchronous REST/gRPC | Real-time queries, < 200ms SLA | HTTP/2, mTLS | Circuit breaker + retry with exponential backoff |
| Asynchronous messaging | Background work, decoupled services | Kafka, SQS, Pub/Sub | Dead letter queue + alerting |
| Event streaming | Real-time data pipelines, fan-out | Kafka | Consumer lag monitoring + replay |
| Service mesh (Istio/Linkerd) | Many services with complex traffic policies | mTLS automatic | Managed retries, traffic shifting |

## Network Design Standards

### Segmentation Model

```
Internet → CDN/WAF → Public Load Balancer (ingress layer)
                          ↓
                    DMZ Subnet (API gateway, reverse proxy)
                          ↓
                    App Subnet (services, stateless compute)
                          ↓
                    Data Subnet (databases, caches, queues)
                          ↓
                    Management Subnet (monitoring, logging, bastion)
```

- Default-deny between subnets; explicit allowlist rules only
- No direct internet access from App or Data subnets
- Database subnets: allow inbound from App subnet only on service port

### Security Group / Network Policy Rules

| Rule | Direction | From | To | Port | Rationale |
|------|-----------|------|-----|------|-----------|
| App to DB | Inbound (DB SG) | App subnet CIDR | DB | 5432 (PG) / 3306 (MySQL) | Principle of least privilege |
| App to cache | Inbound (Cache SG) | App subnet CIDR | Cache | 6379 (Redis) | — |
| Internet to LB | Inbound (LB SG) | 0.0.0.0/0 | LB | 443 only | TLS termination at edge |
| LB to app | Inbound (App SG) | LB SG reference | App | Service port | Not IP-based (SG reference) |

## High Availability Patterns

| SLO Target | HA Pattern | Minimum Deployment |
|-----------|-----------|-------------------|
| 99.0% | Single AZ with health checks | 2 replicas, one AZ |
| 99.5% | Multi-AZ active-active | 2+ replicas per AZ, 2 AZs |
| 99.9% | Multi-AZ with auto-scaling | 3+ replicas across 3 AZs |
| 99.99% | Multi-region active-active | Independent regional stacks |

## Artifact Flow Pattern

```
Developer push → CI builds → SHA-tagged immutable image → Registry
                                                               ↓
                                                        Dev deployment (automatic on merge to dev branch)
                                                               ↓
                                                        Staging deployment (automatic on merge to main)
                                                               ↓
                                                        Production deployment (approval gate + progressive rollout)
```

Rule: Artifacts are promoted between environments — never rebuilt. The same image SHA runs in staging and production.

## Architecture Decision Record (ADR) Template Fields

Every significant deployment architecture decision requires an ADR:
- **Status**: Proposed / Accepted / Superseded
- **Context**: What problem prompted this decision?
- **Decision**: What was decided?
- **Rationale**: Why was this chosen over alternatives?
- **Alternatives considered**: What other options were evaluated?
- **Consequences**: What are the tradeoffs and risks?
