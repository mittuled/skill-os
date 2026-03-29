# Feature Specification: Production-Grade Skill Depth

**Feature Branch**: `003-production-grade-depth`
**Created**: 2026-03-27
**Status**: Draft
**Input**: Deepen all 499 skills to match or exceed zubair-trabzada's production-grade quality, and add 29 missing high-impact skills identified in the zubair comparison report (`specs/001-enrich-skill-directory/zubair-comparison-report.md`).

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Deepen All 495 Skills to Production-Grade Quality (Priority: P1)

Every skill in skill-os (499 total, including 4 tooling skills from 002) is deepened to match or exceed zubair-trabzada's best skills. This means: every workflow step has specific deliverables and decision logic (not generic checklists), every assessment skill has a weighted scoring rubric with grade bands, every skill that produces output has a full pre-built template (not just a format description), and every skill includes signal tables, framework references, or methodology details specific to its domain.

The current 500/1,000/1,500 word limits for the SKILL.md body remain — but depth is achieved through aggressive use of `references/` subdirectories. The lean body provides the workflow and decision logic. The references provide the scoring rubrics, output templates, signal tables, framework details, and domain-specific checklists that make the skill production-ready.

**Why this priority**: The zubair comparison revealed that skill-os skills are 3-5x shallower than the best competitors. A skill that says "Qualify the lead using BANT" is documentation. A skill that provides the BANT scoring rubric with signal-to-score tables, confidence levels, and grade-specific action recommendations is an operating system. Depth is what makes the difference between a directory and a tool that agents can actually execute.

**Independent Test**: Take 5 skills — one from each of Product, Engineering, Marketing, Sales, Legal. Compare each against the equivalent zubair skill (where one exists). The skill-os version should match or exceed on: (1) workflow specificity, (2) scoring/assessment rigour, (3) output template completeness, (4) domain-specific terminology and frameworks. Use the 3-point rubric (completeness, structure, domain accuracy).

**Acceptance Scenarios**:

1. **Given** any enriched skill, **When** an AI agent executes the workflow steps, **Then** every step has enough detail to execute without guessing — specific frameworks named, specific deliverables defined, specific decision criteria listed.
2. **Given** a skill that evaluates or assesses, **When** executed, **Then** it produces a quantitative score using a weighted rubric in `references/scoring-rubric.md` with criteria, weights (summing to 100%), scale (0-10 or 0-100), and grade bands (A+ through F).
3. **Given** a skill that produces a report or document, **When** executed, **Then** it follows a full output template in `assets/` with every section pre-defined — not just "produces a report in markdown" but the actual template with section headings, placeholder content, and formatting guidance.
4. **Given** the deepened skill body + references, **When** the body word count is checked, **Then** it stays within the complexity tier limit (500/1,000/1,500). Depth lives in `references/`, not in a bloated body.
5. **Given** the full set of 499 deepened skills, **When** compared against zubair's equivalent skills, **Then** skill-os matches on depth while exceeding on structural consistency, organizational context, and breadth.

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

### Edge Cases

- What happens when a skill has no natural scoring rubric (e.g., a simple notification sender)? The `references/` requirement is waived for justified simple skills. The SKILL.md body documents why no rubric applies.
- What happens when the depth pass reveals a skill should be split? Follow constitution Principle II — split into two skills with distinct responsibilities. Both get full depth treatment.
- What happens when the 29 new skills overlap with existing skills? The new skill is the deep execution-focused version. The existing skill becomes the lighter coordination/oversight version. Both coexist with cross-references.
- What happens when a zubair skill is 5,000+ words and can't be matched within skill-os word limits? The SKILL.md body captures the workflow and decision logic (within limits). All depth — rubrics, signal tables, templates, checklists — goes into `references/` and `assets/`. The total depth across body + references should match or exceed zubair.

## Clarifications

### Session 2026-03-28

- Q: What size range should individual reference/asset files target? → A: No cap — let domain needs dictate length, validate by content quality only.
- Q: What research granularity should the depth pass use? → A: Per-domain-cluster — research grouped skill families (e.g., "sales qualification", "contract review"), ~50-80 research batches.
- Q: How should existing 002 depth artifacts be handled? → A: Upgrade — review and deepen all 10 existing rubrics to match 003's production-grade standard.

## Requirements *(mandatory)*

### Functional Requirements

**Skill Depth**

- **FR-001**: Every skill MUST have workflow steps specific enough for an AI agent to execute without guessing — named frameworks, defined deliverables, explicit decision criteria. Generic steps like "Analyze the data" are not acceptable; "Apply RICE scoring to the backlog using Reach (0-10), Impact (0-10), Confidence (0-100%), Effort (person-weeks)" is.
- **FR-002**: Every skill that evaluates, assesses, scores, or reviews MUST include a weighted scoring rubric in `references/scoring-rubric.md` with: criteria names, weights summing to 100%, a numeric scale (0-10 or 0-100), grade bands (A+ through F with labels), and signal tables mapping observable evidence to scores.
- **FR-003**: Every skill that produces a report, document, or structured output MUST include a full output template in `assets/` with every section pre-defined — headings, placeholder content, formatting guidance, and examples of good vs. bad content per section.
- **FR-004**: The SKILL.md body stays within word limits (500/1,000/1,500). Depth is achieved through `references/` (rubrics, frameworks, signal tables, checklists) and `assets/` (output templates). The body provides the workflow and decision logic; references provide the domain-specific detail. Reference and asset files have no word cap — length is dictated by domain needs and validated by content quality, not arbitrary limits.
- **FR-005**: Each deepened skill MUST include at minimum: the body SKILL.md, one file in `references/` (scoring rubric, framework detail, or domain checklist), and one file in `assets/` (output template). Simple skills with no assessment or report output may omit `references/` and `assets/` if justified.

**29 Missing Skills**

- **FR-006**: 7 new Marketing skills MUST be created: `marketing-audit-orchestrator`, `copywriting-analyst`, `ad-campaign-builder`, `funnel-optimizer`, `landing-page-auditor`, `seo-auditor`, `brand-voice-analyst`. Each under the appropriate Marketing agent directory.
- **FR-007**: 10 new Sales skills MUST be created: `prospect-analyst-orchestrator`, `company-researcher`, `lead-qualifier`, `decision-maker-mapper`, `cold-outreach-builder`, `follow-up-sequence-builder`, `meeting-prep-builder`, `sales-proposal-builder`, `icp-builder`, `sales-competitive-intel`. Each under the appropriate Sales agent directory.
- **FR-008**: 12 new Legal skills MUST be created: `contract-review-orchestrator`, `contract-risk-analyst`, `contract-comparator`, `plain-english-translator`, `negotiation-strategist`, `missing-protections-finder`, `nda-generator`, `terms-of-service-generator`, `privacy-policy-generator`, `business-agreement-generator`, `compliance-auditor`, `freelancer-contract-reviewer`. Each under the appropriate Legal agent directory.
- **FR-009**: Each of the 29 new skills MUST be created at production-grade depth from day one — scoring rubrics, output templates, domain-specific frameworks, and signal tables included. No "v1 thin, v2 deep" approach.
- **FR-010**: The org chart and status.md MUST be updated to reflect the 29 new skills.

**Phasing**

- **FR-011**: The depth pass MUST proceed department-by-department in this order: (1) Sales + Legal (most gaps from zubair comparison, 29 new skills created here), (2) Marketing (7 new skills + deepening existing), (3) Product (deepening only), (4) Engineering (deepening only), (5) all remaining departments. Within each department, create new skills first, then deepen existing ones.
- **FR-012**: The 29 new skills MUST be created before deepening existing skills in the same department — new skills establish the depth standard that existing skills are deepened to match.
- **FR-012a**: Research MUST be conducted per-domain-cluster (grouped skill families such as "sales qualification", "contract review", "compliance audit"), yielding ~50-80 research batches across the full repo. Each cluster's research informs all skills in that family.
- **FR-012b**: All 10 existing scoring rubrics from branch 002 MUST be upgraded to match 003's production-grade standard — including signal tables, A+ through F grade bands, and domain-specific frameworks. No 002 artifacts are grandfathered.

**Pre-Completed (from 002)**

- ~~FR-013~~: Engineering quality fixes (2 skills rewritten) — completed in 002.
- ~~FR-014~~: Legal anti-pattern rationale — already compliant, confirmed in 002.
- ~~FR-015~~: Constitution v2.1.0 — already amended in 002.

### Key Entities

- **Scoring Rubric**: A structured assessment framework at `<skill>/references/scoring-rubric.md` with weighted criteria (summing to 100%), numeric scale, grade bands (A+ through F), and signal tables mapping evidence to scores. Required for every assessment/evaluation skill.
- **Output Template**: A pre-built document template at `<skill>/assets/<output-name>-template.md` with every section defined, placeholder content, and formatting guidance. Required for every skill that produces a report or document.
- **Signal Table**: A mapping of observable evidence to scores, stored in `references/`. Example: for a lead qualification skill, a table mapping "Company has 50-200 employees" → "Size Fit score: 7/10".
- **Domain Checklist**: A comprehensive list of domain-specific items to verify, stored in `references/`. Example: for a compliance audit skill, a 57-item checklist across 7 regulatory frameworks.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of skills that evaluate or assess have a weighted scoring rubric in `references/scoring-rubric.md`.
- **SC-002**: 100% of skills that produce reports or documents have a full output template in `assets/`.
- **SC-003**: When 10 skill-os skills are compared against their zubair equivalents, skill-os matches or exceeds on workflow specificity, scoring rigour, and output template completeness.
- **SC-004**: All 499 existing skills are deepened — each has at minimum the SKILL.md body + one `references/` or `assets/` file (except justified simple skills).
- **SC-005**: All 29 new skills pass validation with 0 errors and include scoring rubrics + output templates.
- **SC-006**: Total skill count reaches 528 (499 existing + 29 new).
- **SC-007**: All departments score 5.0 in the quality assessment.
- **SC-008**: Validation script passes with 0 errors across the full repo.

## Assumptions

- The depth pass touches all 499 skills (495 original + 4 tooling from 002) at varying levels: assessment skills get scoring rubrics, output-producing skills get templates, workflow-only skills get more specific step detail. Not every skill needs every type of depth artifact. The 10 existing rubrics from 002 are upgraded to match the 003 standard — no grandfathering.
- The 29 new skills are net-new additions, not replacements. They may overlap with existing lighter skills — both coexist with cross-references.
- Depth is achieved through `references/` and `assets/`, not by inflating the SKILL.md body past word limits. Reference/asset files have no word cap — length is driven by domain needs.
- The depth pass proceeds department-by-department: Sales + Legal first (29 new skills + deepening), then Marketing (7 new + deepening), then Product, Engineering, and remaining departments (deepening only). Engineering and Legal quality fixes from 002 are already complete — no re-work needed.
- Web research is conducted per-domain-cluster (~50-80 batches across the repo), not per-individual-skill, to ensure depth reflects real-world best practices without requiring 500+ individual searches.
- Each deepened/new skill is a separate commit, following constitution Principle V.
