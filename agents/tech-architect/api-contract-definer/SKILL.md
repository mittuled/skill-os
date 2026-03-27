---
name: api-contract-definer
description: >
  This skill defines the API contracts between system components including endpoints,
  schemas, versioning, and error handling. Use when asked to design an API, define
  service interfaces, or establish API standards. Also consider when teams are
  integrating and need agreed-upon contracts. Suggest when the user is building
  integrations without documented API contracts.
department: engineering
agent: tech-architect
version: 1.0.0
complexity: complex
related-skills:
  - ../architecture-designer/SKILL.md
  - ../technical-feasibility-check/SKILL.md
triggers:
  - "define the API contract"
  - "design the API endpoints"
  - "what should the API look like"
  - "create the API spec"
---

# api-contract-definer

## Agent: Tech Architect

L2 technical architect (1x) responsible for feasibility assessment, system design, API contract definition, and infrastructure planning. Ensures technical decisions support product goals and scale requirements.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

Defines the API contracts between system components by specifying endpoints, request/response schemas, authentication, versioning strategy, error handling, and rate limiting to enable parallel team development and reliable integration.

## When to Use

- When a new system architecture requires defined interfaces between services before teams can build in parallel.
- When an external API is being designed for partners or customers and needs a formal contract specification.
- When existing APIs are inconsistent and need standardization into a coherent API style guide.

## Workflow

1. **Requirements Gathering**: Identify all consumers and producers for each API. Document the data each consumer needs, the operations they require, and their performance expectations (latency, throughput). Deliverable: API requirements document per interface.
2. **Contract Design**: Design each API contract: endpoints, HTTP methods, URL structure, request/response schemas, authentication method, and content types. Follow the organization's API style guide or establish one. Use OpenAPI/Swagger for REST or protobuf for gRPC. Deliverable: API specification files.
3. **Error Handling and Edge Cases**: Define the error response format, error codes, retry guidance, and edge case behavior (partial failures, empty results, pagination boundaries). Ensure errors are actionable for the consumer. Deliverable: error handling specification.
4. **Versioning Strategy**: Define the API versioning approach (URL path, header, or query parameter). Establish the deprecation policy: how much notice consumers receive, how long deprecated versions are maintained, and what migration support is provided. Deliverable: versioning and deprecation policy.
5. **Rate Limiting and SLAs**: Define rate limits, quotas, and SLAs for each API. Specify how rate limits are communicated to consumers (response headers) and what happens when limits are exceeded. Deliverable: rate limiting and SLA specification.
6. **Contract Review**: Review the contract with both producer and consumer teams. Resolve disagreements on schema structure, naming, and behavior. Finalize and publish the contract as the authoritative interface specification. Deliverable: reviewed and published API contracts.

## Anti-Patterns

- **Implementation-first APIs**: Building the API implementation before defining the contract, then documenting what was built. *Why*: implementation-first APIs leak internal details into the contract and make the interface harder to change; contract-first enables parallel development.
- **Inconsistent error handling**: Returning different error formats from different endpoints or services. *Why*: inconsistent errors force consumers to write per-endpoint error handling; a standard format reduces integration effort and improves debuggability.
- **No versioning plan**: Launching an API without a versioning strategy, then breaking consumers with incompatible changes. *Why*: unversioned APIs cannot evolve without breaking integrations; a versioning strategy from day one prevents costly migrations.
- **Chatty contracts**: Designing APIs that require many sequential calls to complete a single user action. *Why*: chatty APIs amplify latency and increase failure surface; contracts should be designed around consumer use cases, not internal data models.

## Output

**On success**: Produces API specification files, error handling specification, versioning policy, rate limiting configuration, and published contracts. Delivered before implementation begins with updates per design evolution.

**On failure**: Report which interfaces could not be agreed upon, what the blocking disagreements are, and recommended resolution approaches. Escalate to engineering leadership if teams cannot converge on contracts.

## Related Skills

- [`architecture-designer`](../architecture-designer/SKILL.md) -- System architecture defines the component boundaries that API contracts formalize.
- [`technical-feasibility-check`](../technical-feasibility-check/SKILL.md) -- Feasibility checks validate that proposed API designs are implementable within constraints.
