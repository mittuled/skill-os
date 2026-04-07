# Example Output: assumption-mapper

## Assumption Map for TaskFlow

### Assumption Inventory (12 assumptions across 5 domains)

**Desirability**
- D1: Mid-market ops managers spend >3 hours/week on manual invoice reconciliation (Evidence: 5/6 interviewees confirmed; confidence: high, impact: fatal)
- D2: Exception-based review is preferred over full manual review (Evidence: 4/6 mentioned frustration with reviewing all invoices; confidence: medium, impact: degrading)
- D3: Ops managers are the budget holder for this purchase (Evidence: 2/6 confirmed; confidence: low, impact: fatal)

**Feasibility**
- F1: QuickBooks and Xero APIs support real-time invoice data extraction (Evidence: engineering feasibility note; confidence: high, impact: fatal)
- F2: Matching engine can achieve >95% auto-match rate with standard invoice data (Evidence: none — engineering estimate only; confidence: low, impact: fatal)

**Viability**
- V1: Mid-market ops teams will pay $200-500/month for automated reconciliation (Evidence: no WTP research; confidence: low, impact: fatal)
- V2: CAC can be held below $1,500 through content marketing and partnerships (Evidence: industry benchmarks; confidence: medium, impact: degrading)

**Usability**
- U1: Ops managers can configure matching rules without technical support (Evidence: none; confidence: low, impact: degrading)
- U2: Exception review workflow requires <5 minutes per batch (Evidence: prototype estimate; confidence: medium, impact: degrading)

**Adaptability**
- A1: Matching engine scales linearly with invoice volume up to 10K/month (Evidence: architecture review; confidence: medium, impact: degrading)
- A2: Additional ERP integrations can be added within 2-week cycles (Evidence: API pattern analysis; confidence: medium, impact: negligible)
- A3: Multi-currency support is not required for initial ICP segment (Evidence: 4/6 interviewees US-only; confidence: high, impact: negligible)

### Risk Matrix

| | Low Confidence | High Confidence |
|---|---------------|-----------------|
| **High Impact** | **TEST FIRST**: D3, F2, V1 | **MONITOR**: D1, F1 |
| **Low Impact** | **DEFER**: U1 | **SAFE**: D2, U2, A1, A2, A3, V2 |

### Validation Plan

| Assumption | Method | Cost | Timeline | Owner | Success Criteria |
|-----------|--------|------|----------|-------|-----------------|
| V1 | Van Westendorp pricing survey (30 respondents) | $2,000 | 2 weeks | Product Lead | >60% acceptable price range includes $200-500 |
| F2 | Prototype matching engine on 500 real invoices | $0 (eng time) | 1 week | Tech Lead | >90% auto-match rate |
| D3 | 5 additional interviews targeting budget authority | $500 incentives | 1 week | PM | 3/5 confirm ops manager is decision-maker |

### Scored Result

```json
{
  "skill": "assumption-mapper",
  "scores": {
    "assumption_coverage": 8,
    "confidence_impact_scoring": 7,
    "risk_matrix_quality": 9,
    "validation_plan_rigour": 8
  },
  "composite_score": 7.95,
  "grade": "A",
  "label": "Strong",
  "recommended_action": "Minor refinements then proceed to MVP scoping"
}
```
