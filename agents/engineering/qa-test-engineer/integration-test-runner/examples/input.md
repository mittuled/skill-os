# Scenario: Integration Test Run for Payment-Notification Service Boundary

A new feature sends payment confirmation emails through the notification service. Integration tests must validate the payment → notification service boundary before merging.

## Input Parameters

```json
{
  "suite_name": "payment-notification integration suite",
  "test_results": [
    {"test_name": "payment_success_triggers_confirmation_email", "passed": true},
    {"test_name": "payment_failure_triggers_failure_notification", "passed": true},
    {"test_name": "notification_service_timeout_retries_3_times", "passed": false, "failure_type": "genuine_defect", "error": "Retry logic only attempts 2 retries before giving up", "affected_component": "NotificationClient.retry_on_timeout"},
    {"test_name": "duplicate_payment_event_deduplication", "passed": true},
    {"test_name": "notification_payload_schema_validation", "passed": false, "failure_type": "flaky_test", "error": "Intermittent JSON schema validation timeout under high test parallelism"},
    {"test_name": "payment_refund_sends_refund_email", "passed": true},
    {"test_name": "notification_delivery_status_tracked", "passed": true}
  ]
}
```
