---
name: compliance-training-manager
description: >
  This skill validates that all agents meet security, privacy, and regulatory
  constraints. Use when asked to run compliance checks, audit agent behavior
  for policy violations, or prepare for a security review. Also consider when
  regulations change or new data handling rules are introduced. Suggest when
  the user deploys agents handling sensitive data without compliance validation.
department: agent-operations
agent: agent-trainer-skill-optimizer
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "manage compliance training"
  - "run compliance programme"
  - "compliance training setup"
  - "mandatory training tracker"
  - "compliance learning plan"
---

# compliance-training-manager

## Agent: Agent Trainer & Skill Optimizer

L2 Agent Trainer and Skill Optimizer (1x) responsible for evaluating existing skills, running evals, optimising prompts, improving agent performance, and training new agent configurations.

Department ethos: [ideal-agent-operations.md](../../../../departments/agent-operations/ideal-agent-operations.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Validates that all agents meet security, privacy, and regulatory constraints through systematic compliance testing and certification.

## When to Use

- When a compliance audit is scheduled or a regulatory review is approaching.
- When new security or privacy regulations are introduced that affect agent behavior.
- When agents are handling sensitive data (PII, financial, health) and compliance has not been verified.

## Workflow

1. **Inventory Compliance Requirements**: Collect all applicable security, privacy, and regulatory constraints from the governance handbook, legal team, and industry standards. Deliverable: compliance requirements checklist.
2. **Design Compliance Tests**: Create test cases for each requirement -- input scenarios that probe boundary conditions, data handling, and prohibited behaviors. Deliverable: compliance test suite.
3. **Execute Compliance Evaluation**: Run each agent through the compliance test suite. Record pass/fail per test case with evidence (output samples, log entries). Deliverable: compliance evaluation results per agent.
4. **Remediate Failures**: For agents that fail compliance tests, identify the root cause (prompt gap, missing guardrail, tool misconfiguration) and prescribe fixes. Deliverable: remediation plan per failing agent.
5. **Certify and Document**: Issue compliance certification for agents that pass all tests. Document any accepted risks with mitigation plans. Schedule next review cycle. Deliverable: compliance certificates and risk register.

## Anti-Patterns

- **One-time compliance**: Running compliance checks only at deployment and never again. *Why*: model updates, prompt changes, and new tool integrations can introduce compliance regressions at any time.
- **Testing only known scenarios**: Limiting compliance tests to previously encountered situations without adversarial or edge-case testing. *Why*: compliance failures most often occur in unexpected scenarios that routine tests miss.
- **Compliance without enforcement**: Identifying violations but not blocking non-compliant agents from production. *Why*: documented violations without enforcement create legal liability and false assurance.

## Output

**On success**: Produces compliance evaluation results, per-agent compliance certificates, and an updated risk register. Delivered to the VP Agent Operations and legal/security stakeholders.

**On failure**: Report which agents could not be evaluated (test infrastructure issues, unavailable agents), what compliance gaps were found, and what remediation is required before certification.

## Related Skills

- [`employee-handbook-v1`](../../../agent-operations/vp-agent-operations/employee-handbook-v1/SKILL.md) -- Governance policies that define the compliance baseline.
- [`culture-and-performance-system`](../../../agent-operations/vp-agent-operations/culture-and-performance-system/SKILL.md) -- Performance reviews incorporate compliance status.
- [`team-health-monitor`](../../../agent-operations/agent-operations-manager/team-health-monitor/SKILL.md) -- Runtime compliance violations may surface as health anomalies.
