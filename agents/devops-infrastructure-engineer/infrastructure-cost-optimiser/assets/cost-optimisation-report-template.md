# Infrastructure Cost Optimisation Report: [Service / Account]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | DevOps / Infrastructure Engineer |
| Cloud Provider | [AWS / GCP / Azure / Multi-cloud] |
| Account / Project | [Account ID or project name] |
| Analysis Period | [Last 30 / 60 / 90 days] |
| Skill | infrastructure-cost-optimiser |
| Status | [Draft / Approved / Implemented] |

## Executive Summary

[2–3 sentences: total spend analyzed, total identified savings opportunity, quick-win savings implementable in < 1 week, and recommended priority action.
GUIDANCE: Lead with the number — "Total monthly spend: $48,200. Identified savings opportunity: $14,600/month (30.3%). $6,800 of savings are quick wins implementable within 3 days with zero risk to production."]

**Monthly spend (current)**: $[X]
**Identified savings**: $[X]/month ([X]%)
**Quick-win savings (< 1 week, zero downtime)**: $[X]/month
**Projected annual savings if all recommendations implemented**: $[X]

## Spend Analysis

### By Service

| Service | Monthly Cost | % of Total | 30-Day Trend | Notes |
|---------|-------------|-----------|-------------|-------|
| [EC2 / Compute Engine] | $[X] | [%] | [+/-X%] | |
| [RDS / Cloud SQL] | $[X] | [%] | [+/-X%] | |
| [S3 / GCS / Blob] | $[X] | [%] | [+/-X%] | |
| [Data Transfer] | $[X] | [%] | [+/-X%] | |
| [Other] | $[X] | [%] | [+/-X%] | |
| **Total** | **$[X]** | **100%** | | |

### By Environment

| Environment | Monthly Cost | % of Total | Justification |
|------------|-------------|-----------|---------------|
| Production | $[X] | [%] | Revenue-generating |
| Staging | $[X] | [%] | [Running 24/7? Should be scheduled.] |
| Development | $[X] | [%] | [Per-engineer or shared?] |
| DR / Backup | $[X] | [%] | [Retention policy enforced?] |

## Optimisation Opportunities

### Priority 1: Quick Wins (< 1 week, zero downtime risk)

| ID | Action | Service | Estimated Saving | Risk | Effort |
|----|--------|---------|-----------------|------|--------|
| OPT-001 | [Delete unattached EBS volumes] | EC2 | $[X]/mo | None | < 1 hr |
| OPT-002 | [Stop non-production instances outside business hours (nights + weekends)] | EC2 | $[X]/mo | None | 2 hrs |
| OPT-003 | [Remove unused Elastic IPs] | EC2 | $[X]/mo | None | 30 min |
| OPT-004 | [Delete unused load balancers] | ELB | $[X]/mo | Low | 1 hr |

**Subtotal**: $[X]/month

### Priority 2: Medium-Term (1–4 weeks, low risk)

| ID | Action | Service | Estimated Saving | Risk | Effort |
|----|--------|---------|-----------------|------|--------|
| OPT-010 | [Right-size over-provisioned EC2 instances based on CPU/memory utilization] | EC2 | $[X]/mo | Low | 1 week |
| OPT-011 | [Move S3 objects older than 90 days to Glacier Instant Retrieval] | S3 | $[X]/mo | None | 2 hrs |
| OPT-012 | [Convert on-demand RDS instances to Reserved Instances (1-year)] | RDS | $[X]/mo | None | Planning |
| OPT-013 | [Purchase Savings Plans for predictable EC2 baseline] | EC2 | $[X]/mo | None | Planning |

**Subtotal**: $[X]/month

### Priority 3: Architectural (4–12 weeks, requires planning)

| ID | Action | Service | Estimated Saving | Risk | Effort |
|----|--------|---------|-----------------|------|--------|
| OPT-020 | [Migrate batch workloads to Spot Instances] | EC2 | $[X]/mo | Medium | 2 weeks |
| OPT-021 | [Migrate underutilized services to Fargate Spot] | ECS | $[X]/mo | Medium | 3 weeks |
| OPT-022 | [Consolidate cross-region data transfer via VPC endpoints] | Data Transfer | $[X]/mo | Low | 1 week |

**Subtotal**: $[X]/month

## Implementation Plan

| Phase | Actions | Savings | Owner | Timeline |
|-------|---------|---------|-------|----------|
| Phase 1 (Quick wins) | OPT-001, 002, 003, 004 | $[X]/mo | DevOps | Week 1 |
| Phase 2 (Right-sizing) | OPT-010, 011 | $[X]/mo | DevOps + Engineering | Weeks 2–3 |
| Phase 3 (Commitments) | OPT-012, 013 | $[X]/mo | Finance + DevOps | Week 4 |
| Phase 4 (Architectural) | OPT-020, 021, 022 | $[X]/mo | Engineering | Weeks 5–12 |

## Tagging and Governance Gaps

| Resource Type | Untagged Count | % Untagged | Required Tags Missing |
|--------------|---------------|-----------|----------------------|
| EC2 instances | [N] | [%] | [team, service, environment, cost-center] |
| S3 buckets | [N] | [%] | |
| RDS instances | [N] | [%] | |

**Recommended action**: Enforce tag policy via [AWS Config / GCP Policy / Azure Policy]. Block untagged resource creation.

## Anomalies Detected

| Date | Service | Spike Amount | Investigation Status |
|------|---------|-------------|---------------------|
| [Date] | [Service] | $[X] above baseline | [Cause identified: X] |

## Monitoring and Budgets

**Current budget alerts configured?** [Yes / No]
**Recommended budget thresholds**:

| Alert | Threshold | Action |
|-------|-----------|--------|
| Monthly forecast > 110% of budget | $[X] | Notify engineering leads |
| Any single service increases > 30% week-over-week | Alert | Investigate within 24h |
| Total daily spend exceeds $[X] | Daily check | Review anomalies |
