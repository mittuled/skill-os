---
name: support-runbook-builder
description: >
  This skill builds operational runbooks covering common support scenarios, escalation paths, and
  response templates. Use when asked to document support procedures, create troubleshooting guides,
  or standardise agent responses. Also consider when new agents are onboarding and need procedural reference.
  Suggest when ticket resolution time variance is high across agents.
department: customer-support
agent: support-manager
version: 1.0.0
complexity: medium
related-skills:
  - support-activation
  - help-centre-builder-support
  - support-ticket-triage
triggers:
  - "build support runbooks"
  - "document support procedures"
  - "create troubleshooting guides"
  - "standardize agent responses"
---

# support-runbook-builder

## Agent: Support Manager

L1 support manager (1x) reporting to the COO, responsible for support runbooks, help centre, incident response planning, and support activation. Owns queue management, SLA adherence, and support tooling.

Department ethos: [ideal-customer-support.md](../../../../departments/customer-support/ideal-customer-support.md)

## Skill Description

The support runbook builder creates structured, step-by-step operational runbooks for common support scenarios so agents can resolve issues consistently, reduce resolution time variance, and escalate appropriately when a scenario exceeds their scope.

## When to Use

- When new support agents are onboarding and need documented procedures to handle common ticket types.
- When resolution time variance across agents is high, indicating inconsistent approaches to the same issue.
- When a new product feature launches and support needs documented troubleshooting procedures.
- When post-mortem analysis reveals that agents improvised responses for scenarios that should have standard procedures.

## Workflow

1. **Identify scenarios**: Analyse ticket data to identify the top recurring scenarios by volume and resolution complexity. Deliverable: prioritised scenario list.
2. **Draft runbook entries**: For each scenario, write a runbook entry with trigger conditions, diagnostic steps, resolution steps, and escalation criteria. Deliverable: draft runbook set.
3. **Add decision trees**: For complex scenarios with multiple branches, create decision-tree diagrams that guide agents through conditional logic. Deliverable: decision-tree diagrams.
4. **Include response templates**: Attach customer-facing response templates for each resolution path. Deliverable: response template library.
5. **Review with senior agents**: Route drafts through experienced agents for accuracy validation and gap identification. Deliverable: reviewed runbook set with feedback incorporated.
6. **Publish and index**: Publish runbooks in the support knowledge base with search-friendly titles and tags. Deliverable: published, indexed runbook library.

## Anti-Patterns

- **Writing runbooks in isolation**: Drafting procedures without input from agents who handle these scenarios daily. *Why*: the resulting runbooks miss practical nuances and agents ignore them.
- **Monolithic runbooks**: Creating a single massive document instead of modular, scenario-specific entries. *Why*: agents cannot quickly find the relevant procedure during a live customer interaction.
- **No escalation criteria**: Documenting resolution steps without defining when to stop troubleshooting and escalate. *Why*: agents spend excessive time on issues that require engineering intervention, hurting resolution time and customer experience.

## Output

**On success**: A published runbook library with modular, scenario-specific entries containing diagnostic steps, resolution steps, decision trees for complex scenarios, response templates, and clear escalation criteria.

**On failure**: Report which scenarios could not be documented (e.g., resolution path unclear, engineering input needed), what was completed, and recommend specific follow-ups to close gaps.

## Related Skills

- [`support-activation`](../support-activation/SKILL.md) -- activation stands up the support function; runbooks provide the operational content agents use daily.
- [`help-centre-builder-support`](../help-centre-builder-support/SKILL.md) -- customer-facing help articles often derive from internal runbooks.
- [`support-ticket-triage`](../../../customer-support/support-agent/support-ticket-triage/SKILL.md) -- triage routes tickets to the correct queue; runbooks tell agents what to do once they receive them.
