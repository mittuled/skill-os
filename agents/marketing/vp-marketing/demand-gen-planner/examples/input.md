# Scenario: Q3 Demand Gen Plan for B2B SaaS Company

A B2B SaaS company is building its Q3 demand generation plan. The CBO has set a $1.8M quarterly pipeline target. Average deal size is $45,000 and the team has $180,000 in demand gen budget. The marketing team wants to allocate across paid search, content/SEO, paid social, and webinars.

## Input Parameters

```json
{
  "quarterly_revenue_target": 450000,
  "avg_deal_size": 45000,
  "channel_budget_total": 180000,
  "channels": ["paid_search", "content_seo", "paid_social", "webinars"],
  "dashboard_owner": "marketing_ops_manager",
  "mql_definition": {
    "behavioral_criteria": [
      "Visited pricing page 2+ times",
      "Downloaded case study or ROI calculator",
      "Attended live product demo"
    ],
    "firmographic_criteria": [
      "Company size: 100–2000 employees",
      "Industry: SaaS, FinTech, or HealthTech",
      "Title: VP, Director, or C-level"
    ],
    "lead_score_threshold": 45,
    "handoff_sla_hours": 4
  },
  "funnel_overrides": {
    "mql_to_sql_pct": 35,
    "opportunity_to_close_pct": 28
  }
}
```
