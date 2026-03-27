---
name: cap-table-manager
description: >
  This skill maintains the cap table including equity grants, exercises, and dilution
  modelling. Use when asked to update the cap table, model dilution from a new round,
  or process an option exercise. Also consider when equity events occur (grants, exercises,
  terminations) that need cap table reflection. Suggest when the user is issuing equity
  without updating the cap table.
department: finance
agent: investor-relations-manager
version: 1.0.0
complexity: medium
related-skills:
  - ../cap-table-initialisation/SKILL.md
  - ../fundraising-process-manager/SKILL.md
---

# cap-table-manager

## Agent: Investor Relations Manager

L2 investor relations manager (1x) responsible for investor updates, board materials, cap table management, fundraising process, and data room.

Department ethos: [ideal-finance.md](../../../departments/finance/ideal-finance.md)

## Skill Description

Maintains the cap table by recording equity grants, exercises, transfers, and cancellations, and modelling dilution scenarios to ensure accurate ownership records and informed equity decisions.

## When to Use

- When equity events occur (new grants, option exercises, RSU vesting, share transfers, terminations with equity implications).
- When a fundraising round is being modelled and dilution impact needs to be calculated for existing shareholders.
- When the board, auditors, or potential investors request a current cap table or ownership summary.

## Workflow

1. **Event Recording**: Record each equity event in the cap table system with full detail: grant date, vesting schedule, exercise price, share class, and any special terms (acceleration, repurchase rights). Cross-reference against board resolutions and legal documents. Deliverable: updated cap table with event audit trail.
2. **Vesting Schedule Tracking**: Track vesting progress for all outstanding grants. Calculate shares vested, unvested, and exercisable for each holder. Process vesting events (cliff dates, monthly vesting) on schedule. Deliverable: vesting schedule summary.
3. **Dilution Modelling**: Model the dilution impact of proposed transactions (new round, option pool increase, secondary sale) on all existing shareholders. Show pre-money and post-money ownership percentages. Deliverable: dilution model with waterfall analysis.
4. **409A Coordination**: Coordinate with the 409A valuation firm to ensure the current fair market value is updated at least annually or after material events. Verify that all option grants use the current 409A price. Deliverable: 409A valuation status and grant price verification.
5. **Cap Table Reconciliation**: Reconcile the cap table against legal records (stock ledger, board minutes, SAFE/convertible note register) quarterly. Investigate and resolve any discrepancies. Deliverable: reconciliation report with discrepancy resolution.

## Anti-Patterns

- **Spreadsheet-only cap table**: Managing the cap table in a spreadsheet rather than a purpose-built system (Carta, Pulley, AngelList) for companies beyond seed stage. *Why*: spreadsheets do not enforce data integrity, cannot model waterfall distributions, and create audit risk as the cap table grows complex.
- **Delayed event recording**: Waiting to batch-record equity events rather than recording them as they occur. *Why*: delayed recording creates reconciliation gaps and increases the risk of errors, especially around termination-related exercises and post-termination exercise windows.
- **Ignoring convertible instruments**: Tracking only issued shares while neglecting SAFE notes, convertible notes, and warrants in the fully-diluted calculation. *Why*: investors and the 409A firm need the fully-diluted picture; omitting convertibles understates dilution and overstates ownership.

## Output

**On success**: Produces an updated cap table with event audit trail, vesting summary, dilution model, and reconciliation report. Delivered on an ongoing basis with quarterly reconciliation.

**On failure**: Report which equity events could not be recorded (e.g., missing board resolution, unsigned grant agreement), what the cap table reflects as of the latest reconciliation, and what legal or administrative actions are needed. Escalate to CFO and counsel.

## Related Skills

- [`cap-table-initialisation`](../cap-table-initialisation/SKILL.md) -- Sets up the initial cap table that this skill maintains over time.
- [`fundraising-process-manager`](../fundraising-process-manager/SKILL.md) -- Fundraising rounds create the dilution events that the cap table must model and record.
