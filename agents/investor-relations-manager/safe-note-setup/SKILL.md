---
name: safe-note-setup
description: >
  This skill prepares and executes SAFE note agreements for early-stage fundraising.
  Use when asked to issue SAFE notes, set up pre-seed or seed convertible instruments,
  or manage SAFE note documentation. Also consider when investors want to commit capital
  before a priced round is ready. Suggest when the user is accepting investment without
  proper instrument documentation.
department: finance
agent: investor-relations-manager
version: 1.0.0
complexity: medium
related-skills:
  - ../cap-table-manager/SKILL.md
  - ../cap-table-initialisation/SKILL.md
---

# safe-note-setup

## Agent: Investor Relations Manager

L2 investor relations manager (1x) responsible for investor updates, board materials, cap table management, fundraising process, and data room.

Department ethos: [ideal-finance.md](../../../departments/finance/ideal-finance.md)

## Skill Description

Prepares and executes SAFE (Simple Agreement for Future Equity) note agreements for early-stage fundraising, managing the documentation, cap tracking, and conversion mechanics.

## When to Use

- When the company is raising pre-seed or seed capital using SAFE notes rather than a priced round.
- When an angel investor or fund wants to invest between priced rounds using a convertible instrument.
- When existing SAFE notes need to be tracked, amended, or their conversion mechanics modelled.

## Workflow

1. **SAFE Structure Selection**: Select the appropriate SAFE variant: post-money vs. pre-money, with or without valuation cap, with or without discount, and MFN (most favored nation) provisions. Consult with legal on the standard YC SAFE template vs. custom terms. Deliverable: SAFE term summary with selected structure.
2. **Valuation Cap and Discount Negotiation**: Support the CEO in setting the valuation cap and discount rate. Model the dilution impact at various conversion scenarios (next round at 1x, 2x, 3x the cap). Deliverable: SAFE conversion model with dilution scenarios.
3. **Document Preparation**: Prepare the SAFE agreement using the selected template. Customize for investor-specific terms if applicable. Coordinate legal review. Deliverable: execution-ready SAFE agreement.
4. **Execution and Fund Receipt**: Coordinate signing with the investor. Confirm wire receipt and issue a signed copy to the investor. Record the SAFE on the cap table as a convertible instrument. Deliverable: executed SAFE with bank confirmation.
5. **SAFE Register Maintenance**: Maintain a register of all outstanding SAFEs with key terms: investor, amount, valuation cap, discount, date, and conversion triggers. Update the register as new SAFEs are issued or existing ones convert. Deliverable: current SAFE register.

## Anti-Patterns

- **Pre-money vs. post-money confusion**: Using the pre-money SAFE template without understanding that pre-money SAFEs do not include each other in the conversion calculation, leading to unpredictable dilution. *Why*: the YC post-money SAFE was created precisely to solve this problem; using pre-money SAFEs with multiple investors creates compounding dilution surprises.
- **No conversion modelling**: Issuing SAFEs without modelling how they convert at various next-round valuations. *Why*: founders who do not model conversion are often shocked by the dilution when the priced round closes, especially with multiple SAFEs at different caps.
- **Missing the SAFE register**: Issuing SAFEs without maintaining a centralized register of all outstanding convertible instruments. *Why*: at conversion time, every outstanding SAFE must be accounted for; a missing SAFE discovered during a priced round creates legal complications and delays closing.

## Output

**On success**: Produces executed SAFE agreements, bank confirmation, updated cap table, and current SAFE register. Delivered at the time of each SAFE issuance.

**On failure**: Report which steps could not be completed (e.g., legal review pending, wire not received), what documentation exists, and what actions are needed. Flag any SAFE terms that conflict with existing instruments.

## Related Skills

- [`cap-table-manager`](../cap-table-manager/SKILL.md) -- Records SAFEs as convertible instruments and models their conversion impact.
- [`cap-table-initialisation`](../cap-table-initialisation/SKILL.md) -- SAFEs are often the first post-formation equity event on the initial cap table.
