# Framework: Observability Instrumentation Planning

Reference for planning and implementing structured logging, distributed tracing, and metrics across backend services.

## Observability Pillars

### Three-Pillar Model

| Pillar | Purpose | Answers |
|--------|---------|---------|
| Logs | Record discrete events | "What happened and when?" |
| Metrics | Measure aggregated state over time | "How is the system performing right now?" |
| Traces | Track request flow across services | "Where did this specific request spend its time?" |

**Rule**: Instrumentation must cover all three pillars. A service with only logs but no metrics is unmonitorable at scale. A service with only metrics has no debugging path for specific failures.

## Logging Standards

### Structured Log Schema

Every log entry must include these fields (in JSON format):

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `timestamp` | ISO 8601 | Yes | UTC timestamp with millisecond precision |
| `level` | string | Yes | `debug`, `info`, `warn`, `error`, `fatal` |
| `message` | string | Yes | Human-readable event description |
| `service` | string | Yes | Service name as deployed |
| `version` | string | Yes | Service version or git SHA |
| `request_id` | string | Yes (in request context) | Trace correlation ID |
| `user_id` | string | Conditional | Required when action is user-initiated; omit for system events |
| `operation` | string | Yes | Function or endpoint name |
| `duration_ms` | number | Conditional | Required for any operation with latency relevance |
| `error` | object | Conditional | Error code, message, stack trace (sanitized) |
| `metadata` | object | Optional | Domain-specific context |

### Log Level Guidelines

| Level | When to Use | Examples |
|-------|-------------|---------|
| `debug` | Development only; never in production by default | Function entry/exit, variable values |
| `info` | Normal operational events | Request received, job completed, user action |
| `warn` | Unexpected but handled events | Deprecated API used, retry succeeded, cache miss |
| `error` | Handled errors affecting a request | Payment failed, validation error, upstream 500 |
| `fatal` | Unrecoverable errors requiring restart | Config missing, DB pool exhausted, OOM |

**Never log**: passwords, auth tokens, PII (name, email, phone, SSN, credit card), full request bodies containing sensitive fields.

### Sensitive Field Handling

| Field Category | Logging Policy |
|---------------|---------------|
| User identifier | Log `user_id` only (opaque UUID); never email or name |
| Authentication | Log `auth_method` and `outcome`; never token or credential |
| Payment | Log `payment_method_type` and `outcome`; never card number or CVV |
| Personal data | Log `user_id` reference; never raw PII |
| Internal error | Log error code + stack trace; sanitize before logging (remove SQL queries containing data) |

## Metrics Instrumentation

### RED Method (Request-Driven Services)

Every service endpoint must expose:

| Metric | Name Pattern | Type | Labels |
|--------|-------------|------|--------|
| Rate | `{service}_requests_total` | Counter | `method`, `endpoint`, `status_code` |
| Errors | Derived from Rate where `status_code >= 400` | Counter | Same |
| Duration | `{service}_request_duration_seconds` | Histogram | `method`, `endpoint` |

### USE Method (Resource-Bound Components)

For every resource (CPU, memory, DB pool, queue):

| Metric | Name Pattern | Type |
|--------|-------------|------|
| Utilization | `{resource}_utilization_ratio` | Gauge (0.0–1.0) |
| Saturation | `{resource}_queue_depth` | Gauge |
| Errors | `{resource}_errors_total` | Counter |

### Histogram Bucket Configuration

Default buckets for latency histograms (seconds):

```
[0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0]
```

Set buckets based on the SLO target. If SLO is p99 < 500ms, include at least one bucket at 0.5s and one just above.

## Distributed Tracing

### Span Naming Convention

| Span Type | Name Pattern | Example |
|-----------|-------------|---------|
| HTTP server | `{HTTP method} {route template}` | `POST /api/orders/{id}` |
| HTTP client | `{HTTP method}` | `GET` (URL in attributes) |
| Database query | `{db.operation} {db.table}` | `SELECT orders` |
| Async job | `{job.name}` | `send-welcome-email` |
| Cache operation | `{cache.operation} {cache.key_pattern}` | `GET user:*` |
| Third-party call | `{provider}.{operation}` | `stripe.createPaymentIntent` |

### Required Span Attributes (OpenTelemetry Semantic Conventions)

| Attribute | HTTP Server | DB | HTTP Client |
|-----------|------------|-----|------------|
| `http.method` | Yes | — | Yes |
| `http.route` | Yes | — | — |
| `http.status_code` | Yes | — | Yes |
| `http.url` | — | — | Yes (sanitized — no credentials) |
| `db.system` | — | Yes | — |
| `db.operation` | — | Yes | — |
| `db.statement` | — | Yes (no PII) | — |
| `error` (boolean) | Conditional | Conditional | Conditional |

### Trace Context Propagation

- Propagate trace context using W3C Trace Context headers (`traceparent`, `tracestate`).
- Propagate across async message queues by injecting `traceparent` into message headers or metadata.
- Never rely on vendor-specific propagation headers in a multi-vendor environment.

## Instrumentation Coverage Matrix

Use this to verify completeness before shipping:

| Layer | Logging | Metrics | Tracing |
|-------|---------|---------|--------|
| HTTP request entry | [x] Request log at INFO | [x] Rate, latency, error | [x] Root span |
| Authentication | [x] Auth event at INFO/WARN | [x] Auth success/fail counter | [x] Auth span |
| Business logic (key operations) | [x] Operation log at INFO | [x] Domain-specific counters | [x] Child span |
| Database query | [x] Slow query log at WARN (> 100ms) | [x] Query duration histogram | [x] DB span |
| Third-party call | [x] Request/response at INFO | [x] Provider latency + error rate | [x] Third-party span |
| Background job | [x] Job start/end at INFO | [x] Job duration + success/fail | [x] Job root span |
| Error handling | [x] Error at ERROR with context | [x] Error counter by type | [x] Error event on span |
