# First Sales Process Builder — Example Input

## Scenario

A 20-person SaaS company has been closing its first enterprise deals through founder-led heroics. They've hired a Sales Manager and 3 AEs. The Sales Manager needs to design the first repeatable mid-market sales process before bringing on more reps.

## Input JSON

```json
{
  "motion_type": "mid_market",
  "qualification_framework": "MEDDIC",
  "pipeline_stages": [
    {
      "name": "Lead Qualified",
      "entry_criterion": "BANT/MEDDIC score ≥ 6.0 or inbound demo request from ICP company",
      "exit_criterion": "Discovery call scheduled; pain acknowledged by prospect",
      "probability_pct": 10,
      "required_activities": ["Research company profile", "Send personalized outreach", "Confirm meeting time"],
      "qualification_gates": ["ICP fit confirmed", "Decision-maker or champion identified"],
      "avg_days_target": 3
    },
    {
      "name": "Discovery",
      "entry_criterion": "Discovery call completed",
      "exit_criterion": "Pain quantified; economic buyer identified; next step agreed",
      "probability_pct": 20,
      "required_activities": ["Discovery call using question bank", "Pain quantification worksheet", "Stakeholder map draft"],
      "qualification_gates": ["Pain identified and quantified", "Decision timeline confirmed"],
      "avg_days_target": 7
    },
    {
      "name": "Technical Evaluation",
      "entry_criterion": "Discovery complete; AE confirmed technical fit",
      "exit_criterion": "Technical sign-off from champion; no blocking objections",
      "probability_pct": 40,
      "required_activities": ["Custom demo", "SE technical review", "POC scoping (if required)"],
      "qualification_gates": ["Decision criteria confirmed", "Champion identified and active"],
      "avg_days_target": 14
    },
    {
      "name": "Proposal",
      "entry_criterion": "Technical sign-off; pricing approved by Sales Manager",
      "exit_criterion": "Verbal agreement on pricing and terms from economic buyer",
      "probability_pct": 65,
      "required_activities": ["Proposal document sent", "Pricing review with Sales Manager", "Mutual action plan agreed"],
      "qualification_gates": ["Economic buyer engaged", "Decision process mapped", "Timeline confirmed"],
      "avg_days_target": 10
    },
    {
      "name": "Negotiation",
      "entry_criterion": "Verbal agreement; legal or procurement review initiated",
      "exit_criterion": "Contract signed by all parties",
      "probability_pct": 85,
      "required_activities": ["Contract sent", "Legal review coordination", "Procurement checklist completion"],
      "qualification_gates": ["Procurement requirements met", "Legal review complete"],
      "avg_days_target": 14
    },
    {
      "name": "Closed Won",
      "entry_criterion": "Contract signed",
      "exit_criterion": "N/A — terminal stage; CS handoff triggered",
      "probability_pct": 100,
      "required_activities": ["Log deal in CRM", "Trigger CS onboarding workflow", "Send internal #wins notification"],
      "qualification_gates": [],
      "avg_days_target": 1
    }
  ],
  "handoff_protocols": {
    "sdr_to_ae": "SDR books discovery call; transfers BANT notes, company research, and stakeholder map to AE in CRM before meeting",
    "ae_to_se": "AE completes discovery; creates SE brief with use case, technical requirements, and integration needs",
    "ae_to_cs": "AE creates CS handoff note including: deal context, champion contact, use case, success metrics, and known risks"
  },
  "required_crm_fields": ["deal_value", "close_date", "lead_source", "product_line", "deal_owner", "contract_term", "champion_name"],
  "automation_rules": ["Stage transition → notify AE manager", "Close date T-7 days → overdue deal alert", "Closed Won → create CS onboarding task"],
  "rollout_plan": {
    "pilot_group": "2 senior AEs",
    "pilot_weeks": 4,
    "feedback_cadence": "Weekly 30-min process review",
    "full_rollout_week": 5
  }
}
```
