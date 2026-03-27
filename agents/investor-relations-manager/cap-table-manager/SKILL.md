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
complexity: complex
related-skills:
  - ../cap-table-initialisation/SKILL.md
  - ../fundraising-process-manager/SKILL.md
  - ../../corporate-counsel/founder-equity-issuance/SKILL.md
---

# cap-table-manager

## Agent: Investor Relations Manager

L2 investor relations manager (1x) responsible for investor updates, board materials, cap table management, fundraising process, and data room.

Department ethos: [ideal-finance.md](../../../departments/finance/ideal-finance.md)

## Skill Description

Maintains the cap table by recording equity grants, exercises, transfers, and cancellations, modelling dilution scenarios, coordinating 409A valuations, and producing ownership reports to ensure accurate equity records and informed decision-making across fundraising, hiring, and governance.

## When to Use

- When equity events occur (new grants, option exercises, RSU vesting, share transfers, terminations with equity implications, SAFE conversions, warrant exercises).
- When a fundraising round is being modelled and dilution impact needs to be calculated for existing shareholders across multiple scenarios.
- When the board, auditors, or potential investors request a current cap table, ownership summary, or waterfall analysis.
- When employee equity questions arise (vested shares, exercise windows, tax implications) that require cap table data.

## Workflow

1. **Event Recording**: Record each equity event in the cap table system with full detail: grant date, vesting schedule, exercise price, share class, and any special terms (acceleration, repurchase rights, right of first refusal). Cross-reference against board resolutions and legal documents. For option exercises, verify the exercise price matches the grant agreement and confirm payment receipt. For terminations, calculate the post-termination exercise window and notify the departing holder. Deliverable: updated cap table with event audit trail.
2. **Vesting Schedule Tracking**: Track vesting progress for all outstanding grants across all equity types (options, RSUs, restricted stock). Calculate shares vested, unvested, and exercisable for each holder. Process vesting events (cliff dates, monthly vesting, performance milestones) on schedule. Generate individual equity statements for holders upon request. Deliverable: vesting schedule summary with per-holder detail.
3. **Convertible Instrument Management**: Maintain a register of all outstanding convertible instruments (SAFE notes, convertible notes, warrants) with their conversion terms (valuation caps, discount rates, interest rates, maturity dates). Model conversion scenarios under different round terms. Track MFN provisions that may require updating earlier SAFEs. Deliverable: convertible instrument register with conversion models.
4. **Dilution Modelling**: Model the dilution impact of proposed transactions (new priced round, option pool increase, secondary sale, SAFE conversion) on all existing shareholders. Show pre-money and post-money ownership percentages across common, preferred, and fully-diluted bases. Produce waterfall analysis showing liquidation preference distribution at various exit valuations. Deliverable: dilution model with waterfall analysis and scenario comparison.
5. **409A Coordination**: Coordinate with the 409A valuation firm to ensure the current fair market value is updated at least annually or after material events (fundraising close, significant revenue change, pivot). Verify that all option grants use the current 409A price. Flag any grants that need to be repriced or restructured. Deliverable: 409A valuation status and grant price verification.
6. **Cap Table Reconciliation**: Reconcile the cap table against legal records (stock ledger, board minutes, SAFE/convertible note register, stock purchase agreements) quarterly. Investigate and resolve any discrepancies between the cap table system and legal documents. Verify total issued shares against authorized shares to ensure headroom. Deliverable: reconciliation report with discrepancy resolution.
7. **Reporting and Access**: Produce standard reports: ownership summary (by holder, by class, fully-diluted), option pool utilization and remaining pool, vesting schedule overview, and convertible instrument summary. Maintain appropriate access controls so stakeholders see only their authorized view. Deliverable: cap table reports with role-based access.

## Anti-Patterns

- **Spreadsheet-only cap table**: Managing the cap table in a spreadsheet rather than a purpose-built system (Carta, Pulley, AngelList) for companies beyond seed stage. *Why*: spreadsheets do not enforce data integrity, cannot model waterfall distributions accurately, and create audit risk as the cap table grows complex with multiple share classes, convertible instruments, and hundreds of holders.
- **Delayed event recording**: Waiting to batch-record equity events rather than recording them as they occur. *Why*: delayed recording creates reconciliation gaps and increases the risk of errors, especially around termination-related exercises and post-termination exercise windows where timing is legally significant.
- **Ignoring convertible instruments**: Tracking only issued shares while neglecting SAFE notes, convertible notes, and warrants in the fully-diluted calculation. *Why*: investors and the 409A firm need the fully-diluted picture; omitting convertibles understates dilution, overstates ownership, and produces incorrect waterfall analyses.
- **Single-scenario dilution modelling**: Modelling dilution for only one round structure without showing alternatives. *Why*: the CEO and board need to compare scenarios (different valuations, pool sizes, investor allocations) to negotiate effectively; a single model constrains decision-making.

## Output

**On success**: Produces an updated cap table with event audit trail, vesting summary, convertible instrument register, dilution models with waterfall analysis, 409A coordination status, reconciliation report, and standard ownership reports. Delivered on an ongoing basis with quarterly reconciliation and ad hoc reporting for transactions.

**On failure**: Report which equity events could not be recorded (e.g., missing board resolution, unsigned grant agreement, ambiguous SAFE conversion terms), what the cap table reflects as of the latest reconciliation, and what legal or administrative actions are needed to resolve the gaps. Escalate to CFO and counsel with specific action items.

## Related Skills

- [`cap-table-initialisation`](../cap-table-initialisation/SKILL.md) -- Sets up the initial cap table that this skill maintains over time.
- [`fundraising-process-manager`](../fundraising-process-manager/SKILL.md) -- Fundraising rounds create the dilution events that the cap table must model and record.
- [`founder-equity-issuance`](../../corporate-counsel/founder-equity-issuance/SKILL.md) -- Founder equity issuance produces the restricted stock grants that must be recorded in the cap table.
