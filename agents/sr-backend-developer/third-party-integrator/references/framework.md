# Framework: Third-Party Integration Standards

Reference for integrating external APIs, SDKs, and services with production-grade reliability, security, and observability.

## Integration Risk Classification

Classify every third-party integration before implementation to determine the required reliability patterns:

| Factor | Score 1 | Score 2 | Score 3 |
|--------|---------|---------|---------|
| Data sensitivity | Internal metadata only | User-identifiable data | Financial or health data |
| User-facing impact | Background / async | Partial feature impact | Blocks core user flow |
| Uptime SLA of provider | ≥ 99.9% | 99.0–99.9% | < 99.0% or unknown |
| Reversibility of failure | Fully retryable | Partial data loss risk | Irreversible (payment, notification) |

**Total Score** → 4–5: Low Risk | 6–8: Medium Risk | 9–12: High Risk

| Risk Level | Required Patterns |
|-----------|------------------|
| Low | Timeout, structured logging, error classification |
| Medium | + Circuit breaker, retry with backoff, health check |
| High | + Idempotency key, webhook retry handling, fallback behavior, dead-letter queue |

## Reliability Patterns

### Timeout Configuration

Set timeouts at every integration boundary. Never rely on system defaults:

| Layer | Recommended Timeout | Notes |
|-------|---------------------|-------|
| Connection timeout | 2–5 seconds | Time to establish TCP connection |
| Read timeout | 10–30 seconds | Time to receive response after connected |
| Total request timeout | 30–60 seconds | Hard ceiling; return error if exceeded |
| Webhook processing | 5 seconds | External providers expect fast ACK; defer work async |

### Retry Strategy

```
Retryable errors:
  - 429 Too Many Requests (use Retry-After header if present)
  - 503 Service Unavailable
  - 504 Gateway Timeout
  - Network timeout / connection refused

Non-retryable errors (fail fast):
  - 400 Bad Request (your payload is wrong; fix before retrying)
  - 401 Unauthorized (credential issue; retry won't help)
  - 403 Forbidden (permission issue)
  - 404 Not Found (resource doesn't exist)
  - 422 Unprocessable Entity (semantic validation failure)
```

**Retry schedule** (exponential backoff with jitter):

| Attempt | Delay | Max Jitter |
|---------|-------|-----------|
| 1 (immediate) | 0ms | — |
| 2 | 500ms | ±100ms |
| 3 | 1,500ms | ±300ms |
| 4 | 4,500ms | ±500ms |
| 5 | Give up → dead-letter queue or alert | — |

### Circuit Breaker States

```
CLOSED (normal) → failure_count exceeds threshold → OPEN (fail fast)
OPEN → wait cooldown period → HALF-OPEN (allow 1 test request)
HALF-OPEN → success → CLOSED | failure → OPEN
```

| Parameter | Recommended Value | Notes |
|-----------|------------------|-------|
| Failure threshold to open | 50% of requests fail in 30s window | Or 5 consecutive failures |
| Cooldown period (OPEN) | 30–60 seconds | Time before attempting recovery |
| Probe requests (HALF-OPEN) | 1 | Single test request |
| Metric window | 30 seconds | Sliding window for error rate |

## Security Requirements

### Credential Management

| Credential Type | Storage | Rotation Frequency | Access Pattern |
|----------------|---------|-------------------|----------------|
| API key | Secrets manager (Vault / AWS SM) | 90 days | Injected at runtime; never in env vars |
| OAuth client secret | Secrets manager | On breach or 1 year | Injected at runtime |
| Webhook signing secret | Secrets manager | On breach | Used only in webhook validation |
| Service account key (GCP/AWS) | IAM role (preferred) or Secrets manager | 90 days | Never committed to code |

### Webhook Security

1. **Validate signature**: Every inbound webhook must be validated against the provider's HMAC signature before processing.
2. **Verify timestamp**: Reject webhooks with a `timestamp` older than 300 seconds (replay attack prevention).
3. **Return 200 fast**: Acknowledge receipt within 5 seconds; process asynchronously.
4. **Idempotent processing**: Deduplicate webhook IDs — many providers retry on non-200 responses.

```python
# Signature validation pattern (language-agnostic pseudocode)
expected_sig = HMAC_SHA256(signing_secret, timestamp + "." + raw_body)
if not constant_time_compare(expected_sig, received_sig):
    return 400 Bad Request
if abs(current_time - timestamp) > 300:
    return 400 Bad Request
```

### OAuth 2.0 Token Handling

| Concern | Requirement |
|---------|------------|
| Token storage (server-side) | Store in encrypted database or secrets manager, never plaintext |
| Token storage (browser) | HttpOnly, Secure cookie; never localStorage |
| Refresh token rotation | Rotate on every use; invalidate old token |
| Scope minimization | Request only scopes required for the integration |
| Token expiry handling | Auto-refresh before expiry; handle 401 by refreshing, then retrying once |

## Observability for Third-Party Calls

Every outbound call must emit these signals:

| Signal | Fields |
|--------|--------|
| Structured log | `provider`, `endpoint`, `method`, `status_code`, `duration_ms`, `request_id`, `error_code` |
| Metrics | `third_party_request_total{provider, endpoint, status}`, `third_party_request_duration_seconds` |
| Distributed trace | Span named `third_party.{provider}.{operation}`; include `http.url`, `http.status_code`, `http.method` |
| Circuit breaker state | Expose circuit state as a metric: `circuit_breaker_state{provider}` = 0 (closed), 1 (open), 2 (half-open) |

**Never log**: full request/response bodies containing PII, authentication tokens, or payment card data.

## Integration Test Strategy

| Test Type | What to Test | Tools |
|-----------|-------------|-------|
| Contract test | Provider API response matches your expected schema | Pact / JSON schema validation |
| Mock integration test | Your code handles all error cases (429, 500, timeout, malformed response) | WireMock / nock / responses |
| Sandbox/staging test | Happy path via provider's sandbox environment | Provider-specific sandbox |
| Production smoke test | Lightweight end-to-end call (read-only or with test account) | Synthetic monitor |

## SDK vs. HTTP Client Decision

| Criterion | Use Provider SDK | Use HTTP Client Directly |
|-----------|----------------|------------------------|
| SDK maintained by provider | Prefer SDK | — |
| SDK adds < 500 KB to bundle | Prefer SDK | — |
| SDK is outdated (> 1 major version behind) | — | Use HTTP client with your own wrapper |
| SDK lacks retry/circuit breaker support | — | Use HTTP client with your own resilience layer |
| SDK forces synchronous I/O in async service | — | Use async HTTP client |
| Multiple providers with same API shape | — | Adapter pattern with shared interface |
