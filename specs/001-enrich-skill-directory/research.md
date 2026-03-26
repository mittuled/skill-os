# Research: Enrich Skill Directory

**Date**: 2026-03-26
**Method**: Analysis of 22 reference repos + Anthropic's official skill-creator + gstack

## Decision Log

### D1: Skill File Format — 9 Sections with YAML Frontmatter

**Decision**: Adopt a 9-section format: YAML frontmatter, title, Agent header (with ethos reference), Skill Description, When to Use, Workflow, Anti-Patterns, Output, Related Skills.

**Rationale**: Anthropic's official skill format uses YAML frontmatter + markdown body. Research across 22 repos showed production-grade skills include trigger conditions, phased workflows, anti-patterns, and output templates. The 9-section format captures all of these while staying within word limits.

**Alternatives considered**:
- 3-section format (current) — rejected: too thin for executable skills
- Anthropic minimal (frontmatter + free-form body) — rejected: no structural consistency across 600+ skills
- gstack template system (.tmpl + generated .md) — rejected: adds build step complexity inappropriate for a documentation repo

### D2: Skill Body Size Limits — 500/1,000/1,500 Words

**Decision**: Three complexity tiers with strict word limits: Simple (500), Medium (1,000), Complex (1,500). Overflow goes to `references/`.

**Rationale**: Measured across 25 Anthropic official skills and 30+ community skills. Anthropic's median is 200–280 lines / 1,000–1,600 words. Jeffallan's clean pattern is 127–186 lines / 900–1,250 words. Combined with ethos profile (500 words), total context per invocation stays at 1,000–2,000 words — fitting Haiku and Sonnet class models.

**Alternatives considered**:
- Anthropic's stated 5,000-word hard max — rejected: too large for smaller models
- Flat 500-word limit for all skills — rejected: complex skills with scoring rubrics need more room
- No limit with guidelines — rejected: guidelines get ignored; hard limits enforce discipline

### D3: Directory Structure — Skill Subdirectories

**Decision**: Each skill gets its own subdirectory: `agents/<agent>/<skill>/SKILL.md`. Supporting context lives alongside as `references/`, `examples/`, `scripts/`, `assets/`.

**Rationale**: Anthropic's standard is `<skill-name>/SKILL.md`. Every major skill repo uses this pattern. Per-skill directories enable progressive disclosure — the SKILL.md stays lean while deep context is one level away.

**Alternatives considered**:
- Keep flat files with agent-level-only context — rejected: can't distinguish skill-specific from agent-wide resources
- Hybrid (flat for simple, subdirs for complex) — rejected: inconsistent structure makes automation harder

### D4: Three-Level Context Hierarchy

**Decision**: Supporting context at four levels: per-skill, per-agent, per-department, global `_shared/`. Lookup chain: skill → agent → department → `_shared/`.

**Rationale**: Different resources have different scopes. A scoring rubric is skill-specific. A testing methodology is agent-specific (shared by all QA engineer skills). A compliance framework is department-specific (shared by all legal agents). A company-wide style guide is global.

**Alternatives considered**:
- Per-skill only — rejected: massive duplication of shared resources
- Two levels (skill + global) — rejected: no way to share agent-specific or department-specific resources
- Flat shared directory — rejected: no organizational structure for 600+ skills' worth of context

### D5: Department Ethos Profiles — `departments/<dept>/ideal-<dept>.md`

**Decision**: Top-level `departments/` directory parallel to `agents/`. Each department gets an `ideal-<dept>.md` (max 500 words) defining the mindset and principles of ideal practitioners.

**Rationale**: Skills define what to do. Ethos profiles define who to be. The 500-word limit ensures the profile fits alongside any skill body within context window budgets. Placing it in `departments/` (not inside `agents/`) makes it accessible to all agents in the department without belonging to any single agent.

**Alternatives considered**:
- Inside agents: `agents/_departments/` — rejected: conflates agent-specific and department-wide content
- Root-level flat: `ethos/` — rejected: no room for per-department shared references

### D6: Pushy Descriptions for AI Agent Discovery

**Decision**: Frontmatter `description` field must include explicit trigger phrases ("Use when..."), adjacent scenarios ("Also consider when..."), and proactive suggestions ("Suggest when the user is about to...").

**Rationale**: Anthropic's skill-creator explicitly states: "Claude has a tendency to under-trigger skills. Make descriptions a little bit pushy." gstack's skills include both trigger phrases and proactive suggestion triggers. metaskills/skill-builder treats the description as the single most critical element.

**Alternatives considered**:
- Passive descriptions ("This skill reviews contracts") — rejected: causes under-triggering
- Separate trigger file — rejected: Anthropic's model uses the description field as the trigger mechanism

### D7: Writing Voice — Imperative with Rationale

**Decision**: Workflow in imperative voice. Anti-patterns with rationale explaining why. Descriptions in third-person. No second-person ("you should").

**Rationale**: Anthropic's style guide mandates imperative/infinitive form. The skill-creator says "explain the why behind everything — LLMs are smart, they have good theory of mind." gstack's ETHOS.md demonstrates that principles with reasoning outperform rules without reasoning.

**Alternatives considered**:
- Descriptive voice ("The agent identifies risks") — rejected: not executable by AI agents
- Rules-heavy (ALWAYS/NEVER) — rejected: Anthropic explicitly flags this as a yellow flag

### D8: Platform-Agnostic Format

**Decision**: YAML frontmatter + markdown body, no platform-specific syntax. Parseable by Claude, Codex, Cursor, and any standard YAML/markdown parser.

**Rationale**: FrancyJGLisboa/agent-skill-creator (582 stars) demonstrated demand for cross-platform skills with its 14+ platform support. gstack outputs for both Claude and Codex. Skill-os should be consumable by any AI agent, not locked to one platform.

**Alternatives considered**:
- Claude-specific format with `.claude/skills/` conventions — rejected: limits reach
- Platform-specific adapters per platform — rejected: maintenance burden at 600+ skills scale

### D9: Migration Strategy — Department-by-Department Starting with Product

**Decision**: Migrate one department at a time. Product first (82 skills, 5 agents). Write ethos profile → migrate all skills in department → validate cross-references → update org chart.

**Rationale**: Department-by-department ensures each ethos profile is written before its skills are enriched. Product department is first because (a) it's well-understood, (b) it has the most skills (82) providing a comprehensive test of the format, and (c) cross-references within Product are dense enough to validate the linking system.

**Alternatives considered**:
- Complexity-first (all simple skills, then medium, then complex) — rejected: ethos profiles wouldn't exist yet when skills reference them
- Agent-by-agent — rejected: misses department-level ethos and shared context setup
- All at once — rejected: 472 files simultaneously is unreviable
