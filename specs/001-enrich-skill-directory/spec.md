# Feature Specification: Enrich Skill Directory

**Feature Branch**: `001-enrich-skill-directory`
**Created**: 2026-03-26
**Status**: Draft
**Input**: User description: "Create a Skill OS — the world's best directory of agents and skills for running a startup, with continuously improving skill definitions and supporting context like artifacts, examples, and rules."

## Clarifications

### Session 2026-03-26

- Q: Should enriched skills use flat files or Anthropic-standard subdirectories? → A: Skill subdirectories — `agents/<agent>/<skill>/SKILL.md` with per-skill supporting context.
- Q: Where do department ethos profiles live? → A: Top-level `departments/<dept>/ideal-<dept>.md` parallel to `agents/`, with room for department-wide shared context.
- Q: At how many levels can supporting context exist? → A: All three levels supported — per-skill, per-agent, per-department — with lookup chain: skill → agent → department → `_shared/`.
- Q: What migration ordering strategy? → A: Department-by-department, starting with Product.
- Q: What size limit for ethos profiles? → A: 500 words max, loaded alongside every skill in the department.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Enrich Skill File Format (Priority: P1)

A contributor opens a skill file at `agents/<agent>/<skill>/SKILL.md` and finds actionable, executable content — not just a one-sentence description. The file follows Anthropic's three-tier progressive disclosure model: YAML frontmatter with a "pushy" description optimized for AI agent discovery, a concise body written in imperative voice within strict word limits (500/1,000/1,500 by complexity class), and pointers to bundled resources in the skill's own subdirectory for deep context. Each skill file includes trigger conditions (when to activate), a phased workflow (imperative steps with deliverables), anti-patterns with rationale explaining *why* each is harmful, and an output section defining both success artifacts and failure reporting. A contributor or AI agent can read a single skill file and know exactly what to do, when to do it, what to produce, and what to avoid.

**Why this priority**: The skill file is the atomic unit of value. Anthropic's skill-creator research shows production-grade skills are 10-100x richer than one-sentence descriptions. The key insight from Anthropic: "Today's LLMs are smart. They have good theory of mind. Explain the *why* behind instructions rather than rigid MUSTs — that's a more humane, powerful, and effective approach." Skills that explain reasoning outperform skills that list rules.

**Independent Test**: Pick any 3 enriched skill files across different departments. For each: (1) Can an AI agent parse the frontmatter and decide whether to trigger? (2) Can it follow the workflow steps without external context? (3) Does it know what to produce on success and what to report on failure? (4) Does each anti-pattern explain why it matters?

**Acceptance Scenarios**:

1. **Given** an enriched skill file at `agents/<agent>/<skill>/SKILL.md`, **When** an AI agent reads the frontmatter description, **Then** the description includes explicit trigger phrases and proactive suggestion scenarios so the agent knows when to activate — even when the user doesn't explicitly name the skill.
2. **Given** the enriched skill body, **When** a contributor or AI agent reads the Workflow section, **Then** every step is written in imperative voice ("Identify all data flows. Map each flow to STRIDE categories.") with a clear deliverable per step.
3. **Given** the Anti-Patterns section, **When** a reader encounters any anti-pattern, **Then** it includes a rationale explaining why it's harmful — not just a prohibition but the reasoning so the agent can generalize to novel situations.
4. **Given** the Output section, **When** a skill cannot complete, **Then** it defines what the agent reports on failure (what went wrong, what was attempted, what to try next) — because errors are for AI agents and every error must be actionable.
5. **Given** the enriched format, **When** the skill body exceeds its complexity class word limit, **Then** detailed content is moved to `references/` files within the skill's subdirectory, with clear pointers from the body.
6. **Given** the existing 472 skill files, **When** the new format is adopted, **Then** each flat file (`<skill>.md`) is migrated to a subdirectory (`<skill>/SKILL.md`) incrementally, department-by-department starting with Product.

---

### User Story 2 - Create Department Ethos Profiles (Priority: P2)

Each of the 15 departments has an `ideal-<department>.md` file at `departments/<dept>/ideal-<dept>.md` that captures what an ideal member of that department cares about, how they think, what principles guide their decisions, and what excellence looks like in their domain. This is the department's soul — not a job description but a philosophy document (max 500 words) that every agent and skill in that department references. A sales agent that reads `ideal-sales.md` understands not just what to do but *who to be*: the mindset, the priorities, the instincts that separate great from good. The `departments/` directory also holds department-wide shared references that apply to all agents in the department.

**Why this priority**: Skills tell agents what to do. Ethos profiles tell agents who to be while doing it. An ideal salesperson prioritizes customer outcomes over quota. An ideal engineer prioritizes correctness over speed. An ideal marketer prioritizes authentic voice over viral reach. Without these profiles, 603 skills produce technically correct but soulless output. With them, agents embody the judgment and values that make work excellent.

**Independent Test**: Write `departments/sales/ideal-sales.md` for the Sales department. Have an AI agent execute a sales skill (e.g., `deal-qualifier`) with and without the ethos profile loaded. The version with the ethos profile should produce output that reflects sales philosophy (qualifying on fit, not just budget) rather than mechanical checklist completion.

**Acceptance Scenarios**:

1. **Given** a department ethos profile at `departments/<dept>/ideal-<dept>.md`, **When** any agent in that department activates a skill, **Then** the skill file references the department's ethos profile and the agent's behavior reflects the ethos principles.
2. **Given** `departments/engineering/ideal-engineering.md`, **When** a contributor reads it, **Then** they understand the department's values (e.g., "correctness over speed", "explain your reasoning", "measure before optimizing") without needing to read any individual skill file.
3. **Given** all 15 departments, **When** ethos profiles are created, **Then** each profile is authored by or validated against domain expertise — not generic platitudes but specific, opinionated stances that distinguish excellent practitioners from average ones.
4. **Given** an ethos profile, **When** a new agent role is added to that department, **Then** the profile applies automatically — new skills reference the existing department ethos without per-skill configuration.
5. **Given** the ethos profile is max 500 words, **When** loaded alongside a skill body (500–1,500 words), **Then** the combined context (1,000–2,000 words) fits comfortably in smaller model context windows.

---

### User Story 3 - Add Supporting Context Directories (Priority: P3)

Supporting context exists at three levels, each serving a distinct purpose. **Per-skill** (`agents/<agent>/<skill>/references/`, `examples/`, `scripts/`, `assets/`): context specific to one skill, like a scoring rubric reference or an output template. **Per-agent** (`agents/<agent>/references/`, etc.): resources shared across all skills owned by an agent, like a testing methodology shared by all QA engineer skills. **Per-department** (`departments/<dept>/references/`, etc.): cross-agent resources shared by all agents in a department, like a negotiation framework for all sales agents. A global `_shared/` directory holds resources that span departments (e.g., compliance frameworks). When an AI agent needs context, it follows the lookup chain: skill → agent → department → `_shared/`.

**Why this priority**: Anthropic's skill-creator demonstrated that the best skills bundle reusable scripts ("If all test cases independently wrote similar helper scripts, that's a strong signal the skill should bundle that script"). The three-tier loading model — metadata always in context, body on trigger, resources on demand — keeps skills lean while enabling unlimited depth. Three levels of context prevent duplication while keeping resources discoverable close to where they're used.

**Independent Test**: For a sample agent (e.g., `general-counsel`), add supporting context at all three levels. Verify: skill-level `references/` in `agents/general-counsel/contract-review/references/` contains a clause taxonomy, agent-level `references/` in `agents/general-counsel/references/` contains a legal methodology doc shared by all the agent's skills, and department-level `references/` in `departments/legal/references/` contains a compliance framework shared by all legal agents.

**Acceptance Scenarios**:

1. **Given** an agent directory, **When** a user browses it, **Then** they find skill subdirectories (each containing `SKILL.md` and optional `references/`, `examples/`, `scripts/`, `assets/`) alongside optional agent-level context directories.
2. **Given** a `scripts/` directory at the skill level, **When** an AI agent executes that skill, **Then** it can invoke bundled scripts for deterministic tasks rather than reimplementing common operations from scratch.
3. **Given** an `assets/` directory with output templates, **When** a skill produces a report or artifact, **Then** the output follows the template format consistently across every invocation.
4. **Given** a resource needed by multiple agents in the same department, **When** it's placed in `departments/<dept>/references/`, **Then** all agents in that department can reference it without duplication.
5. **Given** a resource needed across departments, **When** it's placed in `_shared/`, **Then** any skill in any department can reference it via relative path.
6. **Given** an AI agent looking for context, **When** it follows the lookup chain (skill → agent → department → `_shared/`), **Then** it finds the most specific version of a resource first, falling back to broader scopes only when no skill- or agent-level version exists.

---

### User Story 4 - Enable Discovery, Cross-Referencing, and Platform Support (Priority: P4)

A user or AI agent searching for capabilities can discover skills by domain, trigger condition, or related skills — regardless of which AI platform they use. Each skill file includes structured YAML frontmatter with a versioned schema enabling automated indexing. Descriptions are written "pushy" — explicitly listing trigger phrases, adjacent scenarios, and proactive suggestion conditions so AI agents activate the skill even when users don't name it directly. The format is platform-agnostic: consumable by Claude, Codex, Cursor, and any future AI agent runtime without modification.

**Why this priority**: With 603+ skills across 86 agents, discovery is critical. Anthropic's research shows Claude under-triggers skills by default — pushy descriptions combat this. Platform-agnostic design ensures skill-os becomes "the world's best resource for work agents on GitHub" for all AI platforms, not just one.

**Independent Test**: Generate a skill index from frontmatter metadata. Search for "compliance" and verify results from Legal, Security, Finance, and Agent Ops. Then load 3 skill files into both a Claude Code session and a Codex session — both should parse the frontmatter and body without platform-specific adapters.

**Acceptance Scenarios**:

1. **Given** skill files with structured frontmatter, **When** a script parses all `SKILL.md` files under `agents/`, **Then** it produces a complete index with skill name, agent, department, version, trigger conditions, and related skills.
2. **Given** two skills that interact, **When** a user reads either skill, **Then** the related skill is listed with its agent and a brief rationale for the relationship.
3. **Given** a skill's frontmatter description, **When** an AI agent evaluates whether to trigger, **Then** the description includes explicit trigger phrases ("Use when..."), adjacent scenarios ("Also consider when..."), and proactive suggestions ("Suggest when the user is about to...").
4. **Given** the skill file format, **When** consumed by Claude, Codex, Cursor, or another AI platform, **Then** the frontmatter and body are parseable without platform-specific transformation — the format works everywhere.
5. **Given** the generated index, **When** a user searches by keyword, **Then** results include skills from any department where the keyword appears in the name, description, or trigger conditions.

---

### User Story 5 - Define Inter-Agent Handoff Protocols (Priority: P5)

When a workflow spans multiple agents (e.g., a product launch involving Product Manager, Marketing, Sales, and Customer Success), the handoff points between agents are explicitly documented. Each skill that produces output consumed by another agent's skill defines the handoff: what artifact is produced, which downstream skill consumes it, and what format the artifact takes. Users can trace end-to-end workflows across the org chart.

**Why this priority**: The org chart maps roles and skills but not how they interact. The best repos (zubair-trabzada's orchestrator pattern, gstack's Think > Plan > Build > Review > Test > Ship > Reflect chain) explicitly define agent-to-agent communication. Without handoff protocols, the 86 agents remain isolated islands rather than an operating system.

**Independent Test**: Document the handoff chain for "new feature launch" across Product Manager → Design → Engineering → QA → Marketing → Sales. Verify each handoff specifies the artifact type, producing skill, and consuming skill.

**Acceptance Scenarios**:

1. **Given** a skill that produces output consumed downstream, **When** a user reads the skill, **Then** the output section names the downstream skill(s) and expected artifact format.
2. **Given** a multi-agent workflow, **When** a user traces the handoff chain, **Then** every link resolves to a real `SKILL.md` file in the repo.
3. **Given** a new agent role is added, **When** its skills are created, **Then** existing skills that should hand off to the new agent are identified and updated.

---

### User Story 6 - Skill Evaluation Framework (Priority: P6)

Each skill can be tested against real prompts to verify it produces the expected behavior — not just that it has the right sections. Following Anthropic's skill-creator pattern, skills include test prompts (realistic scenarios a user would actually say), expected outputs (what good looks like), and optionally quantitative assertions (objectively verifiable checks). This enables continuous improvement: when a skill is enriched, it can be tested to confirm the enrichment actually makes it better, not just longer.

**Why this priority**: Anthropic's skill-creator demonstrates that structure without verified effectiveness is a directory, not an operating system. The eval loop — draft, test, evaluate, iterate — is what separates documentation from production-grade skills.

**Independent Test**: For 3 enriched skills, create 2 test prompts each. Run each prompt with and without the skill loaded. Verify the with-skill output is measurably better (more complete, more accurate, better structured) than the baseline.

**Acceptance Scenarios**:

1. **Given** an enriched skill, **When** a contributor wants to verify it works, **Then** they find test prompts in an `evals/` directory within the skill's subdirectory.
2. **Given** a skill's test prompts, **When** run against an AI agent with the skill loaded, **Then** the output matches the expected behavior described in the eval.
3. **Given** two versions of a skill (before and after enrichment), **When** both are tested against the same prompts, **Then** the enriched version produces measurably better output — confirming the enrichment added real value.

---

### Edge Cases

- What happens when a skill has no meaningful anti-patterns? The section states "None identified — revisit when domain expertise is available" with a brief explanation of why the skill's domain has low risk of misuse. The section is never omitted.
- What happens when a skill operates independently with no cross-references? The `related-skills` field in frontmatter is an empty list, not omitted.
- What happens when supporting context applies to multiple agents in different departments (e.g., a compliance framework relevant to Legal, Security, and Finance)? It lives in the `_shared/` directory at the repo root, with individual skill files linking to it via relative paths.
- What happens when a resource is needed by multiple agents within the same department but not across departments? It lives in `departments/<dept>/references/` rather than duplicated per-agent.
- What happens when the enriched format is applied to a skill where domain knowledge is unavailable? The skill retains its current one-sentence description in the Skill Description section; other sections are marked with `TODO` placeholders indicating they await domain research. The skill is tagged `version: 0.1.0`.
- What happens when two skills claim to produce the same artifact type? The index generation flags this as a conflict for manual resolution.
- What happens when a department has no clear ethos distinct from adjacent departments? The ethos profile must still exist but can acknowledge shared principles while articulating what makes this department's perspective unique — even if the distinction is subtle.
- What happens when a script in `scripts/` depends on external tools not available in all environments? The script's header documents its dependencies and the skill body notes the dependency, offering a manual fallback when the script cannot execute.
- What happens when a skill's pushy description causes false-positive triggers on unrelated prompts? The description is refined through the eval framework (US6) — testing with should-not-trigger prompts alongside should-trigger prompts, following Anthropic's 60/40 train/test split methodology.
- What happens when migrating a flat skill file to a subdirectory? The file `agents/<agent>/<skill>.md` becomes `agents/<agent>/<skill>/SKILL.md`. Any agent-level `references/` or `examples/` that are skill-specific move into the skill subdirectory. Git history is preserved via `git mv`.

## Requirements *(mandatory)*

### Functional Requirements

**Skill File Format**

- **FR-001**: Every skill file MUST live at `agents/<agent-slug>/<skill-slug>/SKILL.md` and include these sections in order: YAML frontmatter, title (`# <skill-slug>`), Agent header (with reference to department ethos profile), Skill Description (third-person declarative, one sentence), When to Use (trigger scenarios), Workflow (imperative numbered steps with deliverables), Anti-Patterns (with rationale explaining why each is harmful), Output (success artifacts AND failure reporting), and Related Skills.
- **FR-002**: Frontmatter MUST include: `name` (kebab-case, max 64 chars), `description` (50–1024 chars, third-person, includes trigger phrases and proactive suggestion scenarios), `department`, `agent`, `version` (semver), `complexity` (one of `simple`, `medium`, `complex` — determines the word limit per FR-003), and `related-skills` (list of relative paths, may be empty `[]`). Additional optional frontmatter fields are permitted but not validated — this allows future extensibility without breaking existing skills.
- **FR-003**: Skill files MUST follow Anthropic's three-tier progressive disclosure model with strict size limits per complexity tier:

  **Tier 1 — Metadata** (~100 words): YAML frontmatter with name, description, and trigger phrases. Always loaded into AI agent context regardless of whether the skill activates. Must be small enough for Haiku-class models.

  **Tier 2 — Skill body** (size by complexity class): The core SKILL.md content loaded when the skill triggers. Three size classes:

  | Class | Max words | Typical use |
  |-------|-----------|-------------|
  | Simple | 500 | Single-phase skills with straightforward workflows (e.g., `press-release-writer`, `email-deliverability-manager`) |
  | Medium | 1,000 | Multi-phase skills with moderate decision logic (e.g., `threat-modelling`, `deal-qualifier`) |
  | Complex | 1,500 | Skills with scoring rubrics, multiple decision branches, or cross-agent coordination (e.g., `vendor-risk-assessor`, `product-launch-coordinator`) |

  Word count is defined as: all whitespace-delimited tokens in the body below the frontmatter closing `---`, excluding markdown heading markers (`#`, `##`), bullet markers (`-`, `*`), and code fence markers. YAML frontmatter itself is excluded from body word count. These limits are hard errors in the validation script — not soft guidelines.

  Content exceeding these limits MUST be moved to `references/` files within the skill's subdirectory with clear pointers from the body. Not every consumer runs Opus — skill bodies must fit comfortably in smaller model context windows.

  **Complexity classification guide**: Assign `simple` if the skill has a single-phase workflow with ≤3 steps and no branching logic. Assign `medium` if the skill has multi-phase workflows (4-7 steps) or moderate decision logic. Assign `complex` if the skill has scoring rubrics, 8+ workflow steps, multiple decision branches, or coordinates across agents. When in doubt, assign the higher class — it's better to have headroom than to force content into references prematurely. If a skill legitimately exceeds 1,500 words after maximum offloading to `references/`, split it into two skills with distinct responsibilities — this signals a Single Responsibility violation (Constitution Principle II).

  **Tier 3 — Bundled resources** (unlimited): `references/`, `examples/`, `scripts/`, `assets/` within the skill subdirectory, loaded on demand. Individual reference files over 300 lines MUST include a table of contents for navigation.
- **FR-004**: The Workflow section MUST be written in imperative voice ("Identify the risk factors. Score each on a 1-5 scale.") — not descriptive ("The agent identifies risk factors") or second-person ("You should identify risk factors").
- **FR-005**: The Anti-Patterns section MUST explain the *why* behind each anti-pattern. The reasoning enables agents to generalize to novel situations rather than pattern-match on specific rules. Format: anti-pattern statement followed by rationale.
- **FR-006**: The Output section MUST define both success artifacts (what format, what content, where delivered) and failure reporting (what the agent communicates when it cannot complete the skill, what was attempted, and what to try next).
- **FR-007**: The description field in frontmatter MUST be written "pushy" for AI agent discovery — including at minimum: one trigger phrase ("Use when asked to..."), one adjacent scenario ("Also consider when..."), and one proactive suggestion ("Suggest when the user is about to..."). All three components are required. This combats the documented tendency of AI agents to under-trigger skills.

**Writing Style**

- **FR-008**: Skill Description: third-person declarative ("This skill assesses vendor risk exposure."). When to Use: scenario-based ("When the team needs to evaluate a new vendor before contract signing."). Workflow: imperative ("Gather vendor financial records. Cross-reference against compliance databases."). Anti-Patterns: rationale-driven ("Skipping financial verification because the vendor is a known brand — brand recognition does not guarantee financial stability, and several high-profile vendors have failed mid-contract.").
- **FR-009**: Skills MUST explain the reasoning behind instructions rather than relying on rigid constraints. Prefer "Verify the contract has been reviewed by legal because unsigned contracts without legal review have caused $X liability exposure" over "ALWAYS verify legal review. NEVER skip this step."

**Department Ethos Profiles**

- **FR-010**: Each of the 15 departments MUST have an `ideal-<department>.md` file at `departments/<department>/ideal-<department>.md` that defines the mindset, priorities, decision-making principles, and quality standards of an ideal practitioner in that domain. Max 500 words (same word-count definition as FR-003 — whitespace-delimited tokens excluding markdown markers). Ethos profiles are not versioned individually — they evolve with the department and are tracked via git history. Loaded alongside every skill in the department, so combined context (ethos + skill body) stays within 1,000–2,000 words.
- **FR-011**: Every skill file MUST reference its department's ethos profile in the Agent header section, enabling AI agents to load the ethos context when executing any skill in that department.
- **FR-012**: Ethos profiles MUST be opinionated and specific — not generic platitudes but actionable principles that distinguish excellent practitioners from average ones. "Move fast and break things" is a platitude. "Prioritize customer trust over shipping speed because a broken promise costs 10x more to repair than a delayed feature" is an opinionated principle.

**Supporting Context**

- **FR-013**: Supporting context MAY exist at four levels following a defined lookup chain (skill → agent → department → `_shared/`). The lookup chain applies to all four resource types (`references/`, `examples/`, `scripts/`, `assets/`):
  - **Per-skill**: `agents/<agent>/<skill>/references/`, `examples/`, `scripts/`, `assets/` — context specific to one skill.
  - **Per-agent**: `agents/<agent>/references/`, `examples/`, `scripts/`, `assets/` — resources shared across all skills owned by one agent.
  - **Per-department**: `departments/<dept>/references/`, `examples/`, `scripts/`, `assets/` — resources shared across all agents in a department, alongside the ethos profile.
  - **Global**: `_shared/` at repo root — cross-cutting resources referenced by multiple departments.

  **Naming conventions for supporting context files**:
  - `references/`: kebab-case `.md` files describing the content (e.g., `stride-framework.md`, `contract-clause-taxonomy.md`).
  - `examples/`: kebab-case directories or files named by scenario (e.g., `vendor-review-sample/input.md` + `output.md`, or `simple-risk-assessment.md`). Examples MUST include both input and expected output.
  - `scripts/`: kebab-case executable files with appropriate extensions (`.py`, `.sh`, `.js`). Each script MUST include a header comment documenting: purpose (one line), dependencies, and usage. Python 3.10+ and shell (bash) are the preferred languages — avoid niche runtimes.
  - `assets/`: kebab-case files of any type used in skill output (e.g., `risk-report-template.md`, `review-scorecard.csv`). Assets are NOT loaded into AI context — they are used by the agent to produce output artifacts.
- **FR-014**: When a resource exists at multiple levels, the most specific version takes precedence (skill > agent > department > `_shared/`).
- **FR-015**: Cross-references between skills MUST use relative paths from the SKILL.md file's location that resolve within the repo. Cross-references MUST be bidirectional — if skill A lists skill B in `related-skills`, skill B MUST also list skill A. The validation script flags unidirectional references as warnings.
- **FR-016**: When a pattern emerges where multiple skills independently produce similar helper logic, that logic MUST be extracted into a shared script at the appropriate level (agent `scripts/` if one agent, department `scripts/` if one department, `_shared/scripts/` if cross-department).

**Discovery and Platform Support**

- **FR-017**: A skill index MUST be generatable from frontmatter metadata by scanning all `SKILL.md` files under `agents/`, without manual curation. Output format: JSON (`skill-index.json` at repo root) with one entry per skill containing `name`, `agent`, `department`, `version`, `complexity`, `description`, `path`, and `related-skills`.
- **FR-018**: The skill file format MUST be platform-agnostic — parseable by Claude, Codex, Cursor, and other AI agent runtimes without platform-specific transformation. No platform-specific frontmatter fields or body syntax.
- **FR-019**: Each skill MUST include a `version` field in frontmatter (semver) to track enrichment iterations. Version increments follow: MAJOR for scope/responsibility changes, MINOR for new sections or significant content additions, PATCH for clarifications and refinements.

**Project-Level**

- **FR-020**: The repository MUST include an `ETHOS.md` at the root that captures the operating philosophy of the Skill OS — the principles that apply to every department and every skill. Format: plain markdown, 300–500 words, containing a Philosophy section (2-3 sentences on the core belief), Principles section (5-7 opinionated principles with rationale), and a Decision Priorities section (ordered list of what to prioritize in tradeoffs). This is the soul of the organization, not operational instructions. Inspired by gstack's ETHOS.md, it answers: what does this organization believe about how work should be done?
- **FR-021**: The org chart (`AGENTS.md`) MUST remain the canonical source for agent roles, departments, and skill assignments. Enriched skill files add depth but do not replace the org chart as the authority on organizational structure.
- **FR-022**: The enriched format MUST be backward-compatible — existing one-sentence skill files remain valid during incremental migration. Unenriched skills retain their current format with a `version: 0.1.0` tag indicating they await enrichment.

**Migration**

- **FR-025**: Migration MUST proceed department-by-department, starting with Product. For each department: (1) write the ethos profile, (2) migrate all agents and skills in that department to the enriched format (flat files → subdirectories with `SKILL.md`), (3) validate cross-references within the department resolve.
- **FR-026**: Migration of a flat skill file (`agents/<agent>/<skill>.md`) to a subdirectory (`agents/<agent>/<skill>/SKILL.md`) MUST preserve git history via `git mv`.
- **FR-027**: If a department migration is partially complete and must be reverted, the rollback procedure is: `git revert` the migration commits in reverse order. Because each skill is a logical-unit commit (Constitution Principle V), partial rollbacks are granular — individual skills can be reverted without affecting other skills in the same department. Cross-references pointing to reverted skills will fail validation, flagging them for cleanup.

**Validation**

- **FR-023**: A validation script MUST exist that checks every skill file for: valid YAML frontmatter, all required frontmatter fields populated, `name` matches directory name, `description` within character limits and in third-person, body within word limit for its complexity class (hard error), all referenced files exist, all cross-reference paths resolve, cross-references are bidirectional (warning), and ethos profile reference is valid. The script MUST run on demand via `python scripts/validate.py` and SHOULD be integrated into CI (GitHub Actions) to run on every PR touching `agents/` or `departments/`.
- **FR-024**: Skill evaluation prompts (test cases) SHOULD exist for enriched skills, stored in an `evals/evals.json` within the skill's subdirectory. Format: JSON array of objects, each containing `id` (integer), `prompt` (realistic user prompt that should trigger this skill), `expected_behavior` (description of what good output looks like), and `should_trigger` (boolean, true for positive tests, false for near-miss negatives). This enables continuous verification that skills produce expected behavior when consumed by AI agents.

### Key Entities

- **Skill**: The atomic unit — a discrete responsibility owned by one agent, documented at `agents/<agent>/<skill>/SKILL.md` with YAML frontmatter and structured sections. The skill subdirectory may also contain `references/`, `examples/`, `scripts/`, `assets/`, and `evals/`. Designed to be consumed by AI agents: the frontmatter triggers activation, the body provides executable instructions, and bundled resources supply depth on demand.
- **Agent**: A role in the org chart that owns one or more skills. Represented as a directory under `agents/` containing skill subdirectories and optional agent-level context (`references/`, `examples/`, `scripts/`, `assets/`).
- **Department**: An organizational unit containing multiple agents. Represented as a directory under `departments/` containing the ethos profile (`ideal-<dept>.md`) and optional department-level context (`references/`, `examples/`, `scripts/`, `assets/`).
- **Department Ethos Profile**: An `ideal-<department>.md` file at `departments/<dept>/ideal-<dept>.md` defining the mindset, principles, and quality standards of an ideal practitioner. Max 500 words. Referenced by every skill in the department. Loaded into context alongside the skill body.
- **Supporting Context**: Four types of bundled resources at four levels (skill, agent, department, global `_shared/`): references (domain docs), examples (input/output pairs), scripts (executable tools), and assets (output templates). Lookup chain: skill → agent → department → `_shared/`.
- **Handoff**: A defined connection between a producing skill and a consuming skill, specifying the artifact type and format exchanged.
- **Skill Index**: An auto-generated, platform-agnostic catalog of all skills with their metadata, enabling search and discovery across the full directory.
- **ETHOS.md**: The root-level philosophy document defining the operating principles of the entire Skill OS — what this organization believes about how work should be done.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: An AI agent can parse any enriched skill file's frontmatter, decide whether to trigger based on the description, follow the imperative workflow steps, and produce the specified output format — all without human intervention or external documentation.
- **SC-002**: 100% of enriched skill files pass the validation script confirming: valid frontmatter, all required fields, body within word limit for complexity class, all cross-references resolve, all referenced files exist, and ethos profile reference is valid.
- **SC-003**: All 15 departments have an `ideal-<department>.md` ethos profile (max 500 words) that is opinionated, specific, and referenced by every skill file in that department.
- **SC-004**: The skill index surfaces relevant results from at least 3 different departments when searched with a cross-cutting keyword (e.g., "compliance", "onboarding", "metrics").
- **SC-005**: At least 5 end-to-end workflows spanning 3+ agents can be traced entirely through cross-references and handoff definitions in skill files.
- **SC-006**: The repository becomes the most comprehensive open-source resource for AI work agent definitions on GitHub, measured by: skill count (600+), depth per skill (7+ structured sections), department breadth (15), ethos profiles (15), and platform compatibility (works on Claude, Codex, Cursor without modification).
- **SC-007**: 80% of skill files are migrated to the enriched subdirectory format (`<skill>/SKILL.md`) within the first migration pass (starting with Product department), with remaining files tagged `version: 0.1.0` indicating they await enrichment.
- **SC-008**: For at least 10 enriched skills, test prompts exist and the with-skill output scores higher than the without-skill baseline on a 3-point rubric: (1) **Completeness** — does the output address all aspects of the prompt? (2) **Structure** — does the output follow the skill's defined output format? (3) **Domain accuracy** — does the output reflect domain best practices consistent with the department ethos? Scoring is human judgment (author or reviewer) using a simple better/same/worse per criterion. "Better" on at least 2 of 3 criteria = pass.

## Assumptions

- The directory structure evolves from flat files (`agents/<agent>/<skill>.md`) to skill subdirectories (`agents/<agent>/<skill>/SKILL.md`). A new top-level `departments/` directory is added parallel to `agents/`. The `_shared/` directory at root holds global cross-cutting resources.
- These skills are designed to be executable by AI agents — not just human-readable documentation. The format choices (imperative voice, pushy descriptions, failure reporting, bundled scripts) all serve this goal.
- Domain expertise for enriching skill content and writing ethos profiles will come incrementally from contributors with specific functional knowledge. Migration proceeds department-by-department starting with Product, not all at once.
- The org chart remains the source of truth for which agents and skills exist. Skill files add operational depth. Ethos profiles add philosophical depth. Neither replaces the org chart.
- Frontmatter metadata follows Anthropic's conventions (name, description as required fields) to maximize compatibility with Claude's skill discovery system while remaining parseable by other platforms.
- Cross-references and handoff protocols are documented aspirationally first. Validation that all links resolve is a follow-up quality pass, not a launch blocker.
- The ETHOS.md captures enduring organizational philosophy — it changes rarely and only through deliberate amendment, similar to the constitution.
- Combined context per skill invocation = ethos profile (max 500 words) + skill body (500–1,500 words) = 1,000–2,000 words total, fitting comfortably in smaller model context windows.
