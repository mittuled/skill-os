---
name: incident-response-planner-support
description: >
  This skill plans incident response procedures for customer-impacting outages and escalations.
  Use when asked to define escalation paths, create incident playbooks, or prepare for outage scenarios.
  Also consider when the team has no documented response procedure for service disruptions.
  Suggest when a post-mortem reveals slow or disorganised incident communication.
department: customer-support
agent: support-manager
version: 1.0.0
complexity: medium
related-skills:
  - support-runbook-builder
  - support-activation
triggers:
  - "plan incident response"
  - "support incident response"
  - "create incident plan"
  - "incident response support"
  - "incident escalation plan"
---

# incident-response-planner-support

## Agent: Support Manager

L1 support manager (1x) reporting to the COO, responsible for support runbooks, help centre, incident response planning, and support activation. Owns queue management, SLA adherence, and support tooling.

Department ethos: [ideal-customer-support.md](../../../../departments/customer-support/ideal-customer-support.md)

## Skill Description

The incident response planner defines the support team's incident response procedures, escalation paths, communication templates, and severity classification so the team can respond to customer-impacting outages in a coordinated and timely manner.

## When to Use

- When the support team has no documented incident response procedure and is handling outages ad hoc.
- When a post-mortem reveals that incident communication to customers was slow, inconsistent, or missing.
- When the product scales to a point where outage impact affects a meaningful number of customers.
- When new SLA commitments require formalised incident response timelines.

## Workflow

1. **Define severity levels**: Establish severity classifications (S1-S4) with clear criteria based on customer impact, scope, and revenue exposure. Deliverable: severity matrix.
2. **Map escalation paths**: Document who gets notified at each severity level, including support, engineering, leadership, and external stakeholders. Deliverable: escalation tree.
3. **Draft communication templates**: Write customer-facing templates for incident acknowledgement, status updates, and resolution notifications per severity level. Deliverable: template library.
4. **Set response time targets**: Define target times for acknowledgement, first update, and resolution by severity level aligned with SLA commitments. Deliverable: response time SLA table.
5. **Design the war-room protocol**: Document how the support team coordinates with engineering during active incidents including communication channels, roles, and handoff procedures. Deliverable: war-room playbook.
6. **Test with a tabletop exercise**: Run a simulated incident scenario with the support team to validate the plan and identify gaps. Deliverable: tabletop exercise report with gap list.

## Anti-Patterns

- **Severity inflation**: Classifying every issue as S1 to get faster response. *Why*: when everything is critical, nothing is, and true S1 incidents get diluted attention.
- **Templates without personalisation guidance**: Providing rigid templates with no guidance on when to adapt tone. *Why*: robotic incident communication during a major outage damages customer trust more than the outage itself.
- **Planning without engineering alignment**: Defining escalation paths that engineering has not agreed to. *Why*: the plan fails at execution when engineering does not honour escalation expectations.

## Output

**On success**: A complete incident response plan containing a severity matrix, escalation tree, communication templates, response time targets, and a war-room playbook, validated by at least one tabletop exercise.

**On failure**: Report which components are incomplete (e.g., engineering escalation paths not confirmed), what was attempted, and recommend specific stakeholder meetings to close gaps.

## Related Skills

- [`support-runbook-builder`](../support-runbook-builder/SKILL.md) -- runbooks handle routine scenarios while incident plans handle outages and escalations.
- [`support-activation`](../support-activation/SKILL.md) -- activation sets up the support function; incident planning defines how it handles crises.
