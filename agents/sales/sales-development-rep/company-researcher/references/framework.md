# 8-Dimension Firmographic Analysis Framework

Defines the research dimensions, data sources, scoring criteria, and buying trigger taxonomy used by the company-researcher skill.

## Dimensions

### 1. Company Size

| Attribute | Description | Primary Sources | Secondary Sources |
|-----------|-------------|-----------------|-------------------|
| Headcount | Total employee count and departmental breakdown | LinkedIn company page, Glassdoor | Job boards (aggregate posting volume), SEC filings |
| Headcount Trend | 6-month and 12-month growth/contraction rate | LinkedIn Insights, Glassdoor trends | News articles, layoff trackers |
| Office Locations | HQ and satellite offices with estimated size | Company website, Google Maps | Job postings (location fields), Glassdoor reviews |

### 2. Industry

| Attribute | Description | Primary Sources | Secondary Sources |
|-----------|-------------|-----------------|-------------------|
| Primary Vertical | Main industry classification | Company website, LinkedIn | Crunchbase, industry directories |
| Sub-Vertical | Niche within the vertical | Product pages, case studies | Analyst reports, G2 categorization |
| NAICS/SIC Codes | Standardized classification codes | SEC filings, D&B | Industry databases, government registries |

### 3. Funding

| Attribute | Description | Primary Sources | Secondary Sources |
|-----------|-------------|-----------------|-------------------|
| Total Raised | Cumulative funding across all rounds | Crunchbase, PitchBook | Press releases, SEC filings |
| Last Round | Most recent funding round details | Crunchbase, TechCrunch | Company blog, investor announcements |
| Investors | Lead and participating investors | Crunchbase, PitchBook | LinkedIn (investor connections), press |
| Runway Indicators | Burn rate signals (hiring velocity vs. revenue) | Job postings volume, headcount trends | Glassdoor reviews mentioning financial health |

### 4. Tech Stack

| Attribute | Description | Primary Sources | Secondary Sources |
|-----------|-------------|-----------------|-------------------|
| Frontend/Backend | Languages, frameworks, infrastructure | Job postings (required skills), BuiltWith | GitHub repos (if open-source), StackShare |
| Infrastructure | Cloud provider, deployment tools | Job postings, Wappalyzer | Conference talks, engineering blog posts |
| Business Tools | CRM, marketing automation, support tools | Integration pages, G2 reviews | Job postings (tool requirements), Glassdoor |
| Data Stack | Analytics, data warehouse, BI tools | Job postings, engineering blog | Conference presentations, open-source contributions |

### 5. Growth Trajectory

| Attribute | Description | Primary Sources | Secondary Sources |
|-----------|-------------|-----------------|-------------------|
| Hiring Velocity | New job postings per month, departments hiring | LinkedIn Jobs, Indeed | Glassdoor, company careers page |
| Revenue Estimates | ARR/revenue range estimates | SEC filings (if public), industry reports | Glassdoor salary data (inferring scale), news articles |
| Market Expansion | New geographies, verticals, or product lines | Press releases, product updates | Job postings in new locations, LinkedIn company updates |

### 6. Competitive Landscape

| Attribute | Description | Primary Sources | Secondary Sources |
|-----------|-------------|-----------------|-------------------|
| Direct Competitors | Companies competing for the same buyers | G2, Gartner, industry reports | Company website (comparison pages), SEO competitors |
| Market Position | Leader/challenger/niche per analyst frameworks | Gartner Magic Quadrant, Forrester Wave | G2 Grid, customer reviews |
| Differentiation | Key differentiators claimed by the company | Company website, sales collateral | Customer reviews, analyst commentary |

### 7. Leadership Team

| Attribute | Description | Primary Sources | Secondary Sources |
|-----------|-------------|-----------------|-------------------|
| C-Suite | CEO, CTO, CFO with tenure and background | LinkedIn, company website | Crunchbase, press releases |
| VP-Level | VPs in departments relevant to the product | LinkedIn | Conference speaker bios, podcast appearances |
| Board Members | Board composition and investor representation | Crunchbase, SEC filings | LinkedIn, company website |

### 8. Recent News

| Attribute | Description | Primary Sources | Secondary Sources |
|-----------|-------------|-----------------|-------------------|
| Press Releases | Official company announcements in last 12 months | Company newsroom, PR Newswire | Google News, industry publications |
| Product Launches | New products or major feature releases | Company blog, Product Hunt | Tech press, G2 new product listings |
| M&A Activity | Acquisitions, mergers, or divestiture signals | Crunchbase, SEC filings | News articles, LinkedIn announcements |
| Partnerships | Strategic partnerships or integration announcements | Company blog, partner directories | Press releases, LinkedIn posts |

## Data Confidence Scoring

| Confidence Level | Criteria | Score Multiplier |
|-----------------|----------|-----------------|
| High | Verified from primary source within 90 days | 1.0 |
| Medium | Secondary source or data is 91-180 days old | 0.7 |
| Low | Single unverified source or older than 180 days | 0.4 |

**Overall Data-Confidence Score** = (Σ dimension confidence scores) / 8, expressed as a percentage.

## Buying Trigger Taxonomy

| Trigger Category | Examples | Urgency |
|-----------------|----------|---------|
| Funding Event | Series B+ raised in last 6 months, IPO filing | Immediate |
| Leadership Change | New CTO/VP Engineering hired in last 3 months | Immediate |
| Technology Migration | Job postings for new stack, RFP for platform change | Immediate |
| Geographic Expansion | New office announced, job postings in new regions | Near-term |
| Competitive Pressure | Competitor acquisition, market share shift | Near-term |
| Regulatory Change | New compliance requirement affecting the industry | Near-term |
| Growth Milestone | Headcount doubled in 12 months, new product line | Long-term |
| Industry Trend | Sector-wide adoption of related technology | Long-term |

**Urgency Classification**:
- **Immediate**: Action likely within 0-3 months; outreach should happen this week
- **Near-term**: Action likely within 3-6 months; begin relationship-building now
- **Long-term**: Action likely within 6-12 months; add to nurture sequence
