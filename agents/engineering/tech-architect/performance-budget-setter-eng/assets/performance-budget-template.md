# Performance Budget

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Tech Architect / author name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | performance-budget-setter-eng |

## Executive Summary

[2-3 sentences stating the service or feature, the most critical budget constraints, and whether the targets are achievable within the current architecture.
GUIDANCE: Lead with the headline constraint, not a list of all metrics. Example: "This budget governs the Checkout API v2 across 4 endpoint classes. The critical constraint is p99 latency < 500ms for the payment-initiation endpoint, which requires a database index change flagged in the feasibility section. All other targets are achievable within the current architecture."]

## Baseline Metrics

[Current measured performance before budget targets are set.

GUIDANCE:
- Good: "Measured over 14 days (2026-03-01 to 2026-03-14), excluding the incident window on 2026-03-08."
- Bad: "We think it's around 200ms"
- Format: Table per endpoint or component; all cells filled with measured values or marked "No baseline — spike required"]

| Endpoint / Component | p50 (ms) | p95 (ms) | p99 (ms) | Peak RPS | Error Rate | Memory (MB) |
|---------------------|----------|----------|----------|----------|------------|-------------|
| `[METHOD] /path` | [N] | [N] | [N] | [N] | [X%] | [N] |

## Performance Budget Targets

[Numeric targets by endpoint and metric.

GUIDANCE:
- Good: Set targets per percentile, derived from user expectations and architectural constraints
- Bad: "Should be fast" or a single "< 200ms" target with no percentile specification
- Format: Table matching baseline table; highlight cells where target is tighter than current baseline]

| Endpoint / Component | p50 target | p95 target | p99 target | Peak RPS target | Error rate target | Memory ceiling |
|---------------------|-----------|-----------|-----------|----------------|------------------|---------------|
| `[METHOD] /path` | [Nms] | [Nms] | [Nms] | [N] | [< X%] | [N MB] |

## Resource Budgets

[Infrastructure and payload constraints in addition to latency.

GUIDANCE:
- Good: Specify bundle size, DB query ceiling, CPU%, and payload limits with rationale
- Bad: Omit resource budgets because "it's fast enough"
- Format: Table per resource type]

| Resource | Budget | Current Baseline | Rationale |
|----------|--------|-----------------|-----------|
| JS bundle (gzip) | [N KB initial / N KB total] | [N KB] | [User expectation or Core Web Vitals target] |
| DB query ceiling | [N ms p99] | [N ms] | [Service budget allocation] |
| CPU at baseline | [< N%] | [N%] | [Headroom for traffic spikes] |
| Max payload (request) | [N KB] | [N KB] | [Mobile bandwidth constraint] |
| Cold start | [N ms] | [N ms] | [First-user experience] |

## Feasibility Assessment

[Engineering review of whether targets are achievable within the current architecture and delivery timeline.

GUIDANCE:
- Good: "p99 < 500ms for /payments is achievable only after adding a composite index on (user_id, created_at). Estimated effort: 1 day. Risk: requires migration on 50M-row table."
- Bad: "Looks fine to me"
- Format: One row per flagged risk; items with no risk need only a green check]

| Target | Feasible? | Blocking Issue | Estimated Effort | Risk |
|--------|----------|---------------|-----------------|------|
| [Endpoint p99 target] | [Yes / No / With changes] | [Specific technical blocker] | [Story points or days] | [Migration risk, regression risk, etc.] |

## Monitoring and Alert Mapping

[Every budget target must be backed by a live alert.

GUIDANCE:
- Good: Link each target to its monitoring dashboard widget and alert rule name
- Bad: "We'll set up monitoring later"
- Format: Table with budget, alert threshold, severity, and assigned owner]

| Budget Target | Warning Threshold | Critical Threshold | Alert Owner | Dashboard Link |
|---------------|------------------|--------------------|-------------|----------------|
| [Endpoint p99] | [> budget × 1.2] | [> budget × 1.5] | [On-call team] | [URL or TBD] |
| Error rate | > 1% | > 5% | [On-call team] | [URL or TBD] |

## Recommendations

[Prioritized actions required before this budget is binding.
GUIDANCE: Each item should be specific, assignable, and labeled P1/P2/P3]

- **P1**: [Action required before development starts — e.g., "Add baseline measurement for cold start on /auth endpoint"]
- **P2**: [Action required before production — e.g., "Implement DB index change to unblock p99 target for /payments"]
- **P3**: [Monitoring improvement — e.g., "Add p99.9 tracking to identify outlier causes"]

## Appendices

### A. Methodology

[Measurement tools and period (APM platform, RUM tool, synthetic monitor), how anomalies were excluded, who participated in the feasibility review]

### B. Supporting Data

[Raw percentile distributions, infrastructure limits (max DB connections, instance sizing), traffic model assumptions for peak RPS calculation]
