---
name: instrumentation-planner-eng
description: >
  This skill plans the logging, metrics, and tracing instrumentation required for observability. Use when asked to design an observability strategy, define SLIs, or plan monitoring for a new service. Also consider when an incident reveals observability blind spots. Suggest when a new service enters development without an observability plan.
department: engineering
agent: sr-backend-developer
version: 1.0.0
complexity: medium
related-skills:
  - ../instrumentation-implementer/SKILL.md
  - ../builder/SKILL.md
  - ../../../engineering/database-expert/data-model-designer/SKILL.md
triggers:
  - "plan instrumentation"
  - "instrumentation planning"
  - "observability planning"
  - "plan telemetry"
  - "instrumentation design"
---

# instrumentation-planner-eng

## Agent: Sr. Backend Developer

L3 senior backend developer (Nx) responsible for third-party integrations, instrumentation, building backend services, and security review.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Plans the logging, metrics, and tracing instrumentation required for service observability, defining what to measure, where to instrument, and how to alert before implementation begins.

## When to Use

- A new service is entering development and needs an observability strategy from day one.
- An incident retrospective identifies gaps in logging, metrics, or tracing that delayed diagnosis.
- SLO definitions require new service-level indicators that are not currently measured.
- A service is being decomposed from a monolith and needs independent observability.
- The team is adopting a new observability stack and needs to re-plan instrumentation.

## Workflow

1. **Map service boundaries**: Identify all entry points, exit points, internal components, and external dependencies of the target service. Deliverable: service dependency diagram with instrumentation attachment points.
2. **Define SLIs and SLOs**: Specify the service-level indicators (latency, error rate, throughput) and their target SLOs. Deliverable: SLI/SLO definition table.
3. **Plan structured logging**: Determine log events, structured fields, log levels, and retention requirements for each component. Deliverable: logging specification per component.
4. **Design metrics**: Define counters, histograms, and gauges with label schemas, aggregation windows, and alert thresholds. Deliverable: metric catalog with label cardinality estimates.
5. **Design trace spans**: Map the distributed trace topology, define span names, attributes, and context propagation points. Deliverable: trace topology diagram with span definitions.
6. **Plan alerting rules**: Define alert conditions, severity levels, runbook links, and escalation paths for each SLO. Deliverable: alerting rule specifications.
7. **Document the plan**: Compile all specifications into an instrumentation plan document for the implementer. Deliverable: approved instrumentation plan.

## Anti-Patterns

- **Planning after launch.** Designing observability after deployment means the first incident hits without visibility. *Why*: instrumentation built under incident pressure is reactive and incomplete.
- **Metric sprawl without purpose.** Planning metrics for every possible measurement without tying them to SLOs or debugging scenarios creates noise. *Why*: unused metrics waste storage and distract from signals that matter.
- **Ignoring cardinality.** Defining label schemas without estimating cardinality leads to metric backend failures at scale. *Why*: high-cardinality labels are the most common cause of monitoring infrastructure overload.
- **Logging as the only strategy.** Relying exclusively on logs without metrics or traces makes aggregate analysis and request-path debugging impractical. *Why*: each observability pillar answers different questions; logs alone cannot replace metrics dashboards or trace waterfalls.

## Output

**On success**: Produces an instrumentation plan containing SLI/SLO definitions, a logging specification, a metric catalog, a trace topology diagram, and alerting rule specifications. Delivered to the instrumentation implementer for codification.

**On failure**: Report which service boundaries could not be mapped (e.g., undocumented dependencies, third-party black boxes), what partial plan was produced, and what information is needed to complete the plan.

## Related Skills

- [`instrumentation-implementer`](../instrumentation-implementer/SKILL.md) -- implements the plan this skill produces.
- [`builder`](../builder/SKILL.md) -- builds the services that this plan targets for instrumentation.
- [`data-model-designer`](../../../engineering/database-expert/data-model-designer/SKILL.md) -- designs data models whose query performance may need observability coverage.
