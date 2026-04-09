---
name: rollout-configurator
description: >
  This skill configures rollout parameters such as canary percentages and
  traffic splitting. Use when asked to define rollout stages, set canary
  percentages, or configure traffic splitting rules. Also consider when a
  deployment strategy needs to be formalized. Suggest when the user is
  deploying without defined rollout parameters.
department: engineering
agent: devops-infrastructure-engineer
version: 1.0.0
complexity: medium
related-skills:
  - ../progressive-rollout-executor/SKILL.md
  - ../rollback-planner/SKILL.md
  - ../../tech-lead-pr-reviewer/ga-rollout-executor-planner/SKILL.md
triggers:
  - "configure rollout"
  - "rollout configuration"
  - "deployment rollout setup"
  - "release rollout config"
  - "rollout strategy setup"
---

# rollout-configurator

## Agent: DevOps / Infrastructure Engineer

L2 DevOps and infrastructure engineer (1x) responsible for CI/CD pipelines, deployment automation, cloud infrastructure, monitoring, alerting, incident response, and rollout management.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Configures rollout parameters including deployment strategy, canary percentages, traffic splitting rules, bake times, and success criteria for progressive deployments.

## When to Use

- When a deployment needs a defined rollout strategy with staged traffic shifting rather than a full cutover.
- When the risk profile of a change requires custom rollout parameters (slower ramp, longer bake times, stricter success criteria).
- When standardizing rollout configurations across services to establish organizational deployment patterns.

## Workflow

1. **Risk Assessment**: Evaluate the change risk based on scope (number of services affected), blast radius (percentage of users impacted), and reversibility (ease of rollback). Deliverable: risk assessment with recommended rollout aggressiveness.
2. **Strategy Selection**: Select the deployment strategy (canary, blue-green, rolling update, feature flag) based on risk assessment and infrastructure capabilities. Deliverable: strategy selection with rationale.
3. **Parameter Definition**: Define rollout stages (e.g., 1% -> 5% -> 25% -> 50% -> 100%), bake time per stage, success criteria (error rate < 0.1%, p99 latency < 200ms), and automatic vs. manual promotion gates. Deliverable: rollout configuration document.
4. **Monitoring Integration**: Configure monitoring queries and alert rules that map to the success criteria. Ensure dashboards show canary vs. baseline comparison. Deliverable: monitoring configuration for rollout.
5. **Configuration Deployment**: Apply the rollout configuration to the deployment pipeline (Argo Rollouts, Flagger, Spinnaker, or custom tooling). Validate the configuration in staging before production use. Deliverable: deployed and validated rollout configuration.

## Anti-Patterns

- **One-size-fits-all configuration**: Using the same rollout parameters for every deployment regardless of risk. *Why*: low-risk changes are slowed unnecessarily while high-risk changes may not get enough caution; configurations should match the change's risk profile.
- **Success criteria without baselines**: Defining success criteria (e.g., error rate < 0.1%) without first establishing the current baseline. *Why*: if the baseline error rate is already 0.08%, the success criteria provides almost no signal; criteria must detect meaningful regression.
- **Manual-only promotion gates**: Requiring manual approval for every stage advancement without an automated option. *Why*: manual gates slow low-risk rollouts and create bottlenecks; use automated promotion for low-risk changes and manual gates for high-risk ones.

## Output

**On success**: Produces a rollout configuration document with strategy selection, stage definitions, success criteria, and monitoring integration. Delivered as a deployable configuration to the CI/CD pipeline.

**On failure**: Report which parameters could not be configured (e.g., infrastructure does not support the selected strategy, monitoring gaps prevent success criteria evaluation), and what alternative configurations are viable. Escalate to VP Engineering.

## Related Skills

- [`progressive-rollout-executor`](../progressive-rollout-executor/SKILL.md) -- The executor uses the configuration this skill produces to run the actual rollout.
- [`rollback-planner`](../rollback-planner/SKILL.md) -- Rollback plans must account for the specific rollout configuration being used.
