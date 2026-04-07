# Scenario: Sizing the Market for AI-Powered Code Review Tools

The analytics lead is sizing the market for an AI code review product targeting software engineering teams at companies with 10+ engineers.

## Input Parameters

```json
{
  "market_name": "AI-Powered Code Review Tools",
  "sizing_date": "2026-03-31",
  "confidence": "medium",
  "tam_inputs": {
    "description": "All companies globally with software engineering teams",
    "units": 5000000,
    "arpu_usd": 1200,
    "sources": ["IDC Software Developer Population Report 2025", "LinkedIn workforce data"]
  },
  "sam_inputs": {
    "description": "English-language companies with 10-5000 engineers in NA/EU/ANZ",
    "units": 450000,
    "arpu_usd": 2400,
    "sources": ["LinkedIn company size filters", "Crunchbase funded company data"]
  },
  "som_inputs": {
    "description": "Reachable via PLG and direct sales in 3 years given current GTM capacity",
    "units": 2500,
    "arpu_usd": 3600,
    "sources": ["Current CAC and sales capacity analysis"]
  },
  "assumptions": [
    "ARPU based on $100/dev/month for 10-person avg team at SAM level",
    "SOM assumes 30% market growth and 1% SAM capture rate in 3 years",
    "TAM ARPU lower as it includes smaller companies with lower willingness to pay"
  ]
}
```
