# Skill OS × Paperclip — Operator Quickstart

Connect Skill OS's 528 skills to your Paperclip AI company.

---

## 1. Setup

Clone Skill OS alongside your Paperclip company repo:

```bash
git clone https://github.com/mittuled/skill-os.git
```

Recommended layout:

```
my-company/
├── paperclip.json        # or however your Paperclip company is configured
└── skill-os/             # Skill OS clone
```

Verify Skill OS is healthy:

```bash
cd skill-os
python3 scripts/validate.py
# Expected: 0 errors
```

---

## 2. Find a Skill

Browse `agents/` by department:

```
skill-os/agents/
├── engineering/          sr-backend-developer, security-engineer, devops-infrastructure-engineer, ...
├── product/              product-manager, vp-product, pmm, ...
├── marketing/            demand-gen-manager, content-marketer, pr-communications-manager, ...
├── design/               ux-ui-designer, ux-researcher, brand-designer, ...
├── data-growth/          analytics-lead, data-analyst, growth-lead, ...
├── finance/              fpa-analyst, controller-accounting, investor-relations-manager, ...
├── legal/                corporate-counsel, product-counsel, security-compliance-programme-manager, ...
└── sales/                account-executive, sales-development-rep, sales-manager, ...
```

**Quick search**: Open `SKILLS.md` at the repo root and use Ctrl+F to search by keyword.

**Match your Paperclip role** → see `role-mapping.md` for the full mapping table.

Each skill lives at: `agents/<dept>/<agent>/<skill>/SKILL.md`

---

## 3. Configure an Agent

Set `instructionsFilePath` in your agent's `adapterConfig` to the skill path:

```json
{
  "adapterType": "claude_local",
  "adapterConfig": {
    "cwd": "/path/to/company-repo",
    "model": "claude-sonnet-4-6",
    "instructionsFilePath": "/path/to/skill-os/agents/product/product-manager/requirements-extractor/SKILL.md",
    "promptTemplate": "You are {{agent.title}} at {{company.name}}.\n\nCurrent task: {{issue.title}} ({{issue.identifier}})\nPriority: {{issue.priority}}\n\nBefore executing your skill workflow:\n1. Fetch full task context: GET /api/issues/{{issue.id}}/heartbeat-context\n2. Review the goal ancestry for strategic context\n3. Follow the workflow steps in your skill instructions exactly"
  }
}
```

**Model selection**:

| Skill complexity | Recommended model | Examples |
|-----------------|-------------------|---------|
| Simple / Medium (L1/L2) | `claude-sonnet-4-6` | `requirements-extractor`, `wireframe-builder`, `funnel-analyser` |
| Complex (L3) | `claude-opus-4-6` | `architecture-designer`, `threat-modelling`, `contract-review-orchestrator` |

Check a skill's complexity in its YAML frontmatter: `complexity: simple|medium|complex`

---

## 4. Routing via Labels

For agents that handle multiple task types, use Paperclip issue labels to load the right skill automatically.

**Step 1**: Create labels in Paperclip (Settings → Labels):
- For a `pm` agent: `prd`, `user-story`, `experiment`, `sprint-planning`
- For an `engineer` agent: `backend-api`, `threat-model`, `ci-pipeline`, `code-review`

**Step 2**: Copy `skill-routing-table.yaml` and customize it:

```yaml
version: "1.0"
skill_os_root: "./skill-os"

bindings:
  - role: pm
    label: prd
    skill_path: agents/product/product-manager/requirements-extractor/SKILL.md

  - role: pm
    label: experiment
    skill_path: agents/product/product-manager/demand-validator/SKILL.md

  - role: engineer
    label: threat-model
    skill_path: agents/engineering/security-engineer/threat-modelling/SKILL.md
    model_override: claude-opus-4-6
```

**Matching logic**: `role` + `IssueLabel.name` → first matching binding wins. If no binding matches, `fallback_ethos` is used.

**v1 limitation**: In v1, set `instructionsFilePath` statically per agent. The routing table is your reference for which skill to set. Dynamic label-switching (auto-changing `instructionsFilePath` per task) requires a Paperclip adapter plugin (planned for v2).

---

## 5. Activation Levels

Skill OS supports three activation levels (FR-007):

### Level 1 — Agent-wide (all tasks)
Set `instructionsFilePath` in the agent's `adapterConfig`. Every task this agent receives uses the same skill. Best for single-purpose agents.

```json
{ "adapterConfig": { "instructionsFilePath": "/path/to/SKILL.md" } }
```

### Level 2 — Task-tag (label-based)
Use `skill-routing-table.yaml` as your reference. Manually update `instructionsFilePath` when creating a task of a specific type, or maintain separate agent instances per skill type (one PM agent per label).

### Level 3 — Single-task override
For a one-off task that needs a different skill than the agent's default:

1. PATCH the agent's config before dispatching:
   ```
   PATCH /api/agents/{agentId}
   Body: { "adapterConfig": { "instructionsFilePath": "/path/to/override-skill/SKILL.md" } }
   ```
2. Create and dispatch the task
3. After the task completes, restore the original `instructionsFilePath`:
   ```
   PATCH /api/agents/{agentId}
   Body: { "adapterConfig": { "instructionsFilePath": "/path/to/original-skill/SKILL.md" } }
   ```

---

## 6. Progressive Loading

Skill OS uses a three-tier loading model to stay within token budgets:

| Tier | Content | Size | When loaded |
|------|---------|------|-------------|
| 1 | YAML frontmatter | ~100 words | Always (part of SKILL.md) |
| 2 | Skill body | ≤500 (simple) / ≤1,000 (medium) / ≤1,500 (complex) words | Always (via `instructionsFilePath`) |
| 3 | References & assets | Unlimited | On demand, when needed |

**Loading references on demand**: When a skill workflow step says "use the scoring rubric", instruct your agent to read it at that step — not upfront:

```
promptTemplate: |
  ...your standard prompt...

  When a workflow step references a file in references/ or assets/:
  Read that file at the moment you need it:
    Read: {{skill_os_root}}/agents/<dept>/<agent>/<skill>/references/<file>.md
  Do not preload all reference files — fetch only what you need, when you need it.
```

**Recommended `budgetMonthlyCents` by agent type**:

| Agent type | Typical monthly budget |
|-----------|----------------------|
| Single-skill, low volume (5–10 tasks/day) | $10–25 (1000–2500¢) |
| Multi-skill, medium volume (20–50 tasks/day) | $50–100 (5000–10000¢) |
| Heavy usage / L3 complex skills | $150–300 (15000–30000¢) |

---

## 7. [GATE] Handling

Some complex skills include `[GATE]` markers on high-stakes workflow steps:

```
5. Draft the final architecture decision record. [GATE]
```

Include this in your `promptTemplate` to handle gates correctly:

```
When you reach a step marked [GATE]:
1. Complete all work up to that point
2. Post your current output as a comment on the issue
3. Create an approval request: POST /api/approvals
   Body: { "issueId": "{{issue.id}}", "subject": "Gate: [step description]", "description": "[your work so far]" }
4. PATCH /api/issues/{{issue.id}} with status "blocked"
5. Stop — do not proceed until the approval is granted
```

When the human approves, Paperclip will wake the agent again with `PAPERCLIP_WAKE_REASON=approval_granted` and `PAPERCLIP_APPROVAL_STATUS=approved`. The agent should then continue from the step after the gate.

---

## 8. Troubleshooting

**Agent isn't following the skill workflow**
- Verify `instructionsFilePath` points to the correct `SKILL.md` and the file exists: `ls <path>`
- Check that the file is readable by the process running Claude Code
- Run: `python3 scripts/validate.py agents/<dept>/<agent>/<skill>/SKILL.md`

**Output doesn't match the expected template**
- The asset template lives at `assets/<skill>-template.md` inside the skill directory
- Add to your `promptTemplate`: `"Use the output template at <path>/assets/<name>-template.md to format your response."`

**Token budget exceeded mid-task**
- Reduce `maxTurnsPerRun` in `adapterConfig` (most medium skills complete in 10–20 turns)
- Switch to progressive loading for reference files (see section 6)
- Consider `claude-haiku-4-5` for high-volume simple skills

**Skill version mismatch after Skill OS update**
- Pin `skill_version` to a git SHA in your routing table: `skill_version: "a1b2c3d"`
- This ensures your production agents don't pick up breaking changes from Skill OS updates
- To upgrade: test the new skill version on a staging agent first, then update the SHA

**How to verify a skill path is valid**
```bash
# From skill-os root
ls agents/product/product-manager/requirements-extractor/SKILL.md
python3 scripts/validate.py agents/product/product-manager/requirements-extractor/SKILL.md
```
