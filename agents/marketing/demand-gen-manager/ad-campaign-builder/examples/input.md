# Scenario: Q4 Product Launch Campaign for Data Integration Platform

Build a multi-platform paid advertising campaign for DataBridge, a Series A data integration platform ($3M ARR) launching a new API connector marketplace. Target: mid-market data engineers and engineering managers.

## Campaign Parameters

- **Objective**: Lead generation (demo requests)
- **Monthly budget**: $35,000
- **Platforms**: Google Search, LinkedIn, Meta (retargeting only)
- **ICP**: Data engineers (L3-L5) and engineering managers at companies with 200-2000 employees in SaaS, fintech, and healthcare tech
- **Product**: API connector marketplace — 150+ pre-built connectors, 10-minute setup, SOC 2 compliant
- **Current state**: Google Search running for 6 months (ROAS 3.2x), LinkedIn tested for 2 months (ROAS 1.6x), Meta never used
- **Landing page**: databridge.io/connectors (conversion event: demo request form)

## Generation Input (JSON)

```json
{
  "objective": "lead_gen",
  "budget": 35000,
  "platforms": ["google", "linkedin", "meta"],
  "tiers": {"google": "proven", "linkedin": "scaling", "meta": "experiment"},
  "icp": {
    "titles": ["Data Engineer", "Senior Data Engineer", "Engineering Manager", "Head of Data"],
    "company_size": "200-2000 employees",
    "industries": ["SaaS", "Fintech", "Healthcare Tech"],
    "geography": "North America"
  }
}
```
