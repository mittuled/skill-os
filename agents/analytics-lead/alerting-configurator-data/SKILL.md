---
name: alerting-configurator-data
description: >
  This skill configures metric alerts and anomaly detection rules for analytics pipelines. Use when asked to set up threshold alerts, configure anomaly detection, or define escalation policies for KPI movements. Also consider when a new metric dashboard ships without alerting coverage. Suggest when a north star metric changes or a new instrumentation spec is approved without corresponding alerts.
department: data-growth
agent: analytics-lead
version: 1.0.0
complexity: medium
related-skills:
  - north-star-metric-reviewer-data
  - metrics-dashboard-builder
  - instrumentation-spec-data
---

# alerting-configurator-data

## Agent: Analytics Lead

L1 analytics leader (1x) responsible for search demand validation, market sizing, goal framing, instrumentation strategy, and north star metric governance.

Department ethos: [ideal-data-growth.md](../../../departments/data-growth/ideal-data-growth.md)
Tool policy: [allowed-tools.yaml](../../../allowed-tools.yaml)

## Skill Description

The alerting configurator defines threshold-based and anomaly-based alert rules for key metrics, ensuring that meaningful deviations in product health, funnel conversion, or cohort behaviour surface to the right stakeholder before impact compounds.

## When to Use

- When a new KPI or north star metric is adopted and has no alerting coverage.
- When a metrics dashboard launches and stakeholders need proactive notification of regressions.
- When false-positive alert fatigue degrades team trust in the monitoring system.
- When a post-mortem reveals that a metric regression went undetected for more than 24 hours.

## Workflow

1. **Inventory metrics**: List all metrics requiring alerts, noting current baseline values, historical variance (standard deviation over trailing 30 days), and business criticality tier.
2. **Define thresholds**: For each metric, set static thresholds (absolute floor/ceiling) and dynamic thresholds (z-score or percentage deviation from rolling average). Document the rationale for each threshold.
3. **Configure anomaly detection**: For high-cardinality or seasonal metrics, configure anomaly detection using statistical methods (e.g., STL decomposition, CUSUM) rather than fixed thresholds.
4. **Set routing and escalation**: Map each alert to an owner, notification channel, and escalation path. Define severity levels (P0-P3) with response-time SLAs.
5. **Validate with historical data**: Backtest alert rules against 90 days of historical data. Count expected true positives, false positives, and missed events. Tune thresholds until the false-positive rate is below 10%.
6. **Document and publish**: Write the alert configuration spec including metric name, condition, severity, owner, and escalation path. Publish to the team wiki and notify stakeholders.

## Anti-Patterns

- **Alert on every metric movement**: Setting tight thresholds on volatile metrics generates noise that teams learn to ignore. *Why*: alert fatigue erodes trust and causes genuine anomalies to be dismissed.
- **Static thresholds on seasonal data**: Using fixed thresholds for metrics with weekly or monthly seasonality produces predictable false positives every cycle. *Why*: the alert fires on expected behaviour, not anomalous behaviour.
- **No owner assigned**: Creating alerts without a designated responder means notifications go unacknowledged. *Why*: an unowned alert is functionally the same as no alert.
- **Skipping backtest validation**: Deploying alert rules without historical validation ships unknown false-positive rates to production. *Why*: untested rules either miss real events or flood channels with noise.

## Output

**Success:**
- An alert configuration spec listing every monitored metric with threshold definition, anomaly detection method, severity level, owner, and escalation path.
- Backtest results showing expected alert volume and false-positive rate below 10%.

**Failure:**
- Alert rules fire on expected variance, generating more than five false positives per week per metric.
- A metric regression goes undetected because the alert was misconfigured or unowned. Report the gap, the root cause, and the corrected configuration.

## Related Skills

- [`north-star-metric-reviewer-data`](../north-star-metric-reviewer-data/SKILL.md) -- when the north star changes, alerting thresholds must be recalibrated.
- [`metrics-dashboard-builder`](../../data-analyst/metrics-dashboard-builder/SKILL.md) -- dashboards and alerts are complementary; every dashboard metric should have corresponding alert coverage.
- [`instrumentation-spec-data`](../instrumentation-spec-data/SKILL.md) -- alert configuration depends on the event schema defined in the instrumentation spec.
