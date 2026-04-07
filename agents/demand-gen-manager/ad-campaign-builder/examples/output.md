# Campaign Plan: DataBridge API Connector Marketplace Launch

## Metadata

| Field | Value |
|-------|-------|
| Date | 2026-10-01 |
| Author | Demand Gen Manager (AI Agent) |
| Version | 1.0 |
| Status | Draft |
| Skill | ad-campaign-builder |

## Executive Summary

Q4 product launch campaign for DataBridge's API connector marketplace targeting mid-market data engineers and engineering managers across Google Search, LinkedIn, and Meta, with $35K monthly budget targeting 93 demo requests at $376 blended CAC. Google Search (proven, $19.3K) drives high-intent capture, LinkedIn (scaling, $8.8K) targets decision-makers by title, and Meta (experiment, $7K) tests retargeting-only conversion.

## Campaign Objective and ICP

Generate 93 demo requests per month from mid-market data engineers and engineering managers evaluating data integration tools in North America. Primary funnel stage: consideration-to-conversion.

### ICP Profile

| Attribute | Value |
|-----------|-------|
| Job Titles | Data Engineer, Senior Data Engineer, Engineering Manager, Head of Data |
| Company Size | 200-2000 employees |
| Industry | SaaS, Fintech, Healthcare Tech |
| Geography | North America |
| Annual Revenue | $20M-$500M (estimated from company size) |
| Buying Signal | Evaluating ETL/ELT tools, searching for API integration solutions, visiting connector comparison pages |

## Budget Allocation

| Platform | Monthly Budget | % of Total | Tier | Rationale |
|----------|---------------|-----------|------|-----------|
| Google Search | $19,250 | 55% | Proven | 6 months of data, ROAS 3.2x — primary pipeline driver |
| LinkedIn | $8,750 | 25% | Scaling | 2 months at 1.6x ROAS, trending up — B2B title targeting is ideal for ICP |
| Meta (Retargeting) | $7,000 | 20% | Experiment | First test — retargeting only to limit risk; re-engage site visitors across Facebook/Instagram |

## Platform: Google Search

### Account Structure

```
DataBridge Account
├── Campaign: Connectors - Search - NA - Brand
│   ├── Ad Group: Brand Terms
│   │   └── 3 RSAs (brand + connector marketplace messaging)
│   └── Ad Group: Brand + Competitor
│       └── 3 RSAs (vs competitor messaging)
├── Campaign: Connectors - Search - NA - Non-Brand
│   ├── Ad Group: API Integration Tools
│   │   └── 3 RSAs (150+ connectors, 10-min setup)
│   ├── Ad Group: Data Connector Platform
│   │   └── 3 RSAs (pre-built connectors, SOC 2)
│   ├── Ad Group: ETL Alternative
│   │   └── 3 RSAs (no-code setup, faster than ETL)
│   └── Ad Group: [Competitor] Alternative
│       └── 3 RSAs (specific competitor comparison)
└── Campaign: Connectors - Display - Remarketing
    ├── Ad Set: Site Visitors 7d (exclude converters)
    └── Ad Set: Site Visitors 30d (exclude 7d + converters)
```

### Targeting Configuration

| Campaign | Audience Type | Targeting Details | Est. Audience Size | Exclusions |
|----------|-------------|-------------------|-------------------|------------|
| Brand Search | Hot | Brand keywords + brand + product terms | 2,000 monthly searches | Existing customers |
| Non-Brand Search | Warm | "api integration platform", "data connector tool", "etl alternative" + variants | 15,000 monthly searches | Brand terms, irrelevant queries via negative list |
| Display Remarketing | Warm | Site visitors via Google tag | 8,000 monthly visitors | Converters, employees |

### Bidding Strategy

| Campaign | Strategy | Daily Budget | Bid Cap/Target | Rationale |
|----------|----------|-------------|----------------|-----------|
| Brand Search | Manual CPC | $75 | $4.50 CPC | Low volume, high intent — maintain control |
| Non-Brand Search | Target CPA | $500 | $180 CPA | 6 months of conversion data enables algorithm optimisation |
| Display Remarketing | Target CPA | $67 | $120 CPA | Retargeting audiences are smaller, warmer — lower CPA target |

### Creative Specifications

| Ad Format | Dimensions | Character Limits | Variants Needed | Key Message |
|-----------|-----------|-----------------|----------------|-------------|
| Responsive Search Ad | N/A (text) | Headlines: 30 chars x 15, Descriptions: 90 chars x 4 | 3 per ad group | "150+ Pre-Built API Connectors — Set Up in 10 Minutes" |
| Display Banner | 300x250, 728x90, 160x600 | N/A | 3 sizes x 2 variants | Connector marketplace visual + demo CTA |

## Platform: LinkedIn

### Account Structure

```
DataBridge Campaign Group: Q4 Connector Launch
├── Campaign: Connectors - Lead Gen - Engineering Managers
│   └── 4 Sponsored Content ads (demo request Lead Gen Form)
├── Campaign: Connectors - Lead Gen - Data Engineers
│   └── 4 Sponsored Content ads (demo request Lead Gen Form)
└── Campaign: Connectors - Retargeting - Website
    └── 3 Sponsored Content ads (case study + demo CTA)
```

### Targeting Configuration

| Campaign | Audience Type | Targeting Details | Est. Audience Size | Exclusions |
|----------|-------------|-------------------|-------------------|------------|
| Engineering Managers | Cold | Title: Engineering Manager, Head of Data, VP Engineering + Company Size: 200-2000 + Industry: SaaS, Fintech, Healthcare | 85,000 | Existing customers, competitors |
| Data Engineers | Cold | Title: Data Engineer, Senior Data Engineer + Skills: ETL, API Integration, Data Pipeline + Company Size: 200-2000 | 120,000 | Existing customers, competitors |
| Retargeting | Warm | Website visitors (LinkedIn Insight Tag) + Matched audiences from CRM | 3,000 | Converters |

### Bidding Strategy

| Campaign | Strategy | Daily Budget | Bid Cap/Target | Rationale |
|----------|----------|-------------|----------------|-----------|
| Engineering Managers | Manual CPC | $120 | $12 CPC | Building data — manual control for 2 more months |
| Data Engineers | Manual CPC | $120 | $8 CPC | Larger audience, lower seniority — lower CPC expected |
| Retargeting | Maximum Delivery | $50 | N/A | Small warm audience — maximise reach within budget |

### Creative Specifications

| Ad Format | Dimensions | Character Limits | Variants Needed | Key Message |
|-----------|-----------|-----------------|----------------|-------------|
| Sponsored Content (Single Image) | 1200x627 | Intro: 150 chars, Headline: 70 chars | 4 per campaign | "150+ connectors. 10-minute setup. SOC 2 certified." |
| Lead Gen Form | N/A | 4-5 fields max | 1 per campaign | First name, last name, work email, company, title |

## Platform: Meta (Retargeting Only)

### Account Structure

```
DataBridge Account
└── Campaign: Connectors - Conversions - Retargeting
    ├── Ad Set: Website Visitors 7d (exclude converters)
    │   └── 3 ads (image + video mix)
    ├── Ad Set: Website Visitors 30d (exclude 7d + converters)
    │   └── 3 ads (case study + social proof)
    └── Ad Set: Pricing Page Visitors 14d (exclude converters)
        └── 3 ads (direct demo offer + urgency)
```

### Targeting Configuration

| Campaign | Audience Type | Targeting Details | Est. Audience Size | Exclusions |
|----------|-------------|-------------------|-------------------|------------|
| Retargeting 7d | Warm | Facebook Pixel — all site visitors, last 7 days | 2,000 | Converters, employees |
| Retargeting 30d | Warm | Facebook Pixel — all site visitors, 8-30 days | 5,000 | 7d visitors, converters |
| Pricing Retargeting | Hot | Facebook Pixel — /pricing and /connectors visitors, last 14 days | 800 | Converters |

## Retargeting Sequence

| Stage | Audience | Window | Frequency Cap | Platform | Creative Focus |
|-------|----------|--------|---------------|----------|----------------|
| 1 | All site visitors | 1-7 days | 3/day | Google Display + Meta | "150+ connectors ready to deploy" — value prop reminder |
| 2 | Feature/pricing page visitors | 8-30 days | 2/day | Meta + LinkedIn | Customer case study: "How [Company] connected 40 APIs in one afternoon" |
| 3 | Demo page visitors who didn't convert | 1-14 days | 4/day | Google Display + Meta | "Book your demo — see your data flowing in 10 minutes" + calendar link |
| 4 | Lapsed visitors (31-90d) | 31-90 days | 1/day | Meta | "New: 50 connectors added this quarter" — feature refresh |

## Measurement Plan

| KPI | Target | Review Cadence | Optimisation Trigger |
|-----|--------|---------------|---------------------|
| Cost per Demo Request | $376 blended | Weekly | Pause ad groups above $500 CPL after 14 days |
| ROAS | 3.0x blended | Biweekly | Reallocate from channels below 1.5x after 30 days |
| Demo-to-Opportunity Rate | 40% | Monthly | If below 30%, review lead quality by source |
| Click-Through Rate | 2%+ (Search), 0.5%+ (Social) | Weekly | Refresh creative when CTR drops 20% from peak |

## Recommendations

| Priority | Recommendation | Owner | Deadline |
|----------|---------------|-------|----------|
| P1 | Install LinkedIn Insight Tag and Meta Pixel on all pages before campaign launch | Engineering / Marketing Ops | 1 week pre-launch |
| P1 | Create landing page variant for LinkedIn traffic with Lead Gen Form fallback | Demand Gen + Design | 1 week pre-launch |
| P2 | Build negative keyword list (500+ terms) for Google non-brand campaigns | Demand Gen Manager | Launch day |
| P3 | Prepare 3 customer case studies for retargeting creative rotation | Content Marketer | 2 weeks post-launch |

## Appendices

### A. Methodology

Campaign plan generated using ad-campaign-builder framework with 70/20/10 budget allocation model. Platform selection based on 6 months of Google data (proven), 2 months of LinkedIn data (scaling), and ICP research for Meta (experiment). Bidding strategies selected per campaign maturity decision tree. Retargeting sequence follows 4-stage framework.

### B. Supporting Data

Historical Google ROAS: 3.2x (6-month average). LinkedIn ROAS: 1.6x (2-month average, trending up from 1.2x month 1). Estimated demo request volume by platform: Google 51 (at $378 CAC), LinkedIn 25 (at $350 CAC), Meta 17 (at $412 CAC). Total projected: 93 demo requests at $376 blended CAC.
