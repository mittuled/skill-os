# Lead Qualifier — Example Input

## Scenario

Inbound SaaS lead from a mid-market fintech company requesting a demo after downloading the ROI calculator. The lead self-identified as a VP of Operations with budget authority. Company has 280 employees and processes $2B+ in annual transactions.

## Input JSON

```json
{
  "company_name": "Meridian Fintech Solutions",
  "bant_scores": {
    "budget": 7,
    "authority": 9,
    "need": 8,
    "timeline": 6
  },
  "meddic_assessment": {
    "metrics": "confirmed",
    "economic_buyer": "confirmed",
    "decision_criteria": "confirmed",
    "decision_process": "unknown",
    "identify_pain": "confirmed",
    "champion": "unknown"
  },
  "evidence": {
    "budget": "VP Ops confirmed $150K annual budget allocated for operational tooling; procurement cycle starts Q2",
    "authority": "Contact is VP Operations — confirmed final sign-off authority for tools under $200K",
    "need": "Current manual reconciliation process takes 3 FTE 40 hrs/week; compliance audit flagged as high-risk area",
    "timeline": "Wants to be live before Q3 audit; no signed urgency yet, evaluating 2 vendors"
  },
  "recommended_action": "Schedule discovery call within 48 hours; map decision process and identify champion before demo",
  "disqualification_reason": ""
}
```
