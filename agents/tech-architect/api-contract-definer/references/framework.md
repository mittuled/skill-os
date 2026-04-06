# Framework: api-contract-definer

Defines the structural approach for designing API contracts that enable parallel team development and reliable integrations.

## Contract Design Phases

### Phase 1: Consumer-Driven Discovery
Identify all consumers before designing a single endpoint. Each consumer states their required operations, data needs, and performance expectations. The contract serves consumers — not the producer's internal data model.

### Phase 2: Interface Design
| Concern | REST (OpenAPI) | gRPC (Protobuf) | When to Choose |
|---------|---------------|-----------------|----------------|
| Request shape | JSON schema in `requestBody` | Message type definition | REST for external/public; gRPC for internal high-throughput |
| Response shape | JSON schema in `responses` | Return message type | Consistency: same error envelope across all endpoints |
| Auth | `securitySchemes` (Bearer, API Key, OAuth2) | Interceptor-level metadata | Bearer JWT for user-scoped; API Key for service-to-service |
| Errors | `4xx`/`5xx` with `$ref` to error schema | Status codes + error details proto | Standard error schema: `{ code, message, details, trace_id }` |

### Phase 3: Versioning Strategy

| Strategy | Path | Header | Query Param |
|----------|------|--------|-------------|
| Format | `/v1/resources` | `Accept: application/vnd.api+json;version=1` | `?api_version=2024-01-01` |
| Best for | Public APIs, clear breaks | Low-churn internal APIs | Date-based SDKs (Stripe model) |
| Deprecation notice | 6 months minimum | 6 months minimum | Per version in changelog |

### Phase 4: Rate Limiting Specification

Every API response MUST include rate limit headers:
```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 847
X-RateLimit-Reset: 1712345678
Retry-After: 30  (on 429 only)
```

SLA tiers:
| Tier | p50 latency | p99 latency | Uptime SLA |
|------|------------|------------|------------|
| Critical path | < 50ms | < 200ms | 99.9% |
| Standard | < 200ms | < 1s | 99.5% |
| Batch/async | N/A | N/A | Best effort |

## Error Handling Standard

Every error response MUST follow this schema:
```json
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "User with id '123' does not exist.",
    "details": [{ "field": "user_id", "reason": "No record found" }],
    "trace_id": "abc-123-xyz",
    "docs_url": "https://docs.example.com/errors/RESOURCE_NOT_FOUND"
  }
}
```

| HTTP Status | Use Case |
|-------------|----------|
| 400 | Malformed request, validation failure |
| 401 | Missing or invalid credentials |
| 403 | Valid credentials, insufficient permissions |
| 404 | Resource does not exist |
| 409 | Conflict (optimistic lock, duplicate) |
| 422 | Semantically invalid (passes syntax, fails business rules) |
| 429 | Rate limit exceeded |
| 503 | Downstream dependency unavailable |

## Contract Review Checklist

Before publishing any API contract:
- [ ] Every endpoint has a complete request and response schema
- [ ] All error codes are defined with remediation guidance
- [ ] Versioning strategy and deprecation policy are documented
- [ ] Rate limits and SLA tiers are specified per endpoint class
- [ ] Both producer and consumer teams have signed off
- [ ] OpenAPI/protobuf file is committed to source control
- [ ] Breaking vs. non-breaking change classification is documented
