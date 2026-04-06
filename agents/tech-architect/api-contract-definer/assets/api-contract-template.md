# API Contract

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Tech Architect / author name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | api-contract-definer |

## Executive Summary

[2-3 sentences describing what this API does, which systems it connects, and the primary consumer use cases it serves.
GUIDANCE: Lead with the business capability this API exposes, not the technical implementation. Example: "This contract defines the Payments API between the checkout service and the payment processor. It covers charge initiation, refund handling, and webhook delivery for 3 consumer teams."]

## API Overview

[High-level description of the API surface: how many endpoints, authentication model, and base URL.

GUIDANCE:
- Good: "REST API with 8 endpoints, Bearer JWT authentication, base URL `https://api.example.com/v1/payments`"
- Bad: "This is the payments API"
- Format: Table of endpoint groups with brief descriptions]

| Endpoint Group | Endpoints | Description |
|---------------|-----------|-------------|
| [Resource name] | [GET/POST/PUT/DELETE /path] | [What this group enables] |

## Endpoint Specifications

[Full specification for each endpoint. Repeat the block below for every endpoint.

GUIDANCE:
- Include all required and optional parameters
- Link to the JSON schema or protobuf definition file
- Show a request and response example for every endpoint
- Document all error codes this endpoint can return]

### `[HTTP METHOD] /path`

**Description**: [What this endpoint does in one sentence.]

**Authentication**: [Bearer JWT / API Key / None — specify required scopes or permissions]

**Request**
```json
{
  "field_name": "string",
  "required_field": "integer (required)"
}
```

**Response (200)**
```json
{
  "id": "uuid",
  "status": "string"
}
```

**Error Codes**
| Code | HTTP Status | Meaning | Remediation |
|------|------------|---------|-------------|
| `RESOURCE_NOT_FOUND` | 404 | [When this occurs] | [What the consumer should do] |
| `VALIDATION_ERROR` | 422 | [When this occurs] | [What the consumer should do] |

## Versioning and Deprecation Policy

[Document the versioning strategy and what constitutes a breaking change.

GUIDANCE:
- Good: "Breaking changes (field removal, type change, endpoint deletion) require a new major version with 6 months deprecation notice. Additive changes (new optional fields, new endpoints) are non-breaking and published as minor versions."
- Bad: "We will try not to break things"
- Format: Table of breaking vs. non-breaking changes]

| Change Type | Breaking? | Versioning Action |
|-------------|-----------|------------------|
| Remove field | Yes | New major version, 6-month notice |
| Add required field | Yes | New major version, 6-month notice |
| Add optional field | No | Minor version, no migration required |
| New endpoint | No | Minor version, no migration required |
| Change field type | Yes | New major version, migration guide required |

## Rate Limits and SLAs

[Specify rate limits per tier and SLA commitments per endpoint class.

GUIDANCE:
- Good: "Standard tier: 1,000 req/min. Premium tier: 10,000 req/min. Rate limit headers included in every response. p99 latency SLA: 200ms for synchronous endpoints."
- Bad: "Don't send too many requests"
- Format: Table per tier]

| Tier | Rate Limit | Burst Limit | p99 Latency SLA | Uptime SLA |
|------|-----------|-------------|----------------|------------|
| Standard | [N req/min] | [N req/burst] | [Xms] | [X%] |
| Premium | [N req/min] | [N req/burst] | [Xms] | [X%] |

## Recommendations

[Prioritized list of actions before this contract is finalized.
GUIDANCE: Each item should be specific, assignable, and labeled P1/P2/P3]

- **P1**: [Action required before contract can be published]
- **P2**: [Action to complete before first consumer integrates]
- **P3**: [Nice-to-have improvement for future revision]

## Appendices

### A. Methodology

[How this contract was produced — stakeholder interviews, existing API audit, consumer discovery workshops, OpenAPI generation tools]

### B. Supporting Data

[Links to OpenAPI/protobuf spec files, Postman collections, error code registry, and consumer requirement documents]
