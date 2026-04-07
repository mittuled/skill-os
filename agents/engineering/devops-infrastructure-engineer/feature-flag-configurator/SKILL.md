---
name: feature-flag-configurator
description: Enables controlled rollout and instant rollback by configuring feature flags for every risky change.
department: engineering
agent: devops-infrastructure-engineer
version: 1.0.0
complexity: simple
related-skills: []
---

# feature-flag-configurator

## Agent

L2 DevOps and infrastructure engineer responsible for CI/CD pipelines, deployment automation, cloud infrastructure, monitoring, alerting, incident response, and rollout management.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

The DevOps / Infrastructure Engineer configures feature flags to enable controlled rollout and instant rollback.

## When to Use

- A new feature needs gradual rollout to a subset of users before full availability.
- A risky change requires an instant kill switch independent of deployment.
- The team wants to decouple deployment from release.
- A/B testing requires traffic splitting controlled by feature flags.

## Workflow

1. Identify the feature or change that requires a feature flag and define the flag's scope.
2. Create the flag in the feature flag platform with a descriptive name and owner.
3. Configure targeting rules: user segments, percentages, or environment-specific overrides.
4. Set the default state (enabled/disabled) for each environment.
5. Verify the flag works as expected in the QA or staging environment.
6. Document the flag's purpose, owner, expected lifetime, and cleanup plan.
   - **Deliverable**: A configured and tested feature flag with targeting rules, documentation, and cleanup plan.

## Anti-Patterns

- **Creating flags without a cleanup plan.** *Why*: Permanent flags accumulate as technical debt, increasing code complexity and testing surface.
- **Using flags for long-term configuration management.** *Why*: Feature flags are for temporary control; permanent configuration belongs in config files or environment variables.
- **Not testing the disabled state.** *Why*: If the flag is toggled off in an emergency, the disabled path must work correctly or the kill switch is useless.

## Output

**Success**: A configured feature flag with correct targeting, tested in staging, documented with owner and cleanup timeline.

**Failure**: A report identifying configuration issues (incorrect targeting, missing defaults) with recommended fixes before rollout.

## Related Skills

*None defined yet.*
