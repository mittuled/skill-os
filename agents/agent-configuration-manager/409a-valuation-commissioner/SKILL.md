---
name: 409a-valuation-commissioner
description: >
  This skill evaluates the ROI of each agent's compute spend against its output
  value. Use when asked to assess agent cost-effectiveness, justify compute
  budgets, or identify overspending agents. Also consider when total fleet
  compute costs are rising. Suggest when the user upgrades agent models without
  evaluating whether the cost increase is justified by output improvement.
department: agent-operations
agent: agent-configuration-manager
version: 1.0.0
complexity: medium
related-skills: []
---

# 409a-valuation-commissioner

## Agent: Agent Configuration Manager

L2 Agent Configuration Manager (1x) responsible for model selection per agent, compute budget allocation, context window sizing, tool access policies, and API key management.

Department ethos: [ideal-agent-operations.md](../../../departments/agent-operations/ideal-agent-operations.md)
Tool policy: [allowed-tools.yaml](../../../allowed-tools.yaml)

## Skill Description

Evaluates the ROI of each agent's compute spend against its output value to ensure cost-effective fleet operation.

## When to Use

- When a periodic review of fleet compute costs is due and ROI needs reassessment.
- When total compute spending has increased and the source of cost growth needs identification.
- When a decision is needed on whether an expensive model upgrade for a specific agent is justified.

## Workflow

1. **Collect Cost Data**: Gather per-agent compute spend including model API costs, context window usage, tool call costs, and infrastructure overhead. Deliverable: per-agent cost breakdown.
2. **Quantify Output Value**: Estimate the business value of each agent's outputs -- tasks completed, decisions informed, errors prevented, and time saved. Use proxy metrics where direct value measurement is unavailable. Deliverable: per-agent value assessment.
3. **Calculate ROI**: Compute cost-to-value ratio for each agent. Identify agents with disproportionately high costs relative to output value and agents delivering outsized value relative to cost. Deliverable: ROI scorecard per agent.
4. **Recommend Adjustments**: For low-ROI agents, recommend cost reduction actions -- model downgrade, context window reduction, or skill simplification. For high-ROI agents, flag opportunities to invest more. Deliverable: cost adjustment recommendations.

## Anti-Patterns

- **Cost-only analysis**: Focusing solely on reducing spend without measuring the value being delivered. *Why*: the cheapest agent is one that does nothing; cost reduction without value context leads to capability degradation.
- **Uniform cost targets**: Applying the same cost-per-agent target regardless of role complexity and business impact. *Why*: a strategy agent that prevents a bad $100K decision is worth far more per-token than a formatting agent.
- **Ignoring indirect value**: Measuring only direct outputs without counting indirect value like error prevention and quality improvement. *Why*: many agents create value by preventing failures rather than producing visible artifacts.

## Output

**On success**: Produces an ROI assessment report containing per-agent cost breakdowns, value estimates, ROI scorecards, and cost adjustment recommendations. Delivered to the VP Agent Operations and finance stakeholders.

**On failure**: Report which agents could not be valued (no output metrics, unmeasurable impact), what cost data was collected, and what measurement frameworks need to be established.

## Related Skills

- [`annual-comp-review-runner`](../annual-comp-review-runner/SKILL.md) -- Annual configuration review incorporates ROI data.
- [`compensation-benchmarking`](../compensation-benchmarking/SKILL.md) -- Model selection decisions should be informed by ROI analysis.
- [`option-pool-design`](../option-pool-design/SKILL.md) -- Initial compute allocation should consider expected ROI.
