---
name: technical-skills-programme
description: >
  This skill builds the retraining and prompt update programme when the
  underlying model changes. Use when asked to plan model migration, update
  prompts for a new model version, or assess model change impact. Also consider
  when a model provider announces deprecation. Suggest when the user upgrades
  models without testing existing skills against the new version.
department: agent-operations
agent: agent-trainer-skill-optimizer
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "build tech skills programme"
  - "technical training plan"
  - "engineering upskilling"
  - "technical learning path"
  - "developer skills programme"
---

# technical-skills-programme

## Agent: Agent Trainer & Skill Optimizer

L2 Agent Trainer and Skill Optimizer (1x) responsible for evaluating existing skills, running evals, optimising prompts, improving agent performance, and training new agent configurations.

Department ethos: [ideal-agent-operations.md](../../../../departments/agent-operations/ideal-agent-operations.md)

## Skill Description

Builds the retraining and prompt update programme when the underlying model changes, ensuring skill continuity across model transitions.

## When to Use

- When a model provider releases a new version and existing agents need migration assessment.
- When a model is being deprecated and all dependent agents must transition to an alternative.
- When performance benchmarks show that a model update has changed behavior in ways that break existing skills.

## Workflow

1. **Impact Assessment**: Identify all agents and skills affected by the model change. Map which skills depend on model-specific behaviors (output format, reasoning patterns, capability boundaries). Deliverable: impact assessment matrix.
2. **Regression Testing**: Run all affected skills against the new model using existing evaluation suites. Compare outputs to baseline expectations. Identify regressions. Deliverable: regression test results with diff analysis.
3. **Design Update Programme**: For each regressed skill, determine the fix -- prompt adjustment, context restructuring, output parsing update, or skill rewrite. Sequence updates by priority. Deliverable: update programme with per-skill fix plans.
4. **Execute Updates**: Implement prompt and configuration changes for each affected skill. Re-run evaluations after each update to confirm the fix resolves the regression without introducing new issues. Deliverable: updated skill configurations with passing evaluations.
5. **Deploy and Monitor**: Roll out updated skills to production with monitoring for the first evaluation cycle. Track post-deployment metrics against pre-change baselines. Deliverable: deployment confirmation with monitoring dashboard.

## Anti-Patterns

- **Big-bang model swap**: Switching all agents to a new model simultaneously without regression testing. *Why*: untested model changes can break skills in unpredictable ways; a single bad swap can take down fleet-wide capabilities.
- **Prompt-only fixes**: Assuming all model-change regressions can be fixed by prompt tweaks without considering structural changes. *Why*: some model behavior changes are fundamental and require workflow redesign, not prompt hacking.
- **Ignoring capability changes**: Focusing only on regressions without checking for new model capabilities that could improve existing skills. *Why*: model upgrades often unlock better performance; treating them purely as risk misses improvement opportunities.

## Output

**On success**: Produces a model transition report containing regression test results, updated skill configurations, and post-deployment monitoring confirmation. Delivered to the VP Agent Operations and Agent Configuration Manager.

**On failure**: Report which skills could not be migrated (fundamental incompatibility, unavailable alternative model), what updates were attempted, and whether the old model must be retained for specific skills.

## Related Skills

- [`skills-gap-analyser`](../skills-gap-analyser/SKILL.md) -- Gap analysis may reveal model-change regressions as a root cause.
- [`compensation-benchmarking`](../../../agent-operations/agent-configuration-manager/compensation-benchmarking/SKILL.md) -- Model selection decisions that trigger retraining programmes.
- [`onboarding-programme-builder`](../onboarding-programme-builder/SKILL.md) -- Agents on new models need re-onboarding to validate performance.
