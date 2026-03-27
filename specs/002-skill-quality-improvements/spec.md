# Feature Specification: Skill Quality Improvements

**Feature Branch**: `002-skill-quality-improvements`
**Created**: 2026-03-27
**Status**: Draft
**Input**: Address all recommendations and shortcomings identified in the comparative report (`specs/001-enrich-skill-directory/comparative-report.md`), add depth to match zubair-trabzada's production-grade skill quality (`specs/001-enrich-skill-directory/zubair-comparison-report.md`), add 29 missing high-impact skills, and build a company tooling onboarding system.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Deepen All 495 Skills to Production-Grade Quality (Priority: P1)

Every skill in skill-os is rewritten to match or exceed the depth of zubair-trabzada's best skills. This means: every workflow step has specific deliverables and decision logic (not generic checklists), every assessment skill has a weighted scoring rubric with grade bands, every skill that produces output has a full pre-built template (not just a format description), and every skill includes signal tables, framework references, or methodology details specific to its domain.

The current 500/1,000/1,500 word limits for the SKILL.md body remain — but depth is achieved through aggressive use of `references/` subdirectories. The lean body provides the workflow and decision logic. The references provide the scoring rubrics, output templates, signal tables, framework details, and domain-specific checklists that make the skill production-ready.

**Why this priority**: The zubair comparison revealed that skill-os skills are 3-5x shallower than the best competitors. A skill that says "Qualify the lead using BANT" is documentation. A skill that provides the BANT scoring rubric with signal-to-score tables, confidence levels, and grade-specific action recommendations is an operating system. Depth is what makes the difference between a directory and a tool that agents can actually execute.

**Independent Test**: Take 5 skills — one from each of Product, Engineering, Marketing, Sales, Legal. Compare each against the equivalent zubair skill (where one exists). The skill-os version should match or exceed on: (1) workflow specificity, (2) scoring/assessment rigour, (3) output template completeness, (4) domain-specific terminology and frameworks. Use the 3-point rubric (completeness, structure, domain accuracy).

**Acceptance Scenarios**:

1. **Given** any enriched skill, **When** an AI agent executes the workflow steps, **Then** every step has enough detail to execute without guessing — specific frameworks named, specific deliverables defined, specific decision criteria listed.
2. **Given** a skill that evaluates or assesses, **When** executed, **Then** it produces a quantitative score using a weighted rubric in `references/scoring-rubric.md` with criteria, weights (summing to 100%), scale (0-10 or 0-100), and grade bands (A+ through F).
3. **Given** a skill that produces a report or document, **When** executed, **Then** it follows a full output template in `assets/` with every section pre-defined — not just "produces a report in markdown" but the actual template with section headings, placeholder content, and formatting guidance.
4. **Given** the deepened skill body + references, **When** the body word count is checked, **Then** it stays within the complexity tier limit (500/1,000/1,500). Depth lives in `references/`, not in a bloated body.
5. **Given** the full set of 495 deepened skills, **When** compared against zubair's equivalent skills, **Then** skill-os matches on depth while exceeding on structural consistency, organizational context, and breadth.

---

### User Story 2 - Add 29 Missing High-Impact Skills (Priority: P2)

29 skills identified in the zubair comparison as critical gaps are added to skill-os. These are the most operationally valuable skills in Marketing (7), Sales (10), and Legal (12) — the capabilities that zubair covers and skill-os doesn't. Each new skill is created at production-grade depth from day one, following the deep format established in US1.

**Why this priority**: skill-os cannot claim to be the world's best skill directory while missing the most commonly needed marketing (SEO, ads, CRO), sales (prospecting, qualification, outreach), and legal (contract review, NDA generation, compliance audit) skills. These 29 skills close the coverage gap with the most popular competitor repos.

**Independent Test**: After adding all 29 skills, run the zubair comparison analysis again. Every capability that was listed as a "skill-os gap" should now show as "Parity" or "skill-os better."

**Acceptance Scenarios**:

1. **Given** the 7 new Marketing skills (audit orchestrator, copywriting analyst, ad campaign builder, funnel optimizer, landing page auditor, SEO auditor, brand voice analyst), **When** compared against zubair's marketing equivalents, **Then** each matches on depth and exceeds on structural consistency.
2. **Given** the 10 new Sales skills (prospect orchestrator, company researcher, lead qualifier, decision-maker mapper, cold outreach builder, follow-up builder, meeting prep builder, sales proposal builder, ICP builder, sales competitive intel), **When** compared against zubair's sales equivalents, **Then** each includes scoring rubrics and output templates at parity.
3. **Given** the 12 new Legal skills (contract review orchestrator, risk analyst, comparator, plain English translator, negotiation strategist, missing protections finder, NDA generator, ToS generator, privacy policy generator, agreement generator, compliance auditor, freelancer reviewer), **When** compared against zubair's legal equivalents, **Then** each includes the domain-specific frameworks (BANT, MEDDIC, STRIDE, GDPR checklists, etc.) that make zubair's skills production-grade.
4. **Given** all 29 new skills, **When** validated, **Then** each has YAML frontmatter, 9 sections, ethos reference, at least one scoring rubric or output template in `references/` or `assets/`, and stays within word limits.

---

### User Story 3 - Company Tooling Onboarding Skill (Priority: P3)

A new company deploying skill-os runs the `company-tooling-onboarder` skill, which interviews the operator about every tool the org uses (Slack, GitHub, Jira, Datadog, HubSpot, etc.), authenticates against each tool's API, and connects them via MCP servers or CLI integrations. After onboarding completes, all company data is accessible to skill-os agents through their connected tools. If a tool doesn't have a CLI or MCP server, the skill offers to create one using open-source MCP/CLI converters.

**Why this priority**: Without connected tools, skill-os agents can describe workflows but can't execute them. Tool onboarding is the bridge from "documentation OS" to "operating system." Every other improvement (triggers, gates, rubrics) is more valuable when agents can actually interact with the org's real tools.

**Independent Test**: Run the onboarding skill in a test environment with 3 tools (GitHub, Slack, a mock CRM). Verify: (1) the skill discovers all three, (2) authenticates successfully, (3) agents can subsequently read from and write to each tool.

**Acceptance Scenarios**:

1. **Given** a fresh skill-os deployment, **When** the operator runs the `company-tooling-onboarder` skill, **Then** it interactively asks about each tool category (communication, source control, project management, observability, CRM, etc.) and records which tools the org uses.
2. **Given** a tool with an existing MCP server (e.g., GitHub, Slack, Linear), **When** the onboarding skill detects it, **Then** it authenticates using the tool's standard auth flow (OAuth, API key, etc.) and connects the MCP server.
3. **Given** a tool without an MCP server or CLI, **When** the onboarding skill detects it, **Then** it offers to create a custom MCP wrapper using open-source converters (e.g., REST-to-MCP, OpenAPI-to-MCP) and delegates to the `mcp-server-builder` skill.
4. **Given** all tools are connected, **When** an agent executes a skill that references a connected tool, **Then** the agent can read from and write to that tool without additional setup.

---

### User Story 4 - Tool Policy Management (Priority: P4)

After onboarding connects the org's tools, a structured `allowed-tools.yaml` policy file at the repo root defines which tools are company-wide (available to all agents), which are restricted to specific departments, agents, or skills. Every agent directory includes a one-line reference to this policy file so agents automatically know what they can access. The `tool-policy-manager` skill manages this file as an ongoing governance function — not a one-time setup.

**Why this priority**: Connecting tools without access control is a security risk. A support agent shouldn't have write access to the production deployment pipeline. A finance agent shouldn't read engineering incident channels. The policy file is the guardrail that makes tool connectivity safe at scale.

**Independent Test**: Create `allowed-tools.yaml` with company-wide tools (Slack, GitHub) and department-restricted tools (Datadog for Engineering only, DocuSign for Legal only). Verify that an Engineering agent can access Datadog but a Sales agent cannot.

**Acceptance Scenarios**:

1. **Given** `allowed-tools.yaml` at repo root, **When** an agent loads its context, **Then** it reads the policy file to determine which tools it may use — company-wide tools are always available, department/agent/skill restrictions are enforced.
2. **Given** a tool restricted to the Engineering department, **When** a Sales agent attempts to use it, **Then** the agent knows from the policy that it lacks access and reports the restriction rather than failing silently.
3. **Given** the `tool-policy-manager` skill, **When** an operator needs to add, remove, or change tool permissions, **Then** the skill updates `allowed-tools.yaml` with proper change tracking.
4. **Given** each agent directory, **When** a contributor browses it, **Then** the Agent header includes a reference: `Tool policy: [allowed-tools.yaml](../../allowed-tools.yaml)` so agents automatically load tool permissions.
5. **Given** the policy file, **When** validated by the validation script, **Then** it checks that referenced departments and agents exist in the repo.

---

### User Story 5 - MCP Server Builder Skill (Priority: P5)

When the onboarding skill encounters a tool without an MCP server or CLI, the `mcp-server-builder` skill (owned by the Skill Builder agent under Agent Operations) creates a custom MCP wrapper. It takes the tool's API documentation (OpenAPI spec, REST docs, or SDK reference), generates an MCP server that exposes the tool's capabilities, and validates it works before marking the tool as connected.

**Why this priority**: Not every SaaS tool has an MCP server. The ability to auto-generate one from API docs is what makes skill-os truly tool-agnostic — it can connect to anything with an API, not just the tools that have first-party MCP support.

**Independent Test**: Point the `mcp-server-builder` at a tool with an OpenAPI spec (e.g., a mock API). Verify it generates a working MCP server, validates it against the spec, and the tool becomes accessible to agents.

**Acceptance Scenarios**:

1. **Given** a tool's OpenAPI specification, **When** the `mcp-server-builder` processes it, **Then** it generates an MCP server that exposes the tool's endpoints as MCP tools.
2. **Given** the generated MCP server, **When** tested against the tool's API, **Then** at least the core CRUD operations work correctly.
3. **Given** no OpenAPI spec but REST API documentation, **When** the skill is invoked, **Then** it attempts to infer the API structure and generates a best-effort MCP wrapper, flagging endpoints it couldn't map.

---

### User Story 6 - Tool Health Checker Skill (Priority: P6)

The `tool-health-checker` skill (owned by Agent Operations Manager) periodically verifies that all connected tools are reachable, credentials are valid, and MCP servers are responding. It produces a health report and alerts when a tool goes offline, a token expires, or an MCP server fails.

**Why this priority**: Stale tokens and unreachable tools cause silent failures — agents attempt tool calls that fail, producing incomplete output without clear error messages. Proactive health checking catches these issues before they affect skill execution.

**Independent Test**: Connect 3 tools, then revoke one tool's API token. Run the health checker. Verify it reports the revoked token as a failure with a specific remediation step.

**Acceptance Scenarios**:

1. **Given** a set of connected tools, **When** the health checker runs, **Then** it tests connectivity and auth for each tool and produces a pass/fail report.
2. **Given** a tool with an expired token, **When** detected, **Then** the report includes the specific tool, the failure type (auth expired), and the remediation step (re-run onboarding for that tool).
3. **Given** a healthy tool environment, **When** the health checker runs, **Then** it reports all-clear with last-checked timestamps.

---

### User Story 7 - Add Triggers Frontmatter Field (Priority: P7)

Each skill's frontmatter MAY include a `triggers` field — a list of short phrases that match user input patterns for more accurate skill activation. This complements the pushy `description` with machine-optimized pattern matching. Triggers are 2-10 word phrases designed for fuzzy matching, not regex.

**Why this priority**: Jeffallan's repo demonstrated that explicit trigger phrases improve activation accuracy beyond description alone. Adding `triggers` to the most commonly used skills reduces false negatives (skills that should activate but don't).

**Independent Test**: Add `triggers` to 5 skills. Test with realistic user prompts and verify skills activate more reliably with triggers than with description alone.

**Acceptance Scenarios**:

1. **Given** a skill with `triggers: ["review this PR", "code review", "check my code"]`, **When** a user types a matching phrase, **Then** the skill activates more reliably.
2. **Given** a skill without `triggers`, **When** validated, **Then** no error — the field is optional.
3. **Given** the frontmatter schema, **When** `triggers` is present, **Then** validation checks it is a list of strings.

---

### User Story 8 - Add Checkpoint Gates to Complex Workflows (Priority: P8)

A contributor enriching a complex skill can mark specific workflow steps as checkpoints where an AI agent should pause for human review before proceeding. Gates are indicated by a `[GATE]` marker appended to the workflow step, signalling the agent must present its output and wait for approval before continuing.

**Why this priority**: Prevents autonomous execution of high-stakes decisions (deploys, legal notices, budget approvals). Without gates, agents either run to completion unsupervised or require external orchestration to pause.

**Independent Test**: Add `[GATE]` markers to 3 complex skills. Verify the marker is visible and the validation script accepts it.

**Acceptance Scenarios**:

1. **Given** a workflow step marked `[GATE]`, **When** an AI agent reaches that step, **Then** it presents its work-so-far and waits for human approval.
2. **Given** a simple skill with no `[GATE]` markers, **When** executed, **Then** it runs to completion without pausing.
3. **Given** the enrichment template, **When** updated, **Then** it includes guidance on when to add `[GATE]` markers.

---

### User Story 9 - Add Scoring Rubrics for Assessment Skills (Priority: P9)

Skills that evaluate, assess, or score include a structured scoring rubric in `references/scoring-rubric.md` defining weighted criteria, scoring scales, and grade mappings for consistent, quantitative assessments.

**Why this priority**: Assessment skills currently produce qualitative output. Rubrics make assessments reproducible and comparable.

**Independent Test**: Add a scoring rubric to `vendor-risk-assessor`. Run against two vendors. Verify both produce numeric scores using the same rubric.

**Acceptance Scenarios**:

1. **Given** a skill with a scoring rubric, **When** the workflow references it, **Then** the agent applies weighted criteria to produce a numeric score and grade.
2. **Given** two assessments from the same skill, **When** compared, **Then** they use identical criteria and scales.

---

### User Story 10 - Add Code Examples for Engineering Skills (Priority: P10)

Engineering skills include working code examples in `examples/` showing realistic input/output pairs in the language most relevant to the skill's domain.

**Why this priority**: Prose-only workflows force agents to infer code patterns. Examples reduce inference errors.

**Independent Test**: Add examples to `ci-cd-pipeline-builder`. Verify an agent references them and produces syntactically correct output.

**Acceptance Scenarios**:

1. **Given** an engineering skill with code examples, **When** an agent executes it, **Then** it references the examples and produces correct output.
2. **Given** a code example, **When** reviewed, **Then** it includes both input scenario and working code output.

---

### User Story 11 - Fix Quality Gaps in Engineering and Legal Skills (Priority: P11)

Rewrite Engineering skills scoring below 5/5 (generalist checklists → practitioner-grade workflows) and Legal skills missing anti-pattern rationale.

**Why this priority**: Only departments scoring below 5.0. Fixes bring the entire repo to a consistent quality floor.

**Independent Test**: Rewrite affected skills. Re-score using the 3-point rubric — both departments should score 5.0.

**Acceptance Scenarios**:

1. **Given** a rewritten Engineering skill, **When** assessed, **Then** it references specific patterns (blue-green, canary, feature flags).
2. **Given** a rewritten Legal skill, **When** validated, **Then** every anti-pattern includes *Why* rationale.

---

### Edge Cases

- What happens when a tool fails authentication during onboarding? The skill logs the failure, skips that tool, and continues with remaining tools. A summary at the end lists all failed tools with remediation steps.
- What happens when `allowed-tools.yaml` references a department that doesn't exist? The validation script flags it as a warning.
- What happens when the MCP server builder can't fully map an API? It generates a partial wrapper, flags unmapped endpoints, and marks the tool as "partially connected" in the health report.
- What happens when `triggers` overlap between two skills? The AI platform's skill selection mechanism handles disambiguation — skill-os does not resolve trigger conflicts.
- What happens when a `[GATE]` is placed in a simple skill? Validation warns but does not error.
- What happens when a scoring rubric's weights don't sum to 100%? Validation warns but does not error — additive scoring is valid.
- What happens when an agent references a tool not in `allowed-tools.yaml`? The agent reports the tool is unavailable per policy and suggests requesting access from the tool-policy-manager.

## Requirements *(mandatory)*

### Functional Requirements

**Skill Depth (Production-Grade Quality)**

- **FR-001**: Every skill MUST have workflow steps specific enough for an AI agent to execute without guessing — named frameworks, defined deliverables, explicit decision criteria. Generic steps like "Analyze the data" are not acceptable; "Apply RICE scoring to the backlog using Reach (0-10), Impact (0-10), Confidence (0-100%), Effort (person-weeks)" is.
- **FR-002**: Every skill that evaluates, assesses, scores, or reviews MUST include a weighted scoring rubric in `references/scoring-rubric.md` with: criteria names, weights summing to 100%, a numeric scale (0-10 or 0-100), grade bands (A+ through F with labels), and signal tables mapping observable evidence to scores.
- **FR-003**: Every skill that produces a report, document, or structured output MUST include a full output template in `assets/` with every section pre-defined — headings, placeholder content, formatting guidance, and examples of good vs. bad content per section.
- **FR-004**: The SKILL.md body stays within word limits (500/1,000/1,500). Depth is achieved through `references/` (rubrics, frameworks, signal tables, checklists) and `assets/` (output templates). The body provides the workflow and decision logic; references provide the domain-specific detail.
- **FR-005**: Each deepened skill MUST include at minimum: the body SKILL.md, one file in `references/` (scoring rubric, framework detail, or domain checklist), and one file in `assets/` (output template). Simple skills with no assessment or report output may omit `references/` and `assets/` if justified.

**29 Missing Skills**

- **FR-006**: 7 new Marketing skills MUST be created: `marketing-audit-orchestrator`, `copywriting-analyst`, `ad-campaign-builder`, `funnel-optimizer`, `landing-page-auditor`, `seo-auditor`, `brand-voice-analyst`. Each under the appropriate Marketing agent directory.
- **FR-007**: 10 new Sales skills MUST be created: `prospect-analyst-orchestrator`, `company-researcher`, `lead-qualifier`, `decision-maker-mapper`, `cold-outreach-builder`, `follow-up-sequence-builder`, `meeting-prep-builder`, `sales-proposal-builder`, `icp-builder`, `sales-competitive-intel`. Each under the appropriate Sales agent directory.
- **FR-008**: 12 new Legal skills MUST be created: `contract-review-orchestrator`, `contract-risk-analyst`, `contract-comparator`, `plain-english-translator`, `negotiation-strategist`, `missing-protections-finder`, `nda-generator`, `terms-of-service-generator`, `privacy-policy-generator`, `business-agreement-generator`, `compliance-auditor`, `freelancer-contract-reviewer`. Each under the appropriate Legal agent directory.
- **FR-009**: Each of the 29 new skills MUST be created at production-grade depth from day one — scoring rubrics, output templates, domain-specific frameworks, and signal tables included. No "v1 thin, v2 deep" approach.
- **FR-010**: The org chart and status.md MUST be updated to reflect the 29 new skills.

**Company Tooling Onboarding**

- **FR-011**: A `company-tooling-onboarder` skill MUST exist at `agents/agent-configuration-manager/company-tooling-onboarder/SKILL.md`. It interactively discovers, authenticates, and connects the org's tools via MCP servers or CLI integrations.
- **FR-012**: The onboarding skill MUST cover standard tool categories: communication (Slack, Teams), source control (GitHub, GitLab), project management (Linear, Jira), observability (Datadog, Grafana), CRM (HubSpot, Salesforce), documentation (Notion, Confluence), finance (QuickBooks, Xero), legal (DocuSign, Ironclad), and design (Figma).
- **FR-013**: For tools without existing MCP servers, the onboarding skill MUST offer to create a custom wrapper by delegating to the `mcp-server-builder` skill.

**Tool Policy Management**

- **FR-014**: A structured `allowed-tools.yaml` file MUST exist at repo root defining tool access at four levels: `company-wide` (all agents), `department` (agents in a specific department), `agent` (a specific agent role), and `skill` (a specific skill). Each entry includes `name`, `mcp` (boolean), and optional `scopes` (list of permitted actions).
- **FR-015**: A `tool-policy-manager` skill MUST exist at `agents/agent-configuration-manager/tool-policy-manager/SKILL.md` for ongoing governance of `allowed-tools.yaml`.
- **FR-016**: Every agent directory's Agent header MUST include a tool policy reference: `Tool policy: [allowed-tools.yaml](../../allowed-tools.yaml)`. This is added at the agent level, not per-skill — agents inherit their tool permissions.
- **FR-017**: The validation script MUST validate `allowed-tools.yaml`: proper YAML syntax, referenced departments exist in `departments/`, referenced agents exist in `agents/`.

**MCP Server Builder**

- **FR-018**: An `mcp-server-builder` skill MUST exist at `agents/skill-builder/mcp-server-builder/SKILL.md`. It generates MCP server wrappers from API documentation (OpenAPI, REST docs, or SDK references).
- **FR-019**: Generated MCP servers MUST be validated against the source API before the tool is marked as connected.

**Tool Health Checker**

- **FR-020**: A `tool-health-checker` skill MUST exist at `agents/agent-operations-manager/tool-health-checker/SKILL.md`. It verifies connectivity, credential validity, and MCP server responsiveness for all connected tools.
- **FR-021**: The health checker MUST produce a structured report: tool name, status (healthy/degraded/unreachable), last checked timestamp, and remediation steps for failures.

**Triggers Frontmatter Field**

- **FR-022**: The frontmatter schema MUST support an optional `triggers` field (list of trigger phrase strings, 2-10 words each). Existing skills without this field remain valid.
- **FR-023**: The validation script MUST validate `triggers` as a list of strings when present.
- **FR-024**: `triggers` complements (does not replace) the pushy `description`. Description is human-readable context; triggers are machine-optimized pattern matching.

**Checkpoint Gates**

- **FR-025**: Complex skill workflows MAY include `[GATE]` markers on steps requiring human approval. Format: `[GATE]` appended to the workflow step text.
- **FR-026**: The enrichment template and quickstart guide MUST include guidance on when to use `[GATE]`.
- **FR-027**: The validation script MUST accept `[GATE]` markers. It SHOULD warn when `[GATE]` appears in a simple-complexity skill.

**Scoring Rubrics**

- **FR-028**: Assessment skills SHOULD include a scoring rubric at `<skill>/references/scoring-rubric.md` defining: criteria, weights, scale, and grade mapping. (Subsumed by FR-002 for the depth pass; retained for clarity.)
- **FR-029**: The skill's Workflow MUST reference the rubric when one exists.

**Code Examples**

- **FR-030**: Engineering skills involving code SHOULD include working examples at `<skill>/examples/` with both scenario (input) and working code (output).
- **FR-031**: Examples MUST use the language most relevant to the skill's domain. Multi-language encouraged.

**Quality Fixes**

- **FR-032**: All Engineering skills scoring below 5/5 MUST be rewritten with domain-specific patterns and terminology. (Subsumed by US1 depth pass.)
- **FR-033**: All Legal skills missing anti-pattern rationale MUST be updated with *Why* explanations. (Subsumed by US1 depth pass.)

**Schema and Constitution Updates**

- **FR-034**: The frontmatter schema MUST be updated to include `triggers` as an optional field.
- **FR-035**: The constitution MUST be amended (MINOR version bump to v2.1.0) to document: `triggers` frontmatter field, `[GATE]` workflow markers, `allowed-tools.yaml` policy file, tool policy reference in Agent headers, the 4 new tooling skills, and the 29 new domain skills.

### Key Entities

- **Tool Policy File** (`allowed-tools.yaml`): A structured YAML file at repo root defining which tools are available at company-wide, department, agent, and skill levels. Each entry includes tool name, MCP availability, and permitted scopes. Referenced by every agent via the Agent header.
- **Company Tooling Onboarder**: A one-time setup skill that discovers, authenticates, and connects the org's tools. Owned by Agent Configuration Manager.
- **Tool Policy Manager**: An ongoing governance skill that maintains `allowed-tools.yaml`. Owned by Agent Configuration Manager.
- **MCP Server Builder**: A skill that generates custom MCP server wrappers from API documentation for tools without native MCP support. Owned by Skill Builder.
- **Tool Health Checker**: A periodic verification skill that tests tool connectivity, credential validity, and MCP responsiveness. Owned by Agent Operations Manager.
- **Triggers**: An optional frontmatter field listing short phrases for machine-optimized skill activation. Complements the pushy description.
- **Checkpoint Gate**: A `[GATE]` marker in a workflow step indicating the agent must pause for human approval.
- **Scoring Rubric**: A structured assessment framework in `references/scoring-rubric.md` with weighted criteria, scales, and grade mappings.

## Success Criteria *(mandatory)*

### Measurable Outcomes

**Depth & Coverage**

- **SC-001**: 100% of skills that evaluate or assess have a weighted scoring rubric in `references/scoring-rubric.md` with criteria, weights, scale, and grade bands.
- **SC-002**: 100% of skills that produce reports or documents have a full output template in `assets/` with pre-defined sections.
- **SC-003**: When 10 skill-os skills are compared against their zubair equivalents, skill-os matches or exceeds on workflow specificity, scoring rigour, and output template completeness while maintaining structural consistency.
- **SC-004**: All 495 existing skills are deepened — each has at minimum the SKILL.md body + one `references/` or `assets/` file (except justified simple skills).
- **SC-005**: All 29 new skills are created at production-grade depth and pass validation with 0 errors.
- **SC-006**: Total skill count reaches 524 (495 existing + 29 new).
- **SC-007**: All departments score 5.0 in the quality assessment (Engineering and Legal currently 4.0).

**Tooling**

- **SC-008**: The `company-tooling-onboarder` skill successfully connects at least 5 tools in a test environment.
- **SC-009**: `allowed-tools.yaml` defines tool policies for all 16 departments with 0 validation errors.
- **SC-010**: The `mcp-server-builder` generates a working MCP wrapper from an OpenAPI spec.
- **SC-011**: The `tool-health-checker` correctly identifies an expired credential with a remediation step.

**Enhancements**

- **SC-012**: At least 50 skills have `triggers` in frontmatter.
- **SC-013**: At least 20 complex skills have `[GATE]` markers.
- **SC-014**: At least 20 engineering skills have code examples in `examples/`.
- **SC-015**: Validation script passes with 0 errors after all changes.
- **SC-016**: Constitution updated to v2.1.0.

## Assumptions

- The onboarding skill runs interactively — it asks questions, receives answers, and configures tools based on responses. It is not a fully autonomous provisioning system.
- `allowed-tools.yaml` is the single source of truth for tool access. Per-skill `allowed-tools` in frontmatter is not used — the policy file at repo root governs all access.
- The MCP server builder produces functional wrappers, not production-grade servers. Generated servers are starting points that may need manual refinement for complex APIs.
- Tool health checking is on-demand (triggered by the operator or scheduled), not continuously running.
- `triggers` are short phrases for fuzzy matching, not regex. They supplement the description.
- `[GATE]` markers are advisory — enforcement depends on the agent runtime.
- Scoring rubrics are domain-specific — the requirement is structural (criteria + weights + scale + grades), not content-prescriptive.
- Code examples are working code, not pseudocode. Copy-pasteable and runnable.
- The depth pass (US1) touches all 495 skills but at varying levels: assessment skills get scoring rubrics, output-producing skills get templates, workflow-only skills get more specific step detail. Not every skill needs every type of depth artifact.
- The 29 new skills (US2) are net-new additions to the repo, not replacements. They may overlap with existing skills in adjacent agents — in such cases, the new skill is the deep, execution-focused version while the existing skill remains the lighter coordination/oversight version.
- The tool policy reference is added at the agent level (in the Agent header), not duplicated into every skill file. Agents inherit their tool permissions.
