# Cap Table Dilution Model

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [IR Manager name] |
| Transaction | [Series A fundraise / Option pool increase / SAFE conversion / Secondary] |
| Pre-Money Valuation | [$X,XXX,XXX] |
| Investment Amount | [$X,XXX,XXX] |
| Post-Money Valuation | [$X,XXX,XXX] |
| Model Version | [1.0] |
| Skill | cap-table-manager |

## Current Cap Table (Pre-Transaction)

| Holder | Share Class | Shares | % Fully Diluted | Notes |
|--------|------------|--------|----------------|-------|
| [Founder 1] | Common | [N,000,000] | [X%] | [X,XXX,XXX vested / X,XXX,XXX unvested] |
| [Founder 2] | Common | [N,000,000] | [X%] | [X,XXX,XXX vested / X,XXX,XXX unvested] |
| [Employee pool — granted] | Common (options) | [N,000,000] | [X%] | [Vested and unvested options outstanding] |
| [Option pool — unissued] | Common (reserved) | [N,000,000] | [X%] | [Unallocated pool] |
| [SAFE — Investor A] | Convertible | [—] | [X% projected] | [$X,XXX,XXX at $X,XXX,XXX cap] |
| [SAFE — Investor B] | Convertible | [—] | [X% projected] | [$X,XXX,XXX at $X,XXX,XXX cap, 20% discount] |
| **Total** | — | **[N,000,000 + convertibles]** | **100%** | — |

## Convertible Instrument Register

| Instrument | Holder | Amount | Valuation Cap | Discount | Interest Rate | Maturity | Conversion Trigger |
|-----------|--------|--------|--------------|---------|--------------|---------|------------------|
| SAFE (post-money) | [Investor A] | [$X,XXX,XXX] | [$X,XXX,XXX] | None | N/A | N/A | Next equity round |
| SAFE (post-money) | [Investor B] | [$X,XXX,XXX] | [$X,XXX,XXX] | 20% | N/A | N/A | Next equity round |
| Convertible Note | [Investor C] | [$X,XXX,XXX] | [$X,XXX,XXX] | 20% | 6% | [YYYY-MM-DD] | Next equity round or maturity |

## Proposed Transaction Terms

| Parameter | Base Scenario | Bull Scenario | Bear Scenario |
|-----------|--------------|--------------|---------------|
| Pre-money valuation | [$X,XXX,XXX] | [$X,XXX,XXX (+25%)] | [$X,XXX,XXX (-20%)] |
| Investment amount | [$X,XXX,XXX] | [$X,XXX,XXX] | [$X,XXX,XXX] |
| Post-money valuation | [$X,XXX,XXX] | [$X,XXX,XXX] | [$X,XXX,XXX] |
| New shares issued (Series A Preferred) | [N,XXX,XXX] | [N,XXX,XXX] | [N,XXX,XXX] |
| Price per share (Series A) | [$X.XX] | [$X.XX] | [$X.XX] |
| Option pool top-up (pre-money) | [N,XXX,XXX shares] | [N,XXX,XXX] | [N,XXX,XXX] |

## Post-Transaction Cap Table — Base Scenario

| Holder | Share Class | Pre-Txn Shares | Post-Txn Shares | Post-Txn % FD | Dilution |
|--------|------------|---------------|----------------|--------------|---------|
| [Founder 1] | Common | [N,000,000] | [N,000,000] | [X%] | [-X pp from pre-txn X%] |
| [Founder 2] | Common | [N,000,000] | [N,000,000] | [X%] | [-X pp] |
| [Employees — granted options] | Common (options) | [N,000,000] | [N,000,000] | [X%] | [-X pp] |
| [Option pool — unissued] | Common (reserved) | [N,000,000] | [N,000,000] | [X%] | [pool top-up included] |
| [SAFE Investor A — converted] | Series A Preferred | — | [N,XXX,XXX] | [X%] | [New] |
| [SAFE Investor B — converted] | Series A Preferred | — | [N,XXX,XXX] | [X%] | [New] |
| [Series A Lead Investor] | Series A Preferred | — | [N,XXX,XXX] | [X%] | [New] |
| **Total** | — | — | **[N,000,000]** | **100%** | — |

## Scenario Comparison

| Holder | Base (% FD) | Bull (% FD) | Bear (% FD) |
|--------|------------|------------|------------|
| Founder 1 | [X%] | [X%] | [X%] |
| Founder 2 | [X%] | [X%] | [X%] |
| All Employees (options) | [X%] | [X%] | [X%] |
| SAFE Investors (converted) | [X%] | [X%] | [X%] |
| Series A Lead | [X%] | [X%] | [X%] |
| Option Pool (unissued) | [X%] | [X%] | [X%] |

## Liquidation Waterfall Analysis

[Show distribution of proceeds at various exit valuations, accounting for liquidation preferences.]

Assumptions: 
- Series A liquidation preference: [1x non-participating / 1x participating]
- Conversion to common: [At investor election]

| Exit Valuation | Series A Preferred | Common Shareholders | Notes |
|---------------|-------------------|---------------------|-------|
| [$X,XXX,XXX (below preference)] | [$X,XXX,XXX (return of capital)] | [$0] | [Preferred liquidation preference not fully covered] |
| [$X,XXX,XXX (at post-money)] | [$X,XXX,XXX or convert to common] | [$X,XXX,XXX] | [Preference = as-converted; investor converts to common] |
| [$X,XXX,XXX (3x exit)] | [$X,XXX,XXX] | [$X,XXX,XXX] | [Participating or converts to common — calculate both] |
| [$X,XXX,XXX (5x exit)] | [$X,XXX,XXX] | [$X,XXX,XXX] | — |

## Key Metrics Post-Transaction

| Metric | Value |
|--------|-------|
| Total shares outstanding (post-close) | [N,XXX,XXX] |
| Founder total ownership (both founders) | [X%] |
| Employee option pool utilization | [X%] issued / [X%] unissued |
| Investor ownership (all preferred) | [X%] |
| Price per share (Series A) | [$X.XX] |
| 409A FMV (common) — estimated post-close | [$X.XX] |
| Option exercise price for next grants | [$X.XX per 409A update] |
