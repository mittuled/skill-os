---
name: risk-register-legal
description: >
  This skill builds and maintains the legal risk register covering contractual,
  regulatory, and litigation risks. Use when asked to assess legal risks, create
  a risk register, or prioritize legal exposures. Also consider when entering
  new markets or signing material contracts. Suggest when the user is scaling
  operations without tracking legal risks.
department: legal
agent: corporate-counsel
version: 1.0.0
complexity: medium
related-skills:
  - ../compliance-scanner/SKILL.md
  - ../third-party-tos-reviewer/SKILL.md
triggers:
  - "build the legal risk register"
  - "what are our legal exposures"
  - "track legal risks"
  - "prioritize legal risks"
---

# risk-register-legal

## Agent: Corporate Counsel

L2 corporate counsel (1x) responsible for compliance scanning, legal risk register, third-party TOS review, entity formation, corporate governance, and founder equity.

Department ethos: [ideal-legal.md](../../../departments/legal/ideal-legal.md)

## Skill Description

Builds and maintains the legal risk register by identifying, categorizing, and prioritizing contractual, regulatory, IP, and litigation risks across the organization.

## When to Use

- When the company needs a consolidated view of its legal risk exposure for board reporting or investor due diligence.
- When entering a new market, launching a new product, or signing a material contract that introduces new legal risks.
- When a compliance scan or third-party TOS review surfaces risks that need ongoing tracking and mitigation.

## Workflow

1. **Risk Identification**: Gather legal risks from all sources: compliance scans, contract reviews, regulatory changes, employee matters, IP concerns, and pending or threatened claims. Deliverable: raw risk inventory.
2. **Risk Assessment**: Evaluate each risk on likelihood (low/medium/high) and impact (low/medium/high/critical). Categorize by type: contractual, regulatory, IP, employment, litigation. Deliverable: assessed risk register with severity matrix.
3. **Mitigation Planning**: Define mitigation actions for each high and critical risk. Assign owners, set deadlines, and identify any risks requiring insurance coverage or external counsel. Deliverable: mitigation plan with ownership assignments.
4. **Register Maintenance**: Update the register quarterly or upon material events. Track mitigation progress, close resolved risks, and add newly identified risks. Deliverable: updated risk register with change log.
5. **Reporting**: Prepare risk register summaries for the board, executive team, and auditors. Highlight changes since last report, top risks, and overdue mitigations. Deliverable: risk report for stakeholders.

## Anti-Patterns

- **Risk hoarding**: Maintaining the risk register in legal without sharing it with the executive team or board. *Why*: legal risks affect business decisions; stakeholders cannot make informed choices without visibility into the risk landscape.
- **Assessment without mitigation**: Identifying and scoring risks without defining mitigation actions or owners. *Why*: an unactioned risk register provides awareness but no risk reduction, creating a false sense of security.
- **Static severity ratings**: Never re-evaluating risk scores as the business or regulatory environment changes. *Why*: a risk rated low at seed stage (e.g., data privacy) may become critical at scale, and the register must reflect current reality.

## Output

**On success**: Produces an assessed risk register with severity matrix, mitigation plan, and stakeholder report. Delivered quarterly with ad hoc updates for material events.

**On failure**: Report which risk domains could not be assessed (e.g., insufficient contract access, pending litigation under privilege review), what partial coverage exists, and what information is needed. Escalate to General Counsel.

## Related Skills

- [`compliance-scanner`](../compliance-scanner/SKILL.md) -- Compliance gaps identified by the scanner feed into the risk register as regulatory risks.
- [`third-party-tos-reviewer`](../third-party-tos-reviewer/SKILL.md) -- TOS reviews surface contractual risks that the register must track.
