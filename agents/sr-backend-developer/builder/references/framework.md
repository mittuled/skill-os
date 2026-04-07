# Framework: Backend Service Implementation Standards

Reference for building production-quality backend services covering API design, database optimization, error handling, and caching strategies.

## API Design Principles

### HTTP Method and Status Code Matrix

| Operation | HTTP Method | Success Code | Common Error Codes |
|-----------|------------|-------------|-------------------|
| Retrieve resource | GET | 200 OK | 404 Not Found, 401, 403 |
| Create resource | POST | 201 Created (with Location header) | 400, 409 Conflict, 422 |
| Full update | PUT | 200 OK | 400, 404, 409 |
| Partial update | PATCH | 200 OK | 400, 404, 422 |
| Delete resource | DELETE | 204 No Content | 404, 409 |
| Non-CRUD operation | POST | 200 OK or 202 Accepted | 400, 422 |
| Bulk operation | POST /bulk | 207 Multi-Status | 400, 422 |
| Async operation start | POST | 202 Accepted + polling URL | 400 |

### Idempotency Rules

| HTTP Method | Idempotent? | Safe? | Notes |
|------------|-------------|-------|-------|
| GET | Yes | Yes | Must never mutate state |
| HEAD | Yes | Yes | Same as GET, no body |
| PUT | Yes | No | Same input → same result |
| PATCH | No (often) | No | Use idempotency keys for financial ops |
| DELETE | Yes | No | Deleting already-deleted resource: 204 or 404 (document your choice) |
| POST | No | No | Use idempotency keys to prevent duplicates |

**Idempotency key pattern**: Accept `Idempotency-Key: <uuid>` header on POST endpoints for payment and order creation. Cache responses by key for 24 hours.

### URL Naming Conventions

| Pattern | Correct | Wrong |
|---------|---------|-------|
| Resource names | `/users`, `/orders` (plural nouns) | `/getUser`, `/createOrder` (verbs) |
| Nested resources | `/users/{id}/orders` (max 2 levels deep) | `/users/{id}/orders/{orderId}/items/{itemId}/reviews` |
| Filtering | `/products?category=shoes&inStock=true` | `/products/shoes/inStock` |
| Pagination | `/products?page=2&limit=20` or `/products?cursor=abc123` | Non-standard pagination schemes |
| Versioning | `/v1/users` or `Accept: application/vnd.api+json; version=1` | No versioning |

## Database Query Optimization

### Query Performance Checklist

Before shipping any database query:

- [ ] Query uses index on the WHERE clause columns
- [ ] Query uses index on JOIN columns
- [ ] Query uses index on ORDER BY columns when combined with LIMIT
- [ ] No SELECT * in production code — columns explicitly listed
- [ ] N+1 queries eliminated: use JOIN, eager loading, or batching
- [ ] Pagination uses cursor-based or keyset pagination for large tables (not OFFSET for > 10K rows)
- [ ] Queries involving user input use parameterized queries (never string concatenation)
- [ ] Expensive queries have a query timeout set (e.g., 5s)
- [ ] Bulk operations use batch inserts, not per-row inserts in a loop

### Index Strategy

| Scenario | Index Type | When to Use |
|----------|-----------|------------|
| Single-column equality filter | B-tree index | Default choice for most filters |
| Multi-column filter | Composite B-tree index (order matters: most selective first) | `WHERE status = ? AND created_at > ?` |
| LIKE prefix search | B-tree index on the column | `WHERE name LIKE 'John%'` |
| Full-text search | Full-text index (GIN/GiST) | `WHERE description @@ to_tsquery('query')` |
| JSON key access | Expression index or GIN | `WHERE (metadata->>'key') = ?` |
| Low-cardinality column | Partial index or composite | `WHERE status = 'active' AND ...` |

### Connection Pool Sizing

```
Optimal pool size = core_count × 2 + number_of_disks (Hikari formula)

Rule of thumb:
- OLTP workload: (CPU cores × 2) + 2, max 20–40 per service instance
- Read-heavy: can increase; write-heavy: decrease
- Microservices: each service manages its own pool; total connections ≤ DB max_connections × 0.8
```

## Caching Strategy

### Cache Decision Tree

```
Is the data user-specific?
  └── Yes → Cache in per-user session cache or private CDN layer; never in shared cache
  └── No → Is the data frequently read and rarely written?
       └── No → Do not cache
       └── Yes → Can stale data cause correctness problems?
            └── Yes → Use cache-aside with short TTL + cache invalidation on write
            └── No → Use read-through cache or CDN with longer TTL
```

### Cache Layer Selection

| Data Type | Cache Layer | TTL | Invalidation |
|-----------|------------|-----|-------------|
| Static assets | CDN (Cloudfront / Fastly) | 1 year (with content hash in URL) | URL change |
| API responses (public) | CDN | 60s–5min | Surrogate key / cache purge on write |
| Session data | Redis (per-user) | 15–30 min sliding | On logout; on permission change |
| Config / feature flags | In-memory (process-local) | 30s–5min (poll refresh) | Periodic refresh |
| DB query results | Redis | 5–60min | On write / TTL |
| Rate limit counters | Redis | 1–60min (sliding window) | TTL |

### Cache Anti-Patterns

| Anti-Pattern | Problem | Fix |
|-------------|---------|-----|
| Caching mutable user-specific data in shared cache | GDPR + data leak risk | Move to user-scoped cache key |
| Infinite TTL | Stale data forever; memory exhaustion | Always set TTL; add eviction policy |
| Cache stampede (thundering herd) | All requests hit DB simultaneously on cache miss | Use probabilistic early expiry or distributed lock for regeneration |
| Caching exceptions/errors | Error responses served as real data | Never cache non-2xx responses |
| Key collision (missing namespace) | Service A overwrites Service B's cache key | Prefix all keys: `service:entity:id` |

## Error Handling Standard

### Error Response Schema

```json
{
  "error": {
    "code": "VALIDATION_FAILED",
    "message": "One or more fields failed validation.",
    "details": [
      {
        "field": "email",
        "code": "INVALID_FORMAT",
        "message": "Email address must be a valid format."
      }
    ],
    "request_id": "req_abc123"
  }
}
```

### Error Code Taxonomy

| Category | Prefix | Example Codes |
|----------|--------|--------------|
| Validation errors | `VALIDATION_` | `VALIDATION_FAILED`, `VALIDATION_REQUIRED_FIELD` |
| Authentication | `AUTH_` | `AUTH_REQUIRED`, `AUTH_INVALID_TOKEN`, `AUTH_TOKEN_EXPIRED` |
| Authorization | `FORBIDDEN_` | `FORBIDDEN_INSUFFICIENT_PERMISSIONS`, `FORBIDDEN_RESOURCE_OWNERSHIP` |
| Not found | `NOT_FOUND_` | `NOT_FOUND_USER`, `NOT_FOUND_ORDER` |
| Conflict | `CONFLICT_` | `CONFLICT_DUPLICATE_EMAIL`, `CONFLICT_RESOURCE_LOCKED` |
| Rate limiting | `RATE_LIMIT_` | `RATE_LIMIT_EXCEEDED` |
| Downstream failure | `UPSTREAM_` | `UPSTREAM_PAYMENT_UNAVAILABLE` |
| Internal error | `INTERNAL_` | `INTERNAL_ERROR` (never expose internal details) |

## Observability Requirements

Every service endpoint must emit:

| Signal | What to Record | Tool |
|--------|---------------|------|
| Structured logs | request_id, user_id, method, path, status_code, duration_ms, error_code | [Winston / structlog / zerolog] |
| Distributed trace | Span per service boundary; propagate trace context via W3C headers | [OpenTelemetry] |
| Metrics | request_count, error_count, latency_p50/p95/p99, DB query duration | [Prometheus / Datadog] |
| Alerts | Error rate > 1%, p99 > SLO, queue depth > threshold | [Alertmanager / PagerDuty] |

**Never log**: passwords, tokens, full PII (email/SSN/credit card), request bodies with sensitive fields.
