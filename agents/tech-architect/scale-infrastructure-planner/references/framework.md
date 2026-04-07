# Framework: scale-infrastructure-planner

Defines the methodology for producing infrastructure scaling plans that are cost-aware, phased, and operationally safe.

## Scale Dimension Reference

### Canonical Bottleneck Order

Infrastructure bottlenecks typically appear in this order as load increases. Investigate in sequence before jumping to complex solutions:

| Order | Bottleneck | Typical Symptom | First Remedy |
|-------|-----------|-----------------|--------------|
| 1 | Database connection pool | Query timeouts at moderate load | PgBouncer / connection pooler |
| 2 | Slow queries / missing indexes | CPU spike on DB server | EXPLAIN ANALYZE; add indexes |
| 3 | Application server CPU | Response time degrades linearly | Horizontal scaling of app tier |
| 4 | Memory / object allocation | GC pauses; OOM restarts | Memory limit tuning; object pooling |
| 5 | Network bandwidth | Throughput plateau | CDN offload; payload compression |
| 6 | Storage IOPS | Disk write latency spikes | SSD-backed volumes; read replicas |
| 7 | Third-party API rate limits | 429 errors at scale | Queue + retry; caching |

## Scaling Strategy Decision Matrix

| Component | Traffic Pattern | Recommended Strategy |
|-----------|----------------|---------------------|
| Stateless API server | Bursty, predictable | Horizontal auto-scaling (HPA / ASG); target 70% CPU utilisation |
| Stateless API server | Baseline + sudden spikes | Pre-scaled capacity + burst buffer; warm-up time matters |
| Relational database (read-heavy) | Growing read traffic | Read replicas with connection-aware routing |
| Relational database (write-heavy) | Growing write traffic | Vertical scaling first; sharding only after exhausting vertical |
| Cache layer | High hit rate desired | Redis cluster with consistent hashing; target > 90% hit rate |
| Job queue | Variable throughput | Worker auto-scaling based on queue depth; dead-letter queues |
| Object storage | Growing asset volume | CDN in front; lifecycle policies for cold storage tiering |
| Search index | Growing document count | Elasticsearch / OpenSearch with shard rebalancing plan |

## Capacity Alert Thresholds

Define monitoring alerts at these standard thresholds to trigger action before limits are hit:

| Resource | Warning | Critical | Action Trigger |
|----------|---------|----------|----------------|
| CPU utilisation | 70% | 85% | Scale out application tier |
| Memory utilisation | 75% | 90% | Investigate leak; scale vertical |
| DB connection pool | 70% of max connections | 85% | Add pooler; increase pool size |
| Disk utilisation | 70% | 85% | Provision additional storage |
| Queue depth | 2× baseline | 5× baseline | Scale workers; investigate consumers |
| Cache eviction rate | > 5% of keyspace/hour | > 15% | Increase cache memory; review TTLs |
| Error rate | > 0.1% of requests | > 1% | PagerDuty; stop rollout |

## Cost Projection Model

Use this model to estimate infrastructure cost at target scale:

```
Projected Monthly Cost =
  (App Tier Units × Unit Cost × Hours/Month)
  + (DB Instance Cost × Replica Count)
  + (Storage GB × Storage Unit Cost)
  + (Egress GB × Egress Unit Cost)
  + (Cache Tier Cost)
  + (Queue / Message Cost)
```

**Cost optimisation levers by priority:**
1. Reserved instances / committed-use discounts (1-year = ~30% savings; 3-year = ~50%)
2. Spot / preemptible instances for fault-tolerant workloads (up to 80% savings)
3. Right-sizing (eliminate over-provisioned instances; run at 70–80% utilisation)
4. Tiered storage (move data > 90 days old to cold storage automatically)
5. CDN offload (reduce origin egress by 60–90% for static/cacheable content)

## Migration Safety Patterns

| Migration Type | Risk Level | Safety Pattern |
|----------------|------------|----------------|
| Adding read replica | Low | Blue-green with read-replica lag monitoring |
| Changing DB instance size | Medium | Maintenance window; test on staging first |
| Horizontal scale-out (stateless) | Low | Rolling deployment; traffic shift via load balancer |
| Database sharding | High | Dual-write migration; canary shard first |
| Storage migration | Medium | Parallel writes; verify checksums before cutover |
| Cache layer introduction | Low | Cache-aside pattern; monitor hit rate for 48h before removing direct reads |

## Time Horizon Planning Model

| Horizon | Focus | Key Deliverable |
|---------|-------|-----------------|
| 0–3 months | Fix current bottlenecks | Capacity gap analysis + remediation plan |
| 3–6 months | Proactive headroom | Scaling strategy per component + cost projection |
| 6–12 months | Architecture evolution | ADR for structural changes (sharding, microservices splits) |
| 12–24 months | Platform investment | Build vs. buy decisions; multi-region architecture |
