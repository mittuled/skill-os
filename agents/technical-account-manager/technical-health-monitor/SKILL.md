---
name: technical-health-monitor
description: >
  This skill monitors the technical health of enterprise accounts including
  integration stability, API usage, and error rates. Use when asked to track
  enterprise account health, diagnose integration issues, or review API usage
  patterns. Also consider when enterprise accounts report reliability concerns.
  Suggest when the user manages enterprise integrations without health tracking.
department: customer-success
agent: technical-account-manager
version: 1.0.0
complexity: medium
related-skills: []
---

# technical-health-monitor

## Agent: Technical Account Manager

L2 technical account manager (1x) responsible for technical health monitoring of enterprise accounts and identifying expansion opportunities.

Department ethos: [ideal-customer-success.md](../../../departments/customer-success/ideal-customer-success.md)

## Skill Description

Monitors the technical health of enterprise accounts including integration stability, API usage patterns, error rates, and performance metrics.

## When to Use

- When enterprise accounts need ongoing technical health monitoring to prevent issues before they escalate.
- When an enterprise account reports integration instability or performance degradation.
- When preparing for quarterly business reviews and technical health summaries are needed.

## Workflow

1. **Define Technical Health Metrics**: Establish per-account metrics: API call volume and error rates, integration uptime, latency percentiles, data sync success rates, and authentication failure rates. Deliverable: technical health metric definitions per account.
2. **Instrument Monitoring**: Set up monitoring for each enterprise account's technical integration. Configure alerts for threshold breaches. Deliverable: monitoring setup with alert rules.
3. **Conduct Health Reviews**: Periodically review technical metrics for each account. Identify degradation trends, capacity concerns, and integration risks. Deliverable: technical health review per account.
4. **Diagnose and Resolve**: When issues are detected, investigate root causes in collaboration with engineering. Communicate status and resolution timeline to the customer. Deliverable: issue diagnosis and resolution record.
5. **Report to Stakeholders**: Produce technical health summaries for QBRs, internal reviews, and customer-facing reports. Highlight risks and recommendations. Deliverable: technical health report.

## Anti-Patterns

- **Reactive-only monitoring**: Waiting for customers to report issues instead of proactively detecting problems. *Why*: by the time a customer reports an issue, it has already impacted their operations and their confidence in the platform.
- **Monitoring without context**: Tracking metrics without understanding the customer's usage patterns and what constitutes abnormal behavior for their specific integration. *Why*: generic thresholds produce false positives for some accounts and miss issues for others.
- **Technical silos**: Monitoring technical health independently of the broader customer success picture. *Why*: technical issues affect customer satisfaction, renewal likelihood, and expansion readiness; health data must flow to CSMs.

## Output

**On success**: Produces technical health reports per enterprise account containing metric trends, issue logs, resolution records, and risk assessments. Delivered to the customer, CSM, and engineering as appropriate.

**On failure**: Report which accounts could not be monitored (missing integrations, insufficient API access), what partial health data was collected, and what infrastructure is needed for complete coverage.

## Related Skills

- [`technical-expansion-identifier`](../technical-expansion-identifier/SKILL.md) -- Healthy accounts with growing usage are expansion candidates.
- [`tam-playbook-contributor`](../tam-playbook-contributor/SKILL.md) -- Health monitoring methodology is documented in the TAM playbook.
- [`cs-health-monitor`](../../cs-manager/cs-health-monitor/SKILL.md) -- Technical health feeds into the broader customer health score.
