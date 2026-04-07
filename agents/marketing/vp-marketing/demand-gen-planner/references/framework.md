# Framework: demand-gen-planner

Defines the revenue-to-pipeline model, channel unit economics benchmarks, and MQL definition standards for building a quarterly demand generation plan.

## Revenue-to-Pipeline Waterfall Model

Work backward from revenue targets to lead volume using historical funnel conversion rates.

| Stage | Formula | Typical B2B SaaS Rate |
|-------|---------|----------------------|
| Closed-Won Revenue | Target | — |
| Pipeline Required | Revenue ÷ Win Rate | Win rate: 20–30% |
| Opportunities Required | Pipeline ÷ ASP | — |
| SQLs Required | Opps ÷ Opp Conversion | SQL→Opp: 50–70% |
| MQLs Required | SQLs ÷ MQL-SQL Rate | MQL→SQL: 20–40% |
| Leads Required | MQLs ÷ Lead-MQL Rate | Lead→MQL: 10–25% |

**Example**: $3M revenue target, 25% win rate, $50K ASP, 60% SQL→Opp, 30% MQL→SQL, 15% Lead→MQL:
- Pipeline needed: $12M
- Opps needed: 240
- SQLs needed: 400
- MQLs needed: 1,333
- Leads needed: 8,889

## Channel Unit Economics Benchmarks

Use as baseline for budget allocation. Adjust quarterly based on actual performance data.

| Channel | Typical CPL Range | MQL Conv. Rate | Notes |
|---------|------------------|----------------|-------|
| Paid Search (branded) | $30–$80 | 20–35% | High intent; volume limited |
| Paid Search (non-branded) | $80–$200 | 10–20% | Scalable; competitive |
| Paid Social (LinkedIn) | $60–$150 | 8–15% | B2B targeting premium |
| Paid Social (Meta/X) | $20–$60 | 4–10% | Lower intent; volume play |
| Content / SEO | $10–$40 | 5–15% | Long-term compounding asset |
| Email (owned list) | $5–$20 | 12–25% | Highest efficiency; list-size limited |
| Events / Webinars | $100–$300 | 15–30% | High intent; high cost-per-contact |
| Outbound / SDR-assisted | $150–$400 | 25–45% | High effort; strategic accounts |
| Partnerships / Referrals | $20–$80 | 20–40% | Quality varies by partner |

**CAC threshold**: Flag any channel where CAC exceeds 33% of ACV (annual contract value).
**LTV:CAC ratio target**: ≥ 3:1 at channel level for sustained investment.
**Payback period ceiling**: 18 months for growth-stage companies; 12 months post-Series C.

## Budget Allocation Model

| Allocation Category | Recommended % | Rationale |
|--------------------|---------------|-----------|
| Proven high-ROI channels | 50–60% | Double down on what converts |
| Emerging / testing channels | 15–20% | Identify tomorrow's proven channels |
| Content and SEO | 15–20% | Long-term compounding pipeline |
| Brand and awareness | 5–10% | Protects conversion rates across all channels |

## MQL Definition Standards

A well-formed MQL definition combines two dimensions: **Fit** (who they are) and **Engagement** (what they've done).

### Fit Dimensions (Firmographic)
| Dimension | Qualifying Criteria Examples |
|-----------|------------------------------|
| Company size | 50–5,000 employees |
| Industry | [Target verticals from ICP] |
| Geography | [Target regions] |
| Title / function | Director+ in [target functions] |
| Tech stack | Uses [complementary tools] |

### Engagement Signals
| Signal | Points (example) | Notes |
|--------|-----------------|-------|
| Demo request | 100 | Immediate MQL regardless of fit score |
| Free trial start | 80 | High intent |
| Pricing page visit | 40 | Clear buying signal |
| Webinar attended (live) | 30 | Active engagement |
| Case study download | 25 | Decision-stage content |
| Whitepaper download | 15 | Consideration-stage content |
| Blog post (2+ visits) | 10 | Research behavior |
| Email click | 5 per click | Intent signal |

**MQL Threshold**: Fit score ≥ [X] AND Engagement score ≥ [Y], OR any single high-intent action (demo request, trial).

### MQL-to-SQL Handoff SLA
| Metric | Standard |
|--------|----------|
| Sales response time to MQL | < 24 business hours |
| MQL review period | 5 business days max |
| Accepted / Rejected / Recycled categorization | Required for all MQLs |
| MQL-to-SQL target conversion rate | ≥ 25% |
| Monthly MQL quality review | Marketing + Sales joint session |

## Measurement Cadence

| Frequency | Metric | Owner | Threshold for Action |
|-----------|--------|-------|---------------------|
| Weekly | Leads, MQLs, spend | Demand Gen Manager | ±15% from plan |
| Weekly | CPL by channel | Demand Gen Manager | > 20% above benchmark |
| Monthly | SQLs, pipeline created | VP Marketing | ±10% from plan |
| Monthly | MQL→SQL conversion rate | Marketing Ops | Drop below 25% |
| Quarterly | CAC by channel, LTV:CAC | VP Marketing | CAC > 33% ACV |
| Quarterly | Plan vs. actuals full review | VP Marketing + CBO | Full replan if >20% off |
