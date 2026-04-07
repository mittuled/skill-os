# Framework: ga-rollout-executor-planner

Defines the methodology for planning and executing general-availability rollouts from beta to full production.

## Rollout Strategy Selection

Choose the rollout strategy before designing the phase plan:

| Strategy | When to Use | Risk Profile |
|----------|-----------|-------------|
| **Canary (percentage-based)** | Feature flag infrastructure available; stateless or idempotent feature | Low — rollback by reducing flag percentage |
| **Dark Launch** | New backend service or infrastructure; no user-visible change yet | Very low — traffic routed but UI hidden |
| **Blue-Green** | Infrastructure change; zero-downtime swap required | Medium — requires 2× infrastructure cost during transition |
| **Phased User Segments** | B2B product; roll out to specific customer tiers first | Low-Medium — targets customers by contract or plan |
| **Big-Bang** | Emergency security patch; simple config change with no user impact | High — use only for non-user-facing changes |

Never use Big-Bang for user-facing features.

## Phase Gate Criteria Model

Every rollout phase requires:
1. **Entry criteria**: What must be true before this phase starts
2. **Observation window**: Minimum time to observe before advancing (even if metrics look clean)
3. **Exit gate metrics**: Quantitative thresholds that must hold over the observation window
4. **Rollback trigger**: Metric thresholds that trigger immediate rollback

### Standard Phase Structure

| Phase | User % | Min Observation Window | Exit Gate (error rate) | Exit Gate (p99 latency) | Rollback Trigger |
|-------|--------|----------------------|----------------------|------------------------|-----------------|
| Internal | 0% (staff only) | 2 hours | < 0.01% | Within budget | Any critical error |
| Canary 1% | 1% | 4 hours | < 0.1% | Within budget | > 0.5% error rate or > budget × 1.5 |
| Limited 10% | 10% | 8 hours (hold overnight) | < 0.5% | Within budget | > 1% error rate |
| Wide 50% | 50% | 8 hours | < 0.5% | Within budget | > 1% error rate |
| Full GA 100% | 100% | 24 hours (monitoring period) | < 0.5% | Within budget | > 1% error rate |

## Rollback Decision Matrix

Define rollback authority levels before execution begins:

| Trigger Condition | Metric Threshold | Authority to Decide | Rollback Method | Time to Execute |
|------------------|-----------------|-------------------|----------------|----------------|
| Error rate spike | > N% for > 5 min | On-call engineer (no approval needed) | Reduce feature flag % | < 5 minutes |
| p99 latency breach | > budget × 1.5 for > 10 min | On-call engineer | Reduce feature flag % | < 5 minutes |
| DB error rate | > 0.1% | On-call + DBA | Full rollback + migration revert | 15–30 minutes |
| Customer-reported data corruption | Any confirmed report | Tech Lead (mandatory) | Full rollback + incident declaration | Immediate |
| On-call judgment call | Undefined metric issue | On-call engineer | Reduce to previous phase % | < 5 minutes |

## Cross-Team Coordination Checklist

Must be completed before Phase 0 begins:

| Team | Required Confirmation | Deadline |
|------|--------------------|---------|
| DevOps / Infrastructure | Feature flag deployed and tested in staging | T-48h |
| DevOps | Rollback procedure tested in staging (including DB migrations if applicable) | T-24h |
| Monitoring / SRE | Dashboards live; alerts routing confirmed | T-24h |
| Product | Customer communication drafted and scheduled | T-24h |
| Customer Success | Escalation runbook shared with support team | T-12h |
| Tech Lead | Go-live approval signed | T-0 (before Phase 0) |

## Rehearsal Protocol

Every GA rollout requires a staging rehearsal before production execution:

1. **Execute the runbook verbatim**: Do not improvise during rehearsal
2. **Test the rollback**: Actually execute the rollback procedure and confirm the feature flag reverts
3. **Time each phase**: Record actual time for each step to calibrate the production schedule
4. **Document deviations**: Note any steps that required improvisation — update the runbook before production

**Rehearsal pass criteria**: All steps execute without improvisation; rollback tested and confirmed; all cross-team owners participated.

## Post-Rollout Monitoring Period

After reaching 100%, maintain elevated monitoring for 24 hours:
- Error rate: alert at 2× baseline
- p99 latency: alert at budget × 1.3
- Support ticket volume: watch for spike > 2× pre-launch baseline
- Key business metrics (conversion, retention): compare day-over-day

After 24 hours without incidents: declare rollout complete, archive runbook, and schedule feature flag cleanup.
