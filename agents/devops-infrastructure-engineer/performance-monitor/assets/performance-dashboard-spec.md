# Performance Monitoring Dashboard Spec: [Service Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | DevOps / Infrastructure Engineer |
| Service | [Service name] |
| Tool | [Datadog / Grafana + Prometheus / CloudWatch / New Relic] |
| Skill | performance-monitor |
| Status | [Spec / Implemented / Active] |

## Dashboard Purpose

Monitor the performance and health of [service] across the four golden signals: latency, traffic, errors, and saturation.

## SLO Reference

| SLO | Target | Measurement Window |
|-----|--------|-------------------|
| Availability | [99.9%] | 30-day rolling |
| p99 latency | [< 500ms] | Per-request |
| Error rate | [< 0.1%] | 5-minute rolling |

## Dashboard Panels

### Row 1: Service Health Overview

**Panel 1.1: SLO Burn Rate (Error Budget)**
- Metric: 1h burn rate and 6h burn rate
- Display: Status badge (green/yellow/red) + burn rate value
- Alert: 1h burn > 14.4× (critical) or 6h burn > 6× (warning)

**Panel 1.2: Uptime (Availability)**
- Metric: `1 - (error_requests / total_requests)` over 30 days
- Display: Single stat — percentage with color coding

**Panel 1.3: Service Status**
- Metric: Health check endpoint up/down
- Display: Green = UP / Red = DOWN

---

### Row 2: Request Metrics (RED)

**Panel 2.1: Request Rate**
- Metric: `rate(http_requests_total[5m])`
- Display: Time series; 7-day overlay
- Alert: Drop > 50% vs. 7-day avg (pipeline failure)

**Panel 2.2: Error Rate**
- Metric: `rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m])`
- Display: Time series with SLO reference line
- Alert: > 0.1% for 2 min (warning); > 1% for 1 min (critical)

**Panel 2.3: Latency Distribution**
- Metrics: p50, p95, p99 from histogram
- Display: Three time-series lines on same chart
- Alert: p99 > SLO threshold for 5 min (critical)

**Panel 2.4: Latency Heatmap**
- Metric: Request duration histogram
- Display: Heatmap — x=time, y=latency bucket, color=request density

---

### Row 3: Resource Saturation

**Panel 3.1: CPU Utilization**
- Metric: Per-instance CPU %
- Display: Time series (avg + max)
- Alert: Avg > 80% for 5 min

**Panel 3.2: Memory Utilization**
- Metric: Per-instance memory %
- Display: Time series (avg + max)
- Alert: Avg > 85% for 5 min

**Panel 3.3: Instance Count**
- Metric: Running instance count vs. desired count
- Display: Time series (shows auto-scaling events)

**Panel 3.4: DB Connection Pool**
- Metric: Active connections / max connections
- Display: Gauge + time series
- Alert: > 80% of pool used

---

### Row 4: Upstream Dependencies

**Panel 4.1: Database Latency**
- Metric: DB query duration p50/p95/p99
- Display: Time series

**Panel 4.2: Cache Hit Rate**
- Metric: `cache_hits / (cache_hits + cache_misses)`
- Display: Percentage time series
- Alert: < 70% hit rate for 10 min

**Panel 4.3: Third-Party API Success Rate**
- Metric: Per-provider success rate
- Display: Time series per provider

---

### Row 5: Business Metrics (Service-Specific)

**Panel 5.1: [Primary Business Metric]**
- Metric: [e.g., orders_created_total rate, signups_total rate]
- Display: Time series with 7-day overlay
- Alert: Drop > 30% vs. 7-day avg

**Panel 5.2: [Secondary Business Metric]**
- Metric: [e.g., payment_success_rate]
- Display: Percentage time series

## Alert Summary

| Alert | Condition | Severity | Runbook |
|-------|-----------|---------|---------|
| SLO critical burn | 1h burn > 14.4× | P1 | [Link] |
| High error rate | > 1% for 1 min | P1 | [Link] |
| p99 latency breach | > SLO for 5 min | P1 | [Link] |
| High CPU | Avg > 80% for 5 min | P2 | [Link] |
| DB pool exhaustion | > 80% connections used | P2 | [Link] |
| Low cache hit rate | < 70% for 10 min | P2 | [Link] |
| Request volume drop | > 50% below 7d avg | P1 | [Link] |
| Business metric drop | > 30% below 7d avg | P1 | [Link] |

## Baseline Values (Captured at Initial Deploy)

| Metric | Baseline | Notes |
|--------|---------|-------|
| Request rate (peak) | [X req/s] | |
| p99 latency | [X ms] | |
| Error rate | [X%] | |
| CPU avg | [X%] | |
| Memory avg | [X%] | |
| Cache hit rate | [X%] | |
