# Financial Model V1: Series A SaaS Company

## Metadata

| Field | Value |
|-------|-------|
| Date | 2026-03-15 |
| Author | CFO / VP Finance |
| Version | 1.0 |
| Status | Review |
| Skill | financial-model-v1 |

## Executive Summary

The v1 financial model projects ARR growth from $1.8M to $6.2M over 24 months (base case), driven by sales capacity expansion from 2 to 5 AEs and 112% NRR on the existing customer base. Unit economics are viable at 4.3x LTV/CAC with 13-month payback, supporting a $8M Series A that provides 26 months of runway under the base case and 18 months under the downside scenario.

## Revenue Model

### Revenue Architecture
| Stream | Driver | Monthly Build |
|--------|--------|--------------|
| New Business | SQLs × close rate × ACV | 120 SQLs × 15% × $19.2K blended ACV |
| Expansion | Existing base × (NRR - 1) / 12 | $1.8M ARR base × 1% monthly expansion |
| Contraction | Existing base × monthly contraction | $1.8M ARR base × 0.3% monthly |
| Churn | Existing base × monthly churn | $1.8M ARR base × 0.5% monthly gross churn |

### Bottoms-Up Revenue Forecast (Quarterly)
| Quarter | New ARR | Expansion | Contraction | Churn | Ending ARR |
|---------|---------|-----------|-------------|-------|------------|
| Q1 (Current) | $345K | $54K | ($16K) | ($27K) | $2.16M |
| Q2 | $414K | $65K | ($19K) | ($32K) | $2.58M |
| Q3 | $518K | $77K | ($23K) | ($39K) | $3.12M |
| Q4 | $621K | $94K | ($28K) | ($47K) | $3.76M |
| Q5 | $745K | $113K | ($34K) | ($56K) | $4.53M |
| Q6 | $828K | $136K | ($41K) | ($68K) | $5.38M |
| Q7 | $897K | $161K | ($48K) | ($81K) | $6.21M |
| Q8 (M24) | $897K | $186K | ($56K) | ($93K) | $6.21M |

### Cohort Analysis
- Month 1-6 cohorts: 112% NRR (validated with 18 months of data)
- Month 7-12 cohorts: 115% NRR assumption (larger customers onboarded with dedicated CSM)
- Month 13+ cohorts: 110% NRR assumption (conservative for unvalidated period)

## Cost Structure

### COGS Breakdown
| Component | Per Customer/Month | At Scale |
|-----------|-------------------|----------|
| AWS Infrastructure | $85 | $72 (volume discount at 100+ customers) |
| Customer Support (allocated) | $42 | $38 |
| Third-party APIs | $28 | $28 |
| **Total COGS per customer** | **$155** | **$138** |
| **Gross Margin** | **76.3%** | **78.9%** |

### OpEx by Department (Monthly at M1 → M24)
| Department | M1 | M12 | M24 | Headcount M1→M24 |
|------------|-----|------|------|-------------------|
| R&D | $142K | $198K | $285K | 10 → 15 |
| S&M | $95K | $165K | $240K | 5 → 10 |
| G&A | $68K | $82K | $105K | 4 → 5 |
| Non-headcount | $45K | $55K | $72K | — |
| **Total OpEx** | **$350K** | **$500K** | **$702K** | **22 → 35** |

## Cash Flow Statement

### Monthly Cash Flow Summary (Quarterly Snapshots)
| Quarter | Cash In | Cash Out | Net Cash | Cumulative | Runway |
|---------|---------|----------|----------|------------|--------|
| Q1 | $540K | $795K | ($255K) | $2.95M | 11.5 mo |
| Q2 | $665K | $920K | ($255K) | $2.69M + $8M raise | $10.4M |
| Q3 | $832K | $1.05M | ($218K) | $9.75M | 33 mo |
| Q4 | $1.01M | $1.18M | ($170K) | $9.24M | 32 mo |
| Q5 | $1.22M | $1.32M | ($100K) | $8.94M | 30 mo |
| Q6 | $1.45M | $1.42M | $30K | $8.97M | Cash flow positive |

### Cash Conversion Assumptions
- Annual prepay mix: 65% (enterprise) / 35% monthly
- DSO: 38 days (current), improving to 32 days by M24
- Vendor payment terms: Net 30 standard

## SaaS Metrics Dashboard

| Metric | Current | M12 | M24 | Benchmark (Median Series A) |
|--------|---------|------|------|---------------------------|
| ARR | $1.8M | $3.76M | $6.21M | $4-8M |
| MRR Growth (MoM) | 6.2% | 5.8% | 4.5% | 5-8% |
| NRR | 112% | 114% | 112% | 110-120% |
| Gross Churn | 6.0% | 5.5% | 5.0% | 5-8% |
| Gross Margin | 76% | 78% | 79% | 70-80% |
| LTV (GM-based) | $232K | $249K | $261K | — |
| CAC | $9.2K | $8.8K | $9.5K | — |
| LTV/CAC | 4.3x | 4.8x | 4.4x | >3x |
| CAC Payback | 13 mo | 12 mo | 13 mo | <18 mo |
| Burn Multiple | 1.8x | 1.2x | 0.4x | <2x |
| Runway | 17.8 mo | 32 mo | Cash flow+ | >18 mo |

## Scenario Analysis

| Driver | Downside | Base | Upside |
|--------|----------|------|--------|
| SQL growth rate | 0% (flat) | 8% MoM | 12% MoM |
| Close rate | 12% | 15% | 18% |
| NRR | 105% | 112% | 118% |
| Hiring pace | +8 (essential only) | +13 (plan) | +18 (accelerated) |
| Non-HC cost growth | 2% MoM | 3% MoM | 4% MoM |

| Outcome | Downside | Base | Upside |
|---------|----------|------|--------|
| M24 ARR | $4.1M | $6.2M | $8.8M |
| M24 Customers | 98 | 142 | 195 |
| Cash flow positive | M28 | M22 | M18 |
| Post-raise runway | 18 mo | 26 mo | 22 mo (higher spend) |

### Scenario Triggers
- **Downside activates if**: 2 consecutive months of SQL volume <100 OR close rate drops below 12%
- **Upside activates if**: 3 consecutive months of SQL volume >150 AND close rate holds >16%
- **Management actions**: Downside triggers hiring freeze and marketing reallocation; Upside triggers accelerated AE hiring

## Recommendations

1. **P1 — Raise at $8M**: Unit economics support the raise; LTV/CAC of 4.3x and 13-month payback exceed Series A benchmarks. Target close by Q2 to maintain >18 months runway under all scenarios.
2. **P1 — Hire 3 AEs in Q2-Q3**: Sales capacity is the binding constraint; each AE at current productivity adds ~$300K ARR within 6 months of ramp.
3. **P2 — Improve NRR to 115%+**: Dedicated CSM for accounts >$24K ACV; expansion revenue is the highest-ROI growth lever with zero incremental CAC.
4. **P3 — Reduce DSO to 32 days**: Shift new contracts to annual prepay default with monthly option (currently 65/35 split; target 75/25).

## Appendices

### A. Methodology

Model built bottoms-up from sales capacity (SQLs × close rate × ACV) with cohort-based retention modelling. Cost structure is headcount-driven with fully-loaded compensation (salary + 25% benefits + equity). Cash flow converts accrual P&L to cash basis using billing mix and DSO assumptions. SaaS metrics calculated per industry-standard definitions (Bessemer, SaaS Capital).

### B. Assumptions Register

| Assumption | Value | Source | Confidence | Sensitivity |
|------------|-------|--------|------------|-------------|
| SQL volume growth | 8% MoM | Trailing 6-month trend | Medium | High |
| Close rate | 15% | Trailing 12-month average | High | High |
| ACV blended | $19.2K | Current tier mix weighted | High | Medium |
| NRR | 112% | Trailing 4-quarter average | High | High |
| Gross margin | 76% | GL actuals LTM | High | Low |
| Fully-loaded cost/employee | $285K | Current payroll + benefits | High | Medium |
| Annual prepay mix | 65% | Current billing data | Medium | Medium |
| DSO | 38 days | Trailing 6-month average | High | Low |
