---
name: decision-maker-mapper
description: >
  This skill maps the buying committee and decision-making structure at a target
  account to enable multi-threaded sales engagement. Use when pursuing enterprise
  deals with multiple stakeholders. Also consider when deal velocity slows due to
  unclear decision authority. Suggest when AE reports single-threaded deal risk.
department: sales
agent: sales-development-rep
version: 1.0.0
complexity: medium
related-skills:
  - ../cohort-selector-sales/SKILL.md
  - ../../sales-manager/sales-playbook-builder/SKILL.md
  - ../../account-executive/sales-signal-collector/SKILL.md
triggers:
  - "map buying committee"
  - "identify decision makers"
  - "stakeholder mapping"
  - "multi-thread this deal"
---

# decision-maker-mapper

## Agent: Sales Development Rep

L3 sales development representative (Nx) responsible for outbound prospecting, stakeholder mapping, and multi-threaded engagement at target accounts.

Department ethos: [ideal-sales.md](../../../departments/sales/ideal-sales.md)
Tool policy: [allowed-tools.yaml](../../../allowed-tools.yaml)

## Skill Description

Maps the buying committee and decision-making structure at a target account, identifying key stakeholders, their influence, and sentiment to enable multi-threaded sales engagement.

## When to Use

- When pursuing an enterprise deal with 3+ potential stakeholders and the buying committee structure is unknown or incomplete.
- When deal velocity has stalled because engagement is single-threaded to one contact who cannot unilaterally approve.
- When an AE flags single-threaded deal risk during pipeline review and broader stakeholder coverage is needed before the next stage gate.

## Workflow

1. **Organizational Research**: Identify the target account's organizational structure using LinkedIn, company website, press releases, and CRM data. Focus on the department(s) that own the problem your product solves. Deliverable: org chart sketch with names, titles, and reporting lines.

2. **Buying Committee Role Assignment**: Map each identified stakeholder to a buying committee role: Economic Buyer, User Buyer, Technical Buyer, Coach, Champion, Gatekeeper, or Blocker. Reference [framework.md](references/framework.md) for role definitions. Flag any role that cannot be assigned to a known individual. Deliverable: buying committee roster with role assignments.

3. **Influence and Sentiment Assessment**: Score each stakeholder's influence level (1-5) based on title seniority, budget authority, and organizational proximity to the decision. Assess sentiment as positive, neutral, negative, or unknown based on engagement history, public statements, and prior interactions. Deliverable: annotated roster with influence scores and sentiment tags.

4. **Coverage Gap Identification**: Compare the mapped committee against the ideal buying committee pattern for the deal size (see [framework.md](references/framework.md)). Identify missing roles, unknown sentiment contacts, and single points of failure. Deliverable: gap analysis listing unengaged or unidentified committee members.

5. **Multi-Threading Strategy**: Recommend entry points for each unengaged stakeholder. Prioritize by influence score and accessibility. Define the approach per stakeholder: warm introduction, content-based outreach, event invitation, or executive alignment. Deliverable: multi-threading plan with per-stakeholder engagement tactics.

6. **[GATE] Stakeholder Map Production**: Compile all findings into the stakeholder map using [stakeholder-map-template.md](assets/stakeholder-map-template.md). Review with the assigned AE before outreach begins. Deliverable: completed stakeholder map document.

## Anti-Patterns

- **Single-thread complacency**: Relying on one champion to navigate the deal internally without engaging other committee members. *Why*: champions leave, get overruled, or lack budget authority — a single-threaded deal has no fallback when the champion disengages, leading to silent deal death.

- **Title-based assumption**: Assuming the most senior person is the Economic Buyer without verifying actual budget authority. *Why*: in many organizations, budget authority sits with a VP or director rather than the C-suite executive, and targeting the wrong person wastes cycles and can trigger a Blocker.

- **Premature outreach to Blockers**: Contacting a known skeptic or competitor-aligned stakeholder before building internal support. *Why*: engaging a Blocker without a Champion to counterbalance gives the Blocker ammunition to shut down evaluation before momentum builds.

- **Stale mapping**: Treating the stakeholder map as a one-time artifact rather than a living document. *Why*: org changes, role rotations, and sentiment shifts during long sales cycles make month-old maps unreliable — review at every deal stage transition.

## Output

**On success**: Produces a completed stakeholder map document following [stakeholder-map-template.md](assets/stakeholder-map-template.md) containing account overview, buying committee roster with roles and influence scores, coverage gaps, and a prioritized multi-threading plan. Delivered to the assigned AE and stored in the CRM opportunity record.

**On failure**: Report what prevented complete mapping (e.g., limited LinkedIn visibility, no CRM history, organization too flat to identify distinct committee roles), what was partially completed, and recommended next steps such as requesting a warm introduction from an existing contact or using intent data to infer stakeholder interest.

## Related Skills

- [`cohort-selector-sales`](../cohort-selector-sales/SKILL.md) — Provides the target account list from which stakeholder mapping candidates are selected.
- [`sales-playbook-builder`](../../sales-manager/sales-playbook-builder/SKILL.md) — Defines the multi-threading engagement plays that this skill's output feeds into.
- [`sales-signal-collector`](../../account-executive/sales-signal-collector/SKILL.md) — Supplies engagement signals and CRM history used to assess stakeholder sentiment.
