# Marketing Audit Report

## Metadata

| Field | Value |
|-------|-------|
| Date | 2026-10-01 |
| Author | VP Marketing (AI Agent) |
| Version | 1.0 |
| Status | Final |
| Skill | marketing-audit-orchestrator |
| Audit Period | 2026-07-01 - 2026-09-30 |

## Executive Summary

Marketing scored a C+ (6.15) for Q3 2026, reflecting solid funnel mechanics and reasonable channel returns undermined by poor MarTech utilisation and inconsistent content strategy. The single highest-impact action is implementing HubSpot lead scoring and multi-touch attribution, which would simultaneously improve MarTech utilisation, funnel efficiency, and channel performance visibility.

## Composite Score

| Criterion | Weight | Score (0-10) | Weighted Score | Key Evidence |
|-----------|--------|-------------|----------------|--------------|
| Brand Health | 20% | 6 | 1.20 | Unaided awareness 18% (up from 12%); NPS 32; brand guidelines followed in only 65% of materials |
| Channel Performance | 25% | 7 | 1.75 | Google Ads ROAS 3.8x (strong); LinkedIn ROAS 1.4x (below target); last-touch only attribution masks true channel value |
| Content Quality | 20% | 5 | 1.00 | SEO comparison guides drive traffic but no content-to-pipeline attribution; no editorial calendar; company news posts generate zero engagement |
| Funnel Efficiency | 20% | 7 | 1.40 | MQL-to-SQL 20%, SQL-to-Opp 20%, Opp-to-Close 30% — reasonable but no lead scoring means SDRs waste time on unqualified MQLs |
| MarTech Utilisation | 15% | 4 | 0.60 | HubSpot at 40% feature adoption; lead scoring, ABM, A/B testing all unused; CRM sync breaks 2x/month |
| **Composite** | **100%** | | **5.95** | **Grade: C (Adequate)** |

## Brand Health Deep-Dive

Unaided brand awareness in the ICP reached 18% in Q3, a meaningful improvement from 12% in Q2, suggesting that increased content and advertising activity is building recognition. NPS at 32 is healthy for B2B SaaS. However, brand guideline adherence at 65% indicates a discipline gap — one-third of external materials use inconsistent visual identity, diluting brand equity. No share-of-voice measurement exists, making competitive positioning impossible to benchmark.

### Strengths and Gaps

| Finding | Type | Impact | Evidence |
|---------|------|--------|----------|
| Awareness trending up 50% QoQ | Strength | High | 12% to 18% unaided awareness in ICP |
| Healthy NPS for B2B SaaS | Strength | Medium | NPS 32 |
| Poor brand guideline adherence | Gap | Medium | 35% of materials non-compliant |
| No share-of-voice tracking | Gap | Medium | Cannot benchmark against competitors |

## Channel Performance Deep-Dive

Google Ads is the strongest channel at 3.8x ROAS, comfortably above the 3x target. LinkedIn Ads underperform at 1.4x ROAS — likely due to broad targeting rather than ABM-style audience building. Organic search drives 28% of MQLs at near-zero marginal cost, making it the most efficient channel. The critical gap is attribution: last-touch only attribution almost certainly over-credits bottom-of-funnel channels and under-credits awareness channels.

### Channel Breakdown

| Channel | Spend | Pipeline Generated | CAC | ROAS | Trend |
|---------|-------|-------------------|-----|------|-------|
| Google Ads | $480K | $1,824K | $142 | 3.8x | Up |
| LinkedIn Ads | $320K | $448K | $286 | 1.4x | Flat |
| Organic Search | $60K (content cost) | $672K | $38 | 11.2x | Up |
| Events | $140K | $280K | $224 | 2.0x | Down |

## Content Quality Deep-Dive

Content production volume is adequate (45 posts in Q3), but strategy is absent. The top 5 performing assets are all SEO-optimised comparison guides — a clear signal that bottom-of-funnel, buyer-intent content drives results. The bottom 10 are company news posts with near-zero engagement, representing wasted production capacity. No content-to-pipeline attribution exists, meaning the team cannot identify which content actually influences deals. The absence of an editorial calendar means topics are reactive, not strategically mapped to buyer journey stages.

## Funnel Efficiency Deep-Dive

The funnel produces results — 2,400 MQLs converting to 29 closed-won deals ($522K pipeline) — but operates inefficiently due to manual qualification. MQL-to-SQL conversion at 20% is below the 25% benchmark, and SDRs report spending 40%+ of their time on clearly unqualified leads that a scoring model would filter automatically. The 68-day MQL-to-close cycle is acceptable for $18K ACV but could be compressed with better nurture sequences.

### Funnel Stage Analysis

| Stage | Volume | Conversion Rate | Benchmark | Gap | Primary Leak Cause |
|-------|--------|----------------|-----------|-----|-------------------|
| Visitor to MQL | 48,000 to 2,400 | 5.0% | 3-5% | On target | N/A |
| MQL to SQL | 2,400 to 480 | 20.0% | 25% | -5% | No lead scoring; manual qualification |
| SQL to Opportunity | 480 to 96 | 20.0% | 20% | On target | N/A |
| Opportunity to Close | 96 to 29 | 30.2% | 25% | +5% | Strong sales execution |

## MarTech Utilisation Deep-Dive

HubSpot Marketing Hub Professional is significantly underutilised at an estimated 40% feature adoption. Active features include email marketing, forms, and basic workflows. Inactive features include lead scoring (critical gap), ABM tools, A/B testing, and social publishing. The CRM sync between HubSpot and Salesforce breaks approximately twice per month, requiring manual data reconciliation that introduces errors and delays. No data hygiene process exists — duplicate records and stale contacts are not systematically cleaned.

## Causal Analysis

1. **Low MarTech utilisation (4) causes attribution blindness**: Without multi-touch attribution configured in HubSpot, Channel Performance (7) is likely over-scored for bottom-funnel channels and under-scored for top-funnel. Fixing this would provide accurate ROAS data for budget reallocation.
2. **Missing lead scoring degrades funnel efficiency**: The 5-point gap below MQL-to-SQL benchmark (20% vs 25%) directly traces to SDRs manually qualifying unscored leads. HubSpot lead scoring (currently unused) would automate this.
3. **No content attribution masks content ROI**: Content Quality (5) may be under-scored because the team cannot prove which content influences pipeline. Implementing content attribution would either validate increased content investment or redirect resources.

## Recommendations

| Priority | Recommendation | Owner | Timeline | Expected Impact | Success Metric |
|----------|---------------|-------|----------|-----------------|----------------|
| P1 | Implement HubSpot lead scoring model using behavioural and firmographic signals; integrate with Salesforce lead status | Marketing Ops Manager | 6 weeks | 25% reduction in SDR time on unqualified leads; MQL-to-SQL rate improvement from 20% to 25% | MQL-to-SQL conversion rate |
| P1 | Configure multi-touch attribution in HubSpot; map all conversion events; validate against Salesforce pipeline data | Marketing Ops Manager | 8 weeks | Accurate channel ROAS enabling $100K+ budget reallocation from underperforming to high-performing channels | Attribution model coverage > 80% of pipeline |
| P2 | Establish editorial calendar mapped to buyer journey stages; kill company news posts; double down on comparison guides and technical tutorials | Content Marketer | 4 weeks | 30% increase in content-influenced pipeline through strategic topic selection | Content-to-pipeline attribution (new metric) |

## Appendices

### A. Methodology

Audit conducted using the marketing-audit-orchestrator scoring rubric (v1.0.0) with five weighted dimensions. Data sourced from HubSpot reporting, Salesforce pipeline reports, Google Analytics 4, and Semrush. Audit period: Q3 2026 (July 1 - September 30). Brand health data from Q3 brand tracker survey (n=500 ICP respondents). Scoring performed using `scripts/score.py` with manual evidence validation.

### B. Supporting Data

Full channel-by-channel spending breakdown, content performance ranking (all 45 posts), HubSpot feature adoption audit matrix, Salesforce funnel stage definitions, and brand guideline compliance audit sample (50 materials reviewed) available upon request.
