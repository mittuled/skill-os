# Scenario: VP Sign-Off for Payments v2 Production Release

The payments team has completed their tech lead review and is requesting VP Engineering sign-off for the Payments v2 production release. The release includes a new payment processor integration and changes to the billing data model. This is a high-blast-radius release requiring leadership approval.

## Input Parameters

```json
{
  "release_name": "Payments v2 — Billing Model Migration",
  "quality_gate_status": {
    "tech_lead_approval_complete": true,
    "ci_cd_pipeline_green": true,
    "no_open_p0_p1_bugs": true,
    "regression_suite_passed": true,
    "test_coverage_meets_threshold": false
  },
  "operational_readiness": {
    "runbooks_exist": true,
    "alerting_configured_to_slos": true,
    "rollback_procedure_documented_and_tested": true,
    "oncall_rotation_staffed": false
  },
  "open_risks": [
    {
      "id": "RISK-014",
      "description": "Stripe webhook retry behavior is untested under high load — could cause duplicate charge events",
      "severity": "high",
      "mitigated": true,
      "mitigation": "Idempotency keys implemented; rate limiter in place",
      "accepted": true
    },
    {
      "id": "RISK-018",
      "description": "Legacy billing records migration script has not been dry-run in production environment",
      "severity": "critical",
      "mitigated": false,
      "accepted": false
    }
  ],
  "post_launch_follow_ups": [
    "Schedule on-call rotation coverage before T+24h",
    "Dry-run migration script in production after on-call is confirmed"
  ]
}
```
