# Quickstart: Using Skill OS with Paperclip

Connect Skill OS's 528 skills to your Paperclip AI company in 5 steps.

---

## How it works

Paperclip gives agents a role and a task. Skill OS gives them the expertise to execute that task the way the best human in that role would.

Each Skill OS skill is a markdown file (`SKILL.md`) with:
- A structured workflow (imperative steps with deliverables)
- Anti-patterns with rationale
- Output templates in `assets/`
- Reference frameworks in `references/`

You load a skill into a Paperclip agent via `adapterConfig.instructionsFilePath`. The agent then follows the skill's workflow when it receives a task.

---

## Step 1: Clone Skill OS

```bash
git clone https://github.com/mittuled/skill-os.git
```

Place it somewhere accessible from your Paperclip company repo. A common pattern:

```
my-company/
├── paperclip/           # Paperclip company config
└── skill-os/            # Skill OS repo (cloned)
```

---

## Step 2: Find the right skill

Browse `agents/` organized by department:

```
agents/
├── engineering/          # vp-engineering, sr-backend-developer, security-engineer, ...
├── product/              # product-manager, vp-product, pmm, ...
├── marketing/            # demand-gen-manager, content-marketer, ...
├── design/               # ux-ui-designer, ux-researcher, ...
├── data-growth/          # analytics-lead, growth-lead, ...
├── finance/              # fpa-analyst, controller-accounting, ...
├── legal/                # corporate-counsel, product-counsel, ...
└── sales/                # account-executive, sales-development-rep, ...
```

Use `SKILLS.md` at the repo root to search by keyword.

Each skill lives at: `agents/<dept>/<agent>/<skill>/SKILL.md`

**Match Paperclip roles to Skill OS agents**:

| Paperclip Role | Best-fit Skill OS Agents |
|----------------|--------------------------|
| `engineer` | `sr-backend-developer`, `sr-frontend-developer`, `security-engineer`, `devops-infrastructure-engineer` |
| `pm` | `product-manager`, `vp-product` |
| `designer` | `ux-ui-designer`, `ux-researcher`, `brand-designer` |
| `qa` | `qa-test-engineer` |
| `devops` | `devops-infrastructure-engineer`, `platform-engineer` |
| `researcher` | `analytics-lead`, `data-analyst`, `applied-research-lead` |
| `cto` | `tech-architect`, `vp-engineering` |
| `cmo` | `vp-marketing` |
| `cfo` | `cfo-vp-finance`, `fpa-analyst` |
| `general` | any agent from sales, legal, CS, support, RevOps |

---

## Step 3: Configure the agent

In your Paperclip agent's `adapterConfig`, set `instructionsFilePath` to the skill path:

```json
{
  "adapterType": "claude_local",
  "adapterConfig": {
    "cwd": "/path/to/company-repo",
    "model": "claude-sonnet-4-6",
    "instructionsFilePath": "/path/to/skill-os/agents/product/product-manager/prd-author/SKILL.md",
    "promptTemplate": "You are {{agent.title}} at {{company.name}}.\n\nCurrent task: {{issue.title}} ({{issue.identifier}})\nPriority: {{issue.priority}}\n\nBefore executing your skill workflow, fetch full context:\nGET /api/issues/{{issue.id}}/heartbeat-context\n\nThen follow the workflow in your instructions exactly."
  }
}
```

**Model selection**:
- `claude-sonnet-4-6` — most skills (L1/L2, simple/medium complexity)
- `claude-opus-4-6` — L3 skills and `complex` complexity skills (e.g., `threat-modelling`, `system-design-author`, `contract-review-orchestrator`)

---

## Step 4: Set up skill routing with issue labels

For agents that handle multiple task types, use Paperclip issue labels to route to different skills.

**Create labels in Paperclip** (Settings → Labels):
- `prd`, `user-story`, `experiment`, `bug-triage` → for `pm` agents
- `backend-api`, `threat-model`, `code-review`, `ci-pipeline` → for `engineer` agents

**Use a routing config file** (`paperclip/skill-routing-table.yaml`):

```yaml
version: "1.0"
skill_os_root: "../skill-os"

bindings:
  - role: pm
    label: prd
    skill_path: agents/product/product-manager/prd-author/SKILL.md

  - role: pm
    label: experiment
    skill_path: agents/product/product-manager/experiment-designer/SKILL.md

  - role: engineer
    label: threat-model
    skill_path: agents/engineering/security-engineer/threat-modelling/SKILL.md
    model_override: claude-opus-4-6

  - role: engineer
    label: backend-api
    skill_path: agents/engineering/sr-backend-developer/builder/SKILL.md
```

In v1, you set `instructionsFilePath` statically per agent. Dynamic label-based routing (auto-switching skills per task) is planned for v2.

---

## Step 5: Progressive loading (token budget)

Skill bodies are ≤1,500 words — they fit comfortably in any model's context. Reference files (`references/`) and templates (`assets/`) load on demand.

When your agent's skill workflow says "Use the scoring rubric in `references/scoring-rubric.md`", the agent should read that file at that step:

```
Read: /path/to/skill-os/agents/engineering/security-engineer/threat-modelling/references/framework.md
```

This keeps base context lean while making full depth available when needed.

**Recommended token budget**: 50,000–100,000 tokens/month per agent for most skill executions. Set `budgetMonthlyCents` accordingly in Paperclip.

---

## Handling [GATE] markers

Some complex skills include `[GATE]` markers on high-stakes steps:

```
5. Draft the final architecture decision record. [GATE]
```

When an agent reaches a `[GATE]` step, it should:
1. Complete all work up to that point
2. Post a comment to the Paperclip issue with the work-in-progress output
3. Create a Paperclip approval request: `POST /api/approvals`
4. Wait for human approval before continuing

In your `promptTemplate`, add:

```
When you reach a step marked [GATE]:
1. Post your current output as an issue comment
2. Create an approval request with subject "Gate: [step description]"
3. Set issue status to "blocked"
4. Stop work until the approval is granted
```

---

## Example configurations

See `paperclip/examples/` for ready-to-use configurations:
- `single-agent.yaml` — minimal single engineer agent
- `engineering-team.yaml` — 5-person eng team (CTO + 3 engineers + QA)
- `full-company.yaml` — full company (CEO, CTO, CMO, CFO, PM, engineer, designer)

---

## Troubleshooting

**Agent isn't following the skill workflow**: Check that `instructionsFilePath` points to the correct `SKILL.md` and the file exists. Run `python3 scripts/validate.py agents/<dept>/<agent>/<skill>/SKILL.md` to verify.

**Output doesn't match the expected template**: The asset template lives in `assets/<skill>-template.md`. Include it explicitly in your prompt: "Use the output template at `assets/<skill>-template.md` to format your response."

**Token budget exceeded mid-task**: Reduce `maxTurnsPerRun` in `adapterConfig`. Most medium-complexity skills complete in 10–20 turns.
