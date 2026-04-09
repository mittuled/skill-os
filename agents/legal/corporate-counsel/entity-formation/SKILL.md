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
  - ../../general-counsel/entity-type-decision/SKILL.md
  - ../83b-election-coordinator/SKILL.md
---

# entity-formation

## Agent: Corporate Counsel

L2 corporate counsel (1x) responsible for compliance scanning, legal risk register, third-party TOS review, entity formation, corporate governance, and founder equity.

Department ethos: [ideal-legal.md](../../../../departments/legal/ideal-legal.md)

## Skill Description

Handles the legal entity formation process including selecting entity type, preparing incorporation documents, filing with the state, and obtaining required registrations.

## When to Use

- When founders are ready to incorporate and need the legal entity established before issuing equity, opening bank accounts, or signing contracts.
- When expanding into a new jurisdiction that requires a subsidiary or foreign qualification filing.
- When converting from one entity type to another (e.g., LLC to C-Corp) in preparation for venture financing.

## Workflow

1. **Entity Type Confirmation**: Follow the pre-filing preparation section of `references/checklist.md`. Confirm the entity type decision (C-Corp, LLC, S-Corp) and verify the chosen state of incorporation. Check name availability with Secretary of State and reserve if needed. Deliverable: entity type confirmation memo.
2. **Document Preparation**: Prepare the certificate of incorporation (DGCL 102 for Delaware C-Corp) or articles of organization for LLC. Follow the certificate checklist in `references/checklist.md`: authorized share structure (standard 10M Common + 5M Preferred at $0.00001 par value), DGCL 102(b)(7) exculpation provision, registered agent designation, and purpose clause. Deliverable: draft formation documents.
3. **State Filing**: File formation documents with the Secretary of State per the state filing section of `references/checklist.md`. Pay filing fees (Delaware C-Corp: $89 standard / $189 expedited). Obtain the stamped filing confirmation and entity number. Deliverable: filed and stamped formation documents. [GATE]
4. **Post-Formation Setup**: Follow the federal and state registrations sections of `references/checklist.md`. Obtain EIN (Form SS-4). Register for state tax accounts. File foreign qualification in each state where the company will transact business. File S-Corp election (Form 2553) within 75 days if applicable. Deliverable: EIN confirmation and state registrations.
5. **Corporate Records Assembly**: Assemble the corporate minute book per the records assembly section of `references/checklist.md`: formation documents, EIN letter, registered agent agreements, state registrations, and blank stock ledger. Calendar annual report deadlines (Delaware: March 1 for C-Corp). Hand off to bylaws-and-board-setup and founder-equity-issuance. Deliverable: organized corporate minute book.

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
