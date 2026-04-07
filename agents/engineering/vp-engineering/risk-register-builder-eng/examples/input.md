# Scenario: Risk Register for Data Pipeline Migration

An engineering team is migrating from a batch ETL pipeline to a real-time streaming architecture using Apache Kafka. The VP Engineering needs a risk register before the first implementation phase begins.

## Input Parameters

```json
{
  "project_name": "Real-Time Data Pipeline Migration",
  "phase": "Phase 1 — Core Streaming Infrastructure",
  "register_date": "2026-03-31",
  "next_review_date": "2026-04-30",
  "risks": [
    {
      "id": "RISK-001",
      "description": "Kafka cluster configuration is novel for the team — limited operational experience may slow incident response",
      "category": "technical",
      "likelihood": "medium",
      "impact": "high",
      "mitigation_strategy": "reduce",
      "mitigation_detail": "Schedule 2-day Kafka operations training before Phase 1 kickoff; pair junior engineers with Kafka-experienced contractor",
      "owner": "Staff Engineer",
      "target_resolution_date": "2026-04-07"
    },
    {
      "id": "RISK-002",
      "description": "Downstream consumers depend on batch data schedule; real-time migration may break their ingestion logic",
      "category": "external",
      "likelihood": "high",
      "impact": "critical",
      "mitigation_strategy": "reduce",
      "mitigation_detail": "Run dual-write mode for 4 weeks post-migration; notify all consumer teams with 6-week lead time",
      "owner": "Tech Lead",
      "target_resolution_date": "2026-05-15"
    },
    {
      "id": "RISK-003",
      "description": "Infrastructure cost may exceed budget if Kafka partition count is misconfigured for peak load",
      "category": "operational",
      "likelihood": "low",
      "impact": "medium",
      "mitigation_strategy": "reduce",
      "mitigation_detail": "Perform load test at 3x expected peak before production cutover; set budget alerts at 80% of allocation",
      "owner": "DevOps Engineer",
      "target_resolution_date": "2026-04-21"
    },
    {
      "id": "RISK-004",
      "description": "Key engineer on leave for 3 weeks during Phase 1 critical path",
      "category": "resource",
      "likelihood": "high",
      "impact": "high",
      "mitigation_strategy": "reduce",
      "mitigation_detail": "Cross-train backup engineer; document all critical implementation decisions before leave begins",
      "owner": "Engineering Manager",
      "target_resolution_date": "2026-04-05"
    }
  ]
}
```
