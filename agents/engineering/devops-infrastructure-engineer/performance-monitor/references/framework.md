# Framework: Performance Monitor

Defines the metric hierarchy, SLO model, alerting strategy, and DORA-aligned monitoring practices for production performance monitoring.

## The Four Golden Signals (Google SRE)

Every production service must instrument and alert on all four:

| Signal | Primary Metric | Unit | Alert Threshold Guidance |
|--------|---------------|------|-------------------------|
| Latency | p50 / p95 / p99 request duration | milliseconds | Alert on p95 and p99; never alert on mean |
| Traffic | Requests per second | req/s | Track for capacity planning; alert on sudden drops (traffic loss) |
| Errors | Error rate (5xx / non-2xx) | % | Alert when error rate exceeds SLO error budget burn |
| Saturation | CPU, memory, disk, connection pool utilization | % | Alert at 80% sustained for 5+ minutes |

## SLO Framework

### SLO Hierarchy

```
SLA (customer-facing commitment)
  └── SLO (internal target, stricter than SLA)
        └── SLI (the metric that measures SLO compliance)
              └── Error Budget (1 - SLO) — consumed by incidents and deploys
```

### Recommended SLO Tiers

| Service Tier | Availability SLO | p99 Latency SLO | Error Budget (30-day) |
|-------------|-----------------|-----------------|----------------------|
| Critical (revenue-blocking) | 99.9% | < 500ms | 43.8 minutes |
| Standard (user-facing) | 99.5% | < 1,000ms | 3.6 hours |
| Internal (service-to-service) | 99.0% | < 2,000ms | 7.2 hours |
| Background (async, batch) | 95.0% | < 10,000ms | 36 hours |

### Error Budget Burn Rate Alerting (Multi-window)

Alert on burn rate, not raw error rate — this detects both slow leaks and fast burns:

| Alert | Burn Rate | Lookback Window | Severity | Action |
|-------|-----------|----------------|----------|--------|
| Fast burn (page) | > 14.4× | 1 hour + 5 minute | P1 | Page on-call immediately |
| Slow burn (ticket) | > 6× | 6 hour + 30 minute | P2 | Create incident ticket |
| Budget warning | > 1× for > 3 days | Daily | P3 | Engineering team review |

## Metric Catalog Standard

Every service must define a metric catalog before going to production:

| Metric Name | Type | Labels Required | SLO Mapped | Alert Configured |
|-------------|------|----------------|-----------|-----------------|
| `http_request_duration_seconds` | Histogram | service, route, method, status_code | Latency SLO | Yes |
| `http_requests_total` | Counter | service, route, method, status_code | Availability SLO | Yes (drop detection) |
| `process_cpu_seconds_total` | Counter | service, instance | Saturation | Yes (80% for 5m) |
| `process_resident_memory_bytes` | Gauge | service, instance | Saturation | Yes (85% for 5m) |
| `db_connection_pool_active` | Gauge | service, db_host | Saturation | Yes (90% for 2m) |
| [Business metric] | Counter/Gauge | service, outcome | Business SLO | Yes |

## DORA Metrics Integration

Incorporate DORA metrics into the monitoring framework:

| DORA Metric | Measurement Source | Target (Elite Performer) |
|-------------|-------------------|--------------------------|
| Deployment Frequency | CI/CD pipeline events | Multiple times per day |
| Lead Time for Changes | Commit timestamp → deploy timestamp | < 1 hour |
| Change Failure Rate | Deployments triggering P1/P2 incidents ÷ total deployments | < 5% |
| Mean Time to Restore (MTTR) | Incident open → resolved timestamp | < 1 hour |

## Dashboard Structure

Every service dashboard must contain these panels in order:

1. **SLO Burn Rate** — primary health indicator (top of dashboard)
2. **Error Rate** — by route and status code
3. **Latency Distribution** — p50/p95/p99 time series
4. **Traffic Volume** — request rate with deployment markers
5. **Saturation** — CPU, memory, connection pool
6. **Business Metrics** — service-specific (conversion rate, queue depth, job success rate)
7. **Dependency Health** — downstream service error rates and latency
