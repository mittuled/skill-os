# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

`skill-os` is the world's most comprehensive open-source directory of AI work agent skills. It maps 86 agent roles across 15 departments to 600+ skills — each enriched with executable workflows, anti-patterns, output templates, and cross-references. See `ETHOS.md` for the operating philosophy.

The primary reference document is `restructured-org-chart-v3.md` (canonical org chart). The constitution is at `.specify/memory/constitution.md` (v2.0.0).

## Directory Structure

```
skill-os/
├── ETHOS.md                      # Operating philosophy
├── CLAUDE.md                     # This file
├── restructured-org-chart-v3.md  # Canonical org chart
├── status.md                     # Enrichment progress tracker
├── allowed-tools.yaml            # Tool policy: 4-level access control
├── departments/                  # Department ethos profiles + shared context
│   └── <dept>/
│       ├── ideal-<dept>.md       # Ethos profile (max 500 words)
│       └── references/           # Department-wide shared refs
├── agents/                       # Agent directories with enriched skills
│   └── <agent>/
│       ├── references/           # Agent-wide shared context
│       └── <skill>/
│           ├── SKILL.md          # Enriched skill file
│           ├── references/       # Skill-specific refs
│           ├── examples/         # Input/output pairs
│           ├── scripts/          # Executable helpers
│           └── assets/           # Output templates
├── _shared/                      # Cross-department resources
│   ├── references/
│   ├── scripts/
│   └── assets/
└── scripts/
    └── validate.py               # Skill validation script
```

## Org Structure

5 C-levels: **CEO, CTO, CPO, CBO, COO, CoS**

- **CTO** → Engineering, Tech Ops (dotted line)
- **CPO** → Product, Design, Data & Growth, Research
- **CBO** → Marketing, Sales, Customer Success, Account Management
- **COO** → RevOps, Support, Finance, Legal, Agent Ops, Implementation, Tech Ops

Roles are tagged with seniority level (`L1`/`L2`/`L3`) and instance count (`1x` singleton or `Nx` multi-instance).

## Enriched Skill File Format (Constitution v2.0.0)

Every enriched skill lives at `agents/<agent-slug>/<skill-slug>/SKILL.md` with YAML frontmatter and 9 sections:

1. **YAML frontmatter**: `name`, `description` (pushy), `department`, `agent`, `version`, `complexity`, `related-skills`, optional `triggers` (list of activation phrases, 5-50 chars each)
2. **Title**: `# <skill-slug>`
3. **Agent header**: Seniority + role description + ethos profile reference + tool policy reference
4. **Skill Description**: One sentence, third-person declarative
5. **When to Use**: Trigger scenarios (min 1)
6. **Workflow**: Imperative numbered steps with deliverables. High-stakes steps may include `[GATE]` markers requiring explicit approval before proceeding.
7. **Anti-Patterns**: What to avoid + why (rationale required)
8. **Output**: Success artifacts + failure reporting
9. **Related Skills**: Bidirectional cross-references with rationale

Word limits by complexity: Simple (500), Medium (1,000), Complex (1,500). Hard errors — not guidelines.

See `specs/001-enrich-skill-directory/contracts/skill-template.md` for the full template.

## Enriching a Skill

1. Create skill subdirectory: `mkdir -p agents/<agent>/<skill>/`
2. Migrate: `git mv agents/<agent>/<skill>.md agents/<agent>/<skill>/SKILL.md`
3. Add YAML frontmatter with pushy description
4. Write all 9 sections using imperative voice for Workflow
5. Add ethos reference: `Department ethos: [ideal-<dept>.md](../../../departments/<dept>/ideal-<dept>.md)`
6. Validate: `python3 scripts/validate.py agents/<agent>/<skill>/SKILL.md`
7. Commit: one skill per commit

See `specs/001-enrich-skill-directory/quickstart.md` for the full guide.

## Validation

```bash
python3 scripts/validate.py                    # Full repo
python3 scripts/validate.py agents/<agent>/    # One agent
python3 scripts/validate.py agents/<agent>/<skill>/SKILL.md  # One skill
```

## Context Lookup Chain

When an AI agent needs resources: skill → agent → department → `_shared/`. Most specific wins.

## Tool Policy

`allowed-tools.yaml` at repo root defines a 4-level access model for tool permissions:

1. **Company-wide**: Tools available to all agents (e.g., GitHub, Slack)
2. **Department**: Tools scoped to a department (e.g., Figma for Design)
3. **Agent**: Tools scoped to a specific agent role
4. **Skill**: Tools scoped to a single skill execution

Agents reference the tool policy via their Agent header: `Tool policy: [allowed-tools.yaml](../../allowed-tools.yaml)`. The `tool-policy-manager` skill governs ongoing changes. The `company-tooling-onboarder` skill handles initial tool discovery and connection.

## Commit Discipline

- Every skill enrichment = 1 commit
- Format: `Enrich skill: <skill-slug> for <Agent Role>`
- Never batch multiple skills in one commit

## Active Technologies
- Markdown + YAML (content project) + None (zero external deps) (003-production-grade-depth)

- Python 3.10+ for executable scripts, Bash for shell helpers
- Markdown + YAML for skill files and policy files
- Zero external dependencies — scripts use stdlib only
- Git-managed filesystem; credentials in platform-native secret stores (never in repo)

## Recent Changes
- 003-production-grade-depth: Added Markdown + YAML (content project) + None (zero external deps)
