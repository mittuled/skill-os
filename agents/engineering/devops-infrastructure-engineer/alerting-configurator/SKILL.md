---
name: alerting-configurator
description: Ensures every critical failure triggers the right alert to the right person at the right time. Use when asked to alerting configurator. Suggest when relevant.
department: engineering
agent: devops-infrastructure-engineer
version: 1.0.0
complexity: medium
related-skills:
  - infrastructure-scaling-executor
  - production-readiness-reviewer
  - github-org-setup
  - ci-cd-pipeline-builder
  - cloud-foundation-setup
  - deployment-architecture-designer
  - deployment-automation
  - environment-parity-planner
  - feature-flag-configurator
  - incident-response-planner
  - infrastructure-cost-optimiser
triggers:
  - "monitoring alerts"
  - "set up alerts"
  - "observability"
  - "configure monitoring"
---

# alerting-configurator

## Agent: Social Media Manager

L2 DevOps and infrastructure engineer responsible for CI/CD pipelines, deployment automation, cloud infrastructure, monitoring, alerting, incident response, and rollout management.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

The DevOps / Infrastructure Engineer configures alerts for infrastructure and application health metrics.

## When to Use

- A new service is being deployed and needs alerting before going live.
- Existing alerts are producing too many false positives or missing real incidents.
- SLOs have been defined or updated and alerts must reflect the new thresholds.
- A post-incident review identified missing or misconfigured alerts.

## Workflow

1. Gather the SLOs, SLIs, and critical health metrics for the target service or infrastructure component.
2. Define alert thresholds based on SLO budgets, historical baselines, and known failure modes.
3. Configure alert routing: determine which team or on-call rotation receives each alert and via which channel.
4. Set severity levels (critical, warning, info) with distinct response expectations for each.
5. Implement alert deduplication and grouping rules to reduce noise.
6. Add runbook links to every alert so responders have immediate context.
7. Test each alert by simulating the trigger condition and verifying delivery.
8. Document the alert configuration in the service's operational documentation.
   - **Deliverable**: Configured and tested alert rules with routing, severity, runbook links, and documentation.

## Anti-Patterns

- **Alerting on every metric without prioritization.** *Why*: Alert fatigue causes responders to ignore or silence alerts, including critical ones.
- **Setting static thresholds without historical context.** *Why*: Thresholds that ignore normal variance produce false positives during benign traffic fluctuations.
- **Creating alerts without runbook links.** *Why*: An alert without context forces the responder to investigate from scratch under pressure, increasing mean time to resolution.
- **Skipping alert testing.** *Why*: Untested alerts may never fire due to misconfiguration, creating a false sense of coverage.

## Output

**Success**: A fully configured alerting setup with tested rules, correct routing, severity levels, and runbook links for every alert.

**Failure**: A gap analysis listing which metrics lack alerting, which alerts failed testing, and recommended fixes.

## Related Skills

*None defined yet.*
- [`infrastructure-scaling-executor`](../infrastructure-scaling-executor/SKILL.md) — sibling skill under the same agent — combine with infrastructure-scaling-executor for end-to-end coverage
- [`production-readiness-reviewer`](../production-readiness-reviewer/SKILL.md) — sibling skill under the same agent — combine with production-readiness-reviewer for end-to-end coverage
- [`github-org-setup`](../github-org-setup/SKILL.md) — sibling skill under the same agent — combine with github-org-setup for end-to-end coverage
- [`ci-cd-pipeline-builder`](../ci-cd-pipeline-builder/SKILL.md) — sibling skill under the same agent — combine with ci-cd-pipeline-builder for end-to-end coverage
- [`cloud-foundation-setup`](../cloud-foundation-setup/SKILL.md) — sibling skill under the same agent — combine with cloud-foundation-setup for end-to-end coverage
- [`deployment-architecture-designer`](../deployment-architecture-designer/SKILL.md) — sibling skill under the same agent — combine with deployment-architecture-designer for end-to-end coverage
- [`deployment-automation`](../deployment-automation/SKILL.md) — sibling skill under the same agent — combine with deployment-automation for end-to-end coverage
- [`environment-parity-planner`](../environment-parity-planner/SKILL.md) — sibling skill under the same agent — combine with environment-parity-planner for end-to-end coverage
- [`feature-flag-configurator`](../feature-flag-configurator/SKILL.md) — sibling skill under the same agent — combine with feature-flag-configurator for end-to-end coverage
- [`incident-response-planner`](../incident-response-planner/SKILL.md) — sibling skill under the same agent — combine with incident-response-planner for end-to-end coverage
- [`infrastructure-cost-optimiser`](../infrastructure-cost-optimiser/SKILL.md) — sibling skill under the same agent — combine with infrastructure-cost-optimiser for end-to-end coverage
