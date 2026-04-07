# Example Input: sla-definer

## Context

**Product**: TaskFlow — automated invoice reconciliation tool for mid-market operations teams.

**Situation**: The team needs to produce a sla document for TaskFlow's Q2 planning cycle.

**Available inputs**:
- Customer discovery findings from 8 interviews with mid-market ops managers
- Competitive landscape analysis (3 incumbents: NetSuite, Tipalti, Bill.com)
- Engineering feasibility assessment confirming ERP API integration capability
- Design wireframes for the core reconciliation workflow

## Parameters (JSON)

```json
{
  "product_name": "TaskFlow",
  "current_capabilities_audit": "Content for Current Capabilities Audit", "competitive_sla_benchmark": "Content for Competitive SLA Benchmark", "sla_metric_definitions": "Content for SLA Metric Definitions"
}
```
