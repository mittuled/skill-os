# Infrastructure Load Test Plan: [Service / System Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | DevOps / Infrastructure Engineer |
| Service | [Service name] |
| Environment | [Staging / Performance / Isolated production clone] |
| Test Tool | [k6 / Gatling / Locust / Artillery] |
| Skill | infrastructure-load-testing |
| Status | [Draft / Approved / Running / Complete] |

## Objectives

1. **Establish baseline**: Confirm the system meets SLO targets under expected peak load.
2. **Find capacity ceiling**: Determine the maximum load before degradation occurs.
3. **Validate auto-scaling**: Confirm scale-out triggers correctly and new instances serve traffic within SLO.
4. **Identify bottlenecks**: Pinpoint which layer (app, DB, cache, network) saturates first.

## Test Scenarios

| Scenario | Virtual Users | Ramp | Duration | Purpose |
|----------|--------------|------|----------|---------|
| Baseline (smoke) | 10 | 0 min | 5 min | Confirm test infrastructure works |
| Expected peak | [X VUs] | 10 min | 30 min | Validate SLO at normal peak |
| Stress (150% peak) | [1.5×X VUs] | 10 min | 20 min | Find degradation point |
| Spike (300% peak, instant) | [3×X VUs] | 0 min | 10 min | Test spike resilience and recovery |
| Soak (expected peak, long) | [X VUs] | 10 min | 4 hours | Detect memory leaks or gradual degradation |

**Scenarios to execute this run**: [List which scenarios]

## Target Thresholds

| Metric | Pass | Warn | Fail |
|--------|------|------|------|
| p50 latency | < [X ms] | < [1.5×X ms] | > [1.5×X ms] |
| p95 latency | < [X ms] | < [1.5×X ms] | > [1.5×X ms] |
| p99 latency | < [X ms] | < [2×X ms] | > [2×X ms] |
| Error rate | < 0.1% | < 0.5% | > 0.5% |
| Throughput | > [X req/s] | | < [0.8×X req/s] |

## Test Endpoints

| Endpoint | Method | % of Traffic | Test Data |
|----------|--------|-------------|-----------|
| [/api/products] | GET | [40%] | [Product ID list — seed data] |
| [/api/cart] | POST | [20%] | [Synthetic cart payloads] |
| [/api/checkout] | POST | [5%] | [Test payment tokens — no real charges] |
| [/api/users/me] | GET | [35%] | [Test user accounts] |

## Infrastructure Monitoring Plan

Capture these during the test:

| Component | Metric | Tool | Alert Threshold |
|-----------|--------|------|----------------|
| App tier | CPU utilization | [Datadog / CloudWatch] | > 80% |
| App tier | Memory | [Datadog] | > 85% |
| Database | CPU | [RDS Metrics] | > 70% |
| Database | Connection count | [RDS Metrics] | > 80% of max |
| Database | Replication lag | [RDS Metrics] | > 5s |
| Cache | Hit rate | [ElastiCache] | < 80% |
| Cache | Memory | [ElastiCache] | > 85% |
| Load balancer | Active connections | [ALB Metrics] | > 70% of limit |
| Network | Bandwidth | [VPC Flow Logs] | > 80% of limit |

## Auto-Scaling Validation

| Event | Expected Behavior | Validation Method |
|-------|------------------|------------------|
| CPU > 70% for 2 min | New instance starts | Watch ASG activity log |
| New instance started | Health check passes within 5 min | ALB target group health |
| Load drops below 30% | Instance count decreases | ASG activity log |

## Test Data Requirements

| Data | Count | Source | Notes |
|------|-------|--------|-------|
| Test user accounts | [1,000] | [Pre-seeded in staging DB] | Do not use real users |
| Product catalog | [10,000 SKUs] | [Production clone — PII-stripped] | |
| Payment test tokens | [Stripe test cards] | [Stripe test mode] | No real charges |

## Execution Checklist

**Before test**:
- [ ] Test environment isolated from production
- [ ] Baseline metrics captured
- [ ] Test data seeded
- [ ] Monitoring dashboards open and recording
- [ ] Team briefed on test schedule

**During test**:
- [ ] Monitor all target metrics in real time
- [ ] Log any anomalies with timestamps
- [ ] Stop test immediately if production impact detected

**After test**:
- [ ] Metrics exported from monitoring tool
- [ ] Auto-scaling events logged
- [ ] Bottlenecks documented
- [ ] Report written with findings and recommendations
