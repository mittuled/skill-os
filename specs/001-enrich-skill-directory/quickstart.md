# Quickstart: How to Enrich a Skill

## Prerequisites

- The department's ethos profile (`departments/<dept>/ideal-<dept>.md`) must exist
- You have domain knowledge for the skill you're enriching (or access to someone who does)
- You know which complexity class the skill falls into (simple/medium/complex)

## Step 1: Create the Skill Subdirectory

```bash
# Move the flat file into a subdirectory
mkdir -p agents/<agent>/<skill>/
git mv agents/<agent>/<skill>.md agents/<agent>/<skill>/SKILL.md
```

## Step 2: Add YAML Frontmatter

Open `agents/<agent>/<skill>/SKILL.md` and add frontmatter at the top:

```yaml
---
name: <skill-slug>
description: >
  This skill <what it does>. Use when asked to <trigger>.
  Also consider when <adjacent scenario>.
  Suggest when the user is about to <proactive trigger>.
department: <dept>
agent: <agent>
version: 1.0.0
complexity: simple
related-skills: []
---
```

Write the description "pushy" — include trigger phrases so AI agents know when to activate.

## Step 3: Expand the Body

Keep the existing Agent header and Skill Description. Add the new sections:

1. **When to Use**: Write 2-3 concrete trigger scenarios
2. **Workflow**: Write numbered imperative steps with deliverables
3. **Anti-Patterns**: List what to avoid with rationale explaining *why*
4. **Output**: Define success artifacts AND failure reporting
5. **Related Skills**: Link to skills that interact with this one

Use the template at `specs/001-enrich-skill-directory/contracts/skill-template.md`.

## Step 4: Add the Ethos Reference

In the Agent header section, add:

```markdown
Department ethos: [ideal-<dept>.md](../../../departments/<dept>/ideal-<dept>.md)
```

## Step 5: Check Word Limits

| Complexity | Max words (body only, excluding frontmatter) |
|------------|----------------------------------------------|
| Simple | 500 |
| Medium | 1,000 |
| Complex | 1,500 |

If you're over the limit, move detailed content to `references/`:

```bash
mkdir -p agents/<agent>/<skill>/references/
# Move detailed methodology, scoring rubrics, etc. into reference files
# Add pointers from SKILL.md: "See references/scoring-rubric.md for the full rubric."
```

## Step 6: Add Supporting Context (Optional)

```bash
# Only create directories you actually need
mkdir -p agents/<agent>/<skill>/examples/    # Input/output pairs
mkdir -p agents/<agent>/<skill>/scripts/     # Executable helpers
mkdir -p agents/<agent>/<skill>/assets/      # Output templates
mkdir -p agents/<agent>/<skill>/evals/       # Test prompts
```

## Step 7: Validate

```bash
python scripts/validate.py agents/<agent>/<skill>/SKILL.md
```

Checks: frontmatter fields, word count, cross-references, ethos reference.

## Step 8: Commit

```bash
git add agents/<agent>/<skill>/
git commit -m "Enrich skill: <skill-slug> for <Agent Role Name>"
```

## Writing Tips

- **Workflow**: Use imperative voice. "Identify the risks." not "The agent identifies risks."
- **Anti-Patterns**: Always explain why. "Don't skip legal review — unsigned contracts without legal review have caused $X liability exposure."
- **Descriptions**: Be pushy. Include "Use when...", "Also consider when...", "Suggest when the user is about to..."
- **Keep it lean**: If you're writing paragraphs, you're probably over the word limit. Move detail to `references/`.

## Complexity Classification Guide

| Class | Signal | Examples |
|-------|--------|---------|
| Simple | Single-phase, one deliverable, no branching logic | `press-release-writer`, `blog-post-writer`, `helpdesk-responder` |
| Medium | Multi-phase, moderate decision logic, 2-3 deliverables | `threat-modelling`, `deal-qualifier`, `contract-reviewer` |
| Complex | Scoring rubrics, multiple decision branches, cross-agent coordination, 4+ deliverables | `vendor-risk-assessor`, `product-launch-coordinator`, `incident-commander-escalation` |
