# Revenue Model Operationaliser — Example Input

## Scenario

A B2B SaaS company is launching a new subscription-based product line alongside its existing one-time implementation service. Finance has flagged that the current CRM mixes both models in the same pipeline, causing revenue recognition errors. RevOps needs to define separate pipeline stage mappings for the subscription model.

## Input JSON

```json
{
  "model_type": "subscription",
  "recognition_method": "ratable",
  "pricing_tiers": [
    {"name": "Starter", "monthly_arr": 500, "annual_arr": 5400, "seats": 5},
    {"name": "Growth", "monthly_arr": 1500, "annual_arr": 16200, "seats": 20},
    {"name": "Enterprise", "monthly_arr": 5000, "annual_arr": 54000, "seats": "unlimited"}
  ],
  "pipeline_stage_mapping": [
    {
      "stage_name": "Lead Qualified",
      "entry_criteria": "BANT score ≥ 6.0 or inbound demo request",
      "exit_criteria": "Discovery call completed; ICP confirmed",
      "probability_pct": 10,
      "forecast_category": "pipeline",
      "required_fields": ["company_name", "deal_owner", "lead_source"]
    },
    {
      "stage_name": "Discovery",
      "entry_criteria": "Discovery call completed",
      "exit_criteria": "Pain confirmed; champion identified; next step agreed",
      "probability_pct": 20,
      "forecast_category": "pipeline",
      "required_fields": ["deal_value", "close_date", "product_line"]
    },
    {
      "stage_name": "Technical Evaluation",
      "entry_criteria": "AE confirmed technical fit; demo scheduled",
      "exit_criteria": "Technical sign-off from champion; no blocking objections",
      "probability_pct": 40,
      "forecast_category": "pipeline",
      "required_fields": ["contract_term", "seats_requested"]
    },
    {
      "stage_name": "Proposal Sent",
      "entry_criteria": "Pricing proposal sent to economic buyer",
      "exit_criteria": "Verbal agreement on pricing and terms",
      "probability_pct": 60,
      "forecast_category": "best_case",
      "required_fields": ["proposed_arr", "discount_pct"]
    },
    {
      "stage_name": "Negotiation",
      "entry_criteria": "Verbal agreement; legal/procurement review underway",
      "exit_criteria": "Contract signed by all parties",
      "probability_pct": 80,
      "forecast_category": "commit",
      "required_fields": ["legal_review_status"]
    },
    {
      "stage_name": "Closed Won",
      "entry_criteria": "Contract signed",
      "exit_criteria": "N/A — terminal stage",
      "probability_pct": 100,
      "forecast_category": "closed",
      "required_fields": ["signed_arr", "subscription_start_date", "billing_frequency"]
    }
  ],
  "notes": "Separate pipeline from one-time implementation model. Finance requires subscription_start_date field for ratable recognition calculations."
}
```
