# SAFE Note Register

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [IR Manager name] |
| Company | [Company name] |
| Total SAFE Capital Raised | [$X,XXX,XXX] |
| Active SAFEs | [N] |
| Converted SAFEs | [N] |
| Skill | safe-note-setup |

## SAFE Register

| # | Investor | Amount | SAFE Type | Valuation Cap | Discount | MFN? | Issue Date | Conversion Trigger | Status |
|---|----------|--------|-----------|--------------|---------|------|-----------|------------------|--------|
| 1 | [Investor A] | [$X,XXX,XXX] | [Post-money YC] | [$X,XXX,XXX] | None | No | [YYYY-MM-DD] | Next equity round | [Active] |
| 2 | [Investor B] | [$X,XXX,XXX] | [Post-money YC] | [$X,XXX,XXX] | 20% | No | [YYYY-MM-DD] | Next equity round | [Active] |
| 3 | [Investor C] | [$XXX,XXX] | [Post-money YC MFN] | None | None | Yes | [YYYY-MM-DD] | Next equity round | [Active — MFN requires update if cap added to new SAFEs] |
| 4 | [Investor D] | [$X,XXX,XXX] | [Post-money YC] | [$X,XXX,XXX] | None | No | [YYYY-MM-DD] | Series A close | [Converted — see conversion record below] |

**Total active SAFE balance**: [$X,XXX,XXX]
**Total converted**: [$X,XXX,XXX]

## Conversion Records

| SAFE # | Investor | Amount | Conversion Event | Conversion Date | Shares Issued | Price Per Share | Share Class | Notes |
|--------|----------|--------|-----------------|----------------|--------------|----------------|------------|-------|
| 4 | [Investor D] | [$X,XXX,XXX] | [Series A close] | [YYYY-MM-DD] | [N,XXX shares] | [$X.XX (cap conversion)] | [Series A Preferred] | [Cap triggered — converted at $X.XX vs. $X.XX Series A price] |

## Conversion Scenarios

[Model conversion of all active SAFEs at various next-round valuations.]

### Assumptions for Conversion Modelling

| Parameter | Value |
|-----------|-------|
| New shares for conversion = | SAFE Amount ÷ Conversion Price |
| Conversion price for capped SAFE = | MIN(Cap ÷ fully diluted shares, Next round price ÷ (1-discount)) |
| Conversion price for MFN SAFE = | Most favorable cap/discount from other SAFEs issued before next round |

### Scenario: Series A at $[X]M Pre-Money

| Investor | SAFE Amount | Cap | Discount | Conversion Price | Shares Issued | % Post-Conversion |
|----------|------------|-----|---------|-----------------|--------------|------------------|
| [Investor A] | [$X,XXX,XXX] | [$X,XXX,XXX] | None | [$X.XX (cap triggered)] | [N,XXX] | [X%] |
| [Investor B] | [$X,XXX,XXX] | [$X,XXX,XXX] | 20% | [$X.XX (discount triggered — exceeds cap)] | [N,XXX] | [X%] |
| [Investor C — MFN] | [$XXX,XXX] | [Inherits lowest cap from above] | None | [$X.XX] | [N,XXX] | [X%] |
| **Total new shares** | — | — | — | — | **[N,XXX]** | **[X%]** |

**Dilution to existing founders at $[X]M pre-money Series A**: [X%]

### Scenario: Series A at $[Y]M Pre-Money (lower valuation)

| Investor | Conversion Price | Shares Issued | % Post-Conversion |
|----------|-----------------|--------------|------------------|
| [Investor A] | [$X.XX (round price — below cap)] | [N,XXX] | [X%] |
| [Investor B] | [$X.XX (discount applied)] | [N,XXX] | [X%] |
| **Total new shares** | — | **[N,XXX]** | **[X%]** |

## MFN Tracker

| MFN Holder | MFN Provision | SAFEs Issued After This SAFE | Best Terms Available | Action Required |
|------------|--------------|------------------------------|---------------------|----------------|
| [Investor C] | [MFN on valuation cap and discount] | [SAFE #1 ($X,XXX,XXX cap), SAFE #2 ($X,XXX,XXX cap + 20% discount)] | [$X,XXX,XXX cap] | [Offer cap amendment to Investor C — or confirm no update if cap is above their original terms] |

## Execution Checklist (Per New SAFE)

| Step | Status | Date | Notes |
|------|--------|------|-------|
| SAFE terms agreed with investor | [ ] | — | — |
| SAFE drafted (YC standard template) | [ ] | — | — |
| Conversion model shared with investor | [ ] | — | — |
| Legal counsel review complete | [ ] | — | — |
| Board approval (if required by bylaws) | [ ] | — | — |
| SAFE signed by both parties | [ ] | [YYYY-MM-DD] | — |
| Wire received and confirmed | [ ] | [YYYY-MM-DD] | [$X,XXX,XXX received] |
| SAFE added to cap table (as convertible) | [ ] | [YYYY-MM-DD] | — |
| MFN provisions reviewed for existing holders | [ ] | [YYYY-MM-DD] | — |
| Signed copy sent to investor | [ ] | [YYYY-MM-DD] | — |
