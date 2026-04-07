# Framework: Infrastructure Requirements Extractor

Defines the structured approach for extracting and categorizing infrastructure requirements from product and engineering specifications.

## Extraction Domains

### Requirement Categories

| Domain | Key Signals to Extract | Quantification Target |
|--------|----------------------|----------------------|
| Compute | Request throughput, processing intensity, concurrency model | QPS, vCPU count, instance type |
| Storage | Data volume, growth rate, access pattern (read/write ratio), retention | GB/TB, IOPS, retention days |
| Networking | Bandwidth, latency targets, cross-region traffic, CDN needs | Mbps, RTT ms, availability zones |
| Security | Data classification, compliance obligations, encryption, audit trail | Regulatory scope, encryption standard |
| Monitoring | Alerting requirements, log retention, metrics resolution | Retention days, scrape interval |
| Compliance | Applicable regulations, data residency, audit trail requirements | Regulation names, jurisdiction |

## Extraction Workflow

### Step 1: Signal Identification

Read each specification section and tag infrastructure signals:

| Signal Type | Examples | Implied Requirement |
|-------------|----------|---------------------|
| Performance targets | "< 200ms p99 latency" | Compute sizing, caching layer |
| Availability targets | "99.9% uptime" | Multi-AZ, load balancer, failover |
| Data volume | "1M users, 10 events/day" | Storage growth rate, partition strategy |
| Compliance mention | "GDPR-regulated EU users" | Data residency, encryption at rest, audit trail |
| Integration point | "calls Stripe API" | Outbound network, secret management |
| Traffic pattern | "end-of-month spike 10x" | Auto-scaling group, burst capacity |

### Step 2: Quantification Method

Derive estimates using these formulas when explicit numbers are absent:

- **Storage growth**: `(avg_record_size_KB × daily_writes × 365) × (1 + index_overhead_factor)`
- **Peak QPS**: `(daily_active_users × avg_requests_per_session) / (active_hours × 3600) × peak_multiplier`
- **Bandwidth**: `peak_QPS × avg_response_size_KB / 1024` → Mbps

## Requirements Classification Matrix

| Priority | Criteria | Action |
|----------|----------|--------|
| P1 — Blocking | Capacity below minimum required for launch | Must provision before deploy |
| P2 — Required | Operational gap that causes degraded experience | Provision within sprint |
| P3 — Recommended | Best practice not yet implemented | Plan for next quarter |

## Cost Estimation Tiers

| Tier | Description | Use Case |
|------|-------------|----------|
| Minimum Viable | Smallest footprint that meets launch requirements | Early-stage, cost-constrained |
| Recommended | Right-sized for 12-month growth with auto-scaling | Standard production |
| High-availability | Full multi-region, maximum redundancy | Mission-critical, enterprise SLA |

## Dependency Classification

| Type | Definition | Planning Implication |
|------|------------|---------------------|
| Shared existing | Relies on infrastructure owned by another team | Requires capacity reservation request |
| New owned | Net-new infrastructure owned by this service | Must be provisioned and operated |
| Third-party managed | External SaaS (e.g., Stripe, Twilio) | Contract review, SLA alignment |
| New shared | Infrastructure that will be shared with other services | Requires platform team review |
