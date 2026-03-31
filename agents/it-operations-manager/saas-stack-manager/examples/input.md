# SaaS Stack Manager — Example Input

## Scenario

Meridian AI is approaching its annual SaaS budget review. The IT Manager is auditing all 8 active SaaS tools to identify underutilised seats, consolidation opportunities, and upcoming renewals that need review before auto-renew. Several tools were purchased for headcount that never materialised.

## Input JSON

```json
{
  "company_name": "Meridian AI",
  "action": "audit",
  "tools": [
    {
      "tool_name": "GitHub",
      "category": "engineering",
      "licensed_seats": 22,
      "active_seats": 18,
      "annual_cost_usd": 4840,
      "days_to_renewal": 120,
      "owner": "CTO",
      "notes": "4 seats from departures not yet removed"
    },
    {
      "tool_name": "Slack",
      "category": "communication",
      "licensed_seats": 25,
      "active_seats": 22,
      "annual_cost_usd": 7500,
      "days_to_renewal": 45,
      "owner": "IT",
      "notes": "Renewal in 45 days — downgrade to 22 seats"
    },
    {
      "tool_name": "Notion",
      "category": "product",
      "licensed_seats": 25,
      "active_seats": 19,
      "annual_cost_usd": 4500,
      "days_to_renewal": 200,
      "owner": "CPO",
      "notes": ""
    },
    {
      "tool_name": "Salesforce",
      "category": "sales",
      "licensed_seats": 10,
      "active_seats": 3,
      "annual_cost_usd": 18000,
      "days_to_renewal": 60,
      "owner": "VP Sales",
      "notes": "Purchased for sales team that hasn't fully hired yet. 7 unused seats."
    },
    {
      "tool_name": "Figma",
      "category": "design",
      "licensed_seats": 5,
      "active_seats": 5,
      "annual_cost_usd": 2250,
      "days_to_renewal": 180,
      "owner": "Head of Design",
      "notes": ""
    },
    {
      "tool_name": "Zoom",
      "category": "communication",
      "licensed_seats": 25,
      "active_seats": 22,
      "annual_cost_usd": 4500,
      "days_to_renewal": 75,
      "owner": "IT",
      "notes": ""
    },
    {
      "tool_name": "1Password Teams",
      "category": "security",
      "licensed_seats": 25,
      "active_seats": 22,
      "annual_cost_usd": 1980,
      "days_to_renewal": 90,
      "owner": "IT",
      "notes": ""
    },
    {
      "tool_name": "Mixpanel",
      "category": "analytics",
      "licensed_seats": 10,
      "active_seats": 2,
      "annual_cost_usd": 8400,
      "days_to_renewal": 30,
      "owner": "Head of Growth",
      "notes": "Only Head of Growth and one PM actively use. Others lost access password."
    }
  ]
}
```
