---
name: rollback-planner
description: >
  This skill plans and documents rollback procedures for every deployment. Use
  when asked to create a rollback plan, define rollback criteria, or prepare
  for deployment failure. Also consider when a deployment lacks a documented
  recovery path. Suggest when the user is deploying without a rollback strategy.
department: engineering
agent: devops-infrastructure-engineer
version: 1.0.0
complexity: medium
related-skills:
  - ../progressive-rollout-executor/SKILL.md
  - ../rollout-configurator/SKILL.md
triggers:
  - "plan rollback"
  - "rollback strategy"
  - "deployment rollback plan"
  - "revert deployment plan"
  - "rollback runbook"
---

# rollback-planner

## Agent: DevOps / Infrastructure Engineer

L2 DevOps and infrastructure engineer (1x) responsible for CI/CD pipelines, deployment automation, cloud infrastructure, monitoring, alerting, incident response, and rollout management.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Plans and documents rollback procedures for every deployment, defining triggers, steps, validation criteria, and data recovery strategies to enable rapid reversion when deployments fail.

## When to Use

- When preparing any deployment to production and a rollback plan must be documented before the deploy can proceed.
- When a deployment involves schema migrations, data transformations, or other changes that make rollback non-trivial.
- When reviewing an existing rollback plan that may be outdated due to architectural changes.

## Workflow

1. **Change Analysis**: Analyze the deployment changes to determine rollback complexity. Classify as simple (code-only, stateless), moderate (configuration changes, feature flags), or complex (schema migrations, data transformations). Deliverable: rollback complexity assessment.
2. **Rollback Procedure**: Document the step-by-step rollback procedure including commands, scripts, and manual steps. For complex rollbacks, include data recovery steps and backward-compatible migration scripts. Deliverable: rollback procedure document.
3. **Trigger Definition**: Define the specific metrics, error conditions, or business impact thresholds that should trigger a rollback decision. Specify who has authority to initiate rollback. Deliverable: rollback trigger criteria.
4. **Validation Steps**: Define how to verify the rollback was successful: health checks, smoke tests, metric comparisons, and data integrity checks. Deliverable: rollback validation checklist.
5. **Rehearsal**: For complex rollbacks, rehearse the procedure in a staging environment. Time the rollback and verify all steps work as documented. Deliverable: rehearsal results with timing.

## Anti-Patterns

- **Rollback plans written after deployment**: Creating the rollback plan during or after deployment rather than before. *Why*: under incident pressure, plans are rushed and incomplete; pre-deployment planning ensures calm, thorough preparation.
- **Assuming all deployments are rollback-safe**: Treating every deployment as a simple code revert without analyzing data and schema changes. *Why*: a code rollback after a forward-only schema migration can corrupt data or break the application entirely.
- **Untested rollback procedures**: Documenting rollback steps without ever rehearsing them. *Why*: untested procedures fail in unexpected ways during real incidents when the team is already under stress.

## Output

**On success**: Produces a rollback procedure document with complexity assessment, trigger criteria, validation checklist, and rehearsal results. Delivered before deployment approval.

**On failure**: Report which aspects of the rollback could not be planned (e.g., irreversible data migration, third-party dependency), what partial rollback is possible, and what alternative recovery strategies exist. Escalate to VP Engineering if no viable rollback path exists.

## Related Skills

- [`progressive-rollout-executor`](../progressive-rollout-executor/SKILL.md) -- Progressive rollouts invoke the rollback plan when degradation is detected.
- [`rollout-configurator`](../rollout-configurator/SKILL.md) -- Rollout configuration defines the deployment that the rollback plan must cover.
