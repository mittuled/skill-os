---
name: team-health-monitor
description: >
  This skill monitors latency, error rates, context window usage, and
  hallucination rates as leading indicators of delivery risk. Use when asked to
  check agent health, diagnose fleet issues, or set up health monitoring. Also
  consider when delivery quality drops unexpectedly. Suggest when the user is
  running agents without health observability.
department: agent-operations
agent: agent-operations-manager
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "monitor team health"
  - "check team pulse"
  - "team health check"
  - "team wellbeing review"
  - "org health monitor"
---

# team-health-monitor

## Agent: Agent Operations Manager

L2 Agent Operations Manager (1x) responsible for message passing infrastructure, context sharing protocols, inter-agent coordination, and agent health monitoring.

Department ethos: [ideal-agent-operations.md](../../../../departments/agent-operations/ideal-agent-operations.md)

## Skill Description

Monitors latency, error rates, context window usage, and hallucination rates across the agent fleet as leading indicators of delivery risk.

## When to Use

- When ongoing monitoring is needed to detect agent degradation before it impacts delivery.
- When a specific agent is suspected of underperforming and needs diagnostic investigation.
- When a model update or configuration change has been deployed and its impact on fleet health needs tracking.

## Workflow

1. **Define Health Metrics**: Establish the metric set per agent role: response latency, error rate, context window utilization, hallucination rate, and task completion rate. Set thresholds for healthy, warning, and critical states. Deliverable: health metric definitions with thresholds.
2. **Instrument Monitoring**: Configure data collection for each metric. Ensure logs, traces, and output samples are captured with sufficient granularity. Deliverable: monitoring instrumentation setup.
3. **Run Health Checks**: Execute periodic health assessments against defined thresholds. Compare current readings to historical baselines. Deliverable: health dashboard with current status per agent.
4. **Diagnose Anomalies**: When metrics breach warning or critical thresholds, investigate root causes -- model degradation, context overflow, tool failures, or upstream data quality issues. Deliverable: anomaly diagnosis report with root cause analysis.
5. **Escalate and Remediate**: Escalate critical issues to the VP Agent Operations with recommended actions. For warning-level issues, create remediation tasks for the Agent Trainer or Configuration Manager. Deliverable: escalation notices or remediation tickets.

## Anti-Patterns

- **Monitoring only errors**: Tracking error rates without monitoring leading indicators like latency increases or context window creep. *Why*: by the time errors spike, the underlying issue has already impacted multiple outputs.
- **Alert fatigue**: Setting thresholds so sensitive that every minor fluctuation triggers an alert. *Why*: teams that receive constant false alarms learn to ignore alerts, missing genuine critical events.
- **Dashboard without action**: Building health dashboards that nobody reviews or acts upon. *Why*: observability without response is expensive decoration; every metric must have an owner and a response procedure.

## Output

**On success**: Produces a fleet health report containing per-agent health status, trend analysis, anomaly diagnoses, and remediation recommendations. Delivered as a dashboard update and periodic report to the Agent Operations Manager.

**On failure**: Report which agents could not be monitored (missing instrumentation, inaccessible logs), what partial health data was collected, and what instrumentation gaps need to be closed.

## Related Skills

- [`culture-and-performance-system`](../../../agent-operations/vp-agent-operations/culture-and-performance-system/SKILL.md) -- Periodic performance reviews use health monitoring data as input.
- [`employment-agreement-setup`](../employment-agreement-setup/SKILL.md) -- Contract violations often manifest as health monitoring anomalies.
- [`skills-gap-analyser`](../../../agent-operations/agent-trainer-skill-optimizer/skills-gap-analyser/SKILL.md) -- Persistent health issues may indicate skill-level deficiencies.
