# Skill OS

The world's most comprehensive open-source directory of AI work agent skills.

**528 skills · 86 agent roles · 15 departments · production-grade depth**

Every skill ships with executable workflows, scoring rubrics, output templates, anti-patterns, and cross-references — written at the depth of the best human practitioners, not generic AI advice.

---

## What this is

Most AI agent prompts tell an agent *what* to do. Skill OS tells it *how the best people actually do it*.

Each skill is a structured markdown file containing:
- **Workflow** — imperative, numbered steps with named deliverables
- **Anti-patterns** — what to avoid and *why*, not just what
- **References** — named frameworks, decision tables, scoring rubrics (loaded on demand)
- **Assets** — production-ready output templates with realistic placeholders
- **Related skills** — bidirectional cross-references with rationale

Skills are scoped to an agent role (e.g. `account-executive`, `sr-backend-developer`, `pmm-product-marketing-manager`) so the context is always domain-specific, never generic.

---

## Coverage

| Department | Agents | Skills |
|-----------|--------|--------|
| Engineering | 12 | 100 |
| Product | 5 | 82 |
| Marketing | 12 | 60 |
| Data & Growth | 4 | 39 |
| Design | 8 | 43 |
| Finance | 5 | 32 |
| Legal & Compliance | 4 | 36 |
| Agent Operations | 6 | 27 |
| Sales | 7 | 27 |
| Customer Success | 6 | 21 |
| Customer Support | 2 | 9 |
| Technical Operations | 3 | 9 |
| Revenue Operations | 1 | 6 |
| Applied Research | 1 | 5 |
| Account Management | 2 | 5 |
| Implementation | 2 | 4 |
| **Total** | **80** | **528** |

Full org chart: [`AGENTS.md`](AGENTS.md)

---

## Structure

```
skill-os/
├── agents/                       # All skills live here
│   └── <agent-slug>/
│       └── <skill-slug>/
│           ├── SKILL.md          # Skill definition (YAML frontmatter + 9 sections)
│           ├── references/       # Frameworks, rubrics, checklists
│           ├── assets/           # Output templates
│           ├── examples/         # Input/output pairs
│           └── scripts/          # Executable helpers
├── departments/                  # Department ethos profiles
│   └── <dept>/
│       └── ideal-<dept>.md       # What excellent looks like in this department
├── _shared/                      # Cross-department resources
├── scripts/
│   └── validate.py               # Validation script (zero external deps)
├── allowed-tools.yaml            # 4-level tool access policy
├── ETHOS.md                      # Operating philosophy
└── status.md                     # Enrichment progress tracker
```

---

## Using a skill

Each `SKILL.md` is self-contained. Load it into your agent's context and the agent will follow the workflow, apply the anti-patterns, and produce output matching the template.

**Example — loading a skill into a Claude prompt:**
```
You are an Account Executive. Execute the following skill:

<skill>
[contents of agents/sales/account-executive/meeting-prep-builder/SKILL.md]
</skill>

Context: [your deal context here]
```

**Progressive loading** — the skill body stays within strict word limits (500/1,000/1,500 by complexity). Reference files and templates load on demand when the agent needs them, so they never bloat the base prompt.

**Context lookup chain**: skill → agent → department → `_shared/`. Most specific wins.

---

## Skill format

Every skill has YAML frontmatter and 9 sections:

```yaml
---
name: Meeting Prep Builder
description: Builds a battle-ready meeting brief so the AE walks in knowing the deal cold.
department: Sales
agent: account-executive
version: "1.0"
complexity: medium
related-skills:
  - deal-qualifier
  - sales-proposal-builder
---
```

Sections: title · agent header · skill description · when to use · workflow · anti-patterns · output · related skills

Full spec: [`specs/001-enrich-skill-directory/contracts/skill-template.md`](specs/001-enrich-skill-directory/contracts/skill-template.md)

---

## Integrations

### Paperclip

Connect Skill OS's 528 skills to [Paperclip](https://github.com/paperclipai/paperclip), the open-source AI agent orchestration platform.

Set `instructionsFilePath` in your Paperclip agent's `adapterConfig` to any `SKILL.md` path — the agent will follow that skill's workflow for every task it receives.

See [`paperclip/QUICKSTART.md`](paperclip/QUICKSTART.md) for setup, routing tables, [GATE] handling, and progressive loading guidance.

---

## Validation

```bash
python3 scripts/validate.py                              # Full repo
python3 scripts/validate.py agents/<agent>/              # One agent
python3 scripts/validate.py agents/<agent>/<skill>/SKILL.md  # One skill
```

No external dependencies. Requires Python 3.10+.

---

## Contributing

1. Pick an agent from the org chart
2. Check `status.md` for coverage gaps
3. Follow the format in [`CLAUDE.md`](CLAUDE.md) and the skill template
4. Validate before opening a PR
5. One skill per commit: `Enrich skill: <skill-slug> for <Agent Role>`

Read [`ETHOS.md`](ETHOS.md) before writing — it defines the depth standard.

---

## Philosophy

> *A skill that does one thing with genuine domain expertise is worth more than ten skills that skim the surface.*

Skills in this repo are written at practitioner depth — not what a generalist imagines a job looks like, but how the best people in that role actually work. Every framework is named. Every anti-pattern has a rationale. Every workflow step has a deliverable.

See [`ETHOS.md`](ETHOS.md) for the full philosophy.

---

## License

MIT
