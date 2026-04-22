---
name: infrastructure-scaling-executor
description: >
  This skill executes infrastructure scaling operations in response to load or
  growth. Use when asked to scale up services, add capacity, or resize
  infrastructure. Also consider when monitoring alerts indicate resource
  saturation. Suggest when the user is experiencing performance degradation
  without scaling response.
department: engineering
agent: devops-infrastructure-engineer
version: 1.0.0
complexity: medium
related-skills:
  - ../infrastructure-load-testing/SKILL.md
  - ../performance-monitor/SKILL.md
  - ../infrastructure-requirements-extractor/SKILL.md
  - ../../platform-engineer/platform-scale-preparation/SKILL.md
  - alerting-configurator
  - ci-cd-pipeline-builder
  - cloud-foundation-setup
  - deployment-architecture-designer
  - deployment-automation
  - environment-parity-planner
  - feature-flag-configurator
  - github-org-setup
  - incident-response-planner
  - infrastructure-cost-optimiser
triggers:
  - "execute infra scaling"
  - "scale infrastructure"
  - "infra scale-up"
  - "run scaling operation"
  - "infrastructure scale out"
---

# infrastructure-scaling-executor

## Agent: DevOps / Infrastructure Engineer

L2 DevOps and infrastructure engineer (1x) responsible for CI/CD pipelines, deployment automation, cloud infrastructure, monitoring, alerting, incident response, and rollout management.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Executes infrastructure scaling operations -- both horizontal and vertical -- in response to load increases, growth projections, or performance degradation.

## When to Use

- When monitoring alerts indicate resource saturation (CPU, memory, disk, or network) approaching threshold limits.
- When load testing results show the current infrastructure cannot meet upcoming traffic targets.
- When planned growth (product launch, market expansion) requires proactive capacity increases.

## Workflow

1. **Scaling Assessment**: Analyze the scaling trigger (alert, load test result, growth plan). Determine whether horizontal scaling (more instances), vertical scaling (larger instances), or architectural changes are needed. Deliverable: scaling assessment with recommended approach.
2. **Change Planning**: Define the specific scaling changes: instance counts, instance types, auto-scaling policies, database read replicas, cache cluster sizes. Calculate cost impact. Deliverable: scaling change plan with cost estimate.
3. **Execution**: Apply scaling changes using infrastructure-as-code (Terraform, Pulumi, CloudFormation) or orchestration tools (Kubernetes HPA/VPA). Execute during low-traffic windows for non-urgent changes. Deliverable: applied infrastructure changes with deployment record. [GATE]
4. **Validation**: Verify the scaling changes are effective by monitoring resource utilization, latency, and error rates post-change. Run targeted load tests if needed. Deliverable: validation report confirming scaling effectiveness.
5. **Documentation Update**: Update infrastructure documentation, runbooks, and capacity plans to reflect the new configuration. Adjust auto-scaling policies and alert thresholds as needed. Deliverable: updated infrastructure documentation.

## Anti-Patterns

- **Manual scaling without automation**: Executing one-off scaling changes without updating infrastructure-as-code or auto-scaling policies. *Why*: manual changes drift from the declared state, causing confusion during incidents and making future scaling unreliable.
- **Scaling without root cause analysis**: Adding capacity to mask a performance bug (memory leak, N+1 query, missing index). *Why*: scaling delays the fix while increasing cost; the underlying issue will eventually overwhelm any amount of capacity.
- **Scaling everything simultaneously**: Scaling all tiers (web, app, database, cache) at once without identifying the actual bottleneck. *Why*: over-scaling wastes resources and obscures which component was the constraint.

## Output

**On success**: Produces applied scaling changes with deployment record, validation report, and updated documentation. Delivered to the engineering team with cost impact summary.

**On failure**: Report which scaling operations failed (e.g., quota limits, provider errors), what partial changes were applied, and rollback actions taken. Escalate to VP Engineering if service degradation continues.

## Related Skills

- [`infrastructure-load-testing`](../infrastructure-load-testing/SKILL.md) -- Load testing validates whether scaling changes achieve the target capacity.
- [`performance-monitor`](../performance-monitor/SKILL.md) -- Performance monitoring detects the resource saturation that triggers scaling.
- [`alerting-configurator`](../alerting-configurator/SKILL.md) — sibling skill under the same agent — combine with alerting-configurator for end-to-end coverage
- [`ci-cd-pipeline-builder`](../ci-cd-pipeline-builder/SKILL.md) — sibling skill under the same agent — combine with ci-cd-pipeline-builder for end-to-end coverage
- [`cloud-foundation-setup`](../cloud-foundation-setup/SKILL.md) — sibling skill under the same agent — combine with cloud-foundation-setup for end-to-end coverage
- [`deployment-architecture-designer`](../deployment-architecture-designer/SKILL.md) — sibling skill under the same agent — combine with deployment-architecture-designer for end-to-end coverage
- [`deployment-automation`](../deployment-automation/SKILL.md) — sibling skill under the same agent — combine with deployment-automation for end-to-end coverage
- [`environment-parity-planner`](../environment-parity-planner/SKILL.md) — sibling skill under the same agent — combine with environment-parity-planner for end-to-end coverage
- [`feature-flag-configurator`](../feature-flag-configurator/SKILL.md) — sibling skill under the same agent — combine with feature-flag-configurator for end-to-end coverage
- [`github-org-setup`](../github-org-setup/SKILL.md) — sibling skill under the same agent — combine with github-org-setup for end-to-end coverage
- [`incident-response-planner`](../incident-response-planner/SKILL.md) — sibling skill under the same agent — combine with incident-response-planner for end-to-end coverage
- [`infrastructure-cost-optimiser`](../infrastructure-cost-optimiser/SKILL.md) — sibling skill under the same agent — combine with infrastructure-cost-optimiser for end-to-end coverage
