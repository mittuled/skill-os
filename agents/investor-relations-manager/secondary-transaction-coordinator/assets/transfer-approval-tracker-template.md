# Secondary Transfer Approval Tracker

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [IR Manager name] |
| Transaction ID | [TXN-[YYYY]-[N]] |
| Seller | [Name / Employee ID] |
| Buyer | [Name / Firm] |
| Shares | [N,XXX shares of [Class]] |
| Proposed Price | [$X.XX per share] |
| Total Value | [$X,XXX] |
| Status | [Request Intake / ROFR / Board Approval / Execution / Complete] |
| Skill | secondary-transaction-coordinator |

## Transaction Summary

| Parameter | Detail |
|-----------|--------|
| Seller | [Name, role, tenure] |
| Buyer | [Name, firm, accredited investor status] |
| Share class | [Common / Series A Preferred / Other] |
| Number of shares | [N,XXX] |
| Price per share | [$X.XX] |
| Pricing reference | [Last 409A FMV of $X.XX / Last round price of $X.XX × discount] |
| Seller's cost basis | [$X.XX per share (exercise price)] |
| Transfer type | [Sale / Gift / Transfer to trust / Other] |
| Estimated close date | [YYYY-MM-DD] |

## Eligibility Verification

| Check | Result | Notes |
|-------|--------|-------|
| Seller owns the shares (cap table confirmed) | [Yes / No] | [Source: Carta export as of YYYY-MM-DD] |
| Shares are vested | [Yes — all vested / Yes — N,XXX vested of N,XXX total] | — |
| No active lock-up restriction | [Yes — clear / No — lock-up expires YYYY-MM-DD] | — |
| Seller is current employee / acceptable transfer category | [Yes] | — |
| Proposed price within 25% of current 409A | [Yes — $X.XX vs. $X.XX 409A / No — pricing concern] | [If No: flag for counsel and 409A update] |

## Transfer Restriction Analysis

| Restriction | Holders | Status |
|------------|---------|--------|
| ROFR — Company | [Company] | [Waived YYYY-MM-DD / Exercising X,XXX shares / Pending] |
| ROFR — Investor A | [Firm A — $X M invested] | [Waived YYYY-MM-DD / Exercising N,XXX shares / Pending] |
| ROFR — Investor B | [Firm B] | [Waived / Not triggered (below threshold) / Pending] |
| Co-sale rights | [Major investors with co-sale] | [Not triggered (founder not selling) / Triggered — see co-sale notice] |
| Lock-up | — | [Clear / Active until YYYY-MM-DD] |
| Board approval required | — | [Yes — see Board Approval section] |

## ROFR Process

| Step | Date | Status | Notes |
|------|------|--------|-------|
| Transfer notice sent to company | [YYYY-MM-DD] | [Sent] | — |
| Company ROFR deadline | [YYYY-MM-DD (30 days)] | [Pending / Waived / Exercising] | — |
| Investor ROFR notice sent | [YYYY-MM-DD] | [Sent / N/A — company exercising] | — |
| Investor ROFR deadline | [YYYY-MM-DD (15 days)] | [Pending] | — |
| All ROFR waivers collected | [YYYY-MM-DD] | [Pending / Complete] | — |

**ROFR result**: [All waived — proceed to board approval / Company exercises partial ROFR — [N,XXX] shares / Investor A exercises — [N,XXX] shares]

## Board Approval

| Requirement | Status |
|------------|--------|
| Board approval required | [Yes] |
| Board consent prepared | [Yes — consent draft at [link]] |
| Board approval method | [Written consent / Board meeting vote] |
| Board approval date | [YYYY-MM-DD] |
| Resolution reference | [R-[YYYY]-[N]] |

Board consent language:
*"RESOLVED, that the proposed transfer of [N,XXX] shares of Common Stock from [Seller name] to [Buyer name] at $[X.XX] per share, as described in Transfer Request [TXN-[YYYY]-[N]], is hereby approved subject to the execution of required transfer documents."*

## Document Execution Tracker

| Document | Required | Prepared | Sent for Signature | Executed | Filed |
|----------|---------|---------|------------------|---------|-------|
| Stock Transfer Agreement | Yes | [ ] | [ ] | [ ] | [ ] |
| Board Consent | Yes | [ ] | [ ] | [ ] | [ ] |
| ROFR Waiver — Company | Yes | [ ] | [ ] | [ ] | [ ] |
| ROFR Waiver — Investor A | [If applicable] | [ ] | [ ] | [ ] | [ ] |
| Joinder to IRA | [If new holder] | [ ] | [ ] | [ ] | [ ] |
| Joinder to Voting Agreement | [If new holder] | [ ] | [ ] | [ ] | [ ] |
| Accredited Investor Questionnaire | [If new holder] | [ ] | [ ] | [ ] | [ ] |
| Spousal Consent | [If applicable] | [ ] | [ ] | [ ] | [ ] |

## Cap Table Update

| Update | Status | Date |
|--------|--------|------|
| Seller shares reduced | [Pending / Complete] | [YYYY-MM-DD] |
| Buyer shares added (or existing position updated) | [Pending / Complete] | [YYYY-MM-DD] |
| Transaction audit trail added in cap table platform | [Pending / Complete] | [YYYY-MM-DD] |
| Transfer agent notified | [Pending / Complete] | [YYYY-MM-DD] |

**Post-transaction ownership impact**:
- Seller ownership: [X%] → [X%] (N,XXX shares sold)
- Buyer ownership: [X%] → [X%] (N,XXX shares acquired)

## Post-Transaction Actions

| Action | Owner | Due Date | Status |
|--------|-------|---------|--------|
| Board report — include in next board materials | IR Manager | [Next board meeting] | [ ] |
| 409A update assessment | CFO | [YYYY-MM-DD] | [Required / Not required — within safe harbor] |
| Form D amendment (if securities offering) | Legal | [YYYY-MM-DD] | [Required / Not required] |
| Seller tax summary / 1099-B prep | Controller | [Year-end] | [ ] |
| Archive all executed documents | IR Manager | [YYYY-MM-DD] | [ ] |
