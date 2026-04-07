# Performance Test Report: [Service / Endpoint Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | QA / Test Engineer |
| Service | [Service name] |
| Environment | [Staging / Performance / Production (read-only)] |
| Test Tool | [k6 / Gatling / Locust / JMeter] |
| Skill | performance-tester |
| Build / Commit | [Git SHA or build number] |
| Status | [Pass / Fail / Conditional Pass] |

## Executive Summary

[2–3 sentences covering the verdict, key metric against target, and single most critical finding.
GUIDANCE: Lead with pass/fail — "Performance test FAILED. p99 latency for POST /api/checkout reached 4,200 ms under 500 concurrent users — 4× above the 1,000 ms SLO. Root cause traced to N+1 query in OrderService.createOrder(); optimization required before production release."]

**Verdict**: [PASS / FAIL / CONDITIONAL PASS]
**Test scenario**: [Load / Stress / Spike / Soak / Smoke]
**Peak load tested**: [X virtual users / X req/sec]

## Test Scenarios

| Scenario | Virtual Users | Ramp-Up | Duration | Test Type |
|----------|--------------|---------|----------|-----------|
| Smoke | 1–5 | 0 min | 5 min | Baseline validation |
| Load | [Expected peak VUs] | 5 min | 30 min | Normal production load |
| Stress | [150% of peak VUs] | 5 min | 20 min | Capacity ceiling |
| Spike | [300% of peak, instant] | 0 min | 10 min | Burst tolerance |
| Soak | [Expected peak VUs] | 5 min | 4 hrs | Memory leak / resource exhaustion |

**Scenario executed this run**: [Load / Stress / Spike / Soak]

## Target Thresholds

| Metric | Target (SLO) | Warning | Critical |
|--------|-------------|---------|---------|
| p50 latency | [< X ms] | [> X ms] | [> X ms] |
| p95 latency | [< X ms] | [> X ms] | [> X ms] |
| p99 latency | [< X ms] | [> X ms] | [> X ms] |
| Error rate | [< 0.1%] | [> 0.5%] | [> 1%] |
| Throughput | [≥ X req/sec] | [< X req/sec] | [< X req/sec] |
| Max concurrent users | [≥ X] | | |

## Results Summary

### Key Metrics

| Metric | Baseline | Load Test Result | Stress Test Result | Status |
|--------|----------|-----------------|-------------------|---------| 
| p50 latency | [X ms] | [X ms] | [X ms] | [Pass/Fail] |
| p95 latency | [X ms] | [X ms] | [X ms] | [Pass/Fail] |
| p99 latency | [X ms] | [X ms] | [X ms] | [Pass/Fail] |
| Error rate | [X%] | [X%] | [X%] | [Pass/Fail] |
| Throughput | [X req/s] | [X req/s] | [X req/s] | [Pass/Fail] |
| Memory usage (peak) | [X MB] | [X MB] | [X MB] | [Pass/Fail] |
| CPU usage (peak) | [X%] | [X%] | [X%] | [Pass/Fail] |

### Throughput Over Time

[Reference Grafana / k6 dashboard screenshot or describe trend]

```
Time (min) | Req/sec | Error rate | p99 latency
0–5        | [ramp]  | [X%]       | [X ms]
5–15       | [peak]  | [X%]       | [X ms]
15–25      | [peak]  | [X%]       | [X ms]
25–30      | [ramp-down] | [X%]  | [X ms]
```

### Bottleneck Analysis

| Layer | Finding | Impact | Priority |
|-------|---------|--------|---------|
| Database | [N+1 query on order creation] | p99 +3,200 ms | P1 |
| Application | [Thread pool saturation at 500 VU] | Error rate 8% | P1 |
| Infrastructure | [CPU throttled at 80% at 400 VU] | p95 degrades] | P2 |
| Network | [None detected] | — | — |
| Cache | [Cache miss rate 40% — cold start] | p95 +200 ms | P3 |

## Failing Checks

| Check | Target | Actual | Status |
|-------|--------|--------|--------|
| [p99 < 1000ms] | 1,000 ms | [4,200 ms] | FAIL |
| [Error rate < 0.1%] | 0.1% | [0.08%] | PASS |

## Recommendations

| Priority | Action | Expected Impact | Owner | Ticket |
|----------|--------|----------------|-------|--------|
| P1 | [Fix N+1 query in OrderService] | p99 -3,000 ms est. | [Backend team] | [Link] |
| P2 | [Increase thread pool size from 50 to 200] | Error rate at 500 VU eliminated | [Backend team] | [Link] |
| P3 | [Pre-warm cache on deploy] | p95 -200 ms at cold start | [Backend team] | [Link] |

## Infra Observations

| Resource | Baseline | Peak Load | Stress Peak | Notes |
|----------|----------|-----------|-------------|-------|
| App CPU | [X%] | [X%] | [X%] | [Throttled at X%] |
| App Memory | [X MB] | [X MB] | [X MB] | [No leak observed / Leak at 4h mark] |
| DB connections | [X] | [X] | [X] | [Pool exhausted at X VU] |
| DB CPU | [X%] | [X%] | [X%] | |

## Appendix: Test Script Reference

**Test script location**: [Git path or link]
**Data set used**: [Synthetic / Anonymized prod sample — N records]
**Seed data**: [How test accounts and data were created]
