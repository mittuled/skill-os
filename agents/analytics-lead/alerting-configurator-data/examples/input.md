# Scenario: Configuring Alerts for Core Product Health Metrics

The analytics lead is setting up alerting for three critical product health metrics: daily active users, onboarding conversion rate, and payment error rate. Critical alerts go to PagerDuty; warnings go to the #metrics-alerts Slack channel.

## Input Parameters

```json
{
  "metrics": [
    {"name": "daily_active_users", "alert_type": "threshold", "severity": "critical"},
    {"name": "conversion_rate", "alert_type": "rate_of_change", "severity": "warning"},
    {"name": "error_rate", "alert_type": "threshold", "severity": "critical", "threshold": {"critical_threshold_pct": 2.0, "warning_threshold_pct": 0.5}}
  ],
  "notification_routing": {
    "critical": ["pagerduty", "slack"],
    "warning": ["slack"],
    "default": ["slack"]
  },
  "eval_frequency_minutes": 5
}
```
