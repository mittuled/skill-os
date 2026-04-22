---
name: environment-parity-planner
description: Keeps dev, staging, and production environments aligned so that what works in one works in all. Use when asked to environment parity planner. Suggest when relevant.
department: engineering
agent: devops-infrastructure-engineer
version: 1.0.0
complexity: medium
related-skills:
  - infrastructure-scaling-executor
  - alerting-configurator
  - production-readiness-reviewer
triggers:
  - "plan environment parity"
  - "dev prod parity"
  - "environment consistency"
  - "staging parity"
  - "environment alignment"
---

# environment-parity-planner

## Agent: Social Media Manager

L2 DevOps and infrastructure engineer responsible for CI/CD pipelines, deployment automation, cloud infrastructure, monitoring, alerting, incident response, and rollout management.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

The DevOps / Infrastructure Engineer plans how to maintain parity between development, staging, and production environments.

## When to Use

- A new set of environments is being provisioned and parity must be designed in from the start.
- Bugs are appearing in production that cannot be reproduced in staging or development.
- Infrastructure drift between environments is causing deployment failures.
- A compliance requirement mandates environment consistency documentation.

## Workflow

1. Inventory all environment-specific differences: infrastructure versions, configurations, data, feature flags, and third-party integrations.
2. Classify each difference as intentional (e.g., scaled-down resources in dev) or unintentional drift.
3. Define the parity policy: which dimensions must be identical and which may differ with justification.
4. Implement infrastructure-as-code templates shared across environments with environment-specific variable overrides.
5. Set up automated drift detection that compares environment configurations on a schedule.
6. Establish a remediation process for detected drift: alert, investigate, and reconcile.
7. Document the parity policy, known intentional differences, and the drift detection setup.
   - **Deliverable**: Environment parity policy, shared IaC templates, drift detection configuration, and documentation.

## Anti-Patterns

- **Manually configuring environments independently.** *Why*: Manual configuration guarantees drift because no two humans will make identical changes across environments.
- **Accepting drift as normal.** *Why*: Every untracked difference is a potential "works in staging, fails in prod" incident waiting to happen.
- **Forcing 100% parity including scale.** *Why*: Development environments do not need production-scale resources; parity means configuration consistency, not resource duplication.

## Output

**Success**: A documented parity policy with shared IaC, automated drift detection, and a remediation process that keeps environments aligned.

**Failure**: A drift report listing all detected discrepancies between environments, their risk level, and a remediation plan.

## Related Skills

*None defined yet.*
- [`infrastructure-scaling-executor`](../infrastructure-scaling-executor/SKILL.md) — sibling skill under the same agent — combine with infrastructure-scaling-executor for end-to-end coverage
- [`alerting-configurator`](../alerting-configurator/SKILL.md) — sibling skill under the same agent — combine with alerting-configurator for end-to-end coverage
- [`production-readiness-reviewer`](../production-readiness-reviewer/SKILL.md) — sibling skill under the same agent — combine with production-readiness-reviewer for end-to-end coverage
