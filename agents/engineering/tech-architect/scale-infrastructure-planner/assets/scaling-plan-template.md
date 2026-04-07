# Infrastructure Scaling Plan

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Tech Architect name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | scale-infrastructure-planner |
| System / Service | [System name] |
| Planning Horizon | [3 / 6 / 12 months — state the end date] |
| Trigger | [What prompted this plan: growth projection / post-mortem / launch] |

## Executive Summary

[2–3 sentences covering the primary bottlenecks identified, the scaling strategy selected, and the projected cost impact.

GUIDANCE: Good — "At projected 10K concurrent users by Q3, the PostgreSQL connection pool (currently at 65% utilisation) will be exhausted first; adding PgBouncer and one read replica extends headroom to 25K users with a $420/month increase. The phased migration can be completed with zero downtime." Bad — "The infrastructure needs to be scaled to handle more traffic."]

## Scale Requirements

| Metric | Current | 3-Month Target | 6-Month Target | 12-Month Target | Data Source |
|--------|---------|---------------|----------------|-----------------|-------------|
| Concurrent users | [N] | [N] | [N] | [N] | [Source] |
| Requests per second (p95) | [N] | [N] | [N] | [N] | [Source] |
| Data storage (GB) | [N] | [N] | [N] | [N] | [Source] |
| Peak-to-average ratio | [N:1] | [N:1] | [N:1] | [N:1] | [Source] |

GUIDANCE: All targets must come from product growth projections or historical trend data — not estimates. If data is unavailable, document the assumption and its confidence level.

## Capacity Gap Analysis

| Component | Current Capacity | Projected Peak Demand | Utilisation at Peak | Headroom | Bottleneck? |
|-----------|-----------------|----------------------|--------------------|---------  |------------|
| App server tier | [e.g., 4 × 2 vCPU] | [N rps] | [N%] | [months until limit] | Yes/No |
| Database primary | [e.g., db.r6g.xlarge] | [N connections / IOPS] | [N%] | [months until limit] | Yes/No |
| Cache layer | [e.g., cache.r6g.large 13GB] | [N MB working set] | [N%] | [months until limit] | Yes/No |
| Object storage | [N TB] | [N TB] | [N%] | [months until limit] | Yes/No |

GUIDANCE: "Bottleneck?" = Yes if utilisation at peak exceeds 80%. Highlight rows with Yes in bold.

## Scaling Strategy Per Component

### [Component 1: e.g., Application Server Tier]

**Strategy**: [Horizontal auto-scaling / Vertical / CDN offload / etc.]

**Implementation**:
- [Specific step 1 — e.g., "Set HPA target CPU utilisation to 70%; min 3 replicas, max 10"]
- [Specific step 2]

**Monitoring Thresholds** (per `references/framework.md`):
- Warning: [N% / metric]
- Critical: [N% / metric]

**Timeline**: [When to implement relative to projected bottleneck date]

---

### [Component 2]

[Repeat structure for each bottleneck component]

## Cost Projection

| Scenario | Monthly Infrastructure Cost | Delta vs. Current | Key Driver |
|----------|----------------------------|-------------------|------------|
| Current state | $[N] | Baseline | — |
| 3-month plan | $[N] | +$[N] (+N%) | [What drives the increase] |
| 6-month plan | $[N] | +$[N] (+N%) | [What drives the increase] |
| 12-month plan | $[N] | +$[N] (+N%) | [What drives the increase] |

**Cost optimisation applied**: [List reserved instances, spot usage, or storage tiering decisions that reduce cost]

## Phased Migration Plan

| Phase | Changes | Risk Level | Duration | Rollback Procedure |
|-------|---------|------------|----------|--------------------|
| Phase 1 | [e.g., Add PgBouncer connection pooler] | Low | 1 day | [Remove PgBouncer; revert app config] |
| Phase 2 | [e.g., Provision read replica; migrate reads] | Medium | 3 days | [Route all reads to primary; delete replica] |
| Phase 3 | [e.g., Resize primary to db.r6g.2xlarge] | Medium | 4h maintenance window | [Resize back; restore from snapshot] |

GUIDANCE: Never group more than one medium-risk or high-risk change in a single phase. Each phase must have a tested rollback procedure.

## Recommendations

**P1 — Implement before projected bottleneck date:**
- [Specific change, owner, target date]

**P2 — Implement within 3-month plan:**
- [Specific change, owner, target date]

**P3 — Implement in 6–12 month plan:**
- [Specific change, owner, target date]

## Appendices

### A. Methodology

Plan produced using `scale-infrastructure-planner` skill and `references/framework.md` decision matrices. Bottleneck order followed canonical sequence. Cost estimates sourced from [AWS/GCP/Azure] pricing calculator as of [date].

### B. Monitoring Dashboard Links

[Links to current dashboards for each component in the capacity gap analysis]

### C. Supporting Data

[Baseline metrics exports, load test results, growth model spreadsheet]
