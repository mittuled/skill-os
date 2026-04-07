# Scenario: Post-Deploy Instrumentation Verification for Notification Service

Notification service v2 was deployed to production. QA engineer verifies instrumentation signals are firing correctly within 30 minutes of deployment.

## Input Parameters

```json
{
  "release_name": "Notification Service v2 Production Deploy",
  "verification_results": [
    {"signal_name": "notification.sent", "signal_type": "metric", "verified": true},
    {"signal_name": "notification.delivery.latency", "signal_type": "metric", "verified": true},
    {"signal_name": "notification.failed", "signal_type": "log_entry", "verified": true},
    {"signal_name": "notification.request.trace", "signal_type": "trace_span", "verified": true, "payload_issue": true, "payload_issue_detail": "channel attribute showing 'undefined' instead of 'email' or 'sms'"},
    {"signal_name": "notification.queue.depth", "signal_type": "metric", "verified": false, "notes": "Queue depth metric not appearing in Prometheus — likely scrape config issue"}
  ]
}
```
