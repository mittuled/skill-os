---
name: progressive-rollout-executor
description: >
  This skill executes progressive rollouts incrementally with monitoring. Use
  when asked to perform a canary deployment, blue-green release, or phased
  rollout. Also consider when deploying a risky change that needs gradual
  exposure. Suggest when the user is deploying directly to 100% traffic without
  a progressive strategy.
department: engineering
agent: devops-infrastructure-engineer
version: 1.0.0
complexity: medium
related-skills:
  - ../rollout-configurator/SKILL.md
  - ../rollback-planner/SKILL.md
---

# progressive-rollout-executor

## Agent: DevOps / Infrastructure Engineer

L2 DevOps and infrastructure engineer (1x) responsible for CI/CD pipelines, deployment automation, cloud infrastructure, monitoring, alerting, incident response, and rollout management.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

Executes progressive rollouts (canary, blue-green, percentage-based) by incrementally shifting traffic to the new version while monitoring for errors and performance degradation.

## When to Use

- When deploying a change that carries risk (new infrastructure, schema migration, core logic change) and needs gradual exposure to limit blast radius.
- When the rollout configuration has been defined and the deployment is ready to begin execution.
- When a previous rollout was paused or rolled back and needs to be re-attempted with adjusted parameters.

## Workflow

1. **Pre-Rollout Verification**: Verify the rollout configuration (stages, percentages, durations, success criteria). Confirm the rollback plan is ready and tested. Verify monitoring dashboards and alerts are active. Deliverable: pre-rollout checklist confirmation.
2. **Initial Canary**: Deploy to the initial canary percentage (typically 1-5% of traffic). Monitor error rates, latency, and business metrics for the configured bake time. Compare canary metrics against the baseline. Deliverable: canary stage metrics and comparison.
3. **Progressive Expansion**: If canary metrics pass success criteria, advance to each subsequent stage (e.g., 10%, 25%, 50%, 100%). At each stage, monitor for the configured bake time before advancing. Deliverable: stage-by-stage metrics report. [GATE]
4. **Anomaly Response**: If metrics degrade at any stage, pause the rollout immediately. Assess whether the degradation is caused by the change or is coincidental. Execute rollback if the change is confirmed as the cause. Deliverable: anomaly assessment and action taken.
5. **Completion**: Once 100% traffic is on the new version and metrics are stable, mark the rollout as complete. Clean up old version resources. Update deployment records. Deliverable: rollout completion report.

## Anti-Patterns

- **Skipping bake time**: Advancing through rollout stages without waiting for the configured observation period. *Why*: some failures are latent (memory leaks, connection pool exhaustion) and only manifest after sustained traffic; short bake times miss these.
- **Monitoring only error rates**: Watching only HTTP error rates without tracking latency, business metrics, and resource utilization. *Why*: a deployment can return correct responses while degrading latency or consuming excessive resources, leading to cascading failures later.
- **Advancing despite ambiguous metrics**: Proceeding with the rollout when metrics are unclear or noisy rather than pausing to investigate. *Why*: ambiguity should bias toward caution; the cost of a slower rollout is far less than the cost of a production incident.

## Output

**On success**: Produces a rollout completion report with stage-by-stage metrics, anomaly assessments (if any), and final validation. Delivered to the engineering team and stakeholders.

**On failure**: Report which stage the rollout failed at, what metrics triggered the pause or rollback, what the current traffic split is, and recommended next steps. Escalate if rollback fails.

## Related Skills

- [`rollout-configurator`](../rollout-configurator/SKILL.md) -- The configurator defines the rollout parameters that this skill executes.
- [`rollback-planner`](../rollback-planner/SKILL.md) -- The rollback plan is invoked if the progressive rollout detects degradation.
