# Scenario: Entering the Mid-Market FinTech Segment

A SaaS compliance automation company is expanding from its SMB base into mid-market FinTech firms (200–1,000 employees). The product automates regulatory reporting workflows. The VP Sales needs to define the sales motion before the segment expansion kicks off next quarter.

## Input Parameters

```json
{
  "segment_name": "Mid-Market FinTech",
  "segment_tier": "mid-market",
  "pain_points": [
    "manual regulatory reporting taking 40+ hours per quarter",
    "audit failures due to inconsistent data trails",
    "compliance team scaling cost outpacing headcount budget"
  ],
  "competitors": ["ComplyAdvantage", "Workiva", "manual spreadsheet workflows"],
  "value_metric": "reports_automated_per_month",
  "value_proposition": "cut regulatory reporting time by 70% with a full audit trail",
  "pricing_model": "per-seat",
  "preferred_motion": "consultative-hybrid",
  "buyer_personas": [
    {"role": "Economic Buyer", "title": "CFO or Chief Compliance Officer", "priority": "Risk reduction and audit readiness"},
    {"role": "Champion", "title": "Compliance Manager", "priority": "Workflow automation ease"},
    {"role": "Technical Evaluator", "title": "IT Director", "priority": "Data integration and SOC 2 posture"}
  ],
  "win_themes": {
    "ComplyAdvantage": ["faster implementation", "lower TCO"],
    "Workiva": ["simpler UX", "better SMB-to-mid-market pricing"],
    "manual spreadsheet workflows": ["audit trail", "time savings", "error reduction"]
  },
  "loss_themes": {
    "ComplyAdvantage": ["narrower feature set for AML-heavy buyers"],
    "Workiva": ["brand recognition gap"],
    "manual spreadsheet workflows": ["change management resistance"]
  }
}
```
