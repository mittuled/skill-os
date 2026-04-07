# Company Researcher — Example Input

## Scenario

An SDR is preparing to reach out to Deel, a global payroll and compliance platform that recently raised a Series D. The SDR needs a full company profile before crafting a personalized enterprise outreach sequence targeting their VP of Operations.

## Input JSON

```json
{
  "company_name": "Deel",
  "dimensions": {
    "company_size": {
      "summary": "2,500 employees globally; HQ San Francisco; offices in 15 countries; 40% headcount growth YoY",
      "confidence": "high",
      "sources": ["LinkedIn company page", "Crunchbase", "TechCrunch profile"]
    },
    "industry": {
      "summary": "HR Tech / Global Payroll & Compliance — vertical: remote workforce management; NAICS 541612",
      "confidence": "high",
      "sources": ["company website", "G2 category listing"]
    },
    "funding": {
      "summary": "Total raised: $679M. Series D ($425M) closed Nov 2023 at $12B valuation. Investors: Andreessen Horowitz, Y Combinator, Coatue.",
      "confidence": "high",
      "sources": ["Crunchbase", "TechCrunch Series D announcement"]
    },
    "tech_stack": {
      "summary": "Salesforce CRM, Workday for internal HR, AWS infrastructure, React frontend, Stripe for payments processing",
      "confidence": "medium",
      "sources": ["BuiltWith", "engineering job postings (React, AWS)", "Stripe partnership announcement"],
      "gap_impact": "Internal tooling stack incomplete — may use competitors in specific segments",
      "gap_remediation": "Ask engineering contacts at Deel about tooling; check recent integration announcements"
    },
    "growth_trajectory": {
      "summary": "120% revenue growth YoY (est.); entering APAC with Singapore and Australia offices; hiring surge in compliance and legal",
      "confidence": "medium",
      "sources": ["CEO LinkedIn posts", "job postings analysis", "press releases"]
    },
    "competitive_landscape": {
      "summary": "Direct competitors: Remote.com, Rippling, Papaya Global. Deel differentiates on contractor-to-employee conversion speed and 150+ country coverage.",
      "confidence": "high",
      "sources": ["G2 competitor comparison", "industry analyst report", "Deel website"]
    },
    "leadership_team": {
      "summary": "Alex Bouaziz (CEO, co-founder), Shuo Wang (President, co-founder), Nadia Bouraked (CPO). VP Ops: Sarah Kim (joined Jan 2024 from Stripe)",
      "confidence": "medium",
      "sources": ["LinkedIn", "company website", "TechCrunch interview"],
      "gap_impact": "VP Sales contact unknown",
      "gap_remediation": "Search LinkedIn for Director/VP Sales at Deel; check recent conference speaker lists"
    },
    "recent_news": {
      "summary": "Nov 2023: Series D $425M raised. Dec 2023: Partnership with HSBC for embedded banking. Jan 2024: Launched Deel HR product for internal workforce. Feb 2024: Acquired Assemble (compensation management)",
      "confidence": "high",
      "sources": ["TechCrunch", "Deel press releases", "PR Newswire"]
    }
  },
  "buying_triggers": [
    {
      "description": "Series D $425M raised — budget available for enterprise tooling",
      "urgency": "immediate",
      "evidence": "TechCrunch Series D announcement Nov 2023"
    },
    {
      "description": "Acquired Assemble (comp management) — integration and workflow needs",
      "urgency": "immediate",
      "evidence": "PR Newswire Feb 2024 acquisition announcement"
    },
    {
      "description": "APAC expansion — need compliance tools in new geographies",
      "urgency": "near_term",
      "evidence": "Singapore/Australia office announcements on LinkedIn"
    },
    {
      "description": "New VP Ops (Sarah Kim, joined Jan 2024) — new exec evaluating vendors",
      "urgency": "near_term",
      "evidence": "LinkedIn profile change, Deel website leadership page"
    }
  ],
  "recommended_outreach_approach": "Lead with APAC expansion compliance angle to VP Ops Sarah Kim (new exec, high openness to change); reference Series D and Assemble acquisition to anchor budget conversation"
}
```
