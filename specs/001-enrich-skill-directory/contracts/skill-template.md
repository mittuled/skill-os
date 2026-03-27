---
name: <skill-slug>
description: >
  This skill <what it does in third person>. Use when asked to <trigger phrase 1>,
  <trigger phrase 2>, or <trigger phrase 3>. Also consider when <adjacent scenario>.
  Suggest when the user is about to <proactive trigger>.
department: <department-slug>
agent: <agent-slug>
version: 1.0.0
complexity: simple | medium | complex
related-skills:
  - ../../<other-agent>/<other-skill>/SKILL.md
triggers:                          # optional — 5-50 chars per item
  - "<short activation phrase 1>"
  - "<short activation phrase 2>"
---

# <skill-slug>

## Agent: <Agent Role Name>

<Seniority level (L1/L2/L3)> <role description> (<instance type: 1x or Nx>) responsible for <scope summary>.

Department ethos: [ideal-<dept>.md](../../../departments/<dept>/ideal-<dept>.md)
Tool policy: [allowed-tools.yaml](../../../allowed-tools.yaml)

## Skill Description

<One sentence in third-person declarative voice describing what this skill does.>

## When to Use

- When <concrete scenario 1 describing a situation where this skill should activate>.
- When <concrete scenario 2>.
- When <concrete scenario 3 — include at least one non-obvious trigger>.

## Workflow

1. **<Phase/Step Name>**: <Imperative instruction>. Deliverable: <what this step produces>.
2. **<Phase/Step Name>**: <Imperative instruction>. Deliverable: <what this step produces>.
3. **<Phase/Step Name>**: <Imperative instruction>. Deliverable: <what this step produces>.

<!-- For high-stakes steps, add [GATE] to require explicit approval before proceeding:
4. **[GATE] <Critical Step>**: <Imperative instruction requiring sign-off>. Deliverable: <what this step produces>.
-->

## Anti-Patterns

- **<Anti-pattern name>**: <What to avoid>. *Why*: <Explanation of why this is harmful — the reasoning that lets an agent generalize to novel situations>.
- **<Anti-pattern name>**: <What to avoid>. *Why*: <Rationale>.

## Output

**On success**: Produces <artifact type> in <format> containing <key content>. Delivered to <where/how>.

**On failure**: Report <what went wrong>, <what was attempted>, and <what to try next>. Every error must be actionable.

## Related Skills

- [`<related-skill-slug>`](../../<agent>/<skill>/SKILL.md) — <Brief rationale for the relationship>.
- [`<related-skill-slug>`](../../<agent>/<skill>/SKILL.md) — <Brief rationale>.
