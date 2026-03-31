# Lead Scoring Model Builder — Example Input

## Scenario

Meridian AI's sales team is rejecting 55% of MQLs as unqualified. The Marketing Ops Manager needs to build a calibrated lead scoring model targeting mid-market compliance and risk teams. The ICP is: VP/Director of Compliance or Risk at fintechs or healthcare companies, 51-500 employees, US-based. The model needs to incorporate product-specific behavioral signals (free trial started, integration connected) and output scored versions of 3 sample leads.

## Input JSON

```json
{
  "company_name": "Meridian AI",
  "icp": "VP/Director of Compliance or Risk at fintech or healthcare companies, 51-500 employees, US-based",
  "mql_threshold": 50,
  "sql_threshold": 75,
  "custom_behavioral_signals": [
    {"signal": "free_trial_started", "points": 30},
    {"signal": "integration_connected", "points": 20},
    {"signal": "invited_teammate", "points": 15},
    {"signal": "viewed_compliance_use_case", "points": 8}
  ],
  "sample_leads": [
    {
      "name": "Rachel Torres",
      "company_size_fit": "ideal",
      "role_fit": "ideal",
      "demo_request": false,
      "pricing_page": true,
      "content_download": true,
      "free_trial_started": true,
      "integration_connected": false,
      "invited_teammate": false,
      "viewed_compliance_use_case": true,
      "free_email": false,
      "competitor": false
    },
    {
      "name": "Kevin Liu",
      "company_size_fit": "acceptable",
      "role_fit": "acceptable",
      "demo_request": false,
      "pricing_page": false,
      "content_download": true,
      "free_trial_started": false,
      "integration_connected": false,
      "invited_teammate": false,
      "viewed_compliance_use_case": false,
      "free_email": true,
      "competitor": false
    },
    {
      "name": "Sarah Park",
      "company_size_fit": "ideal",
      "role_fit": "ideal",
      "demo_request": true,
      "pricing_page": true,
      "content_download": true,
      "free_trial_started": true,
      "integration_connected": true,
      "invited_teammate": true,
      "viewed_compliance_use_case": true,
      "free_email": false,
      "competitor": false
    }
  ]
}
```
