# Due Diligence Coordinator — Example Input

## Scenario

Meridian AI is in Series A diligence with Sequoia Capital. Sequoia sent a 20-item diligence checklist two weeks ago. The IR Manager is tracking progress and needs a status report before the weekly diligence call. Some items are complete, some in progress, and two are blocked pending legal input.

## Input JSON

```json
{
  "company_name": "Meridian AI",
  "investor_name": "Sequoia Capital",
  "target_close_date": "2026-04-30",
  "items": [
    {"item": "Certificate of incorporation and amendments", "category": "corporate", "owner": "General Counsel", "status": "complete", "days_outstanding": 0},
    {"item": "Fully diluted cap table", "category": "corporate", "owner": "General Counsel", "status": "complete", "days_outstanding": 0},
    {"item": "Board minutes last 24 months", "category": "corporate", "owner": "General Counsel", "status": "complete", "days_outstanding": 0},
    {"item": "All stockholder agreements", "category": "corporate", "owner": "General Counsel", "status": "in_progress", "days_outstanding": 10, "notes": "Locating early angel side letters"},
    {"item": "Audited financials FY2025", "category": "financials", "owner": "CFO", "status": "in_progress", "days_outstanding": 14, "notes": "Audit in process, expected April 15"},
    {"item": "Financial model with assumptions", "category": "financials", "owner": "CFO", "status": "complete", "days_outstanding": 0},
    {"item": "Burn and runway analysis", "category": "financials", "owner": "CFO", "status": "complete", "days_outstanding": 0},
    {"item": "Revenue recognition policy", "category": "financials", "owner": "CFO", "status": "blocked", "days_outstanding": 7, "notes": "Blocked: need external accountant sign-off"},
    {"item": "Top 10 customer contracts", "category": "commercial", "owner": "VP Sales", "status": "complete", "days_outstanding": 0},
    {"item": "Standard MSA and order form", "category": "commercial", "owner": "General Counsel", "status": "complete", "days_outstanding": 0},
    {"item": "Churn analysis by cohort", "category": "commercial", "owner": "VP Customer Success", "status": "in_progress", "days_outstanding": 5},
    {"item": "3 customer reference calls", "category": "customer", "owner": "VP Customer Success", "status": "in_progress", "days_outstanding": 8, "notes": "2 of 3 scheduled"},
    {"item": "Architecture and infrastructure overview", "category": "product_tech", "owner": "CTO", "status": "complete", "days_outstanding": 0},
    {"item": "Security and compliance documentation", "category": "product_tech", "owner": "CTO", "status": "in_progress", "days_outstanding": 9},
    {"item": "Open source licence audit", "category": "product_tech", "owner": "CTO", "status": "blocked", "days_outstanding": 12, "notes": "Blocked: audit tool licence not provisioned"},
    {"item": "IP ownership and assignment confirmations", "category": "ip", "owner": "General Counsel", "status": "complete", "days_outstanding": 0},
    {"item": "Key employee agreements", "category": "team_hr", "owner": "COO", "status": "complete", "days_outstanding": 0},
    {"item": "Non-competes and IP assignments — all employees", "category": "team_hr", "owner": "COO", "status": "in_progress", "days_outstanding": 6},
    {"item": "Privacy policy and terms of service", "category": "regulatory", "owner": "General Counsel", "status": "complete", "days_outstanding": 0},
    {"item": "GDPR and CCPA compliance documentation", "category": "regulatory", "owner": "General Counsel", "status": "pending", "days_outstanding": 14}
  ]
}
```
