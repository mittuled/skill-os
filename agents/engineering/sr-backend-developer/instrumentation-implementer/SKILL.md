---
name: instrumentation-implementer
description: >
  This skill implements planned logging, metrics, and tracing instrumentation in code. Use when asked to add observability to a service, implement structured logging, or wire up distributed tracing. Also consider when an instrumentation plan exists but has not been codified. Suggest when a new service is deployed without observability coverage.
department: engineering
agent: sr-backend-developer
version: 1.0.0
complexity: medium
related-skills:
  - ../instrumentation-planner-eng/SKILL.md
  - ../builder/SKILL.md
  - ../third-party-integrator/SKILL.md
---

# instrumentation-implementer

## Agent: Sr. Backend Developer

L3 senior backend developer (Nx) responsible for third-party integrations, instrumentation, building backend services, and security review.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Implements the planned logging, metrics, and tracing instrumentation in code, translating an observability plan into production-ready structured logs, metric counters, histograms, and distributed trace spans.

## When to Use

- An instrumentation plan has been approved and needs to be codified in the service.
- A new service has been deployed without structured logging, metrics, or tracing.
- An incident retrospective identifies observability gaps that delayed root-cause analysis.
- SLO monitoring requires new metrics or refined instrumentation granularity.
- A service migration (e.g., new tracing vendor) requires re-instrumenting existing code.

## Workflow

1. **Review instrumentation plan**: Study the plan from the instrumentation planner, noting required log events, metric definitions, and trace span boundaries. Deliverable: implementation checklist mapped to plan items.
2. **Configure libraries**: Set up or verify the logging, metrics, and tracing libraries (e.g., OpenTelemetry, Prometheus client, structured logger). Deliverable: configured instrumentation dependencies with correct exporters.
3. **Implement structured logging**: Add log statements at specified points with structured fields (request ID, user ID, operation, duration, error type). Use appropriate log levels. Deliverable: structured log output passing format validation.
4. **Add metrics**: Instrument counters, histograms, and gauges at service boundaries, error paths, and business-critical operations. Deliverable: metrics emitting to the collection endpoint with correct labels.
5. **Wire distributed tracing**: Create spans at service entry points, propagate trace context across internal calls, and annotate spans with relevant attributes. Deliverable: traces visible in the tracing backend with correct parent-child relationships.
6. **Validate in staging**: Deploy to a staging environment and verify logs, metrics, and traces appear correctly in their respective backends. Deliverable: validation report confirming instrumentation correctness.

## Anti-Patterns

- **Logging sensitive data.** Including PII, secrets, or tokens in log output creates compliance violations and security risks. *Why*: logs are often stored in less-secured systems than production databases.
- **High-cardinality metric labels.** Using user IDs or request IDs as metric labels causes metric storage explosion and query slowdowns. *Why*: each unique label combination creates a new time series; unbounded cardinality breaks metric backends.
- **Missing trace context propagation.** Creating spans without propagating context across service boundaries produces disconnected traces. *Why*: the value of distributed tracing is the end-to-end request path; gaps make it useless for debugging.
- **Excessive logging.** Logging every operation at INFO or DEBUG level in production generates noise that obscures real signals and inflates storage costs. *Why*: log volume should be proportional to signal value, not code coverage.

## Output

**On success**: Produces instrumented code with structured logging, metrics, and distributed tracing matching the instrumentation plan. Includes a validation report confirming data appears correctly in monitoring backends.

**On failure**: Report which instrumentation items could not be implemented (e.g., unsupported metric type, incompatible tracing library), what partial coverage was achieved, and what changes to the plan or infrastructure are needed.

## Related Skills

- [`instrumentation-planner-eng`](../instrumentation-planner-eng/SKILL.md) -- produces the plan that this skill implements.
- [`builder`](../builder/SKILL.md) -- builds the services that this skill instruments.
