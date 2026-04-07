---
name: third-party-integrator
description: >
  This skill integrates third-party APIs and services into the backend following contract definitions. Use when asked to connect to an external API, implement a webhook consumer, or wrap a vendor SDK. Also consider when an existing integration needs migration to a new API version. Suggest when a feature spec references external data sources or payment providers.
department: engineering
agent: sr-backend-developer
version: 1.0.0
complexity: medium
related-skills:
  - ../builder/SKILL.md
  - ../security-reviewer/SKILL.md
  - ../instrumentation-implementer/SKILL.md
---

# third-party-integrator

## Agent: Sr. Backend Developer

L3 senior backend developer (Nx) responsible for third-party integrations, instrumentation, building backend services, and security review.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Integrates third-party APIs and services into the backend following contract definitions, producing abstracted, testable integration layers that isolate external dependencies from core business logic.

## When to Use

- A feature spec requires data from or interaction with an external service (payment gateway, CRM, analytics provider).
- A vendor SDK needs wrapping in an abstraction layer to decouple the codebase from vendor lock-in.
- An existing third-party integration must migrate to a new API version or replacement vendor.
- A webhook consumer needs implementation to receive asynchronous events from an external system.
- Rate limits, authentication changes, or deprecation notices from a vendor require integration updates.

## Workflow

1. **Review API contract**: Study the third-party API documentation, authentication model, rate limits, error codes, and SLA guarantees. Deliverable: integration requirements document listing endpoints, auth method, rate limits, and data mappings.
2. **Design abstraction layer**: Define an internal interface that isolates the third-party dependency, allowing substitution for testing and future vendor migration. Deliverable: interface definition with method signatures and data transfer objects.
3. **Implement authentication**: Configure API keys, OAuth flows, or webhook signing verification. Store secrets in the secrets manager, never in code. Deliverable: authenticated client passing connectivity tests.
4. **Build request/response mapping**: Implement serialization, deserialization, and data transformation between internal domain models and the external API schema. Deliverable: mapper code with unit tests covering schema variations.
5. **Handle errors and retries**: Implement retry logic with exponential backoff, circuit breakers for sustained failures, and fallback behaviour for degraded operation. Deliverable: resilient client handling all documented error codes.
6. **Add rate limit management**: Implement client-side rate limiting or request queuing to stay within vendor quotas. Deliverable: rate-limited client with backpressure handling.
7. **Test with sandbox**: Validate the integration against the vendor sandbox or staging environment. Deliverable: integration test suite passing against sandbox with representative test data.

## Anti-Patterns

- **Direct vendor calls from business logic.** Calling third-party APIs without an abstraction layer couples core code to vendor specifics and makes unit testing impossible. *Why*: abstraction layers are the boundary that enables testability and vendor migration.
- **Ignoring rate limits.** Assuming unlimited API access leads to throttling, blocked API keys, and cascading failures. *Why*: vendors enforce limits; exceeding them degrades service for all consumers.
- **Hardcoding secrets.** Embedding API keys or tokens in source code creates security vulnerabilities and complicates rotation. *Why*: secrets in code persist in version history even after removal.
- **No circuit breaker.** Retrying indefinitely against a failing external service amplifies the outage and consumes resources. *Why*: circuit breakers protect the calling service from cascading failures caused by downstream outages.

## Output

**On success**: Produces an abstracted integration layer with authenticated client, request/response mapping, error handling with retries and circuit breakers, rate limit management, and a passing integration test suite. Includes API documentation for internal consumers.

**On failure**: Report which integration endpoints could not be connected (e.g., sandbox unavailable, authentication rejected, undocumented API behaviour), what partial integration was achieved, and what vendor support or documentation clarifications are needed.

## Related Skills

- [`builder`](../builder/SKILL.md) -- builds the services that consume the integration layer.
- [`security-reviewer`](../security-reviewer/SKILL.md) -- reviews the integration for security vulnerabilities in auth and data handling.
- [`instrumentation-implementer`](../instrumentation-implementer/SKILL.md) -- instruments the integration for observability of external call latency and error rates.
