# Research: Skill OS × Paperclip Integration

**Phase 0 Output** | **Date**: 2026-04-08

---

## Q1: How does Paperclip deliver context to agents?

**Decision**: Context is delivered through three simultaneous channels — env vars, stdin prompt, and a file path reference — plus an API pull model for full goal ancestry.

**Evidence**:
- `execute.ts` injects `PAPERCLIP_TASK_ID`, `PAPERCLIP_WAKE_REASON`, `PAPERCLIP_WAKE_PAYLOAD_JSON`, and workspace vars as environment variables
- The full heartbeat prompt is piped as stdin to `claude --print -`
- `adapterConfig.instructionsFilePath` causes the file to be read at runtime and appended via `--append-system-prompt-file`
- The heartbeat system prompt instructs agents to call `GET /api/issues/{issueId}/heartbeat-context` to pull full goal ancestry from the API

**Implication**: Skill OS `SKILL.md` files should be referenced via `instructionsFilePath` — this is the idiomatic channel for rich agent instructions. The skill workflow steps can reference `PAPERCLIP_TASK_ID` and the heartbeat-context API as the authoritative source of what work to do.

---

## Q2: What task tag format does Paperclip support?

**Decision**: Tasks use structured `IssueLabel` objects (id/name/color), not free-form string tags. Priority and status are enums.

**Evidence** (`packages/shared/src/types/issue.ts`):
```typescript
export interface IssueLabel { id: string; companyId: string; name: string; color: string; }
export type IssueStatus = "backlog" | "todo" | "in_progress" | "in_review" | "done" | "blocked" | "cancelled";
export type IssuePriority = "critical" | "high" | "medium" | "low";
```

**Alternatives considered**: Free-form string tags would be simpler but aren't how Paperclip models labels.

**Implication**: The Skill OS routing table maps `IssueLabel.name` values to skill slugs. Operators create company-scoped labels (e.g., `prd`, `meeting-prep`, `threat-model`) and the routing table matches against `label.name`. Priority enums can also be used as secondary routing signals.

---

## Q3: What are Paperclip's default role names?

**Decision**: 11 exact role slugs defined as a TypeScript const enum.

**Evidence** (`packages/shared/src/constants.ts`):
```
"ceo", "cto", "cmo", "cfo", "engineer", "designer", "pm", "qa", "devops", "researcher", "general"
```

**Mapping to Skill OS agent roles**:

| Paperclip Role | Skill OS Agents |
|----------------|-----------------|
| `ceo` | (no direct mapping — `general`) |
| `cto` | `vp-engineering`, `tech-architect` |
| `cmo` | `vp-marketing` |
| `cfo` | `cfo-vp-finance` |
| `engineer` | `sr-backend-developer`, `sr-frontend-developer`, `devops-infrastructure-engineer`, `security-engineer`, `ai-ml-engineer`, `platform-engineer`, `data-engineer`, `qa-test-engineer` |
| `designer` | `ux-ui-designer`, `brand-designer`, `ux-researcher` |
| `pm` | `product-manager`, `vp-product` |
| `qa` | `qa-test-engineer` |
| `devops` | `devops-infrastructure-engineer`, `platform-engineer` |
| `researcher` | `applied-research-lead`, `analytics-lead` |
| `general` | all others (sales, legal, CS, support, etc.) |

**Implication**: The routing config uses `role` + `label.name` as the composite key. A single Paperclip `engineer` agent can load different Skill OS skills based on the issue label (e.g., `label:prd` → `prd-author`, `label:threat-model` → `threat-modelling`).

---

## Q4: Does Paperclip support file path references?

**Decision**: Yes — `adapterConfig.instructionsFilePath` is the idiomatic way to load rich agent instructions as a file reference, not inline content.

**Evidence**: `execute.ts` reads the file at runtime, appends a path directive comment, writes to a temp file, and passes `--append-system-prompt-file` to Claude CLI.

**Alternatives considered**: Inline `promptTemplate` content — rejected because it would require inlining entire SKILL.md bodies into the Paperclip agent configuration, making them unmanageable and breaking the progressive disclosure model.

**Implication**: The Paperclip integration config specifies `instructionsFilePath: "path/to/SKILL.md"` per agent. Operators point this at the relevant Skill OS skill path in their local repo checkout. This means Skill OS must be cloned alongside the Paperclip company repo, or the paths must be absolute.

---

## Q5: Agent configuration schema

**Decision**: The relevant fields for Skill OS integration are: `role`, `title`, `capabilities`, `adapterConfig.instructionsFilePath`, `adapterConfig.promptTemplate`, and `budgetMonthlyCents`.

**Evidence** (`packages/shared/src/types/agent.ts` + `docs/adapters/claude-local.md`):
- `capabilities: string | null` — free-form text describing what the agent can do; can reference Skill OS department + skill scope
- `adapterConfig.instructionsFilePath` — path to the primary instruction file (maps to `SKILL.md`)
- `adapterConfig.promptTemplate` — Handlebars template for wake prompt (can inject `{{agent.title}}` and task context)
- `adapterConfig.model` — Claude model to use (recommend `claude-sonnet-4-6` for most skills, `claude-opus-4-6` for complex/L3 skills)

---

## Q6: Heartbeat dispatch and task checkout

**Decision**: Agents receive a compact wake payload (issue ID, reason, comment batch) at heartbeat, then must call `GET /api/issues/{issueId}/heartbeat-context` for full goal ancestry before starting work.

**Evidence** (`heartbeat-system.txt`, `server-utils.ts`):
```
PaperclipWakePayload: { reason, issue: { id, identifier, title, status, priority }, commentIds, comments, fallbackFetchNeeded }
```

**Implication**: Skill OS workflow steps should include a preamble step: "Fetch full task context via `GET /api/issues/$PAPERCLIP_TASK_ID/heartbeat-context` before beginning the workflow." This ensures the agent has goal ancestry (e.g., parent goal: "Reach $1M MRR") in addition to the immediate task.

---

## Summary of Decisions

| Question | Decision |
|----------|----------|
| Context delivery | Use `instructionsFilePath` for SKILL.md; env vars provide task identifiers |
| Task routing key | `role` + `IssueLabel.name` composite key |
| Role mapping | 11 Paperclip roles → 80 Skill OS agents via mapping table |
| File vs inline | File path reference (`instructionsFilePath`) — not inline |
| Model selection | `claude-sonnet-4-6` (L2 skills), `claude-opus-4-6` (L3/complex skills) |
| Context preamble | Skills should instruct agents to fetch heartbeat-context before executing workflow |
