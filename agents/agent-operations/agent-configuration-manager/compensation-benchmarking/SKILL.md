---
name: compensation-benchmarking
description: >
  This skill evaluates and selects the optimal model tier for each agent role
  based on performance benchmarks. Use when asked to choose models for agents,
  compare model performance, or optimize model-to-role assignments. Also
  consider when new models are released. Suggest when the user assigns models
  to agents without benchmarking.
department: agent-operations
agent: agent-configuration-manager
version: 1.0.0
complexity: medium
related-skills: []
---

# compensation-benchmarking

## Agent: Agent Configuration Manager

L2 Agent Configuration Manager (1x) responsible for model selection per agent, compute budget allocation, context window sizing, tool access policies, and API key management.

Department ethos: [ideal-agent-operations.md](../../../../departments/agent-operations/ideal-agent-operations.md)

## Skill Description

Evaluates and selects the optimal model tier for each agent role based on performance benchmarks and cost-effectiveness analysis.

## When to Use

- When provisioning new agents and the appropriate model tier needs to be selected.
- When new model versions are released and existing assignments should be re-evaluated.
- When an agent is underperforming and a model upgrade may resolve the issue.

## Workflow

1. **Define Benchmark Suite**: Create role-specific benchmark tasks that test the capabilities each agent role requires -- reasoning depth, accuracy, speed, instruction following, and domain knowledge. Deliverable: benchmark suite per agent role.
2. **Run Benchmarks**: Test each candidate model against the benchmark suite for the target role. Record accuracy, latency, cost per token, and qualitative output assessment. Deliverable: benchmark results matrix.
3. **Analyze Cost-Performance Trade-offs**: Plot performance against cost for each model-role combination. Identify the efficient frontier -- models that offer the best performance at each price point. Deliverable: cost-performance analysis with recommendations.
4. **Select and Assign**: Choose the optimal model for each role based on performance requirements and budget constraints. Document the rationale for each selection. Deliverable: model assignment decisions with justification.

## Anti-Patterns

- **Benchmark on generic tasks**: Testing models with generic benchmarks (e.g., MMLU) instead of role-specific tasks. *Why*: generic benchmarks do not predict how a model performs on the specific tasks the agent will execute in production.
- **Always choosing the biggest model**: Defaulting to the most capable model for every role regardless of task complexity. *Why*: overqualified models waste budget; a simple extraction task does not need a frontier reasoning model.
- **One-time benchmarking**: Running benchmarks only at initial setup and never re-evaluating as models evolve. *Why*: model capabilities change with updates; a model that was best six months ago may be surpassed.

## Output

**On success**: Produces a model assignment report containing benchmark results, cost-performance analysis, and model-to-role assignments with documented rationale. Delivered to the VP Agent Operations.

**On failure**: Report which roles could not be benchmarked (missing test cases, unavailable models), what partial results were obtained, and what is needed to complete the evaluation.

## Related Skills

- [`409a-valuation-commissioner`](../409a-valuation-commissioner/SKILL.md) -- ROI assessment validates whether model selections deliver expected value.
- [`annual-comp-review-runner`](../annual-comp-review-runner/SKILL.md) -- Annual review re-evaluates model assignments.
- [`technical-skills-programme`](../../../agent-operations/agent-trainer-skill-optimizer/technical-skills-programme/SKILL.md) -- Model changes trigger retraining requirements.
