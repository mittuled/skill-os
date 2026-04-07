# Scenario: Canary Deployment Rollback Plan

Create a rollback procedure for a Kubernetes canary deployment that:

1. Detects failure via error rate or latency thresholds
2. Scales down the canary deployment
3. Restores 100% traffic to the stable version
4. Captures diagnostic data before teardown
5. Notifies the team via Slack webhook
