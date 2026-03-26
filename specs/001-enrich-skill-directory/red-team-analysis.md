# Red Team Analysis: skill-os Spec vs. Industry Best Practices

**Sources**: Anthropic's `claude-plugins-official`, Garry Tan's `gstack`, and the Anthropic `skill-creator` skill
**Date**: 2026-03-26
**Purpose**: Identify what our spec gets right, what it misses, and what we can learn from the people who literally built the platform.

---

## 1. What Matches

These are areas where our spec aligns with proven best practices.

| Our Spec | Anthropic / gstack | Verdict |
| -------- | ------------------ | ------- |
| Structured sections per skill (trigger, workflow, anti-patterns, output) | Anthropic: "name, description, when to trigger, expected output format". gstack: skills have personas, trigger phrases, structured artifacts | Aligned. Our section list is actually more comprehensive than Anthropic's minimum. |
| Progressive disclosure via `references/`, `examples/` dirs | Anthropic: three-tier loading (metadata → body → bundled resources). gstack: `references/`, `templates/` subdirs per skill | Aligned in concept. Implementation details differ (see gaps below). |
| Frontmatter metadata for discovery | Anthropic: YAML frontmatter required (`name`, `description`). gstack: frontmatter with `name`, `version`, `description`, `preamble-tier` | Aligned. We spec `name`, `description`, `department`, `agent`, `related-skills`. |
| Cross-referencing between skills | gstack: skills understand context from previous steps in workflow chain. Anthropic: skills can reference other skills | Aligned in intent. |
| kebab-case naming | Both repos use kebab-case universally | Already enforced by our constitution. |
| Single-sentence skill description | Anthropic: description in frontmatter is the trigger mechanism (~50-500 chars) | Our existing one-sentence format maps to this. Good foundation. |

---

## 2. What Doesn't Match

These are gaps, contradictions, or misalignments between our spec and what the best actually do.

### 2.1 Writing Voice: Imperative, Not Descriptive

**Our spec says**: Skill Description is "one sentence describing what the skill does."

**Anthropic says**: Use imperative/infinitive form. "Parse the frontmatter" NOT "You should parse the frontmatter." Third-person for descriptions. Never reference "Claude" by name.

**gstack says**: Use natural language for logic and state. Express conditionals as English, not code.

**Gap**: Our spec doesn't specify the voice or tense for any section. The current skill files are descriptive ("Conducts full threat modelling exercises") which is fine for the description line, but the Workflow section needs imperative instructions ("Identify all data flows. Map each flow to STRIDE categories. Score each threat.").

**Impact**: Medium-high. Descriptive skills are documentation. Imperative skills are executable instructions an AI agent can follow.

### 2.2 The "Pushy Description" Problem

**Our spec says**: Frontmatter includes `description` field.

**Anthropic's skill-creator says**: "Currently Claude has a tendency to under-trigger skills. To combat this, make descriptions a little bit pushy." Example: Instead of "How to build a dashboard" → "How to build a dashboard. Make sure to use this skill whenever the user mentions dashboards, data visualization, internal metrics, or wants to display any kind of company data, even if they don't explicitly ask for a 'dashboard.'"

**gstack says**: Every description includes explicit trigger phrases AND proactive suggestion triggers ("Proactively suggest when the user is about to merge or land code changes").

**Gap**: Our spec has no guidance on description writing for discoverability. We treat descriptions as passive documentation, not as active trigger mechanisms.

**Impact**: Critical if skills are ever consumed by AI agents (which is the entire point of a Skill OS). Low if the repo remains purely human-navigated.

### 2.3 Three-Tier Loading with Size Constraints

**Our spec says**: Skill files have 7+ sections. Supporting context in subdirectories.

**Anthropic says**: Strict three-tier system:
- Tier 1: Metadata (~100 words) — always in context
- Tier 2: SKILL.md body (<500 lines / <5,000 words) — loaded on trigger
- Tier 3: Bundled resources — loaded as needed, unlimited size

**gstack says**: Preamble tiers 1-4 control injected complexity. T1 skills get minimal overhead; T4 skills get full context.

**Gap**: Our spec has no size guidance. With 7 mandatory sections, an enriched skill file could easily blow past 500 lines — putting workflow details, anti-patterns, output templates, and cross-references all in one file. Anthropic explicitly says: "Keep SKILL.md under 500 lines; if approaching this limit, add hierarchy with clear pointers."

**Impact**: High. Bloated skill files defeat the purpose. We need to decide: what goes in the skill file vs. what goes in `references/`.

### 2.4 `scripts/` and `assets/` Directories

**Our spec says**: Supporting context = `references/`, `examples/`, `rules/`

**Anthropic says**: Four resource types:
- `scripts/` — Executable code for deterministic/repetitive tasks
- `references/` — Docs loaded into context as needed
- `assets/` — Files used in output (templates, icons, fonts) — NOT loaded into context
- `examples/` — Working code examples

**gstack says**: Also uses `bin/` for hook scripts, `templates/` for output templates.

**Gap**: We're missing `scripts/` (executable tools a skill can invoke) and `assets/` (output artifacts like report templates). Our `rules/` directory has no equivalent in either reference repo — Anthropic puts constraints directly in the skill body or references.

**Impact**: Medium. `scripts/` matters if skills become executable. `assets/` matters for output templates. `rules/` may be an over-abstraction — constraints belong in the skill body per Anthropic's pattern.

### 2.5 "Explain the Why" vs. Rigid Constraints

**Our spec says**: Anti-Patterns section lists what the agent must avoid.

**Anthropic's skill-creator says**: "Try hard to explain the **why** behind everything. If you find yourself writing ALWAYS or NEVER in all caps, that's a yellow flag — reframe and explain the reasoning so the model understands why."

**gstack's ETHOS.md**: Two core principles with full philosophical reasoning — "Boil the Lake" and "Search Before Building" — not just rules but explanations of why.

**Gap**: Our spec frames anti-patterns as a list of prohibitions. The best practice is to explain WHY something is an anti-pattern, so the agent can generalize to novel situations rather than pattern-match on specific rules.

**Impact**: Medium. The difference between "Don't mock the database" and "Don't mock the database because mock/prod divergence caused a production outage in Q3 — always test against real data stores."

### 2.6 No Testing/Evaluation Framework

**Our spec says**: Success criteria are about human comprehension and structural validation.

**Anthropic's skill-creator says**: Full eval loop — draft skill → create test prompts → run with-skill vs. baseline → grade with assertions → iterate. Includes a benchmark viewer, blind comparison, and description optimization.

**gstack says**: Three testing tiers (unit, smoke, integration), plus a `skill-check.ts` health dashboard.

**Gap**: Our spec has zero concept of testing whether skills actually work when consumed by AI agents. We validate structure but not effectiveness.

**Impact**: High for the "world's best resource" ambition. Structure without verified effectiveness is a directory, not an operating system.

### 2.7 No Versioning Per Skill

**Our spec says**: Org chart is the authority. No mention of skill-level versioning.

**Anthropic says**: Optional `version` field in frontmatter.

**gstack says**: `version` in frontmatter + a global `VERSION` file + `CHANGELOG.md` with user-facing release notes.

**Gap**: When skills are enriched iteratively, there's no way to track which version of a skill's content a consumer is working with.

**Impact**: Low initially, high at scale. Especially important for the "continuously improving" vision in the project description.

### 2.8 No Concept of Skill Bundles or Workflows

**Our spec's US4**: Defines inter-agent handoff protocols.

**gstack says**: Skills form an explicit workflow chain: Think > Plan > Build > Review > Test > Ship > Reflect. Each skill knows its place in the chain and understands context from previous steps.

**Anthropic says**: No formal workflow chain, but the skill-creator references orchestration and describes how skills can invoke other skills.

**Gap**: Our handoff protocol (US4) treats inter-agent connections as metadata annotations. gstack treats them as a first-class workflow engine where the sequence matters and each step's output shapes the next step's behavior.

**Impact**: Medium. Annotations are a start, but without workflow-level composition, the 86 agents remain a directory rather than an operating system.

---

## 3. Dissecting the Skill-Creator Skill

The `skill-creator` is the most important skill in Anthropic's repo — it's the skill that makes other skills. Here's what we can learn from its design.

### 3.1 Architecture

```
skill-creator/
├── SKILL.md                    # ~800 lines — the full creation workflow
├── scripts/
│   ├── quick_validate.py       # Frontmatter validation
│   ├── package_skill.py        # ZIP packaging with validation
│   ├── run_eval.py             # Trigger evaluation
│   ├── run_loop.py             # Description optimization loop
│   ├── aggregate_benchmark.py  # Statistical aggregation
│   ├── generate_report.py      # Report generation
│   └── improve_description.py  # Description refinement
├── agents/
│   ├── grader.md               # 7-step assertion evaluation
│   ├── comparator.md           # Blind A/B comparison
│   └── analyzer.md             # Benchmark pattern analysis
├── references/
│   └── schemas.md              # JSON structures for evals, grading, benchmarks
├── assets/
│   └── eval_review.html        # Interactive review UI template
└── eval-viewer/
    └── generate_review.py      # HTML viewer generator
```

**Observation**: This is not a document. It's a complete product with 7+ scripts, 3 sub-agents, schema definitions, and a UI. It demonstrates that a "skill" at the highest level is a self-contained operational unit with its own toolchain.

### 3.2 The Core Loop

```
Capture Intent → Interview → Draft SKILL.md → Test → Evaluate → Iterate → Optimize Description
```

Each stage has specific deliverables:

1. **Capture Intent** (4 questions): What does it do? When does it trigger? What's the output format? Should we test it?
2. **Interview**: Edge cases, I/O formats, success criteria, dependencies. Research via MCPs in parallel.
3. **Draft**: Frontmatter + body. Description is "pushy." Instructions are imperative. Why > rules.
4. **Test**: 2-3 realistic prompts. Spawn parallel subagents (with-skill AND baseline). Don't wait — draft assertions while runs execute.
5. **Evaluate**: Grade, aggregate benchmarks, launch viewer for human review, collect feedback.
6. **Iterate**: Generalize from feedback. Keep lean. Remove things not pulling weight. If all test runs independently wrote similar helper scripts, bundle them as `scripts/`.
7. **Optimize Description**: 20 trigger eval queries (10 should-trigger, 10 should-not-trigger), automated optimization loop with 60/40 train/test split.

### 3.3 Key Design Principles (Direct Quotes)

| Principle | Quote | Implication for skill-os |
| --------- | ----- | ----------------------- |
| Generalize, don't overfit | "If the skill works only for those examples, it's useless. Rather than fiddly overfitty changes or oppressively constrictive MUSTs, try branching out and using different metaphors." | Our skills should teach reasoning, not just list rules. |
| Keep it lean | "Remove things that aren't pulling their weight. Read the transcripts — if the skill makes the model waste time doing unproductive things, get rid of those parts." | Every section in our enriched format must earn its place. |
| Explain the why | "Today's LLMs are smart. They have good theory of mind. If you find yourself writing ALWAYS or NEVER in all caps, that's a yellow flag." | Anti-patterns need rationale, not just prohibition. |
| Bundle repeated work | "If all 3 test cases resulted in the subagent writing a create_docx.py, that's a strong signal the skill should bundle that script." | Skills should include reusable scripts when patterns emerge. |
| Descriptions are triggers | "The description field is the primary mechanism that determines whether Claude invokes a skill." | Our frontmatter descriptions must be written for discoverability, not just human comprehension. |
| Communication adapts to audience | "There's a trend now where plumbers are opening their terminals, parents and grandparents googling 'how to install npm.'" | Skills should be accessible to non-technical domain experts, not just engineers. |

### 3.4 The Validation Pipeline

Anthropic has a `quick_validate.py` that checks:
- SKILL.md exists with valid YAML frontmatter
- `name` field: max 64 chars, lowercase + digits + hyphens only
- `description` field: max 1024 chars, no angle brackets, third-person
- Body uses imperative form
- Body size: 1,500–2,000 words ideal, under 3,000 recommended, hard max 5,000
- All referenced files exist
- No duplicated information across files

**Implication**: Our FR-002 says frontmatter "MUST include at minimum: name, description, department, agent, related-skills." We should also specify validation rules for each field (max lengths, allowed characters, format constraints).

---

## 4. What Else We Can Learn

### 4.1 The Template + Generated Pattern (gstack)

gstack separates human-edited templates (`.tmpl`) from generated output (`.md`). A build step resolves shared content (preamble, methodology, command references) so multiple skills stay consistent without copy-paste.

**Relevance**: With 603 skills, our agent description block (identical across all skills for the same agent) is already a maintenance burden. A template system would let us define agent descriptions once and generate them into skill files.

### 4.2 Preamble Tiers (gstack)

Not all skills need the same level of context. gstack's 4-tier preamble system injects progressively more boilerplate:
- T1 (minimal): Core setup only
- T4 (maximum): Full context including test triage, repo ownership, search guidance

**Relevance**: Our enriched skills will vary wildly in complexity. A `complexity-tier` in frontmatter could signal how much operational context the skill needs.

### 4.3 Error Philosophy (gstack)

"Errors are for AI agents, not humans — every error must be actionable. Include guidance on what to do next."

**Relevance**: Our Output section defines what the skill produces on success. We should also define what it produces on failure — what does the agent report when it can't complete the skill?

### 4.4 The "Boil the Lake" Principle (gstack)

"AI makes marginal cost of completeness near-zero. Always do the complete thing."

**Relevance**: This directly supports our ambition. Don't create 603 thin skills — create 603 comprehensive skills. But it also means each skill enrichment should be thorough, not a quick pass with TODO placeholders everywhere.

### 4.5 Dual-Platform Support (gstack)

gstack generates output for both Claude (`.claude/skills/`) and Codex (`.agents/skills/`). Different platforms need different frontmatter and formatting.

**Relevance**: If skill-os aims to be "the world's best resource for work agents on GitHub," it should be consumable by any AI agent platform — not just Claude. Platform-agnostic skill definitions with optional platform-specific adapters would broaden reach significantly.

---

## 5. Recommended Spec Changes

Based on this analysis, here are the changes I'd propose (pending your confirmation):

### High Priority

1. **Add writing voice guidance to FR-001**: Skill Description in third-person declarative. When to Use as trigger scenarios. Workflow in imperative form. Anti-Patterns with rationale (why, not just what).

2. **Add size constraints**: Skill file body MUST stay under 500 lines. Content exceeding this moves to `references/`. Frontmatter description MUST be 50–500 characters.

3. **Replace `rules/` with `scripts/`**: Drop the `rules/` directory (constraints belong in the skill body). Add `scripts/` for executable tools and `assets/` for output templates. Keep `references/` and `examples/`.

4. **Add "pushy" description guidance**: Frontmatter descriptions MUST include explicit trigger phrases and scenarios, written for AI agent discovery, not just human browsing.

### Medium Priority

5. **Add failure output to the Output section**: Define what the skill produces when it succeeds AND what it reports when it cannot complete.

6. **Add `version` to frontmatter**: Skill-level semver to track enrichment iterations.

7. **Add validation rules for frontmatter fields**: Max lengths, allowed characters, required format for each field.

8. **Add complexity tier to frontmatter**: A 1-3 tier indicating operational complexity, guiding how much context an AI agent should load.

### Lower Priority

9. **Consider a template/build system**: For agent descriptions that are identical across skills, define once and generate into files.

10. **Consider platform-agnostic output**: Design skill format to be consumable by Claude, Codex, Cursor, and other AI agent platforms.

11. **Add a skill evaluation framework**: Even lightweight — test prompts + expected behavior for each skill to verify effectiveness, not just structure.

---

## 6. Summary Scorecard

| Dimension | Our Spec | Anthropic | gstack | Gap |
| --------- | -------- | --------- | ------ | --- |
| Structured format | 7 sections | Flexible (frontmatter + body + resources) | Frontmatter + templated body | We're more rigid — may need flexibility |
| Progressive disclosure | references/ examples/ rules/ | references/ examples/ scripts/ assets/ | references/ templates/ bin/ | Missing scripts/ and assets/ |
| Size discipline | None specified | <500 lines body, <5k words | Preamble tiers control injection | Major gap |
| Writing voice | Unspecified | Imperative, third-person, "explain the why" | Natural language, imperative | Major gap |
| Discoverability | Frontmatter metadata | "Pushy" descriptions, trigger optimization | Explicit trigger + proactive suggestion phrases | Major gap |
| Testing/eval | Structural validation only | Full eval loop with benchmarks | 3-tier testing + health dashboard | Major gap |
| Versioning | None per skill | Optional version field | version + CHANGELOG | Minor gap |
| Platform support | Implicit Claude-only | Claude-native | Claude + Codex dual output | Future consideration |
| Workflow composition | Handoff annotations (US4) | Ad-hoc skill invocation | Explicit workflow chain (Think→Plan→Build→Review→Test→Ship→Reflect) | Medium gap |
| Error handling | Not addressed | Actionable error guidance | "Errors are for AI agents" philosophy | Minor gap |
