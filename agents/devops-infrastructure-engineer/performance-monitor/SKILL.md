---
name: performance-monitor
description: >
  This skill monitors production performance metrics and flags degradation. Use
  when asked to set up performance monitoring, investigate latency issues, or
  track SLO compliance. Also consider when deploying a new service without
  observability. Suggest when the user is running production services without
  performance visibility.
department: engineering
agent: devops-infrastructure-engineer
version: 1.0.0
complexity: medium
related-skills:
  - ../infrastructure-scaling-executor/SKILL.md
  - ../runbook-drafter/SKILL.md
---

# performance-monitor

## Agent: DevOps / Infrastructure Engineer

L2 DevOps and infrastructure engineer (1x) responsible for CI/CD pipelines, deployment automation, cloud infrastructure, monitoring, alerting, incident response, and rollout management.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

Monitors production performance metrics including latency, throughput, error rates, and resource utilization, flagging degradation against defined SLOs and triggering appropriate response.

## When to Use

- When a new service is deployed to production and needs performance baselines established and alerts configured.
- When SLO compliance needs tracking and reporting to stakeholders on a regular cadence.
- When a performance incident occurs and real-time metric analysis is needed to identify the degradation source.

## Workflow

1. **Metric Definition**: Define the key performance indicators for each service: request latency (p50/p95/p99), error rate, throughput, and resource utilization (CPU, memory, disk I/O, network). Map metrics to SLOs. Deliverable: metric catalog with SLO mappings.
2. **Instrumentation Verification**: Verify that services emit the required metrics via structured logging, APM agents, or custom instrumentation. Fill any observability gaps. Deliverable: instrumentation coverage report.
3. **Dashboard Setup**: Build monitoring dashboards showing real-time and historical performance for each service. Include SLO burn rate indicators and comparison views (week-over-week, deploy-over-deploy). Deliverable: operational dashboards.
4. **Alert Configuration**: Configure alerts for SLO violations, error rate spikes, latency degradation, and resource saturation. Set appropriate severity levels and routing (page vs. notification). Deliverable: alert rules with escalation paths.
5. **Ongoing Monitoring**: Monitor dashboards, respond to alerts, investigate anomalies, and produce regular SLO compliance reports. Adjust baselines and thresholds as the system evolves. Deliverable: SLO compliance reports and incident triggers.

## Anti-Patterns

- **Alerting on averages**: Setting alert thresholds on mean latency instead of percentiles. *Why*: averages hide tail latency spikes that affect a significant fraction of users; p95 and p99 are the metrics that matter for user experience.
- **Dashboard without alerts**: Building dashboards that require human watching without automated alerting. *Why*: dashboards are for investigation, not detection; unattended dashboards mean degradation goes unnoticed until users complain.
- **Alert fatigue**: Configuring too many low-severity alerts that train operators to ignore notifications. *Why*: when real incidents occur, they get lost in noise; every alert should require action or be removed.

## Output

**On success**: Produces metric catalog, operational dashboards, alert configurations, and SLO compliance reports. Delivered on an ongoing basis with regular reporting cadence.

**On failure**: Report which metrics could not be collected (e.g., missing instrumentation, inaccessible services), what partial monitoring is in place, and what gaps remain. Escalate if SLO tracking is incomplete for production services.

## Related Skills

- [`infrastructure-scaling-executor`](../infrastructure-scaling-executor/SKILL.md) -- Performance monitoring triggers scaling when resource saturation is detected.
- [`runbook-drafter`](../runbook-drafter/SKILL.md) -- Monitoring alerts reference runbooks for incident response procedures.
