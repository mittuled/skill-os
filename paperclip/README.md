# Skill OS × Paperclip Integration

Connect [Skill OS](../) to your [Paperclip](https://github.com/paperclipai/paperclip) AI company. Give every agent the domain expertise to execute tasks the way the best human in that role would.

**Paperclip gives agents a role and a task. Skill OS gives them the expertise to execute it.**

---

## Quick links

| File | Purpose |
|------|---------|
| [QUICKSTART.md](QUICKSTART.md) | Step-by-step operator guide |
| [skill-binding-schema.yaml](skill-binding-schema.yaml) | YAML schema for skill-binding configs |
| [skill-routing-table.yaml](skill-routing-table.yaml) | Default routing: 40 task labels → Skill OS skills |
| [role-mapping.md](role-mapping.md) | Paperclip roles → Skill OS agent directories |
| [examples/single-agent.yaml](examples/single-agent.yaml) | Minimal single-agent config |
| [examples/engineering-team.yaml](examples/engineering-team.yaml) | 5-person engineering team |
| [examples/full-company.yaml](examples/full-company.yaml) | 7-agent full company |

---

## How it works

1. An operator sets `adapterConfig.instructionsFilePath` on a Paperclip agent to point at a Skill OS `SKILL.md` file
2. When Paperclip dispatches a task, the skill is appended to Claude's system prompt via `--append-system-prompt-file`
3. The agent follows the skill's structured workflow, produces output matching the asset template, and respects `[GATE]` markers by creating Paperclip approval requests

---

## QUICKSTART.md section guide

The operator guide covers these sections in order:

1. **Setup** — clone Skill OS alongside your Paperclip company repo
2. **Find a Skill** — browse `agents/` by department, search via `SKILLS.md`
3. **Configure an Agent** — set `instructionsFilePath` and `promptTemplate`
4. **Routing via Labels** — use `skill-routing-table.yaml` for label-based dispatch
5. **Activation Levels** — agent-wide, task-tag, and single-task override patterns
6. **Progressive Loading** — token-budget strategy with three-tier loading model
7. **[GATE] Handling** — approval requests for high-stakes workflow steps
8. **Troubleshooting** — common issues and fixes

---

## Requirements

- Paperclip with `claude_local` adapter
- Claude Code CLI installed
- Skill OS cloned locally (this repo)
