# Scenario: Staging Validation for Billing Service v3

QA engineer is validating the staging environment before promoting the Billing Service v3 release to production. This release includes new subscription tier logic and Stripe integration changes.

## Input Parameters

```json
{
  "release_name": "Billing Service v3 — Subscription Tiers",
  "validation_results": {
    "environment_version_match": {"passed": true, "notes": "Staging matches release-branch HEAD sha abc1234"},
    "data_state_representative": {"passed": true, "notes": "Staging DB refreshed from production snapshot, 2 days old"},
    "end_to_end_test_suite": {"passed": true, "notes": "All 142 E2E tests passed; 3 skipped (known Stripe sandbox rate limit)"},
    "cross_service_integrations": {"passed": false, "notes": "Auth service token refresh fails on 3rd retry — intermittent timeout observed in Stripe webhook handler"},
    "background_jobs_and_async_workflows": {"passed": true, "notes": "Invoice generation job ran successfully for 500 test subscriptions"},
    "observability_logs_metrics_traces": {"passed": true, "notes": "Logs flowing, billing metrics emitting, distributed traces connected through Stripe webhook path"},
    "infrastructure_smoke_tests": {"passed": true, "notes": "Load balancer health checks green, TLS cert valid"}
  }
}
```
