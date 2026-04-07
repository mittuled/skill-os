# Board Materials Coordinator — Example Input

## Scenario

Meridian AI's Q1 2026 board meeting is on April 15. Today is March 31 — 15 days away. The IR Manager is coordinating materials. The CFO has finished the financial sections; the CTO is traveling and can deliver the engineering update on April 6; the CPO has a draft product update pending final data; the CEO hasn't started the executive summary yet (writes it last).

## Input JSON

```json
{
  "company_name": "Meridian AI",
  "meeting_date": "2026-04-15",
  "current_date": "2026-03-31",
  "directors": [
    {"name": "Jane Wu", "firm": "Sequoia Capital", "role": "Lead Investor"},
    {"name": "Marcus Reed", "firm": "Independent", "role": "Angel"},
    {"name": "Sarah Kim", "firm": "Independent", "role": "Independent Director"}
  ],
  "logistics": {
    "format": "Hybrid",
    "video": "Zoom — link sent to directors",
    "in_person": "Conference Room A, 47 Market St Floor 12",
    "dial_in": "+1-800-555-0199 code 4421"
  },
  "sections": [
    {
      "key": "executive_summary",
      "owner": "CEO",
      "status": "pending",
      "notes": "CEO writes last — after all other sections are in"
    },
    {
      "key": "financial_review",
      "owner": "CFO",
      "status": "complete"
    },
    {
      "key": "kpi_dashboard",
      "owner": "CFO",
      "status": "complete"
    },
    {
      "key": "product_update",
      "owner": "CPO",
      "status": "in_progress",
      "notes": "Draft ready; waiting on activation rate data from analytics team"
    },
    {
      "key": "engineering_update",
      "owner": "CTO",
      "status": "pending",
      "notes": "CTO traveling until April 5; commits to delivering April 6"
    },
    {
      "key": "sales_update",
      "owner": "VP Sales",
      "status": "complete"
    },
    {
      "key": "strategy_discussion",
      "owner": "CEO / CFO",
      "status": "in_progress",
      "notes": "Series B strategy discussion outline in progress"
    },
    {
      "key": "consent_items",
      "owner": "General Counsel",
      "status": "complete",
      "notes": "VP Engineering compensation approval — consent package ready"
    }
  ]
}
```
