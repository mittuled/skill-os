---
name: risk-register-builder-eng
description: >
  This skill builds and maintains the engineering risk register for a delivery. Use when asked to
  identify engineering risks, create a risk log, or assess threats to delivery success. Also consider
  when a new phase begins or a significant scope change occurs. Suggest when a project lacks a
  formal risk tracking mechanism.
department: engineering
agent: vp-engineering
version: 1.0.0
complexity: medium
related-skills:
  - ../../../engineering/vp-engineering/go-live-approver-lead/SKILL.md
  - ../../../engineering/vp-engineering/scope-boundary-setter-eng/SKILL.md
---

# risk-register-builder-eng

## Agent: VP Engineering

L1 engineering leader (1x) responsible for spec intake review, team allocation, architecture oversight, velocity monitoring, and go-live approvals. Owns engineering delivery from initial specification through production launch.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Builds and maintains the engineering risk register, cataloging delivery risks with likelihood, impact, mitigations, and owners.

## When to Use

- When a new delivery begins and no risk register exists.
- When a phase transition, scope change, or incident reveals new risks that must be tracked.
- When preparing for a go-live approval that requires a current risk assessment.

## Workflow

1. **Risk identification**: Survey the delivery scope, architecture, dependencies, team composition, and timeline for potential risks. Use categories: technical, operational, resource, external, security. Deliverable: raw risk list.
2. **Risk assessment**: Rate each risk by likelihood (low/medium/high) and impact (low/medium/high/critical). Calculate a risk score. Deliverable: assessed risk list with scores.
3. **Mitigation planning**: For each medium-or-higher risk, define a mitigation strategy (avoid, reduce, transfer, accept). Assign an owner and a timeline. Deliverable: mitigation plan per risk.
4. **Register assembly**: Compile risks into a structured register with ID, description, category, likelihood, impact, score, mitigation, owner, and status. Deliverable: engineering risk register.
5. **Ongoing maintenance**: Review and update the register at phase boundaries, after incidents, and during retrospectives. Close mitigated risks, add new ones. Deliverable: updated risk register with changelog.

## Anti-Patterns

- **Set-and-forget**: Creating the register at project start and never updating it. *Why*: stale risk registers give false confidence and miss emerging threats.
- **Risk inflation**: Listing every conceivable risk without scoring or prioritizing. *Why*: an unprioritized list overwhelms decision-makers and dilutes focus on the risks that matter.
- **Ownerless risks**: Logging risks without assigning a responsible individual. *Why*: unowned risks have no one accountable for mitigation, so they remain open indefinitely.

## Output

**On success**: Produces a risk register containing each risk's ID, description, category, likelihood, impact, risk score, mitigation strategy, owner, and status. Delivered as a living document in the project repository, reviewed at every phase boundary.

**On failure**: Report which risk categories could not be assessed (e.g., pending architecture decisions, unknown third-party SLAs), the impact on register completeness, and what must be resolved to close the gaps.

## Related Skills

- [`go-live-approver-lead`](../../../engineering/vp-engineering/go-live-approver-lead/SKILL.md) -- the risk register is a key input to go-live approval decisions.
- [`scope-boundary-setter-eng`](../../../engineering/vp-engineering/scope-boundary-setter-eng/SKILL.md) -- scope boundary changes often introduce new risks to track.
