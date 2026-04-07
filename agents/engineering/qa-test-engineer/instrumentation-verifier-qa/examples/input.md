# Scenario: Verifying Instrumentation for New Checkout Funnel Events

A new checkout funnel was instrumented with events, metrics, and traces. QA engineer validates signals in the QA environment before promoting to staging.

## Input Parameters

```json
{
  "feature_name": "Checkout Funnel v2 Instrumentation",
  "expected_signals": [
    {"signal_name": "checkout.step.started", "signal_type": "metric", "verified": true},
    {"signal_name": "checkout.step.completed", "signal_type": "metric", "verified": true},
    {"signal_name": "checkout.payment.initiated", "signal_type": "log_entry", "verified": true},
    {"signal_name": "checkout.payment.failed", "signal_type": "log_entry", "verified": false, "notes": "No log entry observed when payment fails — error path not instrumented"},
    {"signal_name": "checkout.funnel.trace", "signal_type": "trace_span", "verified": true, "payload_issue": true, "payload_issue_detail": "Trace span missing user_id attribute — shows null in Jaeger"}
  ]
}
```
