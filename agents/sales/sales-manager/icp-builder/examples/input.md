# ICP Builder — Example Input

## Scenario

A B2B SaaS company provides workflow automation for HR operations. The Sales Manager is scoring two accounts from a new prospecting batch to validate ICP fit before assigning AEs. Account A is a Series C HR tech company with strong signals; Account B is a large enterprise with limited automation needs.

## Input JSON

```json
{
  "account_name": "Workstream Technologies",
  "icp_scores": {
    "company_size": 8,
    "industry_fit": 9,
    "technology_stack": 7,
    "growth_stage": 9,
    "pain_intensity": 9,
    "budget_authority": 7
  },
  "dimension_notes": {
    "company_size": "280 employees — ideal mid-market range (200-500)",
    "industry_fit": "HR tech company with direct workflow pain — perfect vertical alignment",
    "technology_stack": "Uses Slack, Notion, Salesforce — integrates well; missing dedicated HR automation layer",
    "growth_stage": "Series C — active scaling, budget available, internal pressure to systematize",
    "pain_intensity": "Processing 50+ HR workflows manually per week; compliance audit flagged as risk",
    "budget_authority": "CHRO confirmed budget holder; procurement cycle starts Q2"
  },
  "disqualifying_signals": []
}
```
