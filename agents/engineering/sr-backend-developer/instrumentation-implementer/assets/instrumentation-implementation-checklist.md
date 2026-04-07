# Instrumentation Implementation Checklist: [Service / Feature Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | Sr Backend Developer |
| Service | [Service name] |
| Feature | [Feature being instrumented] |
| Skill | instrumentation-implementer |
| Status | [In Progress / Complete] |

## Logging Checklist

- [ ] Structured log library configured (JSON output): [Winston / structlog / zerolog / slog]
- [ ] Log level configurable via environment variable (default: `info` in production)
- [ ] Request entry log: method, path, request_id, user_id, timestamp
- [ ] Request exit log: method, path, status_code, duration_ms, request_id
- [ ] Business event logs: key domain events at INFO (e.g., "order created", "payment succeeded")
- [ ] Error logs at ERROR level with: error_code, message, stack trace (sanitized)
- [ ] No PII in logs (verified): email, name, phone, card number, SSN excluded
- [ ] No secrets in logs (verified): tokens, passwords, API keys excluded
- [ ] Correlation ID / request_id propagated across all log lines in a request context
- [ ] Log output validated in staging environment (confirm logs appear in central aggregation)

## Metrics Checklist

- [ ] Metrics client configured: [Prometheus client / StatsD / Datadog]
- [ ] `{service}_requests_total` counter — labels: method, endpoint, status_code
- [ ] `{service}_request_duration_seconds` histogram — labels: method, endpoint
- [ ] `{service}_errors_total` counter — labels: error_code, endpoint
- [ ] Domain metrics instrumented: [list specific business metrics, e.g., `orders_created_total`]
- [ ] Histogram buckets configured based on SLO target (not default buckets)
- [ ] Metrics endpoint `/metrics` or push to collector validated in staging
- [ ] Grafana / Datadog dashboard exists with these metrics (or ticket created)

## Tracing Checklist

- [ ] OpenTelemetry SDK initialized with correct service name and version
- [ ] Trace context propagation: accepts `traceparent` from inbound requests
- [ ] Trace context propagation: passes `traceparent` to all outbound requests
- [ ] Root span created for each inbound HTTP request
- [ ] Child span for each database query: named `{db.operation} {db.table}`
- [ ] Child span for each third-party API call: named `{provider}.{operation}`
- [ ] Child span for each significant business operation (> 10ms expected)
- [ ] Span attributes: `http.method`, `http.route`, `http.status_code`, `db.system`, `db.statement` (no PII)
- [ ] Error spans: `otel.status_code=ERROR`, error event added with exception message
- [ ] Traces visible in APM tool for happy path and error path flows

## Verification Steps

- [ ] Send a test request; confirm structured log appears in log aggregation with all required fields
- [ ] Send a test request; confirm metrics increment in `/metrics` or dashboard
- [ ] Send a test request; confirm trace appears in APM tool end-to-end
- [ ] Trigger an error; confirm error log, error metric increment, and error span in APM
- [ ] Verify no PII in any signal by reviewing sample logs, metrics labels, and span attributes

## Sign-off

**All checks passing?** [Yes / No — list failing items]

**Verified by**: [Name] | Date: [YYYY-MM-DD]
