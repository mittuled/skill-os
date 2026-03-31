# CRM Setup v1 — Example Input

## Scenario

A 25-person SaaS startup has been tracking deals in a shared Google Sheet for 8 months and has just subscribed to HubSpot CRM. The RevOps lead is configuring the CRM v1 with pipeline stages, deal fields, and automations before onboarding the 5-person sales team next week.

## Input JSON

```json
{
  "crm_platform": "HubSpot CRM",
  "pipeline_stages": [
    "lead_qualification",
    "discovery",
    "technical_evaluation",
    "proposal",
    "negotiation",
    "closed_won",
    "closed_lost"
  ],
  "deal_fields": [
    "deal_value",
    "close_date",
    "lead_source",
    "product_line",
    "deal_owner"
  ],
  "automations": [
    "stage_transition_notification",
    "overdue_deal_alert",
    "new_lead_assignment"
  ],
  "integrations": [
    "email_calendar",
    "marketing_automation"
  ],
  "end_to_end_test_passed": false,
  "data_migration_status": "in_progress"
}
```
