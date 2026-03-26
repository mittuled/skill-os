# Skill Quality & Compliance Checklist: Enrich Skill Directory

**Purpose**: Validate that requirements for skill quality, completeness, and constitutional/spec enforcement are well-defined, unambiguous, and implementation-ready
**Created**: 2026-03-26
**Reviewed**: 2026-03-26
**Feature**: [spec.md](../spec.md)
**Constitution**: v2.0.0 | **Audience**: Reviewer (pre-implementation gate) | **Depth**: Thorough
**Result**: 64/67 PASS (3 accepted risks)

## Skill File Format Requirements

- [x] CHK001 - Is the exact section order for enriched SKILL.md defined without ambiguity? [Completeness, Spec §FR-001] — YES: FR-001 lists all 9 sections in exact order.
- [x] CHK002 - Are the 9 required sections each given a specific heading format (e.g., `## When to Use` vs `### When to Use`)? [Clarity, Gap] — YES: data-model.md Body Sections table specifies exact headings (`## Agent:`, `## Skill Description`, etc.). Template confirms.
- [x] CHK003 - Is the distinction between "Agent header" content and "Skill Description" content clearly defined so they cannot be confused? [Clarity, Spec §FR-001] — YES: Agent header = seniority + role description + instance type + ethos ref. Skill Description = one sentence. Template shows clear separation.
- [x] CHK004 - Is the ethos profile reference format in the Agent header precisely specified (exact markdown link syntax, relative path pattern)? [Clarity, Spec §FR-011, Data Model] — YES: Template shows `Department ethos: [ideal-<dept>.md](../../../departments/<dept>/ideal-<dept>.md)`. Data-model fixed to match.
- [x] CHK005 - Are minimum content requirements defined for each section (e.g., "When to Use MUST have at least 1 scenario") or just for some? [Completeness, Spec §FR-001/003] — YES: Data-model specifies minimums: When to Use (min 1 scenario), Anti-Patterns ("None identified" if N/A), Related Skills (empty section if none). Other sections implicitly require content by their format.
- [x] CHK006 - Is the "Related Skills" section format specified — bulleted list, table, or freeform? [Clarity, Gap] — YES: Template shows bulleted list with relative path links + brief rationale. Data-model says "Reference list".
- [x] CHK007 - Does the spec define what a valid "None identified" anti-pattern entry looks like, including the required brief explanation? [Clarity, Spec §Edge Cases] — YES: Edge cases section specifies exact format: "None identified — revisit when domain expertise is available" + brief explanation of why the domain has low risk.

## YAML Frontmatter Requirements

- [x] CHK008 - Are all 7 required frontmatter fields (`name`, `description`, `department`, `agent`, `version`, `complexity`, `related-skills`) individually constrained with type, format, and validation rules? [Completeness, Spec §FR-002, Data Model] — YES: Data-model schema table specifies type, constraints, and description for each field.
- [x] CHK009 - Is the `description` field's "pushy" requirement quantifiable — are the three components (trigger phrases, adjacent scenarios, proactive suggestions) all mandatory or can some be omitted? [Clarity, Spec §FR-007] — YES: FR-007 now says "at minimum: one trigger phrase, one adjacent scenario, and one proactive suggestion. All three components are required."
- [x] CHK010 - Is the `related-skills` field format specified — list of relative paths, list of skill names, or list of objects with rationale? [Clarity, Spec §FR-002] — YES: Data-model says "List of relative paths to related SKILL.md files, may be empty []". FR-002 now says "list of relative paths."
- [x] CHK011 - Are the allowed values for `department` enumerated or must they match existing directory names dynamically? [Clarity, Data Model] — YES: Data-model says "Must match a departments/ subdirectory name" — dynamic matching.
- [x] CHK012 - Is there a defined process for assigning `complexity` class to a skill, or is it purely author judgment? [Gap, Spec §FR-002] — YES: FR-003 now includes a complexity classification guide with step/branching thresholds.
- [x] CHK013 - Does the frontmatter schema define whether additional optional fields are permitted or strictly forbidden? [Gap, Data Model] — YES: FR-002 now says "Additional optional frontmatter fields are permitted but not validated."

## Word Limit & Progressive Disclosure Requirements

- [x] CHK014 - Is "word count" defined — does it include frontmatter, headings, bullet markers, or only prose? [Clarity, Spec §FR-003] — YES: FR-003 defines "whitespace-delimited tokens in the body below the frontmatter closing ---, excluding markdown heading markers, bullet markers, and code fence markers."
- [x] CHK015 - Are the word limits (500/1,000/1,500) specified as hard errors or soft warnings in the validation script? [Clarity, Spec §FR-003/023] — YES: FR-003 says "hard errors in the validation script — not soft guidelines."
- [x] CHK016 - Is the Tier 1 metadata limit (~100 words) a hard constraint or a guideline? The "~" suggests approximation. [Ambiguity, Spec §FR-003] — ACCEPTED: The ~ is intentionally approximate. Description length varies (50-1024 chars). Tier 2 limits are the critical enforcement points; Tier 1 is guidance.
- [x] CHK017 - Is the 300-line threshold for reference file TOC a hard requirement or recommendation? [Clarity, Spec §FR-003] — YES: FR-003 says "MUST include a table of contents" — hard requirement.
- [x] CHK018 - Are requirements defined for what happens when a skill legitimately needs more than 1,500 words even after offloading to references? [Edge Case, Gap] — YES: FR-003 now says "split it into two skills with distinct responsibilities — this signals a Single Responsibility violation."

## Writing Style & Voice Requirements

- [x] CHK019 - Are the four voice modes (third-person declarative, scenario-based, imperative, rationale-driven) each illustrated with a good AND bad example? [Clarity, Spec §FR-008] — YES: FR-008 provides good examples for all four modes. FR-004 provides bad examples for Workflow. Template illustrates all sections.
- [x] CHK020 - Is the prohibition on second-person ("You should...") explicitly defined for ALL sections or only for Workflow? [Completeness, Spec §FR-004] — YES: FR-004 prohibits second-person for Workflow explicitly. FR-008's voice guidance per section implicitly prevents it everywhere — no section uses second-person.
- [x] CHK021 - Is the "explain the why" requirement (FR-009) measurable — how does a reviewer determine if rationale is sufficient vs. superficial? [Measurability, Spec §FR-009] — YES: FR-009 provides a concrete good vs. bad example. FR-005 specifies the format: "anti-pattern statement followed by rationale." Depth is inherently subjective but the structure is measurable.
- [ ] CHK022 - Are there requirements for language consistency across skills owned by the same agent (same terminology, same level of detail)? [Consistency, Gap] — **ACCEPTED RISK**: The agent description block is already identical per constitution. Skill content naturally varies by domain. Cross-skill terminology consistency is desirable but not formally required. Low impact.

## Constitution v2.0.0 Alignment

- [x] CHK023 - Does Principle I (Template Fidelity) in the constitution exactly match FR-001 in the spec, or are there discrepancies in section names/order? [Consistency, Constitution §I vs Spec §FR-001] — YES: Both list identical 9 sections in the same order.
- [x] CHK024 - Does the constitution's naming constraint (Principle IV) align with the spec's `name` field validation rules (FR-002)? [Consistency, Constitution §IV vs Data Model] — YES: Both require kebab-case, name matching directory name.
- [x] CHK025 - Does the constitution's word limit definition (Principle VI) match the spec's three-tier model (FR-003) without contradiction? [Consistency, Constitution §VI vs Spec §FR-003] — YES: Both specify 500/1,000/1,500 by complexity class.
- [x] CHK026 - Does the constitution's ethos requirement (Principle VII) match the spec's ethos requirements (FR-010/011/012) in all details? [Consistency, Constitution §VII vs Spec §FR-010-012] — YES: Both specify 15 departments, departments/<dept>/ location, max 500 words, every skill references, opinionated.
- [x] CHK027 - Are the constitution's structural conventions (context lookup chain, allowed directories) consistent with the spec's FR-013/014? [Consistency, Constitution §Structural vs Spec §FR-013-014] — YES: Both define skill → agent → department → _shared/, most specific wins.
- [x] CHK028 - Is the constitution's commit discipline (Principle V, logical-unit commits) reflected in the spec's migration requirements (FR-025/026)? [Consistency, Constitution §V vs Spec §FR-025-026] — YES: Both define logical-unit = one skill migration. FR-026 specifies git mv.
- [x] CHK029 - Does the constitution define what happens when a principle is violated during implementation — is there an enforcement mechanism beyond plan.md tracking? [Gap, Constitution §Governance] — YES: Constitution §Governance requires plan.md Constitution Check. FR-023's validation script enforces frontmatter, word limits, cross-refs, and ethos refs at runtime.

## Department Ethos Profile Requirements

- [x] CHK030 - Is the ethos profile format fully specified — required sections, heading levels, content expectations? [Completeness, Spec §FR-010, Ethos Template] — YES: Ethos template defines: Title (`#`), Philosophy (2-3 sentences), Principles (5-7 with rationale), Decision Framework (optional).
- [x] CHK031 - Is "opinionated and specific" (FR-012) measurable — how does a reviewer distinguish an opinionated principle from a generic platitude? [Measurability, Spec §FR-012] — YES: FR-012 provides a concrete platitude vs. opinionated example as a pattern.
- [x] CHK032 - Are requirements defined for how ethos profiles should handle overlapping principles between adjacent departments (e.g., Product and Design both care about "user-centricity")? [Edge Case, Spec §Edge Cases] — YES: Edge cases says "acknowledge shared principles while articulating what makes this department's perspective unique."
- [x] CHK033 - Is the 500-word limit for ethos profiles defined with the same precision as skill word limits — what counts as a word? [Consistency, Spec §FR-010 vs FR-003] — YES: FR-010 now says "(same word-count definition as FR-003 — whitespace-delimited tokens excluding markdown markers)."
- [x] CHK034 - Are requirements defined for ethos profile versioning, or do they have no version tracking? [Gap] — YES: FR-010 says "not versioned individually — they evolve with the department and are tracked via git history."
- [x] CHK035 - Is the "Decision Framework" section in the ethos template required or optional? [Clarity, Ethos Template] — YES: Data-model marks it as "No" in Required column. Template shows it without a Required marker.

## Supporting Context Requirements

- [x] CHK036 - Are requirements defined for when to create supporting context vs. when to keep everything in SKILL.md? [Gap, Spec §FR-013] — YES: FR-003 says "content exceeding limits MUST be moved to references/." FR-016 says "when multiple skills produce similar helper logic."
- [x] CHK037 - Is the four-level lookup chain (skill → agent → department → `_shared/`) specified with "most specific wins" behavior for ALL resource types or only references? [Clarity, Spec §FR-013/014] — YES: FR-013 now says "The lookup chain applies to all four resource types."
- [x] CHK038 - Are naming conventions defined for files within `references/`, `examples/`, `scripts/`, `assets/` directories? [Gap] — YES: FR-013 now has detailed naming conventions for all four types (kebab-case, extensions, documentation requirements).
- [x] CHK039 - Are requirements defined for `scripts/` executability — language constraints, dependency documentation, shebang lines? [Gap, Spec §Edge Cases] — YES: FR-013 says "header comment documenting: purpose, dependencies, usage. Python 3.10+ and shell (bash) are the preferred languages."
- [x] CHK040 - Are requirements defined for `examples/` format — must they have both input and output, or can they be output-only? [Gap, Spec §FR-013] — YES: FR-013 says "Examples MUST include both input and expected output."
- [x] CHK041 - Are requirements defined for `assets/` — file types allowed, naming conventions, how skills reference them? [Gap, Spec §FR-013] — YES: FR-013 says "kebab-case files of any type... NOT loaded into AI context... used by the agent to produce output artifacts."
- [x] CHK042 - Is the `_shared/` directory's internal structure specified, or is it freeform? [Gap, Spec §FR-014] — YES: Follows the same four-type pattern (references/, examples/, scripts/, assets/) as all other levels. Plan confirms structure.

## Cross-Referencing & Handoff Requirements

- [x] CHK043 - Is the `related-skills` cross-reference required to be bidirectional (if A references B, must B reference A)? [Clarity, Spec §FR-015] — YES: FR-015 says "Cross-references MUST be bidirectional... validation script flags unidirectional references as warnings."
- [ ] CHK044 - Are handoff protocol requirements (US5) specific enough — is the artifact format/type vocabulary defined or freeform? [Clarity, Spec §US5] — **ACCEPTED RISK**: Artifact types are freeform (markdown reports, JSON data, slide decks, etc.). A controlled vocabulary would be too rigid for 472 skills across 16 departments. The Output section per-skill defines the specific artifact.
- [x] CHK045 - Are requirements defined for validating cross-references at commit time vs. periodic batch validation? [Gap, Spec §FR-023] — YES: FR-023 says "MUST run on demand... SHOULD be integrated into CI to run on every PR."
- [x] CHK046 - Is the cross-reference path format precisely defined — relative from SKILL.md location, or relative from repo root? [Clarity, Spec §FR-015] — YES: FR-015 says "relative paths from the SKILL.md file's location."

## Discovery & Platform Support Requirements

- [x] CHK047 - Are "platform-agnostic" requirements (FR-018) testable — what specific platform-specific syntax is prohibited? [Measurability, Spec §FR-018] — YES: FR-018 says "No platform-specific frontmatter fields or body syntax." YAML+markdown is inherently platform-agnostic.
- [x] CHK048 - Is the skill index generation (FR-017) specified with output format requirements, or just "must be generatable"? [Completeness, Spec §FR-017] — YES: FR-017 now specifies JSON output (`skill-index.json`) with defined fields per entry.
- [x] CHK049 - Are the "pushy description" components (trigger phrases, adjacent scenarios, proactive suggestions) each given minimum count requirements? [Clarity, Spec §FR-007] — YES: FR-007 now says "at minimum: one trigger phrase, one adjacent scenario, and one proactive suggestion. All three components are required."
- [x] CHK050 - Is the description's 50-character minimum sufficient for a pushy description containing all three components? [Consistency, Spec §FR-002] — YES: 50 chars is a floor. A description with all three components will naturally be 100-500 chars. The 1024-char max is the practical constraint.

## Validation & Enforcement Requirements

- [x] CHK051 - Are all validation rules defined with severity levels (ERROR vs WARNING) so implementers know which block vs. which advise? [Completeness, Spec §FR-023, Data Model] — YES: Data-model Validation Rules table has ERROR/WARNING columns. FR-023 specifies word limits as "hard error" and bidirectional refs as "warning."
- [x] CHK052 - Is the validation script required to check word counts, or only structural elements? [Completeness, Spec §FR-023] — YES: FR-023 says "body within word limit for its complexity class (hard error)."
- [x] CHK053 - Are requirements defined for when validation runs — on commit, on PR, on demand, or all three? [Gap, Spec §FR-023] — YES: FR-023 says "on demand via python scripts/validate.py and SHOULD be integrated into CI on every PR."
- [x] CHK054 - Is the eval framework (US6) specified with enough detail to be implementable — eval file format, expected output structure, grading methodology? [Completeness, Spec §US6] — YES: FR-024 now specifies JSON format with `id`, `prompt`, `expected_behavior`, and `should_trigger` fields. SC-008 defines 3-point rubric.
- [x] CHK055 - Does the spec define what "measurably better" means in SC-008? Is there a rubric or is it subjective human judgment? [Measurability, Spec §SC-008] — YES: SC-008 defines 3-point rubric (completeness, structure, domain accuracy) with better/same/worse. 2/3 criteria = pass.

## Migration Requirements

- [x] CHK056 - Are requirements defined for handling cross-references that point to not-yet-migrated skills in later phases? [Edge Case, Spec §FR-025] — YES: Tasks notes say "Cross-references to not-yet-migrated skills use placeholder paths marked TODO."
- [x] CHK057 - Is the `git mv` preservation requirement (FR-026) testable — how is git history preservation verified? [Measurability, Spec §FR-026] — YES: Testable via `git log --follow <new-path>` showing pre-migration history.
- [ ] CHK058 - Are requirements defined for the org chart update format when paths change from flat to subdirectory? [Gap, Spec §FR-025] — **ACCEPTED RISK**: The org chart format is its own document. FR-025 says "update" without prescribing format changes because the chart's structure predates this feature. Updates are mechanical (path substitution). Low impact.
- [x] CHK059 - Is the department migration order (Product → Marketing+Design → Engineering → Revenue+Governance → Operations) specified as mandatory or recommended? [Clarity, Spec §FR-025, Plan] — YES: FR-025 says "MUST proceed department-by-department, starting with Product." Plan specifies the full order.
- [x] CHK060 - Are rollback requirements defined — what happens if a department migration is partially complete and needs to be reverted? [Gap, Recovery Flow] — YES: FR-027 defines rollback via `git revert` in reverse order with granular per-skill rollback.

## Completeness Across User Stories

- [x] CHK061 - Does US1 (format) define acceptance criteria for ALL 9 sections, or are some sections missing explicit acceptance tests? [Coverage, Spec §US1] — YES: US1 covers frontmatter/trigger (AS1), workflow/imperative (AS2), anti-patterns/rationale (AS3), output/failure (AS4), word limits (AS5), migration (AS6). SC-002 validates structural completeness for all 9 sections.
- [x] CHK062 - Does US2 (ethos) define how to validate that a profile is "opinionated" beyond subjective review? [Measurability, Spec §US2] — YES: FR-012 provides platitude vs. opinionated example pattern. US2 AS3 says "authored by or validated against domain expertise."
- [x] CHK063 - Does US3 (context) define acceptance criteria for each of the four resource types independently? [Coverage, Spec §US3] — YES: US3 has scenarios for scripts (AS2), assets (AS3), shared resources (AS4/5), and lookup chain (AS6). References and examples covered in AS1.
- [x] CHK064 - Does US4 (discovery) define acceptance criteria for platform-agnostic parsing on at least two different AI platforms? [Coverage, Spec §US4] — YES: US4 AS4 names Claude, Codex, Cursor. Independent test specifies "Claude Code session and a Codex session."
- [x] CHK065 - Does US5 (handoffs) define minimum handoff documentation requirements — is one workflow chain sufficient or are five required? [Clarity, Spec §US5 vs SC-005] — YES: SC-005 says "at least 5 end-to-end workflows spanning 3+ agents."
- [x] CHK066 - Does US6 (evals) define the eval file format, or is it left to implementation? [Completeness, Spec §US6] — YES: FR-024 now specifies JSON format with `id`, `prompt`, `expected_behavior`, `should_trigger` fields.
- [x] CHK067 - Are requirements defined for the ETHOS.md root document (FR-020) — format, length, required sections, update process? [Completeness, Spec §FR-020] — YES: FR-020 now specifies: plain markdown, 300–500 words, Philosophy section, Principles section (5-7), Decision Priorities section.

## Notes

- **64/67 PASS** — 3 items marked as accepted risks (CHK022, CHK044, CHK058)
- CHK022 (cross-agent language consistency): Low impact, agent descriptions already identical per constitution
- CHK044 (handoff artifact vocabulary): Freeform is appropriate given 472 skills across 16 departments
- CHK058 (org chart update format): Mechanical path substitution, doesn't need formal specification
- All 8 previously identified gaps (word count definition, complexity guide, measurably better, rollback, naming conventions, ethos versioning, bidirectional refs, validation timing) have been resolved
- Additional gaps fixed during this review: optional frontmatter fields (CHK013), >1500 word edge case (CHK018), pushy description minimums (CHK049), index output format (CHK048), eval format (CHK054/066), ETHOS.md format (CHK067)
