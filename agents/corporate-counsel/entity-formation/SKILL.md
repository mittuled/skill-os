---
name: entity-formation
description: >
  This skill handles legal entity formation including incorporation documents
  and state filings. Use when asked to incorporate a company, form an LLC, or
  file formation documents with a state. Also consider when a founder is
  starting a new venture and needs a legal entity. Suggest when the user is
  signing contracts or issuing equity without a formed entity.
department: legal
agent: corporate-counsel
version: 1.0.0
complexity: medium
related-skills:
  - ../bylaws-and-board-setup/SKILL.md
  - ../founder-equity-issuance/SKILL.md
---

# entity-formation

## Agent: Corporate Counsel

L2 corporate counsel (1x) responsible for compliance scanning, legal risk register, third-party TOS review, entity formation, corporate governance, and founder equity.

Department ethos: [ideal-legal.md](../../../departments/legal/ideal-legal.md)

## Skill Description

Handles the legal entity formation process including selecting entity type, preparing incorporation documents, filing with the state, and obtaining required registrations.

## When to Use

- When founders are ready to incorporate and need the legal entity established before issuing equity, opening bank accounts, or signing contracts.
- When expanding into a new jurisdiction that requires a subsidiary or foreign qualification filing.
- When converting from one entity type to another (e.g., LLC to C-Corp) in preparation for venture financing.

## Workflow

1. **Entity Type Confirmation**: Confirm the entity type decision (C-Corp, LLC, S-Corp, etc.) based on business goals, tax considerations, and financing plans. Verify the chosen state of incorporation. Deliverable: entity type confirmation memo.
2. **Document Preparation**: Prepare the certificate of incorporation (or articles of organization for LLC) including authorized share classes, par value, registered agent designation, and any special provisions. Deliverable: draft formation documents.
3. **State Filing**: File formation documents with the Secretary of State. Pay filing fees and request expedited processing if needed. Obtain the stamped filing confirmation and entity number. Deliverable: filed and stamped formation documents.
4. **Post-Formation Setup**: Obtain an EIN from the IRS. Register for state tax accounts. File foreign qualification in any states where the company will operate. Designate a registered agent in each jurisdiction. Deliverable: EIN confirmation and state registrations.
5. **Corporate Records Assembly**: Assemble the initial corporate records including formation documents, EIN letter, registered agent agreements, and any state registrations into the corporate minute book. Deliverable: organized corporate minute book.

## Anti-Patterns

- **Incorporating in the wrong state**: Choosing a state based on cost alone without considering investor expectations, tax implications, or case law. *Why*: most venture-backed startups incorporate in Delaware for its well-developed corporate law; deviating without reason creates friction during fundraising.
- **Incorrect share authorization**: Authorizing too few shares or wrong share classes at formation, requiring an early amendment. *Why*: amendments cost time and money, and under-authorized shares can block equity issuance to founders and employees.
- **Skipping foreign qualification**: Operating in states without registering as a foreign entity. *Why*: failure to qualify can result in penalties, inability to enforce contracts in that state's courts, and back-taxes.

## Output

**On success**: Produces stamped formation documents, EIN confirmation, state registrations, and an organized corporate minute book. Delivered to founders and General Counsel.

**On failure**: Report which filings could not be completed (e.g., name conflict, missing information), what the current entity status is, and what corrective actions are needed. Escalate to General Counsel.

## Related Skills

- [`bylaws-and-board-setup`](../bylaws-and-board-setup/SKILL.md) -- Bylaws and board setup is the immediate next step after entity formation.
- [`founder-equity-issuance`](../founder-equity-issuance/SKILL.md) -- Founder equity cannot be issued until the entity is legally formed.
