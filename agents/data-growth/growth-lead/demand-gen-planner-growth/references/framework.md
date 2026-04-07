# Framework: Demand Gen Planner Growth

Defines the structural methodology for designing acquisition channel plans aligned to the growth model's CAC targets and acquisition volume requirements.

## Channel Taxonomy

### Tier 1: Owned and Earned (Lowest CAC, Highest Compounding)
- **SEO / Content**: Blog, documentation, comparison pages, programmatic pages
- **Product-Led Growth**: Viral features, collaborative workflows, public outputs
- **Email / CRM**: Nurture of inbound leads, reactivation

### Tier 2: Paid Direct (Scalable, Linear Cost)
- **Paid Search (SEM)**: Google Ads, Bing — captures existing demand
- **Paid Social**: LinkedIn (B2B), Meta/TikTok (consumer) — creates demand
- **Review and Intent Platforms**: G2, Capterra, TrustPilot

### Tier 3: Partner and Ecosystem (Variable, Requires Investment)
- **Affiliate**: Performance-based referral partners
- **Integration Partners**: Co-marketing with complementary tools
- **Resellers / VARs**: Indirect sales channels

## CAC Calculation Method

```
Fully Loaded CAC = (Ad Spend + Agency Fees + Tool Costs + Headcount Hours × Hourly Rate)
                   / New Paid Customers in Period

Maximum Allowable CAC = LTV × (1 / Target LTV:CAC Ratio)
                      = (ARPU × Gross Margin % / Monthly Churn Rate) × (1/3)
```

For pre-revenue products: use estimated LTV from pricing model + comparable products.

## Budget Allocation Framework

### Anchor Allocation (Recommended Starting Point)

| Channel Category | % of Budget | Rationale |
|-----------------|-------------|-----------|
| Primary proven channel (1–2) | 50–60% | Maximize what works before diversifying |
| Secondary proven channels | 20–30% | Maintain diversification across validated channels |
| New channel experiments | 15–20% | Test-and-learn budget; never skip this |
| Retention/reactivation | 5–10% | Lower CAC than new acquisition |

### Experiment Budget Sizing

Minimum viable channel test budget:
```
Test Budget = (Target sample size × CAC estimate) × 1.5 safety multiplier

Target sample: minimum 100 conversions for CAC reliability (Law of Large Numbers)
Duration: minimum 2 weeks; maximum 4 weeks for initial read
```

## Channel Scorecard Template

| Channel | ICP Reach | CAC Target | CAC Estimate | Volume Ceiling/mo | Time to First Data | Status |
|---------|-----------|-----------|-------------|------------------|-----------------|--------|
| [Channel] | [High/Med/Low] | $[X] | $[Y] | [Z] users | [N days] | [Go/Test/No-Go] |

## ICE Prioritization for Channel Experiments

Rate each channel test on:
- **Impact** (1–10): Expected volume at acceptable CAC if validated
- **Confidence** (1–10): Evidence base for CAC estimate (10 = measured, 1 = pure guess)
- **Ease** (1–10): Speed to launch and cost to test (10 = launch in 1 week at $1K)

ICE Score = (Impact + Confidence + Ease) / 3

Run experiments in ICE score order, starting with the highest score.

## Attribution Model

| Model | Use Case | Limitation |
|-------|---------|-----------|
| Last-touch | Default; simplest; works when sales cycle is short | Undervalues awareness channels |
| First-touch | Top-of-funnel attribution; good for brand campaigns | Undervalues bottom-of-funnel |
| Linear (multi-touch) | Longer sales cycles (> 30 days); multiple touchpoints | Requires cross-session tracking |

Minimum UTM taxonomy:
- `utm_source`: Platform (google, facebook, linkedin, partner-name)
- `utm_medium`: Channel type (cpc, organic, email, referral)
- `utm_campaign`: Campaign name (yyyymm-audience-offer)
- `utm_content`: Creative variant (for A/B test attribution)
