# Framework: Platform Scale Preparation

Reference for assessing platform readiness for scale events and executing preparation activities across compute, networking, data, and observability layers.

## Scale Event Classification

| Type | Description | Lead Time | Preparation Level |
|------|-------------|-----------|-----------------|
| Planned peak (predictable) | Black Friday, product launch, marketing campaign | ≥ 2 weeks | Full preparation |
| Planned growth (gradual) | Quarterly user growth trajectory | ≥ 1 quarter | Progressive preparation |
| Unexpected spike (reactive) | Viral moment, PR event, partner integration | < 24 hours | Emergency runbook |
| Architecture-driven (proactive) | Pre-scaling before known limits are reached | ≥ 1 quarter | Architectural preparation |

## Scale Readiness Assessment

Evaluate platform readiness across 6 dimensions before any scale event:

### Dimension 1: Compute Capacity

| Check | Current State | Target State | Gap |
|-------|--------------|-------------|-----|
| Max instance count (auto-scaling limit) | [N] | [N × scale factor] | [N additional] |
| Instance launch time | [X min] | [< 2 min] | |
| Container image pull time | [X sec] | [< 30 sec] | |
| CPU headroom at current peak | [X%] | [≥ 40% headroom] | |
| Memory headroom at current peak | [X%] | [≥ 30% headroom] | |

### Dimension 2: Database Capacity

| Check | Current State | Target State | Gap |
|-------|--------------|-------------|-----|
| Max connections | [N] | [N × instances × pool size] | |
| Read replica count | [N] | [N] | |
| IOPS headroom at peak | [X%] | [≥ 40% headroom] | |
| Query p99 latency at current peak | [X ms] | [< SLO] | |
| Slow query backlog | [N identified] | [0 unoptimized for scale path] | |

### Dimension 3: Caching

| Check | Current State | Target State | Gap |
|-------|--------------|-------------|-----|
| Cache hit rate at peak | [X%] | [≥ 80%] | |
| Cache memory headroom | [X%] | [≥ 30%] | |
| Cache eviction rate | [X/sec] | [< 1% of key space/min] | |
| Hot key analysis completed | [Yes/No] | Yes | |

### Dimension 4: Network and Load Balancing

| Check | Current State | Target State | Gap |
|-------|--------------|-------------|-----|
| Load balancer request limit | [N/sec] | [N × scale factor] | |
| CDN cache-hit ratio | [X%] | [≥ 90% for cacheable content] | |
| DNS TTLs reviewed | [X sec] | [< 60 sec for critical records] | |
| Bandwidth headroom | [X%] | [≥ 50% headroom] | |

### Dimension 5: Observability

| Check | Current State | Target State | Gap |
|-------|--------------|-------------|-----|
| Monitoring dashboards ready | [Yes/No] | Yes — dedicated scale-event dashboard | |
| Alert thresholds calibrated for higher traffic | [Yes/No] | Yes — prevent false positive storms | |
| Log volume capacity at 5× current rate | [Assessed] | [No log loss or sampling at 5×] | |
| On-call engineer briefed | [Yes/No] | Yes | |

### Dimension 6: Runbooks

| Check | Current State | Target State | Gap |
|-------|--------------|-------------|-----|
| Scale-up runbook exists | [Yes/No] | Yes and tested | |
| Scale-down runbook exists | [Yes/No] | Yes | |
| Emergency rollback runbook exists | [Yes/No] | Yes | |
| Runbooks reviewed in last 30 days | [Yes/No] | Yes | |

## Scale Preparation Checklist

### 2 Weeks Before Scale Event

- [ ] Capacity forecast completed (expected peak traffic × 1.5 safety factor)
- [ ] Auto-scaling limits increased to support forecast
- [ ] Load test completed at expected peak × 1.5
- [ ] Database connection pool sized for scaled instance count
- [ ] Read replica count increased if read-heavy workload
- [ ] CDN rules reviewed; cacheable content confirmed cached
- [ ] Monitoring alert thresholds adjusted for higher baseline

### 1 Week Before Scale Event

- [ ] All runbooks reviewed and updated
- [ ] On-call rotation covers scale event window (no vacations)
- [ ] Scale-up runbook dry-run completed
- [ ] Third-party API rate limits confirmed with providers
- [ ] Feature flags reviewed — any features that could disable if needed
- [ ] Support team briefed on expected traffic increase

### Day of Scale Event

- [ ] Scale-event monitoring dashboard open and tracking
- [ ] Team in communication channel for real-time coordination
- [ ] Pre-scaling executed (if planned): scale to target capacity proactively
- [ ] Rollback decision criteria pre-agreed (when to rollback vs. scale further)

## Scale-Down Criteria

After a scale event, return to baseline when:

| Condition | Action |
|-----------|--------|
| Traffic returns to within 20% of pre-event baseline for 2 consecutive hours | Begin gradual scale-down |
| All SLOs met at reduced capacity | Confirm scale-down safe |
| No active incidents | Proceed with scale-down |

**Scale-down rate**: Reduce capacity by 20% every 15 minutes (avoid sudden drops causing a second incident).

## Post-Scale Event Review

| Topic | Review Question |
|-------|---------------|
| Capacity headroom | Was headroom sufficient? Too much? Wasted cost? |
| Auto-scaling performance | Did auto-scaling trigger correctly and recover quickly? |
| Monitoring | Were all issues caught by monitoring before user impact? |
| Runbook accuracy | Were runbooks accurate and executable under pressure? |
| Cost | What was the cost delta? Was it expected? |
