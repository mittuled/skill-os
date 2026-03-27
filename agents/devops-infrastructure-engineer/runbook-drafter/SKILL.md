---
name: runbook-drafter
description: >
  This skill drafts operational runbooks for common infrastructure tasks and
  incident responses. Use when asked to create a runbook, document operational
  procedures, or standardize incident response. Also consider when a new
  service is deployed without operational documentation. Suggest when the user
  is handling incidents ad hoc without documented procedures.
department: engineering
agent: devops-infrastructure-engineer
version: 1.0.0
complexity: medium
related-skills:
  - ../performance-monitor/SKILL.md
  - ../production-readiness-reviewer/SKILL.md
---

# runbook-drafter

## Agent: DevOps / Infrastructure Engineer

L2 DevOps and infrastructure engineer (1x) responsible for CI/CD pipelines, deployment automation, cloud infrastructure, monitoring, alerting, incident response, and rollout management.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

Drafts operational runbooks that document step-by-step procedures for common infrastructure tasks, incident response scenarios, and failure recovery, enabling consistent and rapid operational response.

## When to Use

- When a new service is approaching production and needs operational documentation before the production readiness review.
- When an incident reveals a gap in operational procedures and a runbook needs to be created or updated.
- When on-call engineers need standardized procedures for recurring operational tasks (certificate rotation, database failover, cache flush).

## Workflow

1. **Scenario Identification**: Identify the operational scenarios that need runbooks: common alerts, known failure modes, routine maintenance tasks, and incident response procedures. Prioritize by frequency and impact. Deliverable: runbook backlog prioritized by urgency.
2. **Procedure Documentation**: For each scenario, document the step-by-step procedure including diagnostic commands, remediation actions, validation checks, and escalation criteria. Write in imperative voice with exact commands. Deliverable: draft runbook for each scenario.
3. **Context Addition**: Add context that helps the on-call engineer understand the system: architecture diagrams, dependency maps, key metrics to watch, and common false positives. Deliverable: enriched runbooks with operational context.
4. **Review and Validation**: Review runbooks with the engineering team that owns the service. Walk through each procedure to verify accuracy. Test commands in staging where possible. Deliverable: reviewed and validated runbooks.
5. **Publication and Linking**: Publish runbooks to the operational wiki. Link each runbook to the corresponding monitoring alert so on-call engineers can find it instantly when paged. Deliverable: published runbooks linked to alerts.

## Anti-Patterns

- **Runbooks with ambiguous steps**: Writing steps like "investigate the issue" or "check the logs" without specifying what to look for or which logs. *Why*: ambiguous steps are useless during incidents when engineers are stressed and need precise instructions.
- **Runbooks that are never updated**: Creating runbooks once and never revising them as the system evolves. *Why*: stale runbooks with incorrect commands or outdated architecture references are worse than no runbook because they waste time and can cause harm.
- **Overly long runbooks**: Creating single runbooks that cover too many scenarios or include extensive background information before the actionable steps. *Why*: during incidents, engineers need to find the relevant procedure in seconds; lengthy documents slow response time.

## Output

**On success**: Produces validated runbooks linked to monitoring alerts, covering identified operational scenarios. Delivered to the operations wiki with team notification.

**On failure**: Report which scenarios could not be documented (e.g., system behavior not well understood, missing access to production), what partial documentation exists, and what investigation is needed. Escalate if production services lack basic incident response procedures.

## Related Skills

- [`performance-monitor`](../performance-monitor/SKILL.md) -- Monitoring alerts link to runbooks for incident response guidance.
- [`production-readiness-reviewer`](../production-readiness-reviewer/SKILL.md) -- Runbooks are a required artifact in the production readiness review.
