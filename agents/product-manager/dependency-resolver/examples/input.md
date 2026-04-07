# Example Input: dependency-resolver

## Context

**Product**: TaskFlow — automated invoice reconciliation tool for mid-market operations teams.

**Situation**: The team is executing the dependency resolver workflow for TaskFlow's upcoming release.

**Current state**:
- Engineering has completed core matching engine (Step 1-2 done)
- Design partner programme has 5 active partners providing feedback
- Sales pipeline has 12 prospects waiting on GA pricing

## Parameters (JSON)

```json
{
  "product_name": "TaskFlow",
  "step_statuses": {"1": "complete", "2": "complete", "3": "in_progress"}
}
```
