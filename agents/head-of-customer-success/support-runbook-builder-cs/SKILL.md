---
name: support-runbook-builder-cs
description: >
  This skill builds runbooks for the CS team covering common customer scenarios
  and escalation paths. Use when asked to create CS runbooks, document
  escalation procedures, or standardize customer scenario handling. Also
  consider when CS team members handle the same scenario differently. Suggest
  when the user hires new CSMs without documented procedures.
department: customer-success
agent: head-of-customer-success
version: 1.0.0
complexity: medium
related-skills: []
---

# support-runbook-builder-cs

## Agent: Head of Customer Success

L1 customer success leader reporting to the CBO (1x) responsible for CS strategy, SLA design, playbook creation, expansion motion, and training materials.

Department ethos: [ideal-customer-success.md](../../../departments/customer-success/ideal-customer-success.md)

## Skill Description

Builds runbooks for the CS team covering common customer scenarios, resolution procedures, and escalation paths.

## When to Use

- When the CS team handles recurring customer scenarios inconsistently and needs standardized procedures.
- When new CSMs are joining the team and need documented procedures to ramp quickly.
- When a new product feature or workflow introduces customer scenarios that the team has not encountered before.

## Workflow

1. **Catalog Scenarios**: Inventory common customer scenarios from support tickets, CS conversations, and team input. Categorize by frequency and severity. Deliverable: prioritized scenario catalog.
2. **Document Resolution Procedures**: For each scenario, write step-by-step resolution instructions: diagnosis steps, resolution actions, customer communication templates, and verification that the issue is resolved. Deliverable: resolution procedure per scenario.
3. **Map Escalation Paths**: For each scenario, define when and how to escalate -- triggers for escalation, escalation target (engineering, product, leadership), and required context to include. Deliverable: escalation path per scenario.
4. **Review with Team**: Circulate draft runbooks to the CS team for feedback. Incorporate real-world nuances and edge cases from experienced CSMs. Deliverable: reviewed and validated runbooks.
5. **Publish and Maintain**: Publish runbooks in an accessible location. Establish a process for updating runbooks when scenarios change or new scenarios emerge. Deliverable: published runbooks with maintenance cadence.

## Anti-Patterns

- **Static runbooks**: Writing runbooks once and never updating them as the product evolves. *Why*: outdated procedures lead CSMs to follow wrong steps, making customer situations worse.
- **Over-detailed procedures**: Writing runbooks so detailed that they cannot adapt to scenario variations. *Why*: every customer situation has unique context; runbooks should provide decision frameworks, not scripts.
- **Runbooks without escalation criteria**: Documenting resolution steps but not when to stop troubleshooting and escalate. *Why*: CSMs without escalation guidance either escalate too early (wasting engineering time) or too late (harming the customer).

## Output

**On success**: Produces a runbook library containing categorized scenarios, resolution procedures, escalation paths, and communication templates. Delivered to the CS team.

**On failure**: Report which scenarios could not be documented (insufficient historical data, no established resolution), what partial runbooks were created, and what additional input is needed.

## Related Skills

- [`sla-definer-cs`](../sla-definer-cs/SKILL.md) -- SLAs define the escalation timing that runbooks must respect.
- [`training-material-creator-cs`](../training-material-creator-cs/SKILL.md) -- Training materials teach CSMs how to use the runbooks.
- [`cs-release-readiness`](../../cs-manager/cs-release-readiness/SKILL.md) -- New releases may require runbook updates for new scenarios.
