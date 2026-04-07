# Framework: Cap Table Initialisation

Reference guide for setting up a clean, defensible equity structure at company formation.

## Authorized Share Structure

### Standard Delaware C-Corp Initial Structure

| Parameter | Recommended Value | Rationale |
|-----------|-----------------|-----------|
| Total authorized shares | 10,000,000 | Standard starting amount; leaves room for multiple rounds and option grants before a certificate of amendment is needed |
| Common stock authorized | 9,000,000 | For founders, employees, and advisors |
| Preferred stock authorized (blank check) | 1,000,000 | Reserved for future investors; terms set at time of first issuance |
| Par value | $0.0001 per share | Minimizes state incorporation taxes; standard for Delaware C-Corps |

**When to authorize more shares**: Recapitalization is common before Series A to accommodate the preferred share issuance and increased option pool. Authorize 10-15M additional shares at or before Series A closing.

## Founder Equity Allocation Decision Framework

### Equity Split Principles

| Principle | Guidance |
|-----------|---------|
| Equal splits | Appropriate when all founders start simultaneously with equal time and financial commitment |
| Differentiated splits | Appropriate when one founder has contributed IP, prior funding, or significantly more time |
| Dynamic equity | Slicing Pie or similar model — adjust allocation based on contributions over a defined period; uncommon but defensible |
| Documentation timing | Always document the split in a Restricted Stock Purchase Agreement (RSPA) at incorporation |

### Common Equity Split Patterns

| Scenario | Common Structure |
|----------|-----------------|
| Two co-founders, equal contribution | 50/50 or 55/45 |
| Two co-founders, one is CEO/technical lead | 60/40 or 65/35 |
| Three co-founders, equal contribution | 33/33/34 or weighted by role |
| Solo founder | 80-90% to founder; 10-20% reserved for key hires |

**Rule**: Never issue equity without a signed RSPA and board resolution, even between friends.

## Vesting Schedule Standards

| Parameter | Standard | Rationale |
|-----------|---------|-----------|
| Total vesting period | 4 years | Industry standard; aligns founder incentives through at least Series A |
| Cliff | 1 year (25%) | Protects company from short-tenure founder walking away with vested equity |
| Vesting after cliff | Monthly over 36 months | Smooth vesting; avoids quarterly cliffs that create departure timing games |
| Acceleration — Single trigger | Not recommended | Compensation payment on change of control is a golden parachute; deters acquirers |
| Acceleration — Double trigger | Recommended | Full vesting on: (1) change of control AND (2) termination without cause within 12-18 months |

## Option Pool Sizing Decision Table

| Stage | Recommended Option Pool | Rationale |
|-------|------------------------|-----------|
| At formation | 10% fully diluted | Covers first ~20 employees including advisors |
| Pre-seed close | 10-12% post-close | Investors will request a top-up; negotiate the size before close |
| Seed close | 15% post-close | Include in pre-money valuation; ensure sufficient for Series A hiring plan |
| Series A close | 10-12% post-close | Top-up is standard; VCs require enough pool to hire planned headcount |

**Negotiation note**: Investors want the option pool created from founder shares (pre-money pool). Negotiate for a smaller pre-money pool and a post-close top-up if needed — this protects founders from unnecessary dilution.

## 83(b) Election: Critical Rules

| Rule | Detail |
|------|--------|
| Deadline | 30 days from grant/purchase date — NO EXCEPTIONS |
| Who must file | Any founder or early employee receiving restricted stock (stock subject to vesting = restricted) |
| Filing method | Paper copy to IRS + retain a copy + send a copy to the company |
| Default without 83(b) | Ordinary income tax on FMV at each vesting event — can be catastrophically expensive if company value rises |
| ISO grants | ISOs are NOT restricted stock — 83(b) does not apply; different rules govern ISO exercises |

## Cap Table Platform Selection

| Tool | Best For | Annual Cost | Key Features |
|------|---------|------------|-------------|
| Carta | Seed through IPO | $3,500–$50,000+/yr | Full legal + cap table; most widely used by VCs; electronic exercise |
| Pulley | Seed to Series A | $2,000–$10,000/yr | Lower cost than Carta; growing adoption; self-serve |
| AngelList | Pre-seed, rolling funds | $0–$2,000/yr | Free tier available; integrated with AngelList Raise |
| Spreadsheet | Formation only | $0 | Acceptable at formation only; migrate to a platform before first outside investor |

**Recommendation**: Set up a platform at formation. The cost to migrate a messy spreadsheet cap table to Carta before a Series A is far greater than the platform cost.

## Post-Formation Checklist

- [ ] Authorized share structure filed with Delaware Secretary of State
- [ ] Founders' stock issued via Restricted Stock Purchase Agreement (RSPA)
- [ ] Board resolutions approving stock issuance signed
- [ ] 83(b) elections filed within 30 days (IRS confirmation copies retained)
- [ ] Equity incentive plan adopted by board and stockholders
- [ ] Initial option pool authorized (board resolution)
- [ ] Cap table entered into platform (Carta, Pulley, or AngelList)
- [ ] Legal counsel access granted to cap table platform
