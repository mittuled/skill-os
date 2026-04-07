# Production Instrumentation Verification — Notification Service v2

| Field | Value |
|---|---|
| Date | 2026-03-31 |
| Author | QA Test Engineer |
| Release | Notification Service v2 Production Deploy |
| Recommendation | INVESTIGATE MISSING SIGNALS |
| Rollback Recommended | No |
| Skill | instrumentation-verifier-prod |

## Recommendation

**INVESTIGATE MISSING SIGNALS** — 1 metric not appearing in Prometheus (`notification.queue.depth`). Likely a scrape configuration issue. Core delivery metrics are healthy. No rollback required, but missing metric must be resolved within 2 hours or on-call alerting for queue depth will be blind.

---

## Verification Summary

| Signal | Type | Status | Notes |
|---|---|---|---|
| notification.sent | Metric | HEALTHY | |
| notification.delivery.latency | Metric | HEALTHY | |
| notification.failed | Log Entry | HEALTHY | |
| notification.request.trace | Trace Span | PAYLOAD ISSUE | channel = 'undefined' |
| notification.queue.depth | Metric | MISSING | Not in Prometheus — scrape config suspect |

---

## Missing Signals

### notification.queue.depth

Queue depth metric not appearing in Prometheus. The metric is defined in the application code but the Prometheus scrape target may not be configured to include the new service endpoint.

**Investigation steps:**
1. Check Prometheus targets endpoint (`/prometheus/targets`) for notification-service-v2
2. Verify the scrape config includes the new service port
3. If scrape config is correct, check metric name registration in application startup logs

**Owner:** DevOps Engineer
**Deadline:** Within 2 hours (queue depth alert depends on this metric)

---

## Payload Issues

### notification.request.trace — channel attribute undefined

Trace span fires correctly but `channel` attribute shows 'undefined'. This makes it impossible to filter traces by notification channel type (email vs. SMS) in Jaeger.

**Fix:** Review the span creation code — the `channel` variable may be accessed before it is set in the request context. This is a P3 fix; does not impact alerting but degrades observability quality.

---

## Overall Assessment

Core delivery instrumentation is healthy — `sent`, `latency`, and `failed` signals confirm the service is operating correctly in production. The missing queue depth metric is an operational risk (not a feature risk) and must be resolved before the on-call team's queue backpressure alert becomes unreliable.
