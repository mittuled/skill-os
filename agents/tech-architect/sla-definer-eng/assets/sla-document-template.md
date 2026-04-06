# Service Level Agreement Document

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Tech Architect name] |
| Version | [1.0] |
| Status | [Draft / Review / Ratified] |
| Skill | sla-definer-eng |
| Service Name | [Service or system name] |
| Criticality Tier | [Critical / High / Medium / Low] |
| Review Cadence | [Quarterly / Semi-annual] |
| Next Review Date | [YYYY-MM-DD] |

## Executive Summary

[2–3 sentences covering the service's criticality classification, its primary SLO targets, and the current error budget consumption trend.

GUIDANCE: Good — "The payment-api is classified Critical (revenue path); its monthly availability SLO is 99.95% (21.9 min error budget), p99 latency target is 300ms. Current trailing 30-day availability is 99.97%; the SLA with enterprise customers commits to 99.9% with 3× service credits on breach." Bad — "This document defines SLAs for our services."]

## Service Dependency Map

[Diagram or table showing upstream/downstream services and their criticality impact on this service.]

| Service | Direction | Criticality Impact | Current SLO |
|---------|-----------|-------------------|-------------|
| [e.g., auth-service] | Upstream | Blocking — failure = our failure | 99.95% |
| [e.g., notification-worker] | Downstream | Non-blocking | 99.9% |

## SLI Catalog

| SLI Name | Definition | Measurement Expression | Data Source |
|----------|-----------|----------------------|-------------|
| Availability | % of HTTP requests returning non-5xx | `(total - errors) / total × 100` | [Monitoring platform] |
| Latency (p99) | 99th percentile request completion time | `histogram_quantile(0.99, ...)` | [Monitoring platform] |
| Error rate | % of requests returning 5xx | `errors / total × 100` | [Monitoring platform] |
| [Add service-specific SLIs] | | | |

GUIDANCE: Each SLI must have a metric expression that can be copy-pasted into the monitoring platform. No SLI without a dashboard.

## SLO Targets

| SLI | Internal SLO Target | External SLA Commitment | Justification |
|-----|--------------------|-----------------------|---------------|
| Availability | [e.g., 99.95%] | [e.g., 99.9%] | [Why this target — baseline data or business requirement] |
| Latency (p99) | [e.g., 250ms] | [e.g., 500ms] | [Why this target] |
| Error rate | [e.g., 0.05%] | [e.g., 0.1%] | [Why this target] |

GUIDANCE: Internal SLO must be stricter than external SLA. If no external SLA exists, note "Internal only."

## Error Budgets

| SLI | SLO Target | Monthly Error Budget | Current Consumption (trailing 30d) | Status |
|-----|-----------|---------------------|-------------------------------------|--------|
| Availability | [N%] | [N minutes/month] | [N minutes] ([N% consumed]) | Healthy / Caution / Alert / Violated |
| Latency (p99) | [N ms] | [N% of requests may exceed] | [N% exceeded] | Healthy / Caution / Alert / Violated |

## Error Budget Policy

| Budget Consumed | Engineering Policy | Current State |
|----------------|-------------------|---------------|
| 0–50% | Normal development velocity | — |
| 50–75% | Pause non-critical deployments | — |
| 75–90% | Reliability improvements only | — |
| 90–100% | Feature freeze | — |
| > 100% | Incident review; SLA breach process | — |

[Reference policy detail in `references/framework.md`]

## Alerting Thresholds

| Alert | Burn Rate | Window | Severity | On-call Response |
|-------|-----------|--------|----------|-----------------|
| Availability burn (critical) | 14.4× | 1h | Page | Immediate |
| Availability burn (high) | 6× | 6h | Page | < 30 min |
| Availability burn (medium) | 3× | 24h | Ticket | Same day |
| Latency p99 budget burn | [N×] | [Window] | [Level] | [Response] |

## Monitoring Dashboard Links

| Dashboard | URL | Refreshes |
|-----------|-----|-----------|
| Availability + Error Rate | [URL] | Real-time |
| Latency Percentiles | [URL] | Real-time |
| Error Budget Burn Rate | [URL] | 5-minute |
| SLA Breach History | [URL] | Daily |

## Recommendations

**P1 — Required before ratification:**
- [ ] Verify all SLI measurements are actively collected and visualised
- [ ] Confirm alerting rules are deployed and tested with a synthetic incident

**P2 — Within 30 days of ratification:**
- [ ] Establish error budget review meeting cadence with engineering and product
- [ ] Document SLA breach notification procedure for external commitments

**P3 — At next review cycle:**
- [ ] Adjust SLO targets based on actual performance trend data

## Appendices

### A. Methodology

SLAs defined using `sla-definer-eng` skill. Criticality classification, SLO targets, and alerting thresholds sourced from `references/framework.md`. Ratified by: [names and dates].

### B. Historical Availability Data

[30-day availability chart or table used to justify SLO targets]

### C. SLA Breach Procedure

[Step-by-step process for notifying customers if external SLA is breached, including escalation path and compensation policy]
