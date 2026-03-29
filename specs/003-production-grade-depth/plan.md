# Implementation Plan: Production-Grade Skill Depth

**Branch**: `003-production-grade-depth` | **Date**: 2026-03-28 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/003-production-grade-depth/spec.md`

## Summary

Deepen all 499 existing skills to production-grade quality by adding scoring rubrics, output templates, signal tables, and domain-specific frameworks in `references/` and `assets/` directories. Create 29 new high-impact skills (7 Marketing, 10 Sales, 12 Legal) at production-grade depth from day one. Upgrade 10 existing scoring rubrics from branch 002 to meet the new standard. Target: 528 total skills, all at depth parity with or exceeding zubair-trabzada's best.

## Technical Context

**Language/Version**: Markdown + YAML (content project)
**Primary Dependencies**: None (zero external deps)
**Storage**: Git-managed filesystem
**Testing**: `python3 scripts/validate.py` (stdlib-only validation)
**Target Platform**: Any AI agent runtime consuming skill files
**Project Type**: Content directory / knowledge base
**Performance Goals**: N/A (static content)
**Constraints**: SKILL.md body word limits (500/1,000/1,500 by complexity). Reference/asset files uncapped.
**Scale/Scope**: 528 skills across 86 agents, 16 departments. ~110 assessment skills need rubrics, ~122 output skills need templates, ~267 workflow skills need deeper step detail + at least one reference file.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Template Fidelity | PASS | All skills follow 9-section enriched format. New skills will follow same format. |
| II. Single Responsibility | PASS | Each of 29 new skills is a distinct capability. Edge case: if deepening reveals a split needed, follow the spec's edge case guidance. |
| III. Org Chart Consistency | WATCH | 29 new skills require org chart updates. Plan includes org chart update commits after each department batch. |
| IV. Canonical Naming | PASS | All 29 new skill names are kebab-case per spec FR-006/007/008. |
| V. Atomic Commits | PASS | One skill per commit. Org chart updates in separate commits. |
| VI. Progressive Disclosure | PASS | Body stays within word limits. All depth goes to references/ and assets/. |
| VII. Department Ethos | PASS | All 15 ethos profiles exist. New skills reference them. |
| VIII. Tool Policy | PASS | allowed-tools.yaml exists. All agents already reference it. |
| IX. Optional Frontmatter | PASS | Triggers already on 50 skills. New skills get triggers too. |
| X. Checkpoint Gates | PASS | Complex new skills get [GATE] markers where appropriate. |

No violations. No complexity tracking entries needed.

## Project Structure

### Documentation (this feature)

```text
specs/003-production-grade-depth/
├── spec.md              # Feature specification (done)
├── plan.md              # This file
├── research.md          # Domain cluster research findings
├── data-model.md        # Depth artifact schemas
├── quickstart.md        # Per-skill deepening guide
├── contracts/           # Artifact format contracts
│   ├── scoring-rubric-contract.md
│   └── output-template-contract.md
└── tasks.md             # Phase 2 output (via /speckit.tasks)
```

### Source Code (repository root)

```text
agents/
└── <agent>/
    └── <skill>/
        ├── SKILL.md              # Deepened body (existing, edited)
        ├── references/           # NEW: depth artifacts
        │   ├── scoring-rubric.md # For assessment skills
        │   ├── framework.md      # Domain methodology details
        │   ├── signal-table.md   # Evidence-to-score mappings
        │   └── checklist.md      # Domain-specific checklists
        └── assets/               # NEW: output templates
            └── <output>-template.md
```

**Structure Decision**: No new directories at repo root. All depth artifacts are added inside existing skill subdirectories following the established `references/` and `assets/` convention from constitution Principle VI.

## Domain Cluster Research Plan

Research is conducted per-domain-cluster (~60 clusters), not per-skill. Each cluster informs all skills in that family.

### Phase 1: Sales + Legal (22 new skills + deepen existing)

| Cluster | Skills Covered | Key Frameworks to Research |
|---------|---------------|---------------------------|
| Sales Qualification | lead-qualifier, deal-qualifier, icp-builder | BANT, MEDDIC, CHAMP, GPCTBA/C&I |
| Sales Prospecting | prospect-analyst-orchestrator, company-researcher, decision-maker-mapper | Firmographic analysis, org chart mapping, buying committee theory |
| Sales Outreach | cold-outreach-builder, follow-up-sequence-builder | AIDA, PAS, BAB frameworks, cadence science |
| Sales Execution | meeting-prep-builder, sales-proposal-builder, sales-competitive-intel | Challenger Sale, SPIN, battle card methodology |
| Sales Management | forecast-submitter, proposal-builder, contract-negotiator + all vp-sales skills | Sales forecasting methods, pipeline management |
| Contract Analysis | contract-review-orchestrator, contract-risk-analyst, contract-comparator | Contract law fundamentals, clause taxonomy, risk scoring |
| Contract Generation | nda-generator, terms-of-service-generator, privacy-policy-generator, business-agreement-generator | GDPR, CCPA, standard contract clauses, plain English principles |
| Contract Strategy | negotiation-strategist, missing-protections-finder, freelancer-contract-reviewer | Negotiation theory, standard protections by agreement type, IRS 20-factor test |
| Legal Compliance | compliance-auditor, plain-english-translator | SOC 2, HIPAA, GDPR, CCPA, ISO 27001, PCI DSS, SOX |
| Legal Risk | litigation-risk-assessor, ip-portfolio-manager, product-legal-reviewer + existing legal skills | IP law, regulatory risk frameworks, open source licensing |

### Phase 2: Marketing (7 new skills + deepen existing)

| Cluster | Skills Covered | Key Frameworks to Research |
|---------|---------------|---------------------------|
| Marketing Audit | marketing-audit-orchestrator, brand-guardian, campaign-performance-reviewer | Marketing audit methodology, brand health metrics |
| Content & Copy | copywriting-analyst, brand-voice-analyst, blog-post-writer, content-repurposer | Voice dimensions, headline formulas, readability scoring |
| Demand Gen & CRO | ad-campaign-builder, funnel-optimizer, landing-page-auditor, landing-page-optimiser | Google/Meta/LinkedIn ad platforms, CRO 5-dimension scoring |
| SEO | seo-auditor, seo-keyword-researcher | E-E-A-T, Core Web Vitals, technical SEO, content gap analysis |
| Email & Lifecycle | onboarding-sequence-designer, nurture-campaign-builder, retention-email-designer | Email deliverability, cadence optimization, segmentation |
| Events & PR | all event-marketing + pr-communications skills | Event ROI measurement, earned media tracking |
| Community & DevRel | all community-manager + developer-relations skills | Community health metrics, developer experience measurement |

### Phase 3: Product (deepen only)

| Cluster | Skills Covered | Key Frameworks to Research |
|---------|---------------|---------------------------|
| Product Strategy | product-vision-setter, roadmap-owner, pricing-strategist, platform-vs-feature-arbitrator | Product vision canvas, pricing psychology, platform economics |
| Product Execution | prd-author, user-story-writer, acceptance-criteria-definer, backlog-groomer | RICE, MoSCoW, user story mapping, BDD/ATDD |
| Product Analytics | analytics-interpreter, experiment-designer, product-analytics-reviewer | Bayesian experimentation, cohort analysis, north star metric frameworks |
| Product Operations | process-auditor, workflow-automation-builder, tool-administrator | Process maturity models, automation ROI |
| Product Marketing | messaging-framework-builder, launch-plan-owner, win-loss-analyst, competitive-battle-card-author | Positioning frameworks (April Dunford), competitive intelligence |
| Product Content | content-performance-analyst, content-gap-identifier, content-calendar-strategist | Content scoring frameworks, editorial calendar best practices |

### Phase 4: Engineering (deepen only)

| Cluster | Skills Covered | Key Frameworks to Research |
|---------|---------------|---------------------------|
| Architecture & Design | system-design-author, adr-writer, scalability-reviewer, proof-of-concept-builder | C4 model, ADR format (Michael Nygard), ATAM |
| Code Quality | code-reviewer, coding-standards-enforcer, test-coverage-advocate | Code review checklists, static analysis, coverage strategies |
| Backend | builder, api-implementer, data-model-implementer, background-job-developer | REST/GraphQL API design, job queue patterns |
| Frontend | all sr-frontend-developer skills | Component architecture, performance budgets, a11y standards |
| DevOps & Platform | ci-pipeline-builder, cd-pipeline-builder, infrastructure-as-code-author + all devops skills | GitOps, blue-green/canary, IaC patterns (Terraform/Pulumi) |
| Security | all security-engineer skills | OWASP Top 10, STRIDE, DREAD, CVE management |
| Data & ML | all data-engineer + ai-ml-engineer skills | MLOps, data quality frameworks, feature store patterns |
| QA & Testing | all qa-test-engineer skills | Test pyramid, risk-based testing, exploratory testing heuristics |

### Phase 5: Remaining Departments (deepen only)

| Cluster | Departments | Skills |
|---------|-------------|--------|
| Design Craft | Design | wireframe-creator, prototype-builder, motion-design-creator, usability-heuristic-reviewer |
| UX Research | Design | all ux-research + ux-researcher skills |
| Content Design | Design | all content-design skills |
| Financial Planning | Finance | all fpa-analyst + controller-accounting + cfo skills |
| Investor Relations | Finance | all investor-relations-manager skills |
| Customer Success | CS | all cs-manager + customer-success-manager skills |
| CS Programs | CS | customer-education-programme-builder, uat-test-coordinator, technical-health-assessor |
| Agent Operations | Agent Ops | all agent-ops skills including 4 tooling skills from 002 |
| Support | Support | all support-manager + support-agent skills |
| Tech Ops | Tech Ops | all it-operations + vendor-management skills |
| RevOps | RevOps | all revenue-operations-manager skills |
| Research | Applied Research | all applied-research-lead skills |
| Account Mgmt | Account Mgmt | all account-management skills |
| Implementation | Implementation | all implementation skills |
| Data & Growth | Data & Growth | all analytics-lead + data-analyst + growth-lead + growth-engineer skills |

## Skill Classification Summary

Per-department breakdown informing artifact requirements:

| Department | Total | Assessment (need rubrics) | Output (need templates) | Workflow (need deeper steps) |
|------------|-------|--------------------------|------------------------|------------------------------|
| Product | 82 | 20 | 22 | 40 |
| Engineering | 100 | 27 | 31 | 42 |
| Marketing | 54 | 11 | 17 | 26 |
| Design | 42 | 10 | 12 | 20 |
| Data & Growth | 39 | 8 | 10 | 21 |
| Finance | 32 | 5 | 2 | 25 |
| Legal | 24 | 7 | 4 | 13 |
| Agent Ops | 27 | 5 | 5 | 17 |
| Customer Success | 21 | 6 | 6 | 9 |
| Sales | 17 | 2 | 4 | 11 |
| Customer Support | 9 | 3 | 2 | 4 |
| Tech Ops | 9 | 3 | 1 | 5 |
| RevOps | 6 | 1 | 1 | 4 |
| Applied Research | 5 | 1 | 2 | 2 |
| Account Mgmt | 5 | 1 | 1 | 3 |
| Implementation | 4 | 0 | 2 | 2 |
| **TOTAL** | **499** | **110** | **122** | **267** |
| **+ 29 new** | **528** | ~+15 | ~+14 | — |

**Artifact generation targets**:
- ~125 scoring rubrics (110 existing assessment + ~15 new assessment skills)
- ~136 output templates (122 existing output + ~14 new output skills)
- ~267 workflow skills get at minimum one `references/` file (framework detail, domain checklist, or methodology guide)
- 10 existing rubrics from 002 upgraded to 003 standard

## Depth Treatment by Skill Type

### Assessment/Evaluation Skills (~125)
Each gets:
1. `references/scoring-rubric.md` — weighted criteria, 0-10 scale, A+ through F bands, signal tables
2. `assets/<assessment>-report-template.md` — output template for the assessment report
3. SKILL.md workflow updated to reference rubric by name at the scoring step

### Output-Producing Skills (~136)
Each gets:
1. `assets/<output>-template.md` — full template with sections, placeholders, formatting guidance
2. `references/` — at least one file: framework detail, quality checklist, or methodology guide
3. SKILL.md workflow updated to reference template at the output step

### Workflow-Only Skills (~267)
Each gets:
1. `references/` — at least one file: domain checklist, framework detail, decision matrix, or methodology guide
2. SKILL.md workflow steps made more specific: named frameworks, defined deliverables, explicit decision criteria
3. No rubric or template required unless the skill's depth pass reveals it should produce scored output

## Agent Assignment for 29 New Skills

### Marketing (7 new skills)

| Skill | Agent | Complexity |
|-------|-------|------------|
| marketing-audit-orchestrator | vp-marketing | Complex |
| copywriting-analyst | content-marketer | Medium |
| ad-campaign-builder | demand-gen-manager | Complex |
| funnel-optimizer | demand-gen-manager | Complex |
| landing-page-auditor | demand-gen-manager | Medium |
| seo-auditor | marketing-operations-manager | Complex |
| brand-voice-analyst | brand-designer | Medium |

### Sales (10 new skills)

| Skill | Agent | Complexity |
|-------|-------|------------|
| prospect-analyst-orchestrator | sales-development-rep | Complex |
| company-researcher | sales-development-rep | Medium |
| lead-qualifier | sales-development-rep | Complex |
| decision-maker-mapper | sales-development-rep | Medium |
| cold-outreach-builder | sales-development-rep | Complex |
| follow-up-sequence-builder | sales-development-rep | Medium |
| meeting-prep-builder | account-executive | Medium |
| sales-proposal-builder | account-executive | Complex |
| icp-builder | sales-manager | Complex |
| sales-competitive-intel | sales-manager | Medium |

### Legal (12 new skills)

| Skill | Agent | Complexity |
|-------|-------|------------|
| contract-review-orchestrator | corporate-counsel | Complex |
| contract-risk-analyst | corporate-counsel | Complex |
| contract-comparator | corporate-counsel | Medium |
| plain-english-translator | corporate-counsel | Simple |
| negotiation-strategist | corporate-counsel | Complex |
| missing-protections-finder | corporate-counsel | Medium |
| nda-generator | corporate-counsel | Medium |
| terms-of-service-generator | product-counsel | Complex |
| privacy-policy-generator | product-counsel | Complex |
| business-agreement-generator | corporate-counsel | Complex |
| compliance-auditor | security-compliance-programme-manager | Complex |
| freelancer-contract-reviewer | corporate-counsel | Medium |

## Execution Strategy

### Per-Skill Deepening Process

For each skill:
1. Read current SKILL.md and classify (assessment / output / workflow)
2. Conduct domain-cluster research (shared across cluster)
3. Create `references/` file(s) appropriate to skill type
4. Create `assets/` template if skill produces output
5. Update SKILL.md workflow steps to reference new artifacts
6. Validate: `python3 scripts/validate.py agents/<agent>/<skill>/SKILL.md`
7. Commit: one skill per commit

### Per-Department Batch Process

For each department (in phasing order):
1. **Research**: Conduct cluster research for all skill families in department
2. **Create new skills** (if any): Build 29 new skills at production-grade depth
3. **Deepen existing skills**: Process all existing skills using cluster research
4. **Upgrade 002 rubrics**: If department has existing rubrics from 002, upgrade them
5. **Update org chart**: Add new skills to `restructured-org-chart-v3.md`
6. **Update status.md**: Reflect new skill counts and depth status
7. **Validate**: Run validation across entire department

### Parallelization Strategy

Within each department, skills are independent and can be processed by parallel subagents. Recommended batch sizes:
- Large departments (Engineering 100, Product 82): 5-8 parallel agents, ~12-15 skills each
- Medium departments (Marketing 54, Design 42, Data & Growth 39): 3-5 parallel agents
- Small departments (Finance 32, Legal 24+12, Agent Ops 27): 2-3 parallel agents
- Tiny departments (Support 9, Tech Ops 9, RevOps 6, etc.): 1-2 parallel agents

Each agent receives the cluster research and processes non-overlapping skill sets.

## Complexity Tracking

No constitution violations detected. No complexity justifications needed.
