---
name: cap-table-initialisation
description: >
  This skill sets up the initial cap table at company formation including founder shares
  and option pool. Use when asked to create the cap table for a new company, set up
  founder equity splits, or establish the initial option pool. Also consider when a
  company has been operating without a formal cap table. Suggest when the user is
  incorporating without defining the equity structure.
department: finance
agent: investor-relations-manager
version: 1.0.0
complexity: medium
related-skills:
  - ../cap-table-manager/SKILL.md
  - ../safe-note-setup/SKILL.md
---

# cap-table-initialisation

## Agent: Investor Relations Manager

L2 investor relations manager (1x) responsible for investor updates, board materials, cap table management, fundraising process, and data room.

Department ethos: [ideal-finance.md](../../../../departments/finance/ideal-finance.md)

## Skill Description

Sets up the initial cap table at company formation including authorized shares, founder equity allocation, vesting schedules, and option pool reservation to establish a clean equity foundation.

## When to Use

- When a company is incorporating and needs to define its initial equity structure.
- When founders have agreed on equity splits and need to formalize them in a cap table.
- When an existing company has been operating informally and needs to establish a proper cap table retroactively.

## Workflow

1. **Authorized Share Structure**: Define the authorized share count (typically 10M shares for a Delaware C-Corp), par value ($0.0001 standard), and share classes (common for founders, reserved preferred for future investors). Deliverable: authorized share structure document.
2. **Founder Equity Allocation**: Record founder share issuances based on the agreed split. Ensure shares are issued via proper board resolution and stock purchase agreements. Set up vesting schedules (standard: 4-year with 1-year cliff, single-trigger or double-trigger acceleration). Deliverable: founder equity schedule with vesting terms.
3. **Option Pool Reservation**: Reserve the initial employee option pool (typically 10-15% of fully-diluted shares). Obtain board approval for the equity incentive plan. Set the initial exercise price at FMV (typically par value at incorporation). Deliverable: option pool reservation with plan documentation.
4. **Cap Table Platform Setup**: Set up the cap table in a management platform (Carta, Pulley, AngelList). Enter all share issuances, vesting schedules, and the option pool. Configure user access for founders and legal counsel. Deliverable: initialized cap table platform with all records.
5. **83(b) Election Coordination**: For founders receiving restricted stock, coordinate the filing of 83(b) elections with the IRS within 30 days of share issuance. Confirm receipt by the IRS. Deliverable: filed 83(b) elections with confirmation.

## Anti-Patterns

- **Handshake equity agreements**: Operating on verbal or informal equity arrangements without legal documentation. *Why*: undocumented equity splits become contentious disputes when the company raises money or one founder departs; legal clarity at formation is cheap insurance.
- **Skipping founder vesting**: Issuing founder shares without vesting, giving 100% ownership from day one. *Why*: without vesting, a departing founder walks away with their full equity allocation, leaving the remaining founders and company at a severe disadvantage.
- **Missing the 83(b) deadline**: Failing to file the 83(b) election within the 30-day window after restricted stock issuance. *Why*: missing the 83(b) deadline means founders pay ordinary income tax on the appreciation of their shares as they vest, which can be devastating as the company grows in value.

## Output

**On success**: Produces an initialized cap table with authorized share structure, founder equity schedule, option pool, platform setup, and 83(b) filings. Delivered at company formation.

**On failure**: Report which components could not be completed (e.g., founder split not agreed, legal documents not signed), what partial setup exists, and what decisions or actions are blocking completion. Escalate the 83(b) deadline urgency if applicable.

## Related Skills

- [`cap-table-manager`](../cap-table-manager/SKILL.md) -- Takes over ongoing cap table maintenance after this initial setup.
- [`safe-note-setup`](../safe-note-setup/SKILL.md) -- SAFE notes are often the first post-formation equity event that affects the cap table.
