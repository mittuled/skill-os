# Scenario: Q3 Marketing Audit for Series B SaaS Company

Perform a comprehensive marketing audit for CloudSync, a Series B SaaS company ($8M ARR, $4M annual marketing budget) selling to mid-market IT teams.

## Available Data

- **Brand Health**: Unaided awareness at 18% in ICP (up from 12% Q2). NPS 32. Brand guidelines v2.0 exist but only 65% of materials audited follow them. No share-of-voice tracking in place.
- **Channel Performance**: Google Ads ROAS 3.8x, LinkedIn Ads ROAS 1.4x, organic search drives 28% of MQLs. Total CAC $186 (blended). Attribution model is last-touch only.
- **Content Quality**: 45 blog posts published in Q3. Top 5 by traffic are SEO-optimised comparison guides. Bottom 10 are company news posts with near-zero engagement. No content-to-pipeline attribution. No editorial calendar — topics chosen ad hoc by the content team.
- **Funnel Efficiency**: 2,400 MQLs, 480 SQLs (20% conversion), 96 opportunities (20% conversion), 29 closed-won (30% close rate). Average deal size $18K. MQL-to-close cycle is 68 days. No lead scoring model — SDRs manually qualify all MQLs.
- **MarTech Stack**: HubSpot Marketing Hub (Professional), Salesforce CRM, Google Analytics 4, Semrush. HubSpot feature adoption estimated at 40% (email, forms, basic workflows active; lead scoring, ABM, A/B testing, social tools unused). CRM sync breaks approximately twice per month.

## Scoring Input (JSON)

```json
{
  "brand_health": 6,
  "channel_performance": 7,
  "content_quality": 5,
  "funnel_efficiency": 7,
  "martech_utilisation": 4
}
```
