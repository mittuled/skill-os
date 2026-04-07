# Martech Stack Manager — Example Input

## Scenario

Meridian AI's marketing team has accumulated 7 tools over 18 months with no formal audit. The VP of Marketing asks for a stack audit before the Q2 budget review. HubSpot and Salesforce are not syncing properly; two email tools overlap; one analytics platform is barely used.

## Input JSON

```json
{
  "company_name": "Meridian AI",
  "action": "audit",
  "tools": [
    {
      "tool_name": "HubSpot",
      "category": "marketing_automation",
      "annual_cost_usd": 18000,
      "utilisation_rate": 0.75,
      "crm_integration_status": "broken",
      "days_to_renewal": 65,
      "owner": "Marketing Ops",
      "notes": "HubSpot-Salesforce sync broke 3 weeks ago. Leads not flowing to Salesforce."
    },
    {
      "tool_name": "Salesforce",
      "category": "crm",
      "annual_cost_usd": 18000,
      "utilisation_rate": 0.35,
      "crm_integration_status": "broken",
      "days_to_renewal": 60,
      "owner": "VP Sales",
      "notes": "Underused by sales team. Only 3 of 10 licences active."
    },
    {
      "tool_name": "Mailchimp",
      "category": "email",
      "annual_cost_usd": 3600,
      "utilisation_rate": 0.50,
      "crm_integration_status": "not_integrated",
      "days_to_renewal": 120,
      "owner": "Demand Gen",
      "redundant_with": "HubSpot (email module)",
      "notes": "Purchased before HubSpot. HubSpot now covers email sending."
    },
    {
      "tool_name": "Google Analytics 4",
      "category": "analytics",
      "annual_cost_usd": 0,
      "utilisation_rate": 0.90,
      "crm_integration_status": "active",
      "days_to_renewal": 365,
      "owner": "Marketing Ops",
      "notes": "Free tier. Well-configured."
    },
    {
      "tool_name": "Mixpanel",
      "category": "analytics",
      "annual_cost_usd": 8400,
      "utilisation_rate": 0.20,
      "crm_integration_status": "not_integrated",
      "days_to_renewal": 30,
      "owner": "Head of Growth",
      "redundant_with": "Google Analytics 4",
      "notes": "Only 2 of 10 seats used. Overlaps with GA4 for most use cases."
    },
    {
      "tool_name": "LinkedIn Ads",
      "category": "ads",
      "annual_cost_usd": 24000,
      "utilisation_rate": 0.80,
      "crm_integration_status": "active",
      "days_to_renewal": 365,
      "owner": "Demand Gen",
      "notes": "Core paid acquisition channel. Good utilisation."
    },
    {
      "tool_name": "Webflow",
      "category": "content",
      "annual_cost_usd": 2400,
      "utilisation_rate": 0.85,
      "crm_integration_status": "active",
      "days_to_renewal": 200,
      "owner": "Marketing",
      "notes": "Company website. Well-used."
    }
  ]
}
```
