# API Design Document

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Agent role / human name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | builder |

## Executive Summary

[2-3 sentences summarizing the API: resource model, key endpoints, and non-functional targets.
GUIDANCE: Lead with the business capability this API enables. State the SLO targets.]

## Resource Model

[Define the domain entities and their relationships.

GUIDANCE:
- Good: "Task { id: UUID, title: string(1-200), description: string?(0-2000), priority: enum(low|medium|high), status: enum(todo|in_progress|done), assigneeId: UUID?, createdAt: ISO8601, updatedAt: ISO8601 }. Relationships: Task belongs_to Project (required), Task has_many Comments."
- Bad: "Tasks have fields."
- Format: Entity definitions with field types, constraints, and relationship cardinality]

## Endpoint Specification

[Define each API endpoint with method, path, request/response schemas, and status codes.

GUIDANCE:
- Good: "POST /api/v1/tasks — Create a task. Request: { title: string, description?: string, priority?: 'low'|'medium'|'high' }. Response 201: { data: Task }. Response 400: { error: { field: string[] } }. Response 401: { error: 'Unauthorized' }."
- Bad: "POST /tasks creates tasks."
- Format: Table per endpoint with method, path, request body, response codes, and response shapes]

| Method | Path | Description | Auth | Request Body | Success Response | Error Responses |
|--------|------|-------------|------|-------------|-----------------|----------------|
| [GET/POST/PATCH/DELETE] | [/api/v1/resource] | [What it does] | [Required/Public] | [Schema or N/A] | [Status: Schema] | [Status: Schema] |

## Error Taxonomy

[Define the error response format and error code catalog.

GUIDANCE:
- Good: "Standard error envelope: { error: { code: string, message: string, details?: object } }. Codes: VALIDATION_ERROR (400), NOT_FOUND (404), CONFLICT (409), RATE_LIMITED (429), INTERNAL_ERROR (500)."
- Bad: "Return errors as JSON."
- Format: Table with error code, HTTP status, description, and when it occurs]

## Non-Functional Requirements

[State latency, throughput, and reliability targets.

GUIDANCE:
- Good: "P99 latency: < 200ms for reads, < 500ms for writes. Throughput: 1000 RPS sustained. Error budget: 0.1% 5xx rate over 30-day window. Rate limit: 100 req/min per API key."
- Bad: "Should be fast."
- Format: Table with metric, target, and measurement method]

## Recommendations

[Prioritized implementation steps and architectural decisions.
GUIDANCE: Each recommendation should be:
- Specific (not "build the API" but "implement TaskRepository with Postgres adapter before building HTTP handlers")
- Actionable (assignable to a person/team)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[API design principles followed, OpenAPI spec generation approach, test strategy]

### B. Supporting Data

[Data model diagrams, load estimates, authentication flow diagrams]
