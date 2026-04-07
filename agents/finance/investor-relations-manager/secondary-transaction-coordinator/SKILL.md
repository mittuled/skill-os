---
name: secondary-transaction-coordinator
description: >
  This skill coordinates secondary transactions including shareholder sales, tender
  offers, and transfer approvals. Use when asked to facilitate a secondary sale,
  process a share transfer request, or manage a tender offer. Also consider when
  employees or early investors inquire about liquidity options. Suggest when the
  user is processing share transfers without proper ROFR and board approval workflow.
department: finance
agent: investor-relations-manager
version: 1.0.0
complexity: complex
related-skills:
  - ../cap-table-manager/SKILL.md
  - ../secondary-market-manager/SKILL.md
---

# secondary-transaction-coordinator

## Agent: Investor Relations Manager

L2 investor relations manager (1x) responsible for investor updates, board materials, cap table management, fundraising process, and data room.

Department ethos: [ideal-finance.md](../../../../departments/finance/ideal-finance.md)

## Skill Description

Coordinates secondary transactions by managing the approval workflow, ensuring compliance with transfer restrictions, facilitating buyer-seller matching, and updating the cap table to reflect completed transfers.

## When to Use

- When a shareholder (employee, angel, early investor) requests to sell shares on the secondary market.
- When the company decides to run a structured tender offer to provide employee liquidity.
- When an acquirer or secondary fund approaches the company about purchasing shares from existing holders.

## Workflow

1. **Request Intake**: Receive and log the transfer request with details: seller identity, number of shares, share class, proposed buyer (if identified), proposed price, and reason for sale. Verify the seller's ownership and any lock-up or holding period restrictions. Deliverable: transfer request log with eligibility verification.
2. **Transfer Restriction Review**: Review the company's governing documents (certificate of incorporation, shareholder agreements, stock purchase agreements) for transfer restrictions: right of first refusal (ROFR), co-sale rights, board approval requirements, and information rights triggers. Deliverable: transfer restriction analysis.
3. **ROFR Process**: If ROFR applies, notify the company and other shareholders of the proposed transfer per the required notice period. Track responses and exercise elections. Manage partial exercises. Deliverable: ROFR notice and response tracking.
4. **Valuation and Pricing**: Determine the appropriate price reference (latest 409A, latest round price, negotiated price). If the price deviates significantly from the last 409A or round price, flag for board review. Deliverable: pricing analysis with valuation reference.
5. **Board Approval**: Prepare the board consent for the transfer including transaction summary, pricing rationale, buyer background, and impact on ownership percentages. Obtain board approval per the company's governance requirements. Deliverable: board consent package and approval.
6. **Transaction Execution**: Coordinate the execution of transfer documents (stock transfer agreement, spousal consent if required, updated stock certificates or book entries). Ensure the buyer executes a joinder to the relevant shareholder agreements. Deliverable: executed transfer documents.
7. **Cap Table Update**: Record the transfer in the cap table system. Update ownership percentages, information rights holders, and voting records. Issue new certificates or update book entries. Notify the transfer agent. Deliverable: updated cap table and transfer confirmation.

## Anti-Patterns

- **Skipping ROFR**: Processing transfers without running the required right of first refusal process. *Why*: ROFR violations breach shareholder agreements and can void the transfer, creating legal liability for the company.
- **Informal board approval**: Obtaining verbal board approval rather than formal written consent for share transfers. *Why*: undocumented approvals create governance gaps and expose the company to claims that the transfer was unauthorized.
- **Ignoring information rights triggers**: Failing to check whether a transfer triggers information rights for the buyer under securities regulations (e.g., becoming a holder of record). *Why*: crossing holder thresholds can trigger SEC reporting requirements the company is not prepared to meet.
- **Price manipulation tolerance**: Allowing transfers at prices that create problematic 409A implications without flagging to counsel and the auditor. *Why*: secondary sales at prices significantly above the 409A value can trigger IRS scrutiny and challenge the valuation methodology.

## Output

**On success**: Produces completed secondary transaction with executed transfer documents, board approval, ROFR clearance, updated cap table, and transaction archive. Delivered per the transaction timeline.

**On failure**: Report which step in the approval workflow is blocked (ROFR exercise, board dissent, transfer restriction conflict), what the current status is, and recommended next steps. Escalate to counsel if legal restrictions prevent the transfer.

## Related Skills

- [`cap-table-manager`](../cap-table-manager/SKILL.md) -- Every completed secondary transaction requires a cap table update.
- [`secondary-market-manager`](../secondary-market-manager/SKILL.md) -- Manages the broader secondary market strategy that individual transactions execute within.
