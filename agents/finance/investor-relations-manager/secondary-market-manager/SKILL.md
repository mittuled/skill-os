---
name: secondary-market-manager
description: >
  This skill manages secondary market transactions including tender offers and employee
  liquidity programmes. Use when asked to facilitate secondary share sales, design an
  employee liquidity programme, or evaluate a tender offer. Also consider when employees
  are approaching IPO-eligible stock option expiry or seeking liquidity. Suggest when
  the user has long-tenured employees with significant unrealized equity.
department: finance
agent: investor-relations-manager
version: 1.0.0
complexity: complex
related-skills:
  - ../cap-table-manager/SKILL.md
  - ../fundraising-process-manager/SKILL.md
  - ../secondary-transaction-coordinator/SKILL.md
---

# secondary-market-manager

## Agent: Investor Relations Manager

L2 investor relations manager (1x) responsible for investor updates, board materials, cap table management, fundraising process, and data room.

Department ethos: [ideal-finance.md](../../../../departments/finance/ideal-finance.md)

## Skill Description

Manages secondary market transactions including tender offers, direct secondary sales, and employee liquidity programmes to provide controlled shareholder liquidity while maintaining cap table integrity.

## When to Use

- When employees or early investors request liquidity and the company is not near an IPO or acquisition.
- When the company wants to proactively offer an employee liquidity programme as a retention tool.
- When inbound interest from secondary buyers needs to be evaluated and managed.

## Workflow

1. **Programme Design**: Define the secondary transaction structure: tender offer vs. direct sale, eligible share classes, volume limits (typically 10-25% of vested shares), pricing methodology (last 409A, last round price, negotiated), and eligibility criteria (tenure, vesting thresholds). Deliverable: secondary programme term sheet.
2. **Legal and Tax Framework**: Coordinate with legal counsel on securities law compliance (Rule 144, transfer restrictions, ROFR provisions). Work with tax advisors on seller tax implications (capital gains treatment, AMT for ISOs). Deliverable: legal and tax compliance memo.
3. **Buyer Coordination**: Identify and vet potential buyers (secondary funds, existing investors, strategic buyers). Negotiate pricing and terms. Ensure buyers meet accredited investor requirements. Deliverable: vetted buyer list with negotiated terms.
4. **Seller Management**: Communicate the programme to eligible sellers. Provide tax guidance materials. Collect participation elections and process the required documentation (stock power, spousal consent, legal opinion letters). Deliverable: seller election summary with documentation.
5. **Execution and Settlement**: Coordinate the transaction closing with legal, transfer agent, and cap table platform. Process share transfers, update the cap table, and confirm fund disbursement to sellers. Deliverable: completed transaction with updated cap table.
6. **Post-Transaction Reporting**: Report the transaction to the board, update 409A valuation if the transaction price diverges materially from the last valuation, and file any required regulatory notices. Deliverable: board report and regulatory compliance confirmation.

## Anti-Patterns

- **Uncontrolled secondary sales**: Allowing shareholders to sell freely without company oversight or ROFR enforcement. *Why*: uncontrolled secondary sales can bring unwanted investors onto the cap table, establish unfavorable pricing benchmarks, and create information asymmetry.
- **Pricing without valuation support**: Allowing secondary transactions at prices materially different from the 409A without understanding the tax and accounting implications. *Why*: secondary pricing that diverges from 409A can trigger a new valuation, affect option pricing, and create tax complications for future grantees.
- **Ignoring employee tax implications**: Facilitating secondary sales without providing sellers with clear guidance on tax treatment. *Why*: employees who sell without understanding the tax implications (especially ISO vs. NSO, short-term vs. long-term capital gains) may face unexpected tax liabilities.

## Output

**On success**: Produces a completed secondary transaction with updated cap table, board report, regulatory filings, and seller confirmation. Delivered per the transaction timeline.

**On failure**: Report which aspects of the transaction could not be completed (e.g., legal opinion not obtained, buyer qualification issues), what the current status is, and the path to resolution. Escalate to CFO and counsel.

## Related Skills

- [`cap-table-manager`](../cap-table-manager/SKILL.md) -- Records the share transfers and ownership changes resulting from secondary transactions.
- [`fundraising-process-manager`](../fundraising-process-manager/SKILL.md) -- Secondary transactions must be coordinated with any active or planned primary fundraising.
