# Contributing to Skill OS

Thanks for contributing. Every skill you add makes AI agents across every role more capable.

---

## Before you write anything

Read [`ETHOS.md`](ETHOS.md). It defines the depth standard. The single most common reason PRs get rejected is writing generic advice instead of practitioner-depth content.

The test: would the best person in this role look at this skill and say "yes, that's exactly how I'd do it"? Or would they say "this is how someone who's never done this job imagines it works"?

---

## Adding a new skill

### 1. Check what's already there

Browse `agents/` for the agent role. Check `SKILLS.md` for existing coverage. Don't add a skill that duplicates something already there.

### 2. Create the skill directory

```bash
mkdir -p agents/<agent-slug>/<skill-slug>/
```

Agent slugs match the directory names in `agents/` (e.g. `account-executive`, `sr-backend-developer`).

### 3. Write `SKILL.md`

Use the template at `specs/001-enrich-skill-directory/contracts/skill-template.md`.

Required: YAML frontmatter + 9 sections. Word limits are hard errors, not guidelines:
- `simple`: 500 words max
- `medium`: 1,000 words max  
- `complex`: 1,500 words max

```yaml
---
name: Your Skill Name
description: One pushy sentence starting with a verb — what this skill does and why it matters.
department: Engineering
agent: sr-backend-developer
version: "1.0"
complexity: medium
related-skills:
  - other-skill-slug
---
```

### 4. Add production-grade depth artifacts

Every skill needs both `references/` and `assets/` populated:

| Skill type | References file | Assets file |
|-----------|-----------------|-------------|
| Assessment (auditor, reviewer, analyser) | `scoring-rubric.md` — named dimensions, grade bands A+→F | `<name>-report-template.md` — 80-150 lines |
| Output (builder, generator, writer, creator) | `framework.md` or `checklist.md` | `<output>-template.md` — 80-150 lines |
| Workflow (runner, coordinator, planner) | `framework.md` or `checklist.md` | Optional but recommended |

References files should be 50-120 lines with named frameworks, concrete thresholds, and decision tables — not generic advice.

### 5. Validate

```bash
python3 scripts/validate.py agents/<agent>/<skill>/SKILL.md
```

Fix all errors before opening a PR. Warnings are informational.

### 6. Commit and PR

One skill per commit:
```
Enrich skill: <skill-slug> for <Agent Role>
```

Never batch multiple skills in one commit. This makes reviews easier and history cleaner.

---

## Deepening an existing skill

If a skill already exists but lacks `references/` or `assets/`, add them:

```
Deepen skill: <skill-slug> for <Agent Role>
```

If you're improving the `SKILL.md` body itself:

```
Improve skill: <skill-slug> for <Agent Role>
```

---

## Skill quality checklist

Before opening a PR:

- [ ] Workflow steps use imperative voice ("Run X", "Draft Y", not "You should run X")
- [ ] Every workflow step has a named deliverable
- [ ] Anti-patterns include a rationale (not just "don't do X" but "don't do X because Y")
- [ ] Frameworks are named (e.g. "RICE scoring" not "a prioritisation framework")
- [ ] No generic advice — every sentence should be specific enough that a practitioner could act on it
- [ ] Word limit not exceeded
- [ ] Validation passes with 0 errors
- [ ] Related skills cross-references are bidirectional

---

## What we won't merge

- Skills that skim the surface or repeat generic AI advice
- Skills that exceed word limits
- Skills without both `references/` and `assets/` directories
- Multiple skills in one commit
- Skills for roles not in the org chart (open an issue to propose new roles)

---

## Proposing a new agent role

Open an issue with:
- The role title and seniority level (L1/L2/L3)
- The department it belongs to
- 3-5 skills you'd add for it
- Why it's not already covered by an existing role

---

## Questions

Open an issue. We try to respond within a few days.
