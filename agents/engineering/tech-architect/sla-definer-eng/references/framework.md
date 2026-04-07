# Framework: sla-definer-eng

Defines the methodology for translating business reliability requirements into measurable SLIs, SLOs, and error budgets.

## SLI / SLO / SLA Hierarchy

```
SLI (Service Level Indicator): What you measure
  └── SLO (Service Level Objective): What you target internally
        └── SLA (Service Level Agreement): What you commit to customers
```

**Rule**: SLO targets must be stricter than SLA commitments. If the SLA is 99.9%, the internal SLO should be 99.95% to provide a buffer for measurement variance and incident response time.

## SLI Catalog by Service Type

### HTTP API Service

| SLI | Definition | Measurement Method |
|-----|-----------|-------------------|
| Availability | % of requests returning non-5xx response | `(total_requests - error_requests) / total_requests` |
| Latency | % of requests completing within threshold | `histogram_quantile(0.99, rate(http_request_duration_seconds))` |
| Error rate | % of requests returning 5xx | `rate(http_requests_total{status=~"5.."}[5m])` |
| Saturation | CPU / memory / connection pool utilisation | Infrastructure metrics |

### Asynchronous Queue Worker

| SLI | Definition | Measurement Method |
|-----|-----------|-------------------|
| Processing availability | % of messages processed without error | `(processed - errors) / processed` |
| Processing latency | Time from message enqueue to completion (p99) | Custom event timestamp diff |
| Queue depth | Messages in queue waiting for processing | Queue monitor metric |
| Dead-letter rate | % of messages sent to DLQ | `dlq_messages / total_messages` |

### Batch Processing Pipeline

| SLI | Definition | Measurement Method |
|-----|-----------|-------------------|
| Job completion rate | % of scheduled jobs completing within SLO window | Job scheduler success/failure |
| Data freshness | Age of most recent successful run | `time_since_last_success` |
| Record error rate | % of records failing processing | `error_records / total_records` |

## SLO Target Reference by Service Criticality

| Criticality | Definition | Availability SLO | Latency SLO (p99) | Error Budget/Month |
|-------------|------------|-----------------|-------------------|--------------------|
| Critical | Revenue-generating; customer-facing | 99.95% | < 500ms | 21.9 min |
| High | Core product feature; internal tooling used daily | 99.9% | < 1s | 43.8 min |
| Medium | Supporting service; degraded UX if unavailable | 99.5% | < 2s | 3.65 hours |
| Low | Non-critical background jobs; admin tools | 99.0% | < 5s | 7.3 hours |

## Error Budget Policy

Define what happens as error budget is consumed:

| Budget Consumed | State | Policy |
|----------------|-------|--------|
| 0–50% | Healthy | Normal development; reliability work can be deferred |
| 50–75% | Caution | Pause non-critical deployments; investigate trend |
| 75–90% | Alert | No new feature deployments; reliability improvements only |
| 90–100% | Budget Frozen | Feature freeze; all engineering on reliability |
| > 100% (budget exhausted) | Violated | Incident review required; SLA breach notification process |

## Alerting Strategy: Multi-Window Burn Rate

Use multi-window burn rate alerts (Google SRE Book, Ch. 5) rather than simple threshold alerts:

| Burn Rate | Window | Severity | Response Time |
|-----------|--------|----------|---------------|
| 14.4× normal | 1h | Page (critical) | Immediate |
| 6× normal | 6h | Page (high) | < 30 minutes |
| 3× normal | 24h | Ticket (medium) | Same business day |
| 1× normal | 3 days | Informational | Investigate in next sprint |

A burn rate of 1× means consuming error budget exactly at the target rate. A 14.4× burn rate over 1 hour consumes 1% of the monthly budget.

## Nines Reference Table

| Availability | Monthly Downtime | Weekly Downtime | Hourly Downtime |
|-------------|-----------------|-----------------|-----------------|
| 99.0% | 7.3 hours | 1.68 hours | N/A |
| 99.5% | 3.65 hours | 50.4 minutes | N/A |
| 99.9% | 43.8 minutes | 10.1 minutes | N/A |
| 99.95% | 21.9 minutes | 5.04 minutes | N/A |
| 99.99% | 4.38 minutes | 1.01 minutes | N/A |
