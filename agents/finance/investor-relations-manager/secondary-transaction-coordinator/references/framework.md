# Framework: Secondary Transaction Coordination

Reference guide for managing the workflow of individual share transfer approvals.

## Secondary Transaction Approval Workflow

```
Transfer Request → Eligibility Verification → Transfer Restriction Review → 
ROFR Notice → Board Approval → Document Execution → Cap Table Update
```

## Transfer Restriction Analysis Framework

### Right of First Refusal (ROFR)

| Aspect | Standard Terms |
|--------|--------------|
| Who holds ROFR | Company first; then major investors (pro-rata to ownership) |
| Notice requirement | Written notice to company with: seller name, shares, class, proposed buyer, price, intended transfer date |
| Company ROFR window | 30 days from receipt of complete transfer notice |
| Investor ROFR window | 15 days after company waives (or company assigns its ROFR to investors) |
| Partial exercise | Permitted in most agreements — company or investors may purchase a portion |
| Waiver | Written waiver from all ROFR holders required to proceed without ROFR exercise |

### Co-Sale Rights

| Aspect | Standard Terms |
|--------|--------------|
| Who holds co-sale rights | Major investors (typically >5% holders) |
| Trigger | Founders selling more than N% of vested shares in any rolling 12-month period |
| Co-sale notice | Investor receives same terms as founder/seller |
| Practical impact | Sale of large founder blocks can force a parallel investor sale process |

### Board Approval Requirements

| Transaction Type | Board Approval Required? | Notes |
|-----------------|------------------------|-------|
| Transfer between existing shareholders | Usually not | Verify in governing documents |
| Sale to new investor / outside buyer | Almost always | Board consent to admit new stockholder |
| Transfer by officer or director | Always | Conflict of interest review; may require disinterested board vote |
| Transfer triggering information rights | Always | When buyer acquires ≥5% (check IRA thresholds) |

## Pricing Reference Framework

| Price Reference | When Appropriate | 409A Implications |
|----------------|----------------|-------------------|
| Last 409A FMV | Default — no concurrent primary round | No new 409A needed unless material change |
| Last priced round price × discount | Near a fundraise; or to reflect illiquidity discount | May require updated 409A if diverges >25% |
| Third-party negotiated price | Secondary fund transaction | Trigger new 409A if >25% above current FMV |
| Tender offer price | Structured programme | Board sets price; 409A update required if >FMV |

**Safe harbor**: A secondary transaction price within 25% of the current 409A FMV typically does not require a new 409A valuation. Consult counsel for transactions that diverge more than this.

## Information Rights Triggers

| Holder Threshold | Potential Trigger |
|-----------------|------------------|
| Acquires >5% of any share class | Information rights under IRA (check specific IRA terms) |
| Acquires >5% of voting shares | SEC Section 13 reporting (public companies only) |
| Exceeds 500 holders of record | SEC Section 12(g) registration threshold risk |
| Becomes a "major investor" per IRA | Pro-rata rights, ROFR rights, co-sale rights |

## Joinder Agreement Requirements

New shareholders acquiring shares in secondary transactions must typically execute a joinder to:

| Agreement | Why |
|-----------|-----|
| Investor Rights Agreement (IRA) | Binds buyer to information rights, ROFR, co-sale |
| Voting Agreement | Ensures buyer is part of the voting agreement for director elections |
| Right of First Refusal and Co-Sale Agreement | Subjects buyer to the same ROFR when they later sell |
| Stock Transfer Restriction Agreement | Binds buyer to transfer restrictions |

**Exception**: If the buyer is an existing party to all agreements, no joinder is required.

## Document Checklist for Closing

| Document | Required | Notes |
|----------|---------|-------|
| Stock Transfer Agreement | Yes | Primary transfer document |
| Assignment of stock certificate / book entry instruction | Yes | Or transfer via cap table platform |
| Board consent approving transfer | Yes | Written consent from board |
| ROFR waiver (from all ROFR holders) | Yes | Written waivers collected |
| Joinder to shareholder agreements | Yes (new holders) | No action needed if existing holder |
| Spousal consent | Sometimes | Required in community property states if seller is married |
| Legal opinion (for foreign buyers) | Sometimes | Consult securities counsel |
| Accredited investor questionnaire | Yes | For all new stockholders |

## Post-Transaction Compliance Calendar

| Task | Timing | Owner |
|------|--------|-------|
| Cap table update | Within 2 business days | IR Manager |
| Transfer agent notification | Within 5 business days | IR Manager + Legal |
| Form D amendment (if applicable) | Within 15 days | Legal |
| IRS Form 1099-B (seller tax reporting) | Year-end | Controller |
| 409A update (if triggered by pricing) | Within 30 days | CFO + valuation firm |
| Board report / minutes | Next board meeting | IR Manager |
