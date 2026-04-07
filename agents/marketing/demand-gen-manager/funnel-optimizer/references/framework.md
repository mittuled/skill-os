# Funnel Optimizer Framework

Reference framework for diagnosing conversion performance across the TOFU/MOFU/BOFU funnel, benchmarking stage metrics, and identifying friction points.

## Funnel Stage Definitions

| Stage | Label | Input Metric | Output Metric | Transition Event |
|-------|-------|-------------|---------------|-----------------|
| TOFU | Top of Funnel | Impressions / Sessions | Leads | Form submission, trial signup, content download |
| MOFU | Middle of Funnel | Leads | MQLs | Lead score threshold met OR qualifying action taken |
| BOFU | Bottom of Funnel | MQLs | SQLs → Opportunities | Sales accepted lead, discovery call booked |
| Close | Revenue Stage | Opportunities | Closed-Won | Contract signed, payment received |

## Conversion Benchmarks by Stage (B2B SaaS)

| Stage Transition | Healthy Range | Underperforming | Critical |
|-----------------|---------------|-----------------|----------|
| Session → Lead (overall) | 2.5–5% | 1–2.5% | < 1% |
| Session → Lead (paid search) | 3–8% | 1.5–3% | < 1.5% |
| Session → Lead (paid social) | 1.5–4% | 0.5–1.5% | < 0.5% |
| Session → Lead (organic) | 1–3% | 0.3–1% | < 0.3% |
| Lead → MQL | 20–40% | 10–20% | < 10% |
| MQL → SQL | 20–40% | 10–20% | < 10% |
| SQL → Opportunity | 40–70% | 20–40% | < 20% |
| Opportunity → Closed-Won | 20–35% | 10–20% | < 10% |

> Benchmarks vary by ACV, industry, and sales motion. Adjust thresholds by ±20% for ACV > $50K (enterprise) or products with free trial/PLG motion.

## B2C / PLG Conversion Benchmarks

| Stage Transition | Healthy Range | Underperforming | Critical |
|-----------------|---------------|-----------------|----------|
| Session → Signup | 3–10% | 1–3% | < 1% |
| Signup → Activated | 25–50% | 10–25% | < 10% |
| Activated → Retained (D30) | 20–40% | 8–20% | < 8% |
| Free → Paid Conversion | 2–8% | 0.5–2% | < 0.5% |

## Friction Identification Framework

### TOFU Friction Sources

| Friction Type | Symptoms | Diagnostic Question |
|--------------|---------|-------------------|
| Audience mismatch | High impressions, low CTR | Is the ad targeting the right ICP? |
| Message mismatch | High CTR, low session-to-lead | Does the landing page match the ad promise? |
| Traffic quality | High bounce rate (> 70%), low time-on-site | Is the source channel sending low-intent visitors? |
| Page speed | High exit rate on landing pages | Do Core Web Vitals fail LCP > 2.5s? |
| Offer relevance | Form page views without submissions | Is the offer compelling enough for the ask? |

### MOFU Friction Sources

| Friction Type | Symptoms | Diagnostic Question |
|--------------|---------|-------------------|
| Lead quality | High lead volume, low MQL rate | Is lead scoring calibrated to sales-accepted ICP criteria? |
| Nurture gap | Leads going cold after initial touch | Is there an active nurture sequence with relevant content? |
| Timing mismatch | Leads converting to MQL months after creation | Is the nurture cadence too slow for the buying cycle? |
| Content gap | Leads engaging with TOFU content but not progressing | Is MOFU content available for the evaluation stage? |
| Disqualification | High MQL count, low SQL acceptance | Are MQL criteria misaligned with sales expectations? |

### BOFU Friction Sources

| Friction Type | Symptoms | Diagnostic Question |
|--------------|---------|-------------------|
| Sales process gap | SQLs going dark after discovery | Is the follow-up sequence defined and executed consistently? |
| Competitive loss | Opportunities lost to named competitors | Is sales equipped with comparison content and battle cards? |
| Pricing friction | Late-stage drop-off after pricing discussion | Is pricing communicated clearly before the sales call? |
| Decision committee | Long sales cycles with multiple stakeholders | Is content available for all buying committee personas? |
| Champion weakness | Opportunities stalling internally | Does the champion have the internal business case materials they need? |

## Channel Attribution Heatmap Template

Rate each channel's conversion performance at each funnel stage (G = Green/Healthy, A = Amber/Underperforming, R = Red/Critical):

| Channel | Session→Lead | Lead→MQL | MQL→SQL | SQL→Opp | Opp→Won | Volume |
|---------|-------------|---------|--------|--------|--------|--------|
| Google Search | | | | | | |
| Google Display | | | | | | |
| Meta Paid | | | | | | |
| LinkedIn Paid | | | | | | |
| Organic Search | | | | | | |
| Email Nurture | | | | | | |
| Direct / Dark Social | | | | | | |
| Partner / Referral | | | | | | |

## Impact/Effort Matrix for Interventions

| Quadrant | Impact | Effort | Action |
|---------|--------|--------|--------|
| Quick Win | High | Low | Execute immediately (0–30 days) |
| Strategic Bet | High | High | Plan and resource (30–60 days) |
| Fill-In | Low | Low | Do when capacity allows |
| Avoid | Low | High | Deprioritise or remove from roadmap |

## Common Intervention Library

### TOFU Interventions
- Tighten audience targeting exclusions (negative keywords, audience exclusions)
- Improve message match between ad and landing page headline
- Add landing page variants for different audience segments
- Reduce form field count or replace text fields with selects
- Improve page speed to meet LCP < 2.5s threshold

### MOFU Interventions
- Recalibrate lead scoring with sales input on SQL characteristics
- Build or extend nurture sequence with stage-specific content
- Add MOFU content assets (case studies, comparison guides, ROI calculators)
- Implement re-engagement flow for leads inactive > 30 days
- Introduce progressive profiling to enrich lead records over time

### BOFU Interventions
- Build structured follow-up sequence with defined SLAs
- Create competitive battle cards for top-three named competitors
- Add pricing transparency page or pricing calculator to reduce sales cycle friction
- Develop multi-stakeholder content packs for buying committee personas
- Create internal business case template for champions to use with their leadership
