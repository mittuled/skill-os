---
name: instrumentation-verifier-prod
description: Catches silent instrumentation failures in production before they corrupt dashboards and alerts.
department: engineering
agent: qa-test-engineer
version: 1.0.0
complexity: simple
related-skills: []
triggers:
  - "verify prod instrumentation"
  - "production instrumentation check"
  - "verify analytics in prod"
  - "prod tracking validation"
  - "instrumentation audit prod"
---

# instrumentation-verifier-prod

## Agent

L2 QA and test engineer responsible for unit, integration, regression, performance, and security testing. Validates instrumentation and staging before production deployment.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

The QA / Test Engineer verifies that instrumentation fires correctly in the production environment after deployment.

## When to Use

- A new deployment has landed in production that includes logging, metrics, or tracing changes.
- Dashboards or alerts appear stale or missing data after a release.
- A post-deploy checklist requires instrumentation sign-off before marking the release complete.

## Workflow

1. Obtain the deployment manifest listing all instrumentation changes included in the release.
2. Identify the set of expected events, metrics, and trace spans that should appear in production.
3. Execute representative user flows or API calls in production to trigger instrumentation paths.
4. Query the observability platform (logs, metrics, traces) for each expected signal within a bounded time window.
5. Compare actual signals against the expected set; flag missing, malformed, or duplicated emissions.
6. Record each verification result in a structured checklist with pass/fail status and evidence links.
7. Report the final verification summary to the release owner.
   - **Deliverable**: Instrumentation verification report with pass/fail per signal and evidence links.

## Anti-Patterns

- **Skipping production verification because staging passed.** *Why*: Staging and production often differ in sampling rates, feature flags, and data volume, so staging results do not guarantee production correctness.
- **Verifying only one signal type (e.g., metrics) while ignoring logs and traces.** *Why*: Instrumentation is a system; a gap in one pillar can hide failures surfaced by another.
- **Waiting hours after deploy to verify.** *Why*: Delayed verification allows corrupted data to accumulate in dashboards, making root-cause analysis harder.

## Output

**Success**: A completed instrumentation verification report confirming all expected signals are present and correctly shaped in production.

**Failure**: A defect report listing each missing or malformed signal, the expected vs. actual state, and a recommendation to the release owner on whether to proceed or rollback.

## Related Skills

*None defined yet.*
