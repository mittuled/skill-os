# Tasks: Skill Quality Improvements

**Input**: Design documents from `/specs/002-skill-quality-improvements/`
**Prerequisites**: plan.md (required), spec.md (required), data-model.md, contracts/, quickstart.md

**Commit discipline**: Each skill, script, or schema update = 1 commit.

---

## Phase 1: Setup & Foundational

**Purpose**: Validation script updates and schema artifacts that all user stories depend on.

- [x] T001 Update `scripts/validate.py` to accept optional `triggers` frontmatter field (list of strings). Validation: each item is a non-empty string, 5-50 chars. No error if field absent. 1 commit.
- [x] T002 Update `scripts/validate.py` to accept `[GATE]` markers in workflow steps as valid syntax. Add warning (not error) when `[GATE]` appears in a skill with `complexity: simple`. 1 commit.
- [x] T003 Update `scripts/validate.py` to validate `allowed-tools.yaml` at repo root: check YAML syntax, `schema_version` field present and supported, department keys match `departments/` dirs, agent keys match `agents/` dirs. 1 commit.
- [x] T004 Create `allowed-tools.yaml` at repo root with `schema_version: 1` and empty `company-wide: []` placeholder. 1 commit.
- [ ] T005 Update enrichment template at `specs/001-enrich-skill-directory/contracts/skill-template.md` — add `triggers` as optional frontmatter field, add `[GATE]` guidance in Workflow section comments, add `Tool policy` reference in Agent header. 1 commit.
- [ ] T006 Update `specs/001-enrich-skill-directory/quickstart.md` — add sections for triggers, gates, rubrics, code examples, and tool policy reference. 1 commit.

**Checkpoint**: Validation script handles all new elements. Templates updated. Phase 2+ can begin.

---

## Phase 2: US1 — Company Tooling Onboarder

**Goal**: Create the onboarding skill that discovers, authenticates, and connects org tools.

**Independent Test**: Run in a test environment with 3 tools (GitHub, Slack, mock CRM). Verify discovery, authentication, and agent access.

- [ ] T007 [US1] Create `agents/agent-configuration-manager/company-tooling-onboarder/` directory structure (SKILL.md, scripts/, references/). 1 commit.
- [ ] T008 [US1] Write `agents/agent-configuration-manager/company-tooling-onboarder/SKILL.md` — enriched 9-section format (complexity: complex). Workflow: interview operator about tool categories → detect existing MCP servers → authenticate → connect → generate allowed-tools.yaml → delegate to mcp-server-builder for tools without MCP. 1 commit.
- [ ] T009 [US1] Write `agents/agent-configuration-manager/company-tooling-onboarder/references/tool-categories.md` — standard SaaS tool categories (communication, source control, PM, observability, CRM, documentation, finance, legal, design) with top 3-5 tools per category and their MCP availability status. 1 commit.
- [ ] T010 [US1] Write `agents/agent-configuration-manager/company-tooling-onboarder/scripts/discover-tools.py` — interactive tool discovery script. Presents categories, records selections, checks for existing MCP servers via package registry lookup. Zero external deps. 1 commit.
- [ ] T011 [US1] Write `agents/agent-configuration-manager/company-tooling-onboarder/scripts/connect-mcp.py` — MCP server connection helper. Takes tool name + auth credentials, configures the MCP server endpoint, validates connectivity, records in allowed-tools.yaml. 1 commit.
- [ ] T012 [US1] Write `agents/agent-configuration-manager/company-tooling-onboarder/scripts/configure-secrets.py` — platform secret store setup helper. Detects platform (Claude Code → .env, Codex → vault, generic → env vars), writes credentials to the appropriate store, never to repo. 1 commit.
- [ ] T013 [US1] Update `restructured-org-chart-v3.md` — add `company-tooling-onboarder` to Agent Configuration Manager's skill list. 1 commit.

---

## Phase 3: US2 — Tool Policy Manager

**Goal**: Create the skill that manages `allowed-tools.yaml` as an ongoing governance function.

**Independent Test**: Add/remove/modify tool permissions via the skill. Verify allowed-tools.yaml updates correctly and validation passes.

- [ ] T014 [US2] Create `agents/agent-configuration-manager/tool-policy-manager/` directory structure. 1 commit.
- [ ] T015 [US2] Write `agents/agent-configuration-manager/tool-policy-manager/SKILL.md` — enriched 9-section format (complexity: medium). Workflow: read current policy → apply requested change (add/remove/modify tool at specified level) → validate schema → commit with change tracking. 1 commit.
- [ ] T016 [US2] Write `agents/agent-configuration-manager/tool-policy-manager/scripts/validate-policy.py` — standalone YAML schema validation for allowed-tools.yaml. Checks schema_version, structure, reference resolution. 1 commit.
- [ ] T017 [US2] Write `agents/agent-configuration-manager/tool-policy-manager/assets/allowed-tools-template.yaml` — starter template with example entries for each access level. 1 commit.
- [ ] T018 [US2] Add tool policy reference to all agent directories — add `Tool policy: [allowed-tools.yaml](../../allowed-tools.yaml)` line to the Agent header section of one representative skill per agent (80 agents). This is a batch update, not per-skill. 1 commit.
- [ ] T019 [US2] Update `restructured-org-chart-v3.md` — add `tool-policy-manager` to Agent Configuration Manager's skill list. 1 commit.

---

## Phase 4: US3 — MCP Server Builder

**Goal**: Create the skill that generates MCP server wrappers from API documentation.

**Independent Test**: Point at a tool with an OpenAPI spec. Verify it scaffolds a working MCP server.

- [ ] T020 [US3] Create `agents/skill-builder/mcp-server-builder/` directory structure (SKILL.md, scripts/, references/). 1 commit.
- [ ] T021 [US3] Write `agents/skill-builder/mcp-server-builder/SKILL.md` — enriched 9-section format (complexity: complex). Workflow: receive API docs → parse endpoints → map to MCP tools → scaffold server code → validate against API → report results. 1 commit.
- [ ] T022 [US3] Write `agents/skill-builder/mcp-server-builder/scripts/parse-openapi.py` — OpenAPI spec parser. Extracts endpoints, methods, parameters, response schemas. Outputs structured JSON. Zero external deps (uses json + urllib only). 1 commit.
- [ ] T023 [US3] Write `agents/skill-builder/mcp-server-builder/scripts/scaffold-mcp.py` — MCP server scaffolding script. Takes parsed API structure, generates a FastMCP-compatible Python server with tool definitions. 1 commit.
- [ ] T024 [US3] Write `agents/skill-builder/mcp-server-builder/references/mcp-protocol.md` — MCP protocol reference covering: tool definition format, transport options, error handling patterns, best practices for tool naming and descriptions. 1 commit.
- [ ] T025 [US3] Update `restructured-org-chart-v3.md` — add `mcp-server-builder` to Skill Builder's skill list. 1 commit.

---

## Phase 5: US4 — Tool Health Checker

**Goal**: Create the skill that verifies tool connectivity, credentials, and MCP responsiveness.

**Independent Test**: Connect 3 tools, revoke one token. Verify health report catches the failure.

- [ ] T026 [US4] Create `agents/agent-operations-manager/tool-health-checker/` directory structure (SKILL.md, scripts/, assets/). 1 commit.
- [ ] T027 [US4] Write `agents/agent-operations-manager/tool-health-checker/SKILL.md` — enriched 9-section format (complexity: medium). Workflow: read allowed-tools.yaml → for each tool, test connectivity + auth → classify status (healthy/degraded/unreachable) → generate report. 1 commit.
- [ ] T028 [US4] Write `agents/agent-operations-manager/tool-health-checker/scripts/check-health.py` — connectivity and auth checker. For each tool in allowed-tools.yaml, attempts a lightweight API call (e.g., whoami endpoint), reports pass/fail with latency. 1 commit.
- [ ] T029 [US4] Write `agents/agent-operations-manager/tool-health-checker/assets/health-report-template.md` — output template with tool name, status, last checked, latency, and remediation steps columns. 1 commit.
- [ ] T030 [US4] Update `restructured-org-chart-v3.md` — add `tool-health-checker` to Agent Operations Manager's skill list. 1 commit.

---

## Phase 6: US5 — Add Triggers to Skills

**Goal**: Add `triggers` frontmatter to the 50 most commonly activated skills.

**Independent Test**: Verify 5 skills with triggers activate more reliably in Claude Code.

- [ ] T031 [US5] Identify the top 50 skills by cross-reference count and domain importance — produce a prioritized list. Save to `specs/002-skill-quality-improvements/triggers-target-list.md`. 1 commit.
- [ ] T032 [US5] Add `triggers` to the first 10 skills from the list (Product department). Each skill gets 3-5 trigger phrases. 1 commit per skill (10 commits).
- [ ] T033 [US5] Add `triggers` to the next 10 skills (Engineering department). 1 commit per skill (10 commits).
- [ ] T034 [US5] Add `triggers` to the next 10 skills (Marketing department). 1 commit per skill (10 commits).
- [ ] T035 [US5] Add `triggers` to the next 10 skills (Sales + Legal). 1 commit per skill (10 commits).
- [ ] T036 [US5] Add `triggers` to the final 10 skills (remaining departments). 1 commit per skill (10 commits).

---

## Phase 7: US6 — Add Checkpoint Gates

**Goal**: Add `[GATE]` markers to 20 complex skills with high-stakes workflow steps.

**Independent Test**: Verify `[GATE]` markers are visible in workflow and validation script accepts them.

- [ ] T037 [US6] Identify 20 complex skills with irreversible or high-stakes steps (deploys, legal filings, budget approvals, security exceptions). Save target list to `specs/002-skill-quality-improvements/gates-target-list.md`. 1 commit.
- [ ] T038 [US6] Add `[GATE]` markers to 10 skills (Engineering + Legal). 1 commit per skill (10 commits).
- [ ] T039 [US6] Add `[GATE]` markers to 10 skills (Product + Finance + Sales). 1 commit per skill (10 commits).

---

## Phase 8: US7 — Add Scoring Rubrics

**Goal**: Create scoring rubrics for 10 assessment-type skills.

**Independent Test**: Run an assessment skill against two subjects. Verify identical rubric produces comparable numeric scores.

- [ ] T040 [US7] Identify 10 assessment skills (vendor risk, code review, compliance audit, etc.). Save target list. 1 commit.
- [ ] T041 [US7] Create `references/scoring-rubric.md` for each of the 10 skills — criteria, weights (sum to 100%), 0-10 scale, A+ through F grade bands, signal tables. Update each skill's Workflow to reference the rubric. 1 commit per skill (10 commits).

---

## Phase 9: US8 — Add Code Examples

**Goal**: Add working code examples to 20 engineering skills.

**Independent Test**: Verify an agent executing an engineering skill references the examples and produces correct output.

- [ ] T042 [US8] Identify 20 engineering skills that produce or review code. Save target list. 1 commit.
- [ ] T043 [US8] Create `examples/` for 10 skills (DevOps + Platform) — each with input.md + output file in the relevant language. 1 commit per skill (10 commits).
- [ ] T044 [US8] Create `examples/` for 10 skills (Frontend + Backend + Security) — each with input.md + output file. 1 commit per skill (10 commits).

---

## Phase 10: US9 — Quality Fixes

**Goal**: Rewrite Engineering skills scoring <5/5 and Legal skills missing anti-pattern rationale.

**Independent Test**: Re-score rewritten skills — both departments should score 5.0.

- [ ] T045 [US9] Identify all Engineering skills scoring below 5/5 in the quality assessment. Run validation to find skills missing frontmatter or with generalist content. Save list. 1 commit.
- [ ] T046 [US9] Rewrite identified Engineering skills with domain-specific patterns and terminology. 1 commit per skill.
- [ ] T047 [US9] Identify all Legal skills with anti-patterns missing *Why* rationale. 1 commit.
- [ ] T048 [US9] Update identified Legal skills — add *Why* rationale to every anti-pattern. 1 commit per skill.

---

## Phase 11: Polish & Finalize

**Purpose**: Constitution amendment, full validation, status update.

- [ ] T049 Amend constitution to v2.1.0 — document `triggers` frontmatter, `[GATE]` workflow markers, `allowed-tools.yaml` policy file, tool policy reference in Agent headers, 4 new tooling skills. 1 commit.
- [ ] T050 Update frontmatter schema at `specs/001-enrich-skill-directory/contracts/frontmatter-schema.yaml` — add `triggers` as optional field. 1 commit.
- [ ] T051 Run full repo validation: `python3 scripts/validate.py` — confirm 0 errors across all 499+ skills. Fix any errors. 1 commit per fix.
- [ ] T052 Update `status.md` — reflect 4 new skills, tool policy, triggers/gates/rubrics/examples counts. 1 commit.
- [ ] T053 Update `CLAUDE.md` — add tool policy reference, triggers guidance, gate guidance. 1 commit.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: No dependencies — start immediately
- **Phase 2 (Onboarder)**: Depends on Phase 1 (needs allowed-tools.yaml + validation)
- **Phase 3 (Policy Manager)**: Depends on Phase 2 (manages what onboarder creates)
- **Phase 4 (MCP Builder)**: Depends on Phase 1 only (called by onboarder but independently testable)
- **Phase 5 (Health Checker)**: Depends on Phase 2 (reads allowed-tools.yaml)
- **Phase 6-9 (Enhancements)**: Depend on Phase 1 only (validation script must support new elements)
- **Phase 10 (Quality Fixes)**: Independent of tooling phases
- **Phase 11 (Finalize)**: Depends on ALL previous phases

### Parallel Opportunities

- Phases 4 + 5 can run in parallel (different agents, different skills)
- Phases 6 + 7 + 8 + 9 + 10 can ALL run in parallel (different files, no dependencies)
- Within Phase 6: T032-T036 can run in parallel (different departments)

---

## Implementation Strategy

### MVP First (Phases 1-2)

1. Phase 1: Setup (validation + schema)
2. Phase 2: Company Tooling Onboarder
3. **STOP and VALIDATE**: Test onboarding with 3 tools

### Incremental Delivery

1. Phase 1 → Foundation ready
2. Phase 2 → Onboarder works (MVP!)
3. Phase 3 → Policy management
4. Phase 4 + 5 → MCP builder + health checker (parallel)
5. Phase 6-10 → All enhancements (parallel)
6. Phase 11 → Polish, constitution, finalize

---

## Task Count

| Phase | Tasks | Description |
|-------|-------|-------------|
| 1 | 6 | Setup & foundational |
| 2 | 7 | US1: Onboarder |
| 3 | 6 | US2: Policy manager |
| 4 | 6 | US3: MCP builder |
| 5 | 5 | US4: Health checker |
| 6 | 6 | US5: Triggers (~50 skills) |
| 7 | 3 | US6: Gates (~20 skills) |
| 8 | 2 | US7: Rubrics (~10 skills) |
| 9 | 3 | US8: Code examples (~20 skills) |
| 10 | 4 | US9: Quality fixes |
| 11 | 5 | Polish & finalize |
| **Total** | **53** | |

Note: Phases 6-9 involve batch updates (1 commit per skill within each batch task), so the actual commit count is ~53 tasks + ~110 individual skill commits = ~163 total commits.
