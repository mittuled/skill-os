# Infrastructure Scaling Execution Log: [Service / Event Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Executor | DevOps / Infrastructure Engineer |
| Service | [Service name] |
| Scaling Event | [Planned peak / Unexpected load spike / Capacity increase] |
| Skill | infrastructure-scaling-executor |
| Status | [Planned / In Progress / Complete / Rolled Back] |

## Scaling Objective

**Reason**: [Planned peak event (Black Friday) / Unexpected traffic spike / Proactive capacity increase]
**Current capacity**: [X instances / Y vCPUs / Z GB RAM]
**Target capacity**: [N instances / M vCPUs / P GB RAM]
**Traffic increase expected**: [X% above normal peak]

## Pre-Scaling Checks

- [ ] Baseline metrics captured (see below)
- [ ] Database connection pool limits reviewed (pool size × max instances ≤ DB max_connections)
- [ ] Cache capacity sufficient for scaled instance count
- [ ] Downstream service capacity confirmed (won't become bottleneck)
- [ ] Scaling change tested in staging
- [ ] Rollback plan documented
- [ ] On-call engineer briefed

## Baseline Metrics (Before Scaling)

| Metric | Value | Timestamp |
|--------|-------|-----------|
| Instance count | [N] | [HH:MM UTC] |
| CPU utilization (avg) | [X%] | |
| Memory utilization (avg) | [X%] | |
| Request rate | [X req/sec] | |
| p99 latency | [X ms] | |
| Error rate | [X%] | |
| DB connections used | [X / max Y] | |

## Scaling Actions

| Time (UTC) | Action | Command / Console Path | Expected Result |
|-----------|--------|----------------------|----------------|
| [HH:MM] | [Increase min instance count from 3 to 10] | [kubectl scale / ASG update / Terraform apply] | [All 10 instances healthy within 5 min] |
| [HH:MM] | [Pre-warm cache] | [Cache warm script: path/to/script.sh] | [Cache hit rate > 80%] |
| [HH:MM] | [Increase DB max_connections] | [RDS parameter group update] | [Requires reboot — scheduled] |

## Post-Scaling Verification

### Instance Health

| Component | Target Count | Actual Running | Healthy? |
|-----------|-------------|---------------|---------|
| [Service A] | [N] | [N] | [Yes/No] |
| [Database connections] | [N available] | [N used] | [Yes/No] |
| [Cache] | — | [Hit rate X%] | [Yes/No] |

### Metrics After Scaling

| Metric | Before | After | Change | Target Met? |
|--------|--------|-------|--------|------------|
| Instance count | [N] | [M] | +[X] | [Yes] |
| CPU utilization (avg) | [X%] | [X%] | [+/-] | [< 70%] |
| p99 latency | [X ms] | [X ms] | [+/-] | [< SLO] |
| Error rate | [X%] | [X%] | [+/-] | [< 0.1%] |

## Scale-Down Plan

**Trigger for scale-down**: [Event ends on YYYY-MM-DD / Traffic returns to baseline for > 2 hours]
**Scale-down target**: [Return to X instances minimum]
**Scale-down method**: [Gradual over 30 min / Immediate]
**Scheduled scale-down**: [YYYY-MM-DD HH:MM UTC]

## Issues Encountered

| Issue | Time | Impact | Resolution |
|-------|------|--------|------------|
| [Issue] | [HH:MM] | [Impact description] | [How resolved] |

## Lessons Learned

1. [What to do differently next time]
2. [What worked well and should be repeated]
