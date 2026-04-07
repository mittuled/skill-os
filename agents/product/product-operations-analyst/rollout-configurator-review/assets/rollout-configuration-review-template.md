# Rollout Configuration Review

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Product Operations Analyst] |
| Feature | [Feature name] |
| Flag Name / ID | [Exact flag identifier in the feature flag system] |
| Target Activation Date | [YYYY-MM-DD] |
| Reviewer | [Name] |
| Skill | rollout-configurator-review |

## Configuration Verification

[Verify the flag configuration matches the approved rollout plan.

GUIDANCE: Pull the current flag configuration from the feature flag system and compare against the approved cohort specification document. Document any discrepancy.]

| Configuration Dimension | Approved | Configured | Match? |
|------------------------|---------|-----------|--------|
| Targeting rule (plan tier) | | | Yes / No |
| Rollout percentage | | | Yes / No |
| Exclusion rules | | | Yes / No |
| Geographic restriction | | | Yes / No |
| Account-level exclusions | | | Yes / No |

**Overall Configuration Match**: Yes / No (if No, list discrepancies below)

## Discrepancies

[Document any difference between approved plan and current configuration.
GUIDANCE: Each discrepancy must be resolved before activation — either fix the configuration or update the approval to reflect the change.]

## Rollback Readiness

- [ ] Flag-off tested in staging — feature disabled as expected
- [ ] Rollback runbook documented and linked: [URL]
- [ ] On-call engineer confirmed aware of rollback procedure: [Name]
- [ ] Rollback time estimate: [X minutes]
- [ ] Post-rollback data cleanup required: [Yes (describe) / No]

## Monitoring Coverage

- [ ] Primary metric [metric name] instrumented: [Yes / No]
- [ ] Alert threshold set at [value] for [metric]: [Yes / No]
- [ ] Dashboard linked: [URL]
- [ ] On-call acknowledged alert thresholds: [Name, date]
- [ ] Error rate baseline documented: [X%]

## Approval Record

| Approver | Role | Status | Date |
|----------|------|--------|------|
| [Name] | Product Manager | Approved / Pending | |
| [Name] | Engineering Lead | Approved / Pending | |
| [Name] | CS / Account Manager | Approved / Pending / N/A | |

## Scoring Summary

| Criterion | Score (0-10) | Weight | Weighted Score |
|-----------|-------------|--------|---------------|
| Flag Configuration Accuracy | | 30% | |
| Rollback Readiness | | 25% | |
| Monitoring Coverage | | 25% | |
| Approval Completeness | | 20% | |
| **Composite** | | **100%** | |

**Grade**: [A+ / A / B / C / D / F]
**Verdict**: [Cleared / Conditional / Hold / Blocked]

## Conditional Items (if applicable)

[Items that must be resolved before or immediately after activation.]

| Item | Owner | Due |
|------|-------|-----|
| | | |
