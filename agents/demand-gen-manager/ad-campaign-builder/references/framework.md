# Ad Campaign Builder Framework

Reference framework for building structured paid advertising campaigns across Google, Meta, LinkedIn, and TikTok.

## Platform Selection Guide

| Platform | Best For | ICP Signal | Min Monthly Budget | Typical B2B SaaS CAC |
|----------|---------|------------|-------------------|---------------------|
| Google Search | High-intent capture | ICP actively searching for solutions | $3,000 | $80-250 |
| Google Display/YouTube | Awareness, remarketing | ICP consumes content on Google properties | $2,000 | $150-400 |
| Meta (Facebook/Instagram) | Lookalike targeting, retargeting | ICP active on Meta platforms; visual product | $2,000 | $100-300 |
| LinkedIn | B2B targeting by job title, company | ICP is professionals; ACV > $10K | $5,000 | $200-500 |
| TikTok | Younger audience, product-led | ICP includes IC-level, developer, or SMB buyers | $1,500 | $80-200 |

## Budget Allocation Framework (70/20/10)

| Tier | Allocation | Criteria | Example |
|------|-----------|----------|---------|
| **Proven** | 70% | Channels with 3+ months of positive ROAS data | Google Search with ROAS > 3x |
| **Scaling** | 20% | Channels showing early promise, need more data | LinkedIn with ROAS 1.5-3x |
| **Experiment** | 10% | New channels or campaign types with no data | TikTok first campaign |

## Account Structure Best Practices

### Google Ads

```
Account
├── Campaign: [Product] - Search - [Geo]
│   ├── Ad Group: [Keyword Theme 1]
│   │   ├── 3-5 Responsive Search Ads
│   │   ├── Keywords (10-20 per group, tight theme)
│   │   └── Negative Keywords (shared list + group-specific)
│   └── Ad Group: [Keyword Theme 2]
├── Campaign: [Product] - Display - Remarketing
│   ├── Ad Set: Site Visitors (7-day)
│   ├── Ad Set: Site Visitors (30-day)
│   └── Ad Set: Converters - Exclude
└── Campaign: [Product] - YouTube - Awareness
```

**Key rules**: Single keyword theme per ad group. Minimum 3 responsive search ads per group. Negative keyword lists shared at account level. Separate campaigns for search, display, and video.

### Meta Ads

```
Account
├── Campaign: [Product] - Conversions - Cold
│   ├── Ad Set: Lookalike 1% - [ICP Interest]
│   │   └── 3-5 Ad Variants (image + video mix)
│   ├── Ad Set: Lookalike 3% - [Broader Interest]
│   └── Ad Set: Interest Targeting - [Category]
├── Campaign: [Product] - Conversions - Retargeting
│   ├── Ad Set: Website Visitors 7d (exclude converters)
│   ├── Ad Set: Website Visitors 30d (exclude 7d + converters)
│   └── Ad Set: Video Viewers 50%+ (exclude converters)
└── Campaign: [Product] - Awareness - Broad
```

**Key rules**: Use Campaign Budget Optimization (CBO) with minimum spend per ad set. Separate cold and retargeting into different campaigns. Always exclude converters from prospecting.

### LinkedIn Ads

```
Account
├── Campaign Group: [Product] - [Quarter]
│   ├── Campaign: [Product] - Lead Gen - Decision Makers
│   │   ├── Targeting: Job titles + Company size + Industry
│   │   └── 3-5 Sponsored Content ads
│   ├── Campaign: [Product] - Lead Gen - Practitioners
│   │   ├── Targeting: Job functions + Skills + Seniority
│   │   └── 3-5 Sponsored Content ads
│   └── Campaign: [Product] - Retargeting - Website
│       ├── Targeting: Website visitors + Matched audiences
│       └── 3-5 Sponsored Content ads
```

**Key rules**: Separate decision-maker and practitioner audiences. Use Lead Gen Forms for gated content (higher conversion than landing pages on LinkedIn). Minimum audience size 50,000 for cold campaigns.

### TikTok Ads

```
Account
├── Campaign: [Product] - Conversions
│   ├── Ad Group: Interest - [Category 1]
│   │   └── 3-5 Video Ads (9:16, 15-60s)
│   ├── Ad Group: Lookalike - Website Visitors
│   └── Ad Group: Creator Spark Ads
└── Campaign: [Product] - Retargeting
    ├── Ad Group: Video Viewers 75%+
    └── Ad Group: Website Visitors 7d
```

**Key rules**: Video-only platform — no static images. UGC-style creative outperforms polished ads. Use Spark Ads with creator content when possible. Minimum 50 conversions per week per ad group for optimisation.

## Bidding Strategy Decision Tree

| Campaign Maturity | Objective | Recommended Strategy | Rationale |
|-------------------|-----------|---------------------|-----------|
| New (< 50 conversions) | Learn | Manual CPC / Lowest Cost | Gather data without algorithm constraints |
| Growing (50-200 conversions) | Optimise | Target CPA / Cost Cap | Enough data for algorithm to optimise |
| Scaled (200+ conversions) | Maximise | Maximise Conversions / Value-based | Algorithm has sufficient signal to scale |

## Retargeting Sequence Framework

| Stage | Audience | Recency Window | Frequency Cap | Creative Focus |
|-------|----------|---------------|---------------|----------------|
| 1 - Re-engage | All site visitors | 1-7 days | 3/day | Value proposition reminder, social proof |
| 2 - Nurture | Visited key pages (pricing, features) | 8-30 days | 2/day | Case studies, comparison content |
| 3 - Convert | High-intent (started trial, visited checkout) | 1-14 days | 4/day | Direct offer, urgency, risk reversal |
| 4 - Win-back | Lapsed visitors | 31-90 days | 1/day | New features, refreshed offer |

**Exclusion rules**: Always exclude converters from retargeting. Exclude stage N audience from stage N-1 to prevent overlap.

## Creative Testing Framework

| Platform | Min Variants | Test Duration | Statistical Significance |
|----------|-------------|---------------|------------------------|
| Google RSA | 3 per ad group | 14 days minimum | 95% confidence on CTR |
| Meta | 3-5 per ad set | 7 days minimum | 50+ conversions per variant |
| LinkedIn | 3-5 per campaign | 14 days minimum | 50+ clicks per variant |
| TikTok | 3-5 per ad group | 7 days minimum | 50+ conversions per variant |
