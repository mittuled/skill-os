# Framework: Secondary Market Management

Reference guide for designing and executing employee liquidity programmes and secondary transactions.

## Secondary Transaction Types

| Type | Description | Best For | Complexity |
|------|-------------|---------|-----------|
| Tender offer | Company-run programme offering to buy shares from employees/investors | Broad employee liquidity; controlled pricing | High — SEC rules apply if >35 holders or >$10M |
| Direct secondary sale | Individual seller transacts directly with a secondary buyer | Single-employee liquidity; fast execution | Medium |
| Secondary fund sale | Block sale to a secondary fund (Lexington, Greenhill Cogent) | Large liquidity need; investor-driven | High — 4-8 week process |
| Structured liquidity round | Dedicated liquidity round alongside a primary round | Combining liquidity with new capital raise | High — requires parallel processes |

## Programme Design Decision Framework

| Parameter | Conservative | Balanced | Generous |
|-----------|------------|---------|---------|
| Eligible share classes | [Common only] | [Common + vested options] | [Common + options + early-exercise] |
| Volume limit (per employee) | [10% of vested shares] | [15-25% of vested shares] | [Up to 50% of vested] |
| Minimum tenure | [3 years] | [2 years] | [1 year] |
| Minimum vested shares | [N shares] | [Lower threshold] | [Any vested shares] |
| Pricing methodology | [Last 409A × 1.0x (conservative)] | [Last round price × 0.85x] | [Negotiated near last round price] |
| Buyer type preference | [Existing investors only] | [Existing investors + secondary funds] | [Open to all accredited buyers] |

**Programme cap (recommended)**: Total programme size ≤ 10-15% of total capitalization to avoid triggering SEC reporting obligations.

## Pricing Methodology

| Method | When to Use | Considerations |
|--------|-------------|---------------|
| Last 409A FMV | Programme not tied to a primary raise | Clean for tax purposes; may be below market |
| Last round price (post-money) | Concurrent with a primary raise | Signals company confidence; may exceed 409A |
| Negotiated with secondary buyers | Secondary fund-led transaction | Market-clearing price; may diverge from 409A |
| 409A × premium factor | When secondary demand suggests above-FMV pricing | Requires updated 409A; affects option pricing |

**Tax implication**: If secondary price materially exceeds the current 409A, a new 409A must be commissioned. This affects option exercise prices for all future grants.

## SEC Compliance Thresholds

| Threshold | Regulatory Trigger | Requirement |
|-----------|------------------|-------------|
| >35 shareholders of record | Section 12(g) registration risk | Company should not exceed 2,000 holders of record (1,500 non-accredited) |
| >$10M in securities offered | Regulation A or D | File Form D within 15 days of first sale |
| Tender offer >$5M | SEC Rule 14e | Full tender offer rules may apply |
| Foreign buyers | OFAC + local securities laws | Counsel review required |

**Standard compliance path**: File a Regulation D exemption (Rule 506(b) or 506(c)). All buyers must qualify as accredited investors.

## Transfer Restriction Checklist

| Restriction | Where to Find | Typical Term | Action |
|------------|--------------|-------------|--------|
| Right of First Refusal (ROFR) | Stock Purchase Agreement, IRA | Company + major investors must be notified | Send ROFR notice; track exercise elections |
| Co-sale rights | IRA / CFPB | Major investors can tag along on founder sales | Notify co-sale right holders |
| Board approval | Bylaws or SPCA | Required for most transfers | Prepare board consent |
| Lock-up periods | SPCA, employee offer letter | 180-day IPO lock-up; post-fundraising restrictions | Verify no active lock-up |
| Transfer restrictions | Shareholder agreement | Share class-specific restrictions | Verify buyer qualifies |

## Post-Transaction Obligations

| Obligation | Timing | Owner |
|-----------|--------|-------|
| Update cap table | Immediately post-close | IR Manager |
| Notify transfer agent | Within 5 business days | IR Manager + Legal |
| Issue/update stock certificates | Per platform requirements | IR Manager |
| Tax reporting (Form 1099-B) | Year-end | Controller |
| 409A update (if price diverges significantly) | Within 30 days of transaction close | CFO |
| Board report | Next board meeting | IR Manager |
| SEC Form D amendment (if applicable) | Within 15 days | Legal |
