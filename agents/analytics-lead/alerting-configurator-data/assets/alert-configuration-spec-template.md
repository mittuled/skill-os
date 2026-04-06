# Alert Configuration Spec

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Analytics Lead name] |
| Version | [1.0] |
| Status | [Draft / Review / Active] |
| Skill | alerting-configurator-data |

## Executive Summary

[2-3 sentences describing the scope of this alert configuration — which product area or metric set is covered, the total number of alerts configured, and the expected false-positive rate after backtest validation.

GUIDANCE: Lead with the coverage statement. Example: "This spec defines 14 alert rules covering the onboarding funnel, core feature engagement, and data pipeline health. Backtest against 90 days of historical data projects a 6% false-positive rate and zero missed P0 events."]

## Metric Inventory

[List of all metrics included in this configuration.

GUIDANCE:
- Good: Table with metric name, current baseline value, 30-day σ, criticality tier, and platform source.
- Bad: A paragraph listing metric names without baseline context.
- Format: Table with columns: Metric Name | Baseline (30d avg) | Std Dev (30d) | Criticality Tier | Source Platform]

| Metric Name | Baseline (30d avg) | Std Dev (30d) | Criticality Tier | Source |
|-------------|-------------------|--------------|-----------------|--------|
| [metric_name] | [value] | [±value] | [North Star / Primary / Secondary / Operational] | [Amplitude / Mixpanel / Warehouse] |

## Alert Rules

[Full specification of every configured alert rule.

GUIDANCE:
- Good: One row per alert with all parameters filled in — name, metric, condition, severity, detection method, owner, notification channel.
- Bad: "We alert when things go wrong." Every field must be explicit and unambiguous.
- Format: Table below, plus a separate Anomaly Detection Config section for any rules using STL or CUSUM.]

| Alert Name | Metric | Condition | Threshold | Severity | Detection Method | Owner | Channel |
|-----------|--------|-----------|-----------|----------|-----------------|-------|---------|
| [alert_name] | [metric_name] | [drops below / rises above / deviates by] | [value or N×σ] | [P0–P3] | [static / dynamic z-score / STL / CUSUM] | [name] | [#channel / PagerDuty] |

### Anomaly Detection Configuration

[For any alert using anomaly detection, document the model parameters.

GUIDANCE: Include decomposition method, training window, sensitivity, and seasonality assumptions.]

| Alert Name | Model | Training Window | Seasonality | Sensitivity |
|-----------|-------|----------------|-------------|------------|
| [alert_name] | [STL / CUSUM / Prophet] | [N days] | [daily / weekly / none] | [low / medium / high] |

## Escalation Paths

[Document the full escalation chain for each severity tier.

GUIDANCE:
- Good: "P0 alerts page the on-call engineer via PagerDuty (15-min response SLA). If unacknowledged after 15 min, escalate to Analytics Lead. Root-cause doc required within 24 hours."
- Bad: "P0 alerts go to the team."
- Format: Prose with explicit names, tools, and time windows per tier.]

**P0 – Critical:**
[Response path, tools, SLA, escalation trigger, documentation requirement]

**P1 – High:**
[Response path, tools, SLA, escalation trigger]

**P2 – Medium:**
[Response path, tools, SLA]

**P3 – Low:**
[Response path, review cadence]

## Backtest Results

[Results of the 90-day historical backtest.

GUIDANCE:
- Good: Table showing true positives, false positives, false negatives, and FP rate per alert. Highlight any alerts that required threshold adjustment.
- Bad: "Alerts look good in testing." Numbers are required.
- Format: Table plus narrative on any rules adjusted post-backtest.]

| Alert Name | True Positives | False Positives | False Negatives | FP Rate | Status |
|-----------|---------------|----------------|----------------|---------|--------|
| [alert_name] | [N] | [N] | [N] | [X%] | [Approved / Tuned / Suppressed] |

**Tuning Notes:**
[Describe any thresholds adjusted during backtest and the rationale.]

## Recommendations

[Prioritized list of improvements or next steps.

GUIDANCE:
- P1: Alerts that did not meet the < 10% FP rate target and require further tuning or suppression windows.
- P2: Metrics lacking coverage that should be added in the next iteration.
- P3: Ownership gaps or notification channel configurations that need cleanup.]

## Appendices

### A. Methodology

[Document the threshold calibration approach: rolling window length, σ multipliers used, STL/CUSUM parameters, backtest date range.]

### B. Supporting Data

[Raw backtest summary tables, seasonal decomposition charts, or baseline metric distributions used to calibrate thresholds.]
