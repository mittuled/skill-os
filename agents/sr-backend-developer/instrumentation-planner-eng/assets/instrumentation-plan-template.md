# Instrumentation Plan

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Agent role / human name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | instrumentation-planner-eng |

## Executive Summary

[2-3 sentences summarizing the instrumentation strategy: which service, how many SLIs defined, key metrics and alerts.
GUIDANCE: Lead with the SLO targets. Highlight any observability blind spots that remain.]

## Service Boundaries

[Map all entry points, exit points, internal components, and external dependencies.

GUIDANCE:
- Good: "OrderService: HTTP entry (POST /orders, GET /orders/:id), gRPC exit (InventoryService.Reserve), Postgres read/write, Redis cache, Stripe webhook receiver. Internal: OrderValidator, PricingEngine, FulfillmentDispatcher."
- Bad: "OrderService talks to other services."
- Format: Table with boundary type, endpoint/dependency, protocol, and instrumentation attachment point]

| Boundary | Type | Protocol | Instrumentation Point |
|----------|------|----------|----------------------|
| [Endpoint/dependency] | [Entry/Exit/Internal/External] | [HTTP/gRPC/SQL/Redis/etc.] | [Where to attach spans/metrics] |

## SLI/SLO Definitions

[Define service-level indicators and their target objectives.

GUIDANCE:
- Good: "Availability SLI: % of requests returning non-5xx in 5-min window. SLO: 99.9%. Latency SLI: P99 response time for POST /orders. SLO: < 500ms."
- Bad: "Service should be fast and reliable."
- Format: Table with SLI name, definition, measurement method, SLO target, and error budget]

| SLI | Definition | Measurement | SLO Target | Error Budget (30d) |
|-----|-----------|-------------|------------|-------------------|
| [Name] | [What is measured] | [How: counter ratio, histogram percentile] | [Target] | [Allowed failures] |

## Logging Specification

[Define structured log events per component.

GUIDANCE:
- Good: "Event: order.created. Level: INFO. Fields: {orderId, userId, totalAmount, itemCount, latencyMs}. Retention: 30d."
- Bad: "Log when orders happen."
- Format: Table per component with event name, level, fields, and retention]

| Component | Event | Level | Structured Fields | Retention |
|-----------|-------|-------|-------------------|-----------|
| [Name] | [event.name] | [DEBUG/INFO/WARN/ERROR] | [field list with types] | [Days] |

## Metric Catalog

[Define counters, histograms, and gauges with label schemas.

GUIDANCE:
- Good: "Metric: http_request_duration_seconds (histogram). Labels: method, path, status_code. Cardinality estimate: ~200 series. Alert: P99 > 500ms for 5 min."
- Bad: "Track response times."
- Format: Table with metric name, type, labels, cardinality estimate, and alert threshold]

| Metric | Type | Labels | Cardinality Est. | Alert Threshold |
|--------|------|--------|-----------------|----------------|
| [name] | [counter/histogram/gauge] | [label list] | [estimated series count] | [condition] |

## Trace Topology

[Map distributed trace span structure.

GUIDANCE:
- Good: "Root span: HTTP POST /orders → child: OrderValidator.validate → child: PricingEngine.calculate → child: gRPC InventoryService.Reserve → child: SQL INSERT orders. Context propagation: W3C traceparent header."
- Bad: "Add tracing."
- Format: Indented span tree with span names, attributes, and propagation method]

## Recommendations

[Prioritized list of instrumentation implementation steps.
GUIDANCE: Each recommendation should be:
- Specific (not "add monitoring" but "implement http_request_duration_seconds histogram at API gateway with method/path/status labels")
- Actionable (assignable to the instrumentation implementer)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[How this plan was developed: service documentation reviewed, existing instrumentation audited, SLO negotiation with product/engineering]

### B. Supporting Data

[Service dependency diagrams, existing metric inventory, alert history, incident retrospective references]
