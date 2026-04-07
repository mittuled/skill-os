# Framework: Alert Configuration

Reference framework for configuring infrastructure and application alerts aligned with SLOs.

## Severity Levels

| Severity | Response Time | Notification Channel | Examples |
|----------|--------------|---------------------|----------|
| Critical (P1) | Immediate (page) | PagerDuty / phone | Service down, data loss, security breach |
| Warning (P2) | Within 1 hour | Slack #alerts | Error rate approaching SLO, disk 85% full |
| Info (P3) | Next business day | Slack #ops-info | Deployment completed, certificate expiring in 30 days |

## Alert Design Principles

1. **Every alert must be actionable**: If the responder cannot take action, remove the alert
2. **Symptom-based over cause-based**: Alert on user-facing impact (error rate, latency), not internal cause (CPU usage) unless it predicts impact
3. **Include runbook link**: Every critical/warning alert links to a runbook with diagnostic and remediation steps
4. **Use multi-window burn rates**: For SLO alerts, use 1h/6h burn-rate windows to catch both fast burns and slow bleeds
5. **Deduplicate and group**: Group related alerts to prevent paging on cascading failures

## SLO-Based Alert Template

```
Alert: <service>_<slo_type>_burn_rate
Condition: error_budget_consumption_rate > threshold
Windows:
  - Fast burn: 2% budget in 1 hour -> page immediately
  - Slow burn: 5% budget in 6 hours -> warn
Routing: <on-call team>
Runbook: <link>
```

## Anti-Noise Checklist

- [ ] Alert has fired in the past 30 days (if not, consider removing)
- [ ] False positive rate < 5% over past 30 days
- [ ] Alert is not a duplicate of another alert at a different threshold
- [ ] Responder can distinguish this alert from related alerts within 30 seconds
