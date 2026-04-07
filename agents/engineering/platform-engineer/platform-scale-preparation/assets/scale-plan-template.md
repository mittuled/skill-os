# Platform Scale Plan

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Agent role / human name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | platform-scale-preparation |

## Executive Summary

[2-3 sentences summarizing the scale assessment: current capacity headroom, projected exhaustion date, and top bottlenecks.
GUIDANCE: Lead with the most urgent bottleneck. State whether the platform can handle the next planned launch.]

## Capacity Profile

[Profile current capacity across all critical dimensions.

GUIDANCE:
- Good: "API tier: 8 instances x c5.2xlarge, handling 3,200 RPS (peak 4,100). Headroom: 22% before P99 degrades past SLO. Database: RDS r6g.2xlarge, 1,800 QPS (peak 2,400). Headroom: 12%. Binding constraint: database read throughput."
- Bad: "We have enough servers."
- Format: Table with component, current capacity, peak usage, headroom %, and binding constraint flag]

| Component | Instance/Config | Current Capacity | Peak Usage | Headroom | Binding? |
|-----------|----------------|-----------------|-----------|----------|----------|
| [Name] | [Instance type/count] | [metric + unit] | [metric + unit] | [%] | [Y/N] |

## Growth Model

[Translate user growth forecasts into infrastructure load.

GUIDANCE:
- Good: "User growth: 15% MoM. Current: 50K DAU → 85K DAU in 6 months. Load translation: 1 DAU = ~20 API calls/day = 11.5 RPS at peak. Projected peak RPS in 6 months: 19,700. Database QPS scales 1.3x per RPS due to N+1 queries. Capacity exhaustion: database at 3 months, API tier at 5 months."
- Bad: "We're growing fast."
- Format: Table with time horizon, projected users, projected load, and capacity status]

| Horizon | Projected DAU | Peak RPS | DB QPS | API Headroom | DB Headroom | Status |
|---------|--------------|----------|--------|-------------|-------------|--------|
| [Now / +3m / +6m / +12m] | [count] | [RPS] | [QPS] | [%] | [%] | [OK / Warning / Critical] |

## Bottleneck Inventory

[Map components that do not scale horizontally or degrade non-linearly.

GUIDANCE:
- Good: "Bottleneck 1: PostgreSQL primary (single-writer). Cannot scale horizontally without sharding. Degrades non-linearly above 2,000 QPS (lock contention). Blast radius: all write operations. Proximity to exhaustion: 3 months."
- Bad: "Database is slow."
- Format: Table with bottleneck, scaling constraint, degradation behavior, blast radius, and time to exhaustion]

## Scale Remediation Plan

[Sequenced remediations with cost and effort estimates.

GUIDANCE:
- Good: "Phase 1 (Month 1): Read replicas for database (2x read capacity, $800/mo, 2 engineer-weeks). Phase 2 (Month 2): Application-level caching with Redis for hot queries (3x reduction in DB QPS, $400/mo, 3 engineer-weeks). Phase 3 (Month 4): Database sharding by tenant ID (10x write capacity, 8 engineer-weeks)."
- Bad: "Scale up the database."
- Format: Phased table with remediation, capacity gain, cost, effort, and dependencies]

## Recommendations

[Prioritized scale preparation actions.
GUIDANCE: Each recommendation should be:
- Specific (not "scale the platform" but "provision 2 read replicas for PostgreSQL primary to extend database headroom from 3 months to 9 months")
- Actionable (assignable to a person/team)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[Profiling tools used, load testing methodology, growth data sources, cost estimation approach]

### B. Supporting Data

[Capacity profiling data, load test results, infrastructure cost calculator, growth forecast spreadsheet]
