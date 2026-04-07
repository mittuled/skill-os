# Revenue Tooling Readiness — Example Input

## Scenario

A SaaS company is launching a new Enterprise pricing tier in 5 days. The RevOps team is running a pre-launch tooling validation to confirm that CRM, billing, and analytics are ready to process Enterprise contracts before the first deal closes.

## Input JSON

```json
{
  "go_live_date": "2026-04-05",
  "e2e_transaction_passed": false,
  "tools": [
    {
      "name": "crm",
      "criteria_passed": [
        "data_flowing",
        "automations_firing",
        "user_access_configured"
      ],
      "issues": ["Revenue reports showing $0 for Enterprise tier deals — pipeline field mapping error"]
    },
    {
      "name": "billing",
      "criteria_passed": [
        "test_invoice_sent",
        "payment_method_configured",
        "subscription_lifecycle_tested"
      ],
      "issues": ["Revenue recognition rules not configured for Enterprise annual prepay — will default to point-of-sale"]
    },
    {
      "name": "analytics",
      "criteria_passed": [
        "dashboards_populated",
        "data_refresh_scheduled",
        "kpi_definitions_confirmed"
      ],
      "issues": []
    }
  ]
}
```
