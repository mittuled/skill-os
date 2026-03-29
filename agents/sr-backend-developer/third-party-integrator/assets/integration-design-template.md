# Third-Party Integration Design

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Agent role / human name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | third-party-integrator |

## Executive Summary

[2-3 sentences summarizing the integration: which vendor, what capability, key design decisions.
GUIDANCE: Lead with the business capability enabled. Highlight the abstraction strategy and key risks.]

## API Contract Summary

[Document the third-party API endpoints, authentication, rate limits, and error codes.

GUIDANCE:
- Good: "Stripe Charges API: POST /v1/charges. Auth: Bearer token (sk_live_*). Rate limit: 100 req/s (burst: 200). Errors: 400 (invalid_request), 402 (card_declined), 429 (rate_limited). SLA: 99.95% uptime."
- Bad: "Uses Stripe API."
- Format: Table with endpoint, method, auth, rate limit, key error codes, and SLA]

| Endpoint | Method | Auth | Rate Limit | Key Errors | SLA |
|----------|--------|------|-----------|------------|-----|
| [path] | [GET/POST/etc.] | [Bearer/OAuth/API Key] | [req/s] | [error codes] | [uptime %] |

## Abstraction Layer Design

[Define the internal interface that isolates the vendor dependency.

GUIDANCE:
- Good: "Interface: PaymentGateway { charge(amount, currency, source): ChargeResult; refund(chargeId, amount?): RefundResult; }. DTOs: ChargeRequest, ChargeResult, RefundResult. Adapter: StripePaymentGateway implements PaymentGateway."
- Bad: "Wrap the Stripe SDK."
- Format: Interface definition with method signatures and DTOs]

## Error Handling and Resilience

[Define retry, circuit breaker, and fallback strategies.

GUIDANCE:
- Good: "Retry: exponential backoff (100ms, 200ms, 400ms) for 5xx and 429. Max 3 retries. Circuit breaker: open after 5 failures in 30s window; half-open after 60s. Fallback: queue charge for async retry; return pending status to caller."
- Bad: "Retry on failure."
- Format: Table with error type, strategy, parameters, and fallback behavior]

| Error Type | Strategy | Parameters | Fallback |
|-----------|----------|-----------|----------|
| [5xx / 429 / timeout / network] | [Retry / Circuit break / Fallback] | [backoff, max retries, window] | [Degraded behavior] |

## Data Mapping

[Map internal domain models to external API schemas.

GUIDANCE:
- Good: "Internal Order.amount (integer cents) → Stripe Charge.amount (integer cents, no conversion). Internal Order.currency (ISO 4217) → Stripe Charge.currency (lowercase ISO 4217, map USD → usd)."
- Bad: "Map fields."
- Format: Table with internal field, external field, transformation, and edge cases]

## Recommendations

[Prioritized implementation steps.
GUIDANCE: Each recommendation should be:
- Specific (not "implement integration" but "implement StripePaymentGateway adapter with retry policy and circuit breaker before connecting to sandbox")
- Actionable (assignable to a person/team)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[API documentation version reviewed, sandbox environment details, authentication setup steps]

### B. Supporting Data

[API documentation links, rate limit documentation, error code reference, SLA agreement]
