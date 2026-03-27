---
name: skills-gap-analyser
description: >
  This skill identifies where agent skill accuracy or quality falls below
  acceptable thresholds. Use when asked to audit skill quality, find
  underperforming skills, or prioritize skill improvements. Also consider when
  performance reviews reveal systemic quality issues. Suggest when the user
  notices repeated output failures without investigating skill-level causes.
department: agent-operations
agent: agent-trainer-skill-optimizer
version: 1.0.0
complexity: medium
related-skills: []
---

# skills-gap-analyser

## Agent: Agent Trainer & Skill Optimizer

L2 Agent Trainer and Skill Optimizer (1x) responsible for evaluating existing skills, running evals, optimising prompts, improving agent performance, and training new agent configurations.

Department ethos: [ideal-agent-operations.md](../../../departments/agent-operations/ideal-agent-operations.md)

## Skill Description

Identifies where agent skill accuracy or quality falls below acceptable thresholds through systematic evaluation and gap prioritization.

## When to Use

- When fleet performance reviews reveal quality issues that need root-cause analysis at the skill level.
- When a specific agent's outputs are consistently below expectations and the underperforming skills need identification.
- When planning the next training or skill improvement cycle and priorities need data-driven ranking.

## Workflow

1. **Collect Skill Performance Data**: Gather accuracy scores, error rates, and output quality ratings for each skill across all agents. Source data from health monitors, performance reviews, and user feedback. Deliverable: skill performance dataset.
2. **Benchmark Against Thresholds**: Compare each skill's performance against its defined accuracy and quality thresholds. Flag skills that fall below acceptable levels. Deliverable: skill gap list with deviation from threshold.
3. **Classify Gap Types**: Categorize each gap -- is it a prompt deficiency, training data issue, model capability limitation, or tool integration failure? Deliverable: classified gap analysis.
4. **Prioritize Remediation**: Rank gaps by business impact (how much does this skill's failure affect delivery) and fix difficulty (effort to remediate). Deliverable: prioritized remediation backlog.
5. **Recommend Actions**: For each prioritized gap, recommend a specific action -- prompt update, skill rewrite, model upgrade, or retirement. Deliverable: remediation recommendation report.

## Anti-Patterns

- **Analyzing skills in isolation**: Evaluating each skill without considering how it interacts with upstream and downstream skills in workflows. *Why*: a skill may appear adequate alone but fail when receiving poor inputs from an upstream skill.
- **Threshold inflation**: Setting quality thresholds so high that most skills appear to have gaps. *Why*: when everything is flagged, nothing is prioritized, and remediation effort is scattered across trivial and critical gaps alike.
- **Gap analysis without action**: Producing detailed gap reports that are not connected to remediation workflows. *Why*: analysis without action is wasted effort; every identified gap must have a clear path to resolution.

## Output

**On success**: Produces a prioritized skill gap report containing per-skill performance data, classified gap types, and remediation recommendations ranked by business impact. Delivered to the Skill Builder Lead and VP Agent Operations.

**On failure**: Report which skills could not be evaluated (missing performance data, undefined thresholds), what partial analysis was completed, and what data collection is needed.

## Related Skills

- [`culture-and-performance-system`](../../vp-agent-operations/culture-and-performance-system/SKILL.md) -- Fleet performance reviews that surface skill-level issues.
- [`recruiting-pipeline-builder`](../../skill-builder-lead/recruiting-pipeline-builder/SKILL.md) -- Skill gaps feed into the pipeline for new skill development.
- [`technical-skills-programme`](../technical-skills-programme/SKILL.md) -- Retraining programmes address skill gaps caused by model changes.
