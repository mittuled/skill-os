# Checklist: Observability Instrumentation Implementation

Comprehensive checklist for implementing production-grade structured logging, metrics, and distributed tracing. Aligned with OpenTelemetry standards, Prometheus metrics conventions, and structured logging best practices.

## How to Use

Work through each section in sequence. Mark items `[x]` when verified. Items marked `[REQUIRED]` are non-negotiable for production observability. Items marked `[RECOMMENDED]` are best practices that significantly improve incident response speed.

---

## Section 1: Library and Configuration Setup

- [ ] `[REQUIRED]` OpenTelemetry SDK installed and configured (or equivalent: Prometheus client, structured logger)
- [ ] `[REQUIRED]` Exporters configured for all three signals:
  - Traces: OTLP exporter → trace backend (Jaeger, Tempo, Datadog, etc.)
  - Metrics: Prometheus exporter or OTLP exporter → metrics backend
  - Logs: Structured log shipper (Fluentd, Vector, Logstash) → log backend (Loki, CloudWatch, Datadog)
- [ ] `[REQUIRED]` Service name, service version, and environment attributes set on the resource (these appear on every signal)
- [ ] `[REQUIRED]` Instrumentation libraries configured for framework (HTTP, gRPC, database, etc.) — use auto-instrumentation where available
- [ ] `[RECOMMENDED]` Sampling strategy configured for traces (not 100% if high-throughput; use tail-based sampling for error preservation)

---

## Section 2: Structured Logging

- [ ] `[REQUIRED]` All log output is structured (JSON) — no unstructured string concatenation
- [ ] `[REQUIRED]` Log levels used correctly:
  - `ERROR`: Unhandled exceptions, service degradation
  - `WARN`: Recoverable issues, exceeded thresholds, retries
  - `INFO`: Service lifecycle events, business milestones
  - `DEBUG`: Detailed diagnostic data (disabled in production by default)
- [ ] `[REQUIRED]` Every log entry at INFO+ includes: `timestamp`, `level`, `service`, `trace_id`, `span_id`, `message`
- [ ] `[REQUIRED]` Request-scoped context propagated to all log statements within the request: `request_id`, `user_id` (or session token — not PII directly), `operation`
- [ ] `[REQUIRED]` Error logs include: `error.type`, `error.message`, `error.stack` (server-side only)
- [ ] `[REQUIRED]` PII and secrets absent from all log output — verified with a log sample review
- [ ] `[REQUIRED]` Duration logged for every external call (database, external API) at DEBUG with latency at WARN if exceeds threshold
- [ ] `[RECOMMENDED]` Correlation ID propagated across service boundaries via HTTP header (`X-Correlation-ID` or `traceparent`)
- [ ] `[RECOMMENDED]` Log output format validated against log shipper schema (no log parsing errors in staging)

---

## Section 3: Metrics Implementation

### Counter Metrics (for totals and rates)

- [ ] `[REQUIRED]` Request counter implemented: `http_requests_total{method, path, status_code}`
- [ ] `[REQUIRED]` Error counter implemented: `errors_total{error_type, operation}`
- [ ] `[REQUIRED]` Business event counters implemented per plan (e.g., `orders_created_total`, `payments_processed_total`)

### Histogram Metrics (for latency and duration)

- [ ] `[REQUIRED]` Request latency histogram: `http_request_duration_seconds{method, path, status_code}`
- [ ] `[REQUIRED]` External call latency histograms: `db_query_duration_seconds{operation, table}`, `external_api_duration_seconds{service, operation}`
- [ ] `[REQUIRED]` Histogram bucket boundaries match SLA targets (include SLA value as a bucket boundary)

### Gauge Metrics (for current state)

- [ ] `[RECOMMENDED]` Connection pool utilization: `db_pool_connections_active`, `db_pool_connections_idle`
- [ ] `[RECOMMENDED]` Queue depth gauges for async processing: `queue_depth{queue_name}`
- [ ] `[RECOMMENDED]` Cache hit rate: `cache_hits_total`, `cache_misses_total`

### Metric Quality Rules

- [ ] `[REQUIRED]` No user IDs, request IDs, or other high-cardinality values used as metric labels
- [ ] `[REQUIRED]` All metric names follow Prometheus convention: `<namespace>_<subsystem>_<unit>_<suffix>` (e.g., `http_request_duration_seconds`)
- [ ] `[REQUIRED]` Metrics verified to appear in scrape endpoint or export before production deployment
- [ ] `[RECOMMENDED]` Metric documentation added: `Help` text explains what the metric measures and its unit

---

## Section 4: Distributed Tracing

- [ ] `[REQUIRED]` Trace spans created at all service entry points (HTTP handlers, gRPC handlers, job workers)
- [ ] `[REQUIRED]` Trace context propagated via HTTP headers (`traceparent` W3C standard) on all outbound calls
- [ ] `[REQUIRED]` Parent-child span relationships correctly established (incoming request span is parent of all work spans)
- [ ] `[REQUIRED]` Span attributes added at span creation: `http.method`, `http.url`, `http.status_code`, `db.system`, `db.statement` (parameterized only)
- [ ] `[REQUIRED]` Spans record error status on exception: `span.set_status(ERROR)` + `span.record_exception(e)`
- [ ] `[REQUIRED]` Span names follow convention: `<verb> <resource>` (e.g., `GET /users/{id}`, `SELECT users`)
- [ ] `[RECOMMENDED]` Baggage used to propagate business context (e.g., `user.tier`) across service boundaries for filtering traces
- [ ] `[RECOMMENDED]` Database spans include parameterized query text (never include actual parameter values with PII)

---

## Section 5: Staging Validation

- [ ] `[REQUIRED]` Generate representative load in staging and verify:
  - Logs appear in log backend with correct structure and fields
  - Metrics appear in metrics backend with correct labels and no cardinality explosions
  - Traces appear in trace backend with correct parent-child relationships and no broken traces
- [ ] `[REQUIRED]` Correlation verified: a single request produces a log entry, 1+ metric increments, and a complete trace
- [ ] `[REQUIRED]` Error path validated: trigger an error and confirm ERROR log, error metric increment, and error span appear
- [ ] `[REQUIRED]` PII audit: review 10 sample log entries from staging for any PII or secret leakage
- [ ] `[RECOMMENDED]` Alerting rules verified: trigger threshold condition in staging and confirm alert fires

---

## Instrumentation Completion Sign-Off

| Section | Status | Coverage Notes |
|---------|--------|---------------|
| 1. Library Setup | [ ] Complete / [ ] Partial | |
| 2. Structured Logging | [ ] Complete / [ ] Partial | [X log events instrumented] |
| 3. Metrics | [ ] Complete / [ ] Partial | [X counters, Y histograms, Z gauges] |
| 4. Distributed Tracing | [ ] Complete / [ ] Partial | [X services instrumented] |
| 5. Staging Validation | [ ] Complete / [ ] Partial | |

**Instrumentation Status**: `[ ] PRODUCTION READY` `[ ] PARTIAL — see gaps` `[ ] FAILED VALIDATION`

**Sr. Backend Developer**: _________________________ Date: _________
