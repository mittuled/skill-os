# Scenario: Reviewing Event-Driven Microservices Architecture for Payment Processing

A payments team is proposing a migration from a monolithic payment processing service to an event-driven microservices architecture using Kafka as the message broker. The VP Engineering must review the ADR before the team commits to the 6-week implementation sprint.

## Input Parameters

```json
{
  "proposal_name": "Event-Driven Payment Processing — ADR-042",
  "scores": {
    "structural_soundness": 72,
    "scalability": 85,
    "standards_alignment": 68,
    "operational_risk": 55
  },
  "present_elements": [
    "observability_plan",
    "capacity_projections",
    "failure_mode_analysis"
  ],
  "criterion_notes": {
    "structural_soundness": "Component boundaries are clear but consumer group isolation is underspecified — multiple services reading from the same topic without documented partition ownership",
    "scalability": "Kafka partition model supports 10x current load with documented headroom calculation. Consumer scaling is horizontal.",
    "standards_alignment": "Observability plan covers structured logging and metrics. Distributed tracing integration not yet specified. No threat model submitted.",
    "operational_risk": "No rollback strategy documented for the 3-step data migration. On-call runbooks for consumer lag not yet written."
  },
  "action_items": [
    "Document partition ownership and consumer group isolation policy",
    "Add distributed tracing integration spec (OpenTelemetry preferred)",
    "Define rollback strategy for each of the 3 migration phases",
    "Write on-call runbook for consumer lag and dead-letter queue handling"
  ],
  "reviewer_notes": "Strong scalability design. Operational readiness is the primary risk — team should not proceed without rollback and on-call runbooks."
}
```
