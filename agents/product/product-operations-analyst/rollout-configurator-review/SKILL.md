---
name: rollout-configurator-review
description: >
  This skill reviews rollout configuration (flags, cohorts, percentages) before activation.
  Use when a feature flag or rollout configuration is ready for review before being turned on in production.
  Also consider when a rollout plan has changed since initial setup and the configuration needs revalidation.
  Suggest when an engineer is about to activate a feature flag but no ops review of the configuration has occurred.
department: product
agent: product-operations-analyst
version: 1.0.0
complexity: medium
related-skills: []
---

# rollout-configurator-review

## Agent: Product Operations Analyst
L3 product operations analyst (multi-instance) responsible for rollout configuration, adoption tracking, revenue impact monitoring, support triage, and iteration prioritisation.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Reviews rollout configuration (flags, cohorts, percentages) before activation.

## When to Use
- When a feature flag or rollout configuration has been set up and needs review before activation
- When the rollout plan specifies staged percentages and the configuration needs to match the plan
- When a rollout configuration was created weeks ago and the plan has since changed, requiring revalidation
- When a previous rollout had configuration errors (wrong cohort, wrong percentage, missing kill switch) and the team wants to prevent recurrence

## Workflow
1. **Pull the rollout plan**: Retrieve the approved rollout plan including target cohorts, rollout percentages, timing, and success/rollback criteria. Confirm the plan is current and has PM sign-off. Deliverable: rollout plan reference with version and approval status.
2. **Inspect the configuration**: Review the actual feature flag or rollout configuration in the tooling (LaunchDarkly, Split, internal system). Check flag name, targeting rules, cohort definitions, percentage allocations, and any environment-specific overrides. Deliverable: configuration snapshot documenting every setting.
3. **Validate against the plan**: Compare the configuration to the rollout plan point by point. Check that cohort targeting matches the cohort selector output, percentages match the planned stages, and no unintended users are included or excluded. Deliverable: validation checklist with pass/fail per configuration element.
4. **Verify rollback capability**: Confirm that a kill switch exists and works — the flag can be turned off instantly without a deployment. Verify who has permission to trigger the rollback. Deliverable: rollback verification confirming mechanism, permissions, and estimated time-to-rollback.
5. **Approve or request changes**: If all checks pass, approve the configuration for activation. If issues are found, document them with specific remediation steps and route back to the engineer. Deliverable: approval sign-off or change request with itemised issues.

## Anti-Patterns
- **Rubber-stamping without inspection**: Approving the configuration based on trust without actually checking the targeting rules and percentages. *Why*: Configuration errors are the most common cause of rollout incidents — a typo in a targeting rule can expose the wrong users or the entire user base.
- **Reviewing configuration without the rollout plan**: Checking that the flag "looks reasonable" without comparing it to the specific approved plan. *Why*: A configuration can be internally consistent but wrong relative to what was planned — the plan is the source of truth.
- **Skipping rollback verification**: Assuming the kill switch works without testing or confirming permissions. *Why*: Discovering the rollback mechanism is broken during an incident is the worst possible time — verification must happen before activation.

## Output
**On success**: A configuration review sign-off confirming the rollout configuration matches the approved plan, targeting is correct, percentages are accurate, and rollback capability is verified — clearing the configuration for activation.
**On failure**: Report which configuration elements failed validation (e.g., cohort mismatch, missing kill switch, incorrect percentage), what the configuration currently shows vs. what the plan requires, and the specific changes needed before re-review.

## Related Skills
- (none yet — cross-references added in Phase 1.6)
