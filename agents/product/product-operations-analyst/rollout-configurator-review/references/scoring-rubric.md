# Scoring Rubric: rollout-configurator-review

Reviews rollout configuration (flags, cohorts, percentages) before activation to ensure it matches the approved rollout plan and will not cause unintended exposure.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Flag Configuration Accuracy | 30% | Feature flag matches the approved cohort definition: correct targeting rules, percentage, exclusions |
| 2 | Rollback Readiness | 25% | Rollback mechanism is tested, documented, and accessible to on-call engineer |
| 3 | Monitoring Coverage | 25% | Key metrics are instrumented and alerting thresholds are set before activation |
| 4 | Approval Completeness | 20% | All required sign-offs obtained (PM, Engineering, CS if enterprise-exposed) |
| **Total** | | **100%** | |

## Scale

Each criterion is scored **0-10**:
- **0**: Not present / completely misconfigured
- **5**: Partially correct with significant gaps
- **10**: Fully correct, no gaps, verified

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Score | Label | Recommended Action |
|-------|-------|-------|-------------------|
| A+ | 9.0–10.0 | Cleared | Activate — configuration is production-ready |
| A | 8.0–8.9 | Cleared with notes | Activate — address notes post-launch |
| B | 7.0–7.9 | Conditional | Resolve flagged items before activating |
| C | 5.0–6.9 | Hold | Block activation; significant issues must be resolved |
| D/F | < 5.0 | Blocked | Do not activate; escalate to PM and Engineering |

## Signal Tables

### Flag Configuration Accuracy

| Score | Evidence |
|-------|----------|
| 9-10 | All targeting rules verified against approval document; percentage matches; exclusions applied; tested in staging with correct cohort sample |
| 7-8 | Rules mostly correct; minor discrepancy in one exclusion or segment boundary |
| 5-6 | Targeting partially correct; at least one rule differs from approved plan |
| 3-4 | Flag exists but configuration has not been verified against approval document |
| 0-2 | Flag misconfigured or missing; activation would expose wrong cohort |

### Rollback Readiness

| Score | Evidence |
|-------|----------|
| 9-10 | Rollback tested in staging; one-click disable verified; runbook linked in incident doc; on-call engineer confirmed awareness |
| 7-8 | Rollback procedure documented; not tested but straightforward flag-off |
| 5-6 | Rollback possible but not documented; requires manual steps |
| 3-4 | Rollback requires code change or migration; no documented procedure |
| 0-2 | No rollback path identified |

### Monitoring Coverage

| Score | Evidence |
|-------|----------|
| 9-10 | All primary metrics instrumented; alert thresholds set at agreed levels; dashboard linked; on-call acknowledged thresholds |
| 7-8 | Primary metrics instrumented; thresholds set but not all reviewed by on-call |
| 5-6 | Some metrics tracked; key metrics missing or thresholds not set |
| 3-4 | Monitoring exists for general health but not feature-specific metrics |
| 0-2 | No feature-specific monitoring in place |

### Approval Completeness

| Score | Evidence |
|-------|----------|
| 9-10 | All required approvals documented (PM, Engineering, CS/AM if applicable); approvals dated within 48 hours of activation |
| 7-8 | Core approvals present; one secondary approver outstanding |
| 5-6 | PM approval only; Engineering or CS sign-off missing |
| 3-4 | Verbal approval only; no written record |
| 0-2 | No documented approvals |
