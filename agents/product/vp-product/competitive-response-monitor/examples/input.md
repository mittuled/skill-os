# Example Input: competitive-response-monitor

## Context

**Signal**: Competitor "ReconcileAI" launched real-time bank feed matching on 2026-03-15, directly overlapping TaskFlow's core differentiator.

**Source**: Product Hunt launch post + G2 review from mutual prospect. Confidence: High.

**Current state**: TaskFlow does batch reconciliation (hourly). ReconcileAI now claims <5 second matching latency.

## Scoring Input (JSON)

```json
{
  "signal_capture": 9,
  "customer_impact_assessment": 7,
  "severity_classification": 8,
  "response_recommendation": 8
}
```
