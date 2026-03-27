---
name: tam-playbook-contributor
description: >
  This skill contributes to the TAM playbook covering technical health
  frameworks and escalation procedures. Use when asked to create TAM processes,
  document technical health frameworks, or define technical escalation paths.
  Also consider when TAM processes are inconsistent across accounts. Suggest
  when the user assigns TAMs to accounts without documented procedures.
department: customer-success
agent: technical-account-manager
version: 1.0.0
complexity: simple
related-skills: []
---

# tam-playbook-contributor

## Agent: Technical Account Manager

L2 technical account manager (1x) responsible for technical health monitoring of enterprise accounts and identifying expansion opportunities.

Department ethos: [ideal-customer-success.md](../../../departments/customer-success/ideal-customer-success.md)
Tool policy: [allowed-tools.yaml](../../../allowed-tools.yaml)

## Skill Description

Contributes to the TAM playbook covering technical health frameworks, escalation procedures, and best practices for enterprise account management.

## When to Use

- When the TAM function needs documented processes for consistent enterprise account management.
- When new TAMs are joining and need standardized procedures to follow.
- When lessons learned from account management need to be captured as reusable playbook content.

## Workflow

1. **Identify Playbook Gaps**: Review current TAM practices and identify undocumented procedures, inconsistent approaches, and lessons learned that should be standardized. Deliverable: playbook gap list.
2. **Document Frameworks**: Write playbook sections covering technical health assessment methodology, escalation procedures, account review cadence, and integration monitoring approaches. Deliverable: drafted playbook sections.
3. **Validate with Peers**: Review drafted content with other TAMs and the CS Manager. Incorporate practical feedback and edge cases. Deliverable: peer-reviewed playbook content.
4. **Publish and Integrate**: Add approved content to the TAM playbook. Ensure it is accessible and referenced in TAM onboarding. Deliverable: published playbook updates.

## Anti-Patterns

- **Theoretical procedures**: Writing escalation procedures based on how things should work rather than how they actually work. *Why*: theoretical playbooks are ignored when real incidents occur because they do not match reality.
- **Static playbook**: Writing playbook content once without updating as the product and customer base evolve. *Why*: outdated procedures lead to wrong actions; playbooks must be living documents.
- **Individual knowledge hoarding**: Keeping effective practices as personal knowledge instead of contributing to the shared playbook. *Why*: knowledge that is not shared is lost when people leave; the playbook preserves institutional knowledge.

## Output

**On success**: Produces validated playbook sections covering technical health frameworks and escalation procedures. Delivered as additions to the TAM playbook.

**On failure**: Report which sections could not be documented (insufficient experience, undefined processes), what was drafted, and what operational experience is needed.

## Related Skills

- [`technical-health-monitor`](../technical-health-monitor/SKILL.md) -- The health monitoring practice that the playbook documents.
- [`technical-expansion-identifier`](../technical-expansion-identifier/SKILL.md) -- Expansion identification procedures documented in the playbook.
- [`support-runbook-builder-cs`](../../head-of-customer-success/support-runbook-builder-cs/SKILL.md) -- CS runbooks complement TAM playbooks for escalation alignment.
