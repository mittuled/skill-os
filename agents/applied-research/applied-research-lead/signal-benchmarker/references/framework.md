# Framework: Signal Benchmarker

Defines the methodology for selecting appropriate benchmark cohorts, sourcing data, normalising for comparability, and interpreting benchmark results.

## Benchmark Cohort Selection

### Cohort Dimensions

Select benchmark cohorts along these dimensions to ensure fair comparison:

| Dimension | Options | Selection Guidance |
|-----------|---------|-------------------|
| Company stage | Pre-PMF / Post-PMF / Growth / Scale / Public | Match within one stage level |
| ARR range | <$1M / $1-10M / $10-50M / $50-200M / $200M+ | Match within same band or adjacent |
| Business model | SaaS / Marketplace / Transactional / Hybrid | Same model only |
| Market segment | SMB / Mid-market / Enterprise / Multi-segment | Match primary segment |
| Go-to-market | PLG / Sales-led / Channel / Hybrid | Same motion or note the difference |
| Geography | Single-market / Multi-region / Global | Note if expansion stage differs |

### Cohort Mismatch Warning Signs

Flag and adjust if:
- Benchmark company is 3+ years older in the same growth phase
- Benchmark uses a fundamentally different GTM motion (PLG vs. Sales-led changes most SaaS metrics significantly)
- Benchmark data is from a different macro environment (e.g., 2021 vs. 2024 SaaS multiples are not comparable)

## Benchmark Data Sources (by Metric Category)

| Metric Category | Primary Sources | Reliability |
|----------------|----------------|-------------|
| SaaS growth (ARR, NDR, NRR) | OpenView OKR, KeyBanc SaaS Survey, Bessemer Cloud Index | High (annual surveys, n>100) |
| Customer retention (churn, LTV) | Paddle, Stripe, ChartMogul benchmarks | High (transactional data) |
| Conversion rates | Lenny's Newsletter benchmarks, First Round Capital data | Medium (self-reported) |
| NPS / CSAT | Bain, Satmetrix industry benchmarks, Medallia | Medium (varies by industry) |
| Product engagement (DAU/MAU) | Amplitude benchmarks, Mixpanel reports | Medium (opt-in reporting) |
| Sales efficiency (magic number, CAC payback) | Bessemer, Battery Ventures SaaS benchmarks | High (investor-grade data) |

## Key Metric Benchmark Reference Values

SaaS benchmarks for post-PMF, $1-50M ARR, primarily mid-market:

| Metric | Strong | Median | Weak | Source Reference |
|--------|--------|--------|------|-----------------|
| Net Revenue Retention (NRR) | >120% | 105-115% | <100% | OpenView 2024 |
| Gross Revenue Retention (GRR) | >95% | 88-92% | <85% | OpenView 2024 |
| CAC Payback Period | <12 months | 15-24 months | >24 months | Bessemer 2024 |
| Magic Number (Sales Efficiency) | >1.0 | 0.5-0.75 | <0.5 | SaaS Capital |
| DAU/MAU Ratio | >50% | 25-40% | <15% | Amplitude Benchmark |
| Free-to-Paid Conversion (PLG) | >5% | 2-4% | <1% | OpenView 2024 |
| Trial-to-Paid Conversion | >25% | 15-20% | <10% | Lenny's 2024 |
| Support Ticket Rate (per user/month) | <0.1 | 0.2-0.5 | >1.0 | Zendesk Benchmark |

Note: Always verify against current-year sources; benchmark values shift with market conditions.

## Normalisation Methods

When benchmark cohorts are not perfectly matched:
- **Stage normalisation**: Apply 15-20% performance premium for each stage level of advantage; apply equivalent discount for stage disadvantage
- **GTM normalisation**: PLG companies typically show 2-3× higher trial-to-paid conversion and lower CAC payback than sales-led; do not compare directly
- **Seasonality**: Note fiscal quarter effects on conversion and expansion data; annualise where possible
