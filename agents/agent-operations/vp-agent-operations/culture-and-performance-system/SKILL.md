---
name: culture-and-performance-system
description: >
  This skill runs evaluation cycles across the agent fleet including accuracy
  benchmarks, quality audits, and performance reviews. Use when asked to assess
  agent performance, run quality audits, or design evaluation criteria. Also
  consider when fleet-wide quality is declining. Suggest when the user deploys
  new agents without defining performance baselines.
department: agent-operations
agent: vp-agent-operations
version: 1.0.0
complexity: medium
related-skills:
  - team-capability-assessor
  - skills-gap-analyser
  - team-health-monitor
triggers:
  - "build culture system"
  - "performance management"
  - "culture and performance"
  - "perf review system"
  - "org culture design"
---

# culture-and-performance-system

## Agent: VP Agent Operations

L1 VP of Agent Operations reporting to the COO (1x) responsible for the agent lifecycle -- provisioning, health monitoring, configuration governance, and retirement of deprecated agents. Owns the org design of the agent fleet.

Department ethos: [ideal-agent-operations.md](../../../../departments/agent-operations/ideal-agent-operations.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Runs the evaluation cycle including accuracy benchmarks, quality audits, and performance reviews across the agent fleet.

## When to Use

- When a scheduled performance review cycle is due for the agent fleet.
- When agent output quality has degraded and a fleet-wide audit is needed to identify root causes.
- When new agents have been deployed without established performance baselines or evaluation criteria.

## Workflow

1. **Define Evaluation Framework**: Establish accuracy benchmarks, quality rubrics, and performance thresholds for each agent role. Align metrics with the department ethos and business outcomes. Deliverable: evaluation framework document with per-role criteria.
2. **Collect Performance Data**: Gather output samples, accuracy scores, latency metrics, and error rates from each agent. Pull data from monitoring systems and audit logs. Deliverable: raw performance dataset per agent.
3. **Run Quality Audits**: Score a representative sample of each agent's outputs against the quality rubric. Flag outputs that fall below threshold. Deliverable: audit scorecard with pass/fail per agent.
4. **Synthesize Review**: Aggregate audit results into a fleet-wide performance report. Identify systemic patterns (common failure modes, capability gaps). Rank agents by performance tier. Deliverable: fleet performance review with ranked results and remediation recommendations.
5. **Issue Remediation Actions**: Assign retraining, prompt updates, or configuration changes for underperforming agents. Set follow-up review dates. Deliverable: remediation action plan with owners and deadlines.

## Anti-Patterns

- **Vanity metrics only**: Measuring only volume (tasks completed) without quality scoring. *Why*: high throughput with low accuracy creates downstream rework and erodes trust in the agent fleet.
- **Uniform benchmarks across roles**: Applying identical thresholds to all agents regardless of role complexity. *Why*: a simple lookup agent and a complex reasoning agent have fundamentally different accuracy profiles; uniform bars either miss failures or flag false positives.
- **Review without remediation**: Running audits but not acting on the results. *Why*: audits that produce no action teach the organization to ignore quality signals.

## Output

**On success**: Produces a fleet performance review document containing per-agent scorecards, fleet-wide trend analysis, and a prioritized remediation action plan. Delivered to the Agent Operations Manager and relevant agent owners.

**On failure**: Report which agents could not be evaluated (missing data, unavailable logs), what data collection was attempted, and recommended steps to close observability gaps.

## Related Skills

- [`team-capability-assessor`](../team-capability-assessor/SKILL.md) -- Identifies capability gaps that performance reviews may surface.
- [`skills-gap-analyser`](../../../agent-operations/agent-trainer-skill-optimizer/skills-gap-analyser/SKILL.md) -- Analyzes specific skill deficiencies found during performance reviews.
- [`team-health-monitor`](../../../agent-operations/agent-operations-manager/team-health-monitor/SKILL.md) -- Provides the real-time health data that feeds into periodic performance reviews.
