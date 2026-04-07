# GA Rollout Plan

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Tech Lead / author name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | ga-rollout-executor-planner |

## Executive Summary

[2-3 sentences stating the feature/release name, the GA date, and the rollout strategy (phased vs. immediate) with the most critical risk.
GUIDANCE: Lead with the headline. Example: "Payments v2 will reach GA on 2026-04-15 via a 4-phase canary rollout over 5 days. The critical risk is the database migration at Phase 2, which requires a 15-minute maintenance window and tested rollback. All teams have confirmed readiness; DevOps will lead the deployment sequence."]

## Rollout Scope

[What is changing, for which users, and in which systems.

GUIDANCE:
- Good: List every service, config, and data migration included in this release; explicitly state what is NOT included
- Bad: "The new feature will go live"
- Format: Table]

| Component | Change Type | Affected User Segment | Owner Team |
|-----------|------------|----------------------|------------|
| [Service name] | [Code deploy / Config change / Schema migration / Feature flag] | [All users / Segment name / Internal only] | [Team name] |

**Explicitly out of scope**: [List items specifically excluded from this GA to prevent scope confusion]

## Phased Rollout Plan

[Step-by-step phases with entry criteria, actions, and exit gate metrics.

GUIDANCE:
- Good: Specific percentage gates with observable metrics (error rate, latency, support ticket volume) and exact thresholds
- Bad: "Roll out gradually and monitor"
- Format: One section per phase]

### Phase 0: Internal (Day 1)
**Target**: Engineering and internal staff only
**Entry criteria**: Go-live approval granted
**Actions**:
- [ ] Enable feature flag for internal user list
- [ ] Confirm monitoring dashboards active
- [ ] Alert runbooks distributed to on-call

**Exit gate**: 0 critical errors in 4 hours; p99 latency within budget; on-call team briefed

### Phase 1: Canary — 1% (Day 1)
**Target**: 1% of production users (random sample)
**Entry criteria**: Phase 0 exit gate passed
**Actions**:
- [ ] Update feature flag percentage to 1%
- [ ] Monitor error rate, latency, and key conversion metric for 4 hours

**Exit gate**: Error rate < 0.1%; p99 latency < [budget]; no user-reported blocking issues

### Phase 2: Limited — 10% (Day 2)
**Target**: 10% of production users
**Entry criteria**: Phase 1 exit gate passed
**Actions**:
- [ ] Update feature flag to 10%
- [ ] Monitor for 8 hours; hold overnight before proceeding

**Exit gate**: Error rate < 0.5%; p99 latency < [budget]; support ticket volume baseline unchanged

### Phase 3: Wide — 50% (Day 4)
**Target**: 50% of production users
**Entry criteria**: Phase 2 exit gate passed; no open P1 issues
**Exit gate**: All metrics within budget; product team confirms conversion metrics on target

### Phase 4: Full GA — 100% (Day 5)
**Target**: All users
**Entry criteria**: Phase 3 exit gate passed
**Actions**:
- [ ] Remove feature flag; feature enabled by default
- [ ] Archive rollout runbook; update on-call documentation

## Rollback Decision Matrix

[Define the exact conditions that trigger rollback and who has authority to call it.

GUIDANCE:
- Good: Specific metric thresholds tied to automated alerts
- Bad: "Roll back if something goes wrong"
- Format: Table]

| Trigger Condition | Threshold | Who Can Decide | Rollback Procedure |
|------------------|-----------|---------------|-------------------|
| Error rate spike | > [N]% for > 5 minutes | On-call engineer | Revert feature flag to previous percentage |
| p99 latency breach | > [budget × 1.5] for > 10 minutes | On-call engineer | Revert feature flag |
| DB error rate | > 0.1% | On-call + DBA | Immediate full rollback; page DBA for migration revert |
| Customer-reported data loss | Any report | Tech Lead (mandatory) | Full rollback + incident declaration |

**Rollback owner**: [Name and contact]
**Rollback tested in staging**: [Yes / No — date tested]

## Cross-Team Coordination Checklist

[All teams must confirm readiness before Phase 0 begins.

GUIDANCE:
- Each item must have a named owner and a confirmation status
- Do not start the rollout until all P1 items are confirmed]

| Team | Action Required | Owner | Confirmed? |
|------|----------------|-------|-----------|
| DevOps | Feature flag infrastructure deployed and tested | [Name] | [ ] |
| DevOps | Rollback procedure tested in staging | [Name] | [ ] |
| Product | Customer communication scheduled | [Name] | [ ] |
| Support | Escalation runbook distributed to support team | [Name] | [ ] |
| Data / Analytics | Metrics dashboards and alerts active | [Name] | [ ] |

## Recommendations

[Prioritized items to resolve before rollout begins.
GUIDANCE: P1 items are go/no-go blockers]

- **P1**: [Blocker that must be resolved before Phase 0 starts]
- **P2**: [Action that should complete before Phase 3]
- **P3**: [Post-rollout improvement for future releases]

## Appendices

### A. Methodology

[How phased percentages were determined, how rollback was tested, DORA baselines used to calibrate exit gate thresholds]

### B. Supporting Data

[Feature flag configuration, monitoring dashboard links, rollback runbook location, support escalation guide, rehearsal results]
