---
name: builder
description: >
  This skill builds backend services, APIs, and business logic according to specifications. Use when asked to implement an API endpoint, create a service layer, or build backend business logic. Also consider when a data model is ready and needs service-layer consumers. Suggest when sprint stories require new backend functionality.
department: engineering
agent: sr-backend-developer
version: 1.0.0
complexity: complex
related-skills:
  - ../security-reviewer/SKILL.md
  - ../instrumentation-implementer/SKILL.md
  - ../third-party-integrator/SKILL.md
  - ../../../engineering/database-expert/data-model-designer/SKILL.md
triggers:
  - "build backend API"
  - "implement service"
  - "create endpoint"
  - "backend implementation"
---

# builder

## Agent: Sr. Backend Developer

L3 senior backend developer (Nx) responsible for third-party integrations, instrumentation, building backend services, and security review.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Builds backend services, APIs, and business logic according to specifications, producing tested, documented, and deployable code that meets functional requirements and non-functional quality standards.

## When to Use

- Sprint stories require new API endpoints or service-layer logic.
- A data model has been finalized and needs service-layer consumers with CRUD operations.
- An existing service needs extension to support new product requirements.
- A backend rewrite or refactoring has been approved to address technical debt.
- A proof-of-concept needs to be elevated to production-grade implementation.

## Workflow

1. **Review specification**: Study the API contract, data model, acceptance criteria, and non-functional requirements (latency, throughput, error budget). Deliverable: implementation checklist with acceptance criteria mapped to test cases.
2. **Design service structure**: Define the module layout, dependency graph, and interface boundaries. Choose patterns (repository, service layer, event-driven) appropriate to the domain. Deliverable: service design document or ADR.
3. **Write tests first**: Author unit tests and integration tests covering happy paths, edge cases, and error scenarios before writing implementation code. Deliverable: failing test suite defining expected behaviour.
4. **Implement business logic**: Build the service layer, API handlers, validation, error handling, and data access code. Follow existing project conventions for structure, naming, and error taxonomy. Deliverable: implementation code passing all tests.
5. **Add instrumentation hooks**: Insert structured logging, metrics counters, and trace spans at service boundaries and critical decision points. Deliverable: instrumented code ready for observability.
6. **Write API documentation**: Document endpoints, request/response schemas, error codes, and authentication requirements. Deliverable: OpenAPI spec or equivalent documentation.
7. **Submit for review**: Open a PR with test results, documentation, and a description of architectural decisions. Deliverable: reviewable PR with passing CI.

## Anti-Patterns

- **Building without tests.** Writing implementation code before tests inverts the feedback loop and makes it difficult to verify correctness. *Why*: tests written after implementation tend to test what was built rather than what was specified.
- **Ignoring error handling.** Focusing on the happy path and deferring error scenarios produces fragile services that fail silently or leak internal details. *Why*: production traffic is mostly edge cases; robust error handling is the primary code path.
- **Tight coupling to external dependencies.** Calling third-party APIs or databases directly from business logic without abstraction layers makes services untestable and migration-resistant. *Why*: abstractions allow dependency substitution for testing and future migration.
- **Skipping API contracts.** Implementing endpoints without a formal API contract causes frontend/backend integration mismatches. *Why*: contracts are the communication protocol between teams; informal agreements break at scale.
- **Premature optimization.** Optimizing code paths before measuring performance in a realistic environment wastes effort on non-bottlenecks. *Why*: profiling reveals actual bottlenecks, which rarely match intuition.

## Output

**On success**: Produces tested, documented backend services with API endpoints, business logic, data access layer, and instrumentation hooks. Includes passing test suites, API documentation, and a reviewable PR with CI green.

**On failure**: Report which acceptance criteria could not be met, what implementation was completed, what blockers were encountered (missing data model, unclear requirements, dependency unavailability), and recommended next steps.

## Related Skills

- [`security-reviewer`](../security-reviewer/SKILL.md) -- reviews the built code for security vulnerabilities before merge.
- [`instrumentation-implementer`](../instrumentation-implementer/SKILL.md) -- deepens the instrumentation hooks added during build.
- [`third-party-integrator`](../third-party-integrator/SKILL.md) -- handles external API integrations that the builder may depend on.
- [`data-model-designer`](../../../engineering/database-expert/data-model-designer/SKILL.md) -- designs the data model that the builder's data access layer consumes.
