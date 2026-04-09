---
name: engineering-talent-sourcer
description: >
  This skill builds, tests, and validates individual skills against specific
  capability requirements. Use when asked to create a new skill, write a
  SKILL.md file, or validate a skill against its specification. Also consider
  when an existing skill fails quality gates. Suggest when the user identifies
  a capability gap that needs a concrete skill implementation.
department: agent-operations
agent: skill-builder
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "source engineering talent"
  - "find engineers"
  - "engineer sourcing"
  - "technical candidate search"
  - "recruit engineers"
---

# engineering-talent-sourcer

## Agent: Skill Builder

L3 Skill Builder (Nx) responsible for building and testing individual SKILL.md files. Multiple Skill Builders can work across different domains simultaneously.

Department ethos: [ideal-agent-operations.md](../../../../departments/agent-operations/ideal-agent-operations.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Builds, tests, and validates individual skills against specific capability requirements and quality standards.

## When to Use

- When a skill specification has been assigned from the recruiting pipeline and needs to be implemented.
- When an existing skill has failed quality gates and needs to be rewritten or significantly revised.
- When a new agent role requires domain-specific skills that do not yet exist in the skill registry.

## Workflow

1. **Review Specification**: Read the skill specification including capability requirements, acceptance criteria, target agent, and complexity class. Identify any ambiguities and resolve with the Skill Builder Lead. Deliverable: confirmed skill specification.
2. **Research Domain**: Gather domain context -- department ethos, related skills, agent role description, and any reference materials. Understand how the skill fits into the agent's workflow. Deliverable: domain context notes.
3. **Draft Skill File**: Write the SKILL.md following the constitution template: YAML frontmatter, 9 sections, imperative workflow steps, anti-patterns with rationale, and cross-references. Stay within word limits. Deliverable: draft SKILL.md file.
4. **Test Against Criteria**: Validate the skill against acceptance criteria -- does the workflow produce the specified outputs? Are anti-patterns actionable? Are cross-references bidirectional? Deliverable: test results with pass/fail per criterion.
5. **Submit for Review**: Submit the completed skill to the Skill Builder Lead for quality gate review. Address any revision requests. Deliverable: approved SKILL.md registered in the skill directory.

## Anti-Patterns

- **Copy-paste skills**: Duplicating an existing skill and changing surface details without adapting the workflow to the new domain. *Why*: copied skills produce generic outputs that miss domain-specific nuances and edge cases.
- **Workflow without deliverables**: Writing workflow steps that describe activity without specifying what each step produces. *Why*: steps without deliverables cannot be validated, making quality assessment impossible.
- **Ignoring word limits**: Exceeding complexity-based word limits with verbose descriptions. *Why*: overly long skills dilute focus and increase the chance that agents skip or misinterpret critical instructions.

## Output

**On success**: Produces a validated SKILL.md file conforming to the constitution template, passing all acceptance criteria, and registered in the skill directory. Delivered to the Skill Builder Lead.

**On failure**: Report which acceptance criteria the skill failed, what revisions were attempted, and what domain clarifications are needed to produce a passing skill.

## Related Skills

- [`recruiting-pipeline-builder`](../../../agent-operations/skill-builder-lead/recruiting-pipeline-builder/SKILL.md) -- Provides the skill specifications and assignments this skill executes.
- [`scale-hiring-executor`](../../../agent-operations/skill-builder-lead/scale-hiring-executor/SKILL.md) -- Coordinates parallel execution when multiple skills are being built.
- [`skills-gap-analyser`](../../../agent-operations/agent-trainer-skill-optimizer/skills-gap-analyser/SKILL.md) -- Identifies skill deficiencies that may require new skills to be built.
