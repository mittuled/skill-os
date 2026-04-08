---
name: staging-validator
description: Blocks broken releases by validating the full system in staging before production promotion.
department: engineering
agent: qa-test-engineer
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "release sign-off"
  - "release validation"
  - "staging validation"
  - "pre-release check"
---

# staging-validator

## Agent

L2 QA and test engineer responsible for unit, integration, regression, performance, and security testing. Validates instrumentation and staging before production deployment.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

The QA / Test Engineer validates the full system in the staging environment before production promotion.

## When to Use

- A release candidate is deployed to staging and requires sign-off before production.
- Staging has been refreshed with new infrastructure or data and needs re-validation.
- Multiple feature branches have merged and the combined behavior must be verified end-to-end.

## Workflow

1. Confirm the staging environment matches the expected release version and configuration.
2. Verify staging data state is representative of production (schema, volume, edge cases).
3. Execute the full end-to-end test suite covering critical user journeys.
4. Validate cross-service integrations, background jobs, and async workflows.
5. Confirm observability is functioning: logs are flowing, metrics are emitting, traces are connected.
6. Run smoke tests on any infrastructure changes (DNS, load balancers, certificates).
7. Document pass/fail results for each validation area in a staging sign-off checklist.
8. Apply the scoring rubric at `references/scoring-rubric.md`. Issue a promotion recommendation (proceed, proceed with caveats, or block).
   - **Deliverable**: Staging validation checklist with pass/fail per area and a promotion recommendation.

## Anti-Patterns

- **Treating staging as a second QA environment instead of a production mirror.** *Why*: If staging diverges from production in configuration or data, validation results do not predict production behavior.
- **Skipping observability validation.** *Why*: A release that works functionally but has broken logging or metrics will be undebuggable in production.
- **Signing off staging based on partial test coverage.** *Why*: Untested paths are where production incidents hide; partial coverage gives false confidence.
- **Promoting to production immediately without reviewing staging results.** *Why*: Rubber-stamping defeats the purpose of the staging gate and normalizes skipping quality checks.

## Output

**Success**: A completed staging validation checklist with all areas passing and a clear recommendation to promote to production.

**Failure**: A validation report listing each failing area, the impact assessment, and a recommendation to block promotion until issues are resolved.

## Related Skills

*None defined yet.*
