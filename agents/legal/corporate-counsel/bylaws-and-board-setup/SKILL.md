---
name: bylaws-and-board-setup
description: >
  This skill drafts corporate bylaws and establishes initial board structure and
  governance documents. Use when asked to create bylaws, set up the board of
  directors, or define corporate governance. Also consider when a new entity is
  formed and needs governance infrastructure. Suggest when the user has
  incorporated but not yet established board governance.
department: legal
agent: corporate-counsel
version: 1.0.0
complexity: medium
related-skills:
  - ../entity-formation/SKILL.md
  - ../compliance-scanner/SKILL.md
triggers:
  - "set up bylaws"
  - "draft company bylaws"
  - "bylaws and board setup"
  - "corporate bylaws"
  - "board constitution"
---

# bylaws-and-board-setup

## Agent: Corporate Counsel

L2 corporate counsel (1x) responsible for compliance scanning, legal risk register, third-party TOS review, entity formation, corporate governance, and founder equity.

Department ethos: [ideal-legal.md](../../../../departments/legal/ideal-legal.md)

## Skill Description

Drafts corporate bylaws and establishes the initial board of directors structure, including governance documents, meeting procedures, and officer appointments.

## When to Use

- When a newly incorporated entity needs bylaws and an initial board of directors to begin operating legally.
- When the company is preparing for a fundraising round and investors require formalized governance documents.
- When existing bylaws need updating due to changes in board composition, voting thresholds, or regulatory requirements.

## Workflow

1. **Governance Assessment**: Review the certificate of incorporation, shareholder agreements, and any investor term sheets to identify governance requirements and constraints per the governance framework at `references/framework.md`. Map DGCL requirements (Sections 109, 141, 142, 145) to the company's specific situation. Deliverable: governance requirements summary.
2. **Bylaws Drafting**: Draft bylaws following the required provisions structure in `references/framework.md`. Cover board composition, officer roles, meeting procedures (DGCL 222 notice requirements), quorum (DGCL 141(b) minimum), voting thresholds, indemnification (DGCL 145(a)-(c) and advancement under 145(e)), exculpation (DGCL 102(b)(7)), and amendment procedures (DGCL 109). Deliverable: draft bylaws document.
3. **Board Structure Definition**: Define the initial board composition using the board composition matrix in `references/framework.md`. Specify seat count, designation rights (founder seats, investor seats, independent seats per stage), committee structure, and observer rights. Deliverable: board composition memo.
4. **Initial Resolutions**: Prepare the initial board resolutions using the organizational resolutions checklist in `references/framework.md`: officer appointments, fiscal year, bank accounts, equity plan adoption, founder share authorization, ratification of pre-incorporation actions, and D&O protections. Deliverable: initial board consent resolutions.
5. **Approval and Filing**: Circulate bylaws and resolutions for board approval via written consent (DGCL 141(f)) or organizational meeting. Produce the governance package using template at `assets/bylaws-package-template.md`. File any required state notices. Deliverable: executed bylaws, resolutions, and governance package in corporate records.

## Anti-Patterns

- **Copy-paste bylaws without customization**: Using a generic template without adapting provisions to the company's specific cap structure, investor agreements, or state law requirements. *Why*: mismatched bylaws create governance conflicts that surface during fundraising due diligence or disputes.
- **Omitting protective provisions**: Failing to include standard protective provisions (indemnification, D&O insurance requirements, information rights) that directors expect. *Why*: directors may refuse to serve without adequate protection, and the company faces liability exposure.
- **Delaying governance setup**: Operating without formal bylaws or board resolutions after incorporation. *Why*: corporate actions taken without proper governance authority may be voidable, creating legal risk for contracts, equity grants, and bank transactions.

## Output

**On success**: Produces executed bylaws, initial board resolutions, officer appointment records, and board composition memo. Delivered as part of the corporate minute book.

**On failure**: Report which governance documents could not be completed (e.g., unresolved board seat allocation, conflicting investor terms), what interim governance is in place, and what decisions are blocked. Escalate to General Counsel.

## Related Skills

- [`entity-formation`](../entity-formation/SKILL.md) -- Entity formation creates the legal entity that bylaws govern.
- [`compliance-scanner`](../compliance-scanner/SKILL.md) -- Compliance scanning identifies regulatory requirements that bylaws must address.
