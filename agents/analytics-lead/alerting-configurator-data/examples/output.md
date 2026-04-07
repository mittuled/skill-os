# Alert Configuration: Product Health Metrics

| Field | Value |
|-------|-------|
| Date | 2026-03-31 |
| Analytics Lead | Analytics Lead |
| Total Rules | 3 |
| Evaluation Frequency | Every 5 minutes |
| Skill | alerting-configurator-data |

## Alert Rules

| Metric | Type | Severity | Window | Notify |
|--------|------|---------|--------|--------|
| daily_active_users | Threshold | Critical | 1 day vs 7d average | PagerDuty + Slack |
| conversion_rate | Rate of Change | Warning | 7 days vs previous period | Slack |
| error_rate | Threshold | Critical | 1 hour (absolute) | PagerDuty + Slack |

## Rule Specifications

### Rule 1: Daily Active Users
- **Type**: Threshold (drop detection)
- **Warning**: > 15% drop vs 7-day rolling average
- **Critical**: > 30% drop vs 7-day rolling average
- **Silence window**: 60 minutes (prevents alert storms during known maintenance)
- **Runbook**: https://wiki.internal/runbooks/daily-active-users-alert

### Rule 2: Conversion Rate
- **Type**: Rate of Change
- **Warning**: > 10% drop vs previous 7-day period
- **Critical**: > 20% drop vs previous 7-day period
- **Silence window**: 60 minutes
- **Runbook**: https://wiki.internal/runbooks/conversion-rate-alert

### Rule 3: Error Rate
- **Type**: Threshold (absolute)
- **Warning**: error rate > 0.5%
- **Critical**: error rate > 2.0% (overrides default template)
- **Silence window**: 60 minutes
- **Runbook**: https://wiki.internal/runbooks/error-rate-alert

## Notification Routing

| Severity | Channels |
|---------|---------|
| Critical | PagerDuty (on-call) + #metrics-alerts (Slack) |
| Warning | #metrics-alerts (Slack) |

## Global Settings

| Setting | Value |
|---------|-------|
| Evaluation frequency | Every 5 minutes |
| Default silence window | 60 minutes |

## Anti-Patterns Avoided

- No vanity metric alerts — all metrics tied to business outcomes
- Silence windows configured to prevent alert fatigue
- Runbook URLs included in every alert for actionable response
