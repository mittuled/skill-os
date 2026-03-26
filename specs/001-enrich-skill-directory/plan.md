# Implementation Plan: Enrich Skill Directory

**Branch**: `001-enrich-skill-directory` | **Date**: 2026-03-26 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-enrich-skill-directory/spec.md`

## Summary

Transform skill-os from a flat directory of one-sentence skill descriptions into the world's best executable skill resource for AI work agents. Enrich 472 skill files from a 3-section format to a 9-section format with YAML frontmatter, migrate from flat files to skill subdirectories (`<skill>/SKILL.md`), add department ethos profiles, supporting context at three levels, cross-referencing, and a validation pipeline. Migration proceeds department-by-department across 5 phases, with web research informing every domain.

## Technical Context

**Language/Version**: Markdown + YAML frontmatter (no programming language — pure documentation repo)
**Primary Dependencies**: None — no runtime, no build process, no framework
**Storage**: Git-managed filesystem. Skill files at `agents/<agent>/<skill>/SKILL.md`, ethos profiles at `departments/<dept>/ideal-<dept>.md`
**Testing**: Validation script (Python or shell) for frontmatter/structure checks. Manual eval via Anthropic's skill-creator eval pattern for skill effectiveness.
**Target Platform**: GitHub (consumed by Claude, Codex, Cursor, and other AI agent runtimes)
**Project Type**: Documentation repository / AI agent skill library
**Performance Goals**: Skill body must fit in small model context windows — max 500/1,000/1,500 words by complexity class. Ethos profiles max 500 words. Combined context per invocation: 1,000–2,000 words.
**Constraints**: Platform-agnostic format (no Claude-specific or Codex-specific syntax). YAML frontmatter parseable by any standard YAML parser. Backward-compatible during migration.
**Scale/Scope**: 472 existing skills across 80 agents in 16 departments. Target: 600+ skills, 15 ethos profiles, 5+ documented workflows.

## Constitution Check

*Verified against constitution v2.0.0 (amended 2026-03-26).*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Template Fidelity | **PASS** | Constitution v2.0.0 defines the 9-section enriched format as the standard. |
| II. Single Responsibility | **PASS** | Each skill file still describes exactly one discrete responsibility. |
| III. Org Chart Consistency | **PASS** | Org chart remains canonical. Updated to reflect new paths per phase. |
| IV. Canonical Naming | **PASS** | Subdirectory format `<skill>/SKILL.md` is now constitutional. |
| V. Atomic Commits | **PASS** | Logical-unit commits (one skill per commit) are now constitutional. |
| VI. Progressive Disclosure | **PASS** | Word limits enforced per complexity class. |
| VII. Department Ethos | **PASS** | Ethos profiles created per phase before skill enrichment begins. |

All gates pass under the amended constitution.

## Project Structure

### Documentation (this feature)

```text
specs/001-enrich-skill-directory/
├── plan.md              # This file
├── research.md          # Phase 0 output — reference repo analysis
├── data-model.md        # Phase 1 output — skill file schema
├── contracts/
│   ├── skill-template.md    # The enriched SKILL.md template
│   ├── ethos-template.md    # The ideal-<dept>.md template
│   └── frontmatter-schema.yaml  # YAML frontmatter validation schema
├── quickstart.md        # Phase 1 output — how to enrich a skill
├── checklists/
│   └── requirements.md  # Spec quality checklist
└── red-team-analysis.md # Reference repo comparison
```

### Repository Structure (post-enrichment)

```text
skill-os/
├── ETHOS.md                          # Operating philosophy (FR-020)
├── CLAUDE.md                         # Dev guidance (updated)
├── restructured-org-chart-v3.md      # Canonical org chart (FR-021)
├── status.md                         # Enrichment progress tracker
│
├── departments/                      # Department-level context
│   ├── product/
│   │   ├── ideal-product.md          # Ethos profile (max 500 words)
│   │   └── references/               # Department-wide shared refs
│   ├── engineering/
│   │   ├── ideal-engineering.md
│   │   └── references/
│   └── ... (15 departments total)
│
├── agents/                           # Enriched skill files
│   ├── product-manager/
│   │   ├── references/               # Agent-level shared context
│   │   ├── backlog-groomer/
│   │   │   ├── SKILL.md              # Enriched skill file
│   │   │   ├── references/           # Skill-specific references
│   │   │   ├── examples/             # Input/output pairs
│   │   │   ├── scripts/              # Executable helpers
│   │   │   └── assets/               # Output templates
│   │   └── ...
│   └── ...
│
├── _shared/                          # Cross-department resources
│   ├── references/
│   ├── scripts/
│   └── assets/
│
└── scripts/                          # Repo-level tooling
    └── validate.py                   # Validation script (FR-023)
```

**Structure Decision**: Documentation-only repo. The "source code" IS the skill files. Tooling scripts live at repo root `scripts/`.

## Complexity Tracking

No constitutional violations — all principles pass under v2.0.0.

---

## Phase Overview

| Phase | Departments | Agents | Skills | Focus |
|-------|------------|--------|--------|-------|
| 0 | — | — | — | Foundation: ETHOS.md, directories, validation script, templates |
| 1 | Product | 5 | 82 | Product management, PMM, product ops — the department that defines what gets built |
| 2 | Marketing, Design | 20 | 96 | Go-to-market, brand, UX, content — the departments that shape how the product reaches users |
| 3 | Engineering | 12 | 100 | Build, deploy, test, secure — the department that makes it real |
| 4 | Data & Growth, Finance, Legal & Compliance, Sales | 20 | 112 | Revenue engine + governance — the departments that scale and protect the business |
| 5 | Agent Ops, Customer Success, Customer Support, Tech Ops, RevOps, Applied Research, Account Management, Implementation | 24 | 82 | Operations + customer lifecycle — the departments that run the machine |
| | **TOTAL** | **81** | **472** | |

---

## Phase 0: Foundation

**Goal**: Set up the infrastructure that all subsequent phases depend on.

**Deliverables**:

1. **ETHOS.md** — Root-level operating philosophy for the entire Skill OS
2. **`departments/` directory structure** — Create all 15 department directories with placeholder ethos profiles
3. **`_shared/` directory** — Global shared context directory
4. **`scripts/validate.py`** — Validation script checking frontmatter, word limits, cross-references, ethos references
5. **Updated CLAUDE.md** — Reflect new directory structure and enrichment workflow
6. **Updated `restructured-org-chart-v3.md`** — Add note about enrichment and new file paths

**No web research needed** — this phase is structural scaffolding.

---

## Phase 1: Product (82 skills, 5 agents)

**Goal**: Fully enrich the Product department as the reference implementation. Every skill in this department becomes the gold standard that all subsequent phases follow.

### Research Required

Before enriching any skills, research the following from the web to ensure world-class domain content:

- **Product management best practices**: How top PMs at companies like Stripe, Linear, and Notion run product processes. Frameworks like RICE, MoSCoW, Jobs-to-Be-Done, Opportunity Solution Trees.
- **Product marketing frameworks**: Positioning (April Dunford), messaging hierarchies, competitive intelligence methodologies, launch planning playbooks.
- **Product operations**: How product ops teams operate at scale — tooling, process audits, OKR tracking, knowledge base curation patterns.
- **PMM analytics**: SEO research workflows, content performance measurement, audience persona development, editorial calendar management.

### Departments & Agents

**Product** (5 agents, 82 skills):

| Agent | Dir | Skills | Complexity Mix |
|-------|-----|--------|---------------|
| VP Product | `vp-product` | 18 | Mostly complex — strategic, cross-functional |
| Product Manager | `product-manager` | 30 | Mix of simple, medium, complex |
| Product Operations Analyst | `product-operations-analyst` | 12 | Mostly medium — process and tooling |
| PMM — Product Marketing Manager | `pmm-product-marketing-manager` | 16 | Mix of medium and complex |
| PMM Analyst / Content Strategist | `pmm-analyst-content-strategist` | 6 | Mostly simple and medium |

### Execution Sequence

1. **Research**: Web research on product management, PMM, and product ops best practices
2. **Ethos**: Write `departments/product/ideal-product.md`
3. **VP Product** (18 skills): Start with the most strategic agent to establish the tone
4. **Product Manager** (30 skills): The largest agent — validates the format at scale
5. **Product Operations Analyst** (12 skills): Process-oriented, tests medium complexity
6. **PMM** (16 skills): Marketing-adjacent, tests cross-department referencing
7. **PMM Analyst** (6 skills): Smallest agent, quick to complete
8. **Validate**: Run validation script across all Product skills
9. **Update**: status.md + org chart

### Checkpoint

After Phase 1, review:
- Does the enriched format work at scale (82 skills)?
- Are the word limits realistic?
- Is the ethos profile actually influencing skill content?
- Do cross-references within the department resolve?
- Adjust templates/process before proceeding to Phase 2.

---

## Phase 2: Marketing + Design (96 skills, 20 agents)

**Goal**: Enrich the go-to-market and user experience departments. These departments have high overlap with Product (Phase 1), so cross-department references start forming here.

### Research Required

- **Marketing**: Demand generation funnels, content marketing strategies, PR/comms best practices (crisis communications, media relations), marketing operations (martech stacks, attribution models, lead scoring), social media management, lifecycle/email marketing (onboarding sequences, nurture campaigns), event marketing, analyst relations, community building, developer relations.
- **Design**: Design systems (Brad Frost's Atomic Design, Figma best practices), UX research methodologies (Nielsen Norman Group), content design (UX writing patterns, voice & tone frameworks), visual/interaction design, brand design, accessibility standards (WCAG).

### Departments & Agents

**Marketing** (12 agents, 54 skills):

| Agent | Dir | Skills | Complexity Mix |
|-------|-----|--------|---------------|
| VP Marketing | `vp-marketing` | 3 | Complex — strategic |
| Demand Gen Manager | `demand-gen-manager` | 3 | Medium |
| Content Marketer | `content-marketer` | 1 | Simple |
| PR / Communications Manager | `pr-communications-manager` | 5 | Medium to complex |
| Marketing Operations Manager | `marketing-operations-manager` | 5 | Medium — technical/tooling |
| Social Media Manager | `social-media-manager` | 4 | Simple to medium |
| Lifecycle / Email Marketing Manager | `lifecycle-email-marketing-manager` | 5 | Medium |
| Event Marketing Manager | `event-marketing-manager` | 6 | Medium |
| Analyst Relations Manager | `analyst-relations-manager` | 5 | Medium to complex |
| Community Manager | `community-manager` | 5 | Simple to medium |
| Developer Relations Lead | `developer-relations-lead` | 7 | Medium to complex |
| Technical Writer | `technical-writer` | 5 | Medium |

**Design** (8 agents, 42 skills):

| Agent | Dir | Skills | Complexity Mix |
|-------|-----|--------|---------------|
| Head of Design | `head-of-design` | 8 | Complex — leadership |
| UX / UI Designer | `ux-ui-designer` | 8 | Medium |
| Visual / Interaction Designer | `visual-interaction-designer` | 2 | Simple to medium |
| Brand Designer | `brand-designer` | 5 | Medium |
| UX Research Lead | `ux-research-lead` | 6 | Complex |
| UX Researcher | `ux-researcher` | 4 | Medium |
| Content Design Lead | `content-design-lead` | 5 | Complex |
| Content Designer / UX Writer | `content-designer-ux-writer` | 4 | Medium |

### Execution Sequence

1. **Research**: Web research on marketing disciplines and design methodologies
2. **Ethos**: Write `departments/marketing/ideal-marketing.md` and `departments/design/ideal-design.md`
3. **Marketing agents**: VP Marketing → Demand Gen → Content → PR/Comms → MarOps → Social → Lifecycle → Events → Analyst Relations → Community → DevRel → Technical Writer
4. **Design agents**: Head of Design → UX/UI → Visual/Interaction → Brand → UX Research Lead → UX Researcher → Content Design Lead → Content Designer
5. **Cross-references**: Link Marketing ↔ Product and Design ↔ Product skills
6. **Validate**: Run validation across Marketing + Design
7. **Update**: status.md + org chart

---

## Phase 3: Engineering (100 skills, 12 agents)

**Goal**: Enrich the largest single department. Engineering skills are the most technical and have the highest density of cross-references (to QA, Security, DevOps, Platform).

### Research Required

- **Software engineering practices**: Code review best practices (Google's engineering practices), architecture decision records (ADRs), system design patterns, technical debt management.
- **DevOps/Infrastructure**: CI/CD pipeline design, infrastructure as code (Terraform, Pulumi), container orchestration (Kubernetes), observability (OpenTelemetry), incident response (PagerDuty/Opsgenie patterns).
- **Security engineering**: OWASP top 10, threat modeling (STRIDE, PASTA), vulnerability management, penetration testing coordination, access control patterns, encryption best practices.
- **Data engineering**: ETL/ELT patterns, data warehouse design (dimensional modeling), data quality frameworks, streaming architectures (Kafka patterns).
- **AI/ML engineering**: MLOps practices, model training pipelines, feature stores, experiment tracking, model monitoring, AI ethics frameworks.
- **QA/Testing**: Test pyramid, test plan authoring, exploratory testing heuristics, performance testing methodologies, release qualification.
- **Platform engineering**: Internal developer platforms (IDP), developer experience metrics (DORA/SPACE), self-service provisioning.

### Departments & Agents

**Engineering** (12 agents, 100 skills):

| Agent | Dir | Skills | Complexity Mix |
|-------|-----|--------|---------------|
| VP Engineering | `vp-engineering` | 12 | Complex — strategic |
| Tech Architect | `tech-architect` | 9 | Complex — design authority |
| Tech Lead / PR Reviewer | `tech-lead-pr-reviewer` | 12 | Medium to complex |
| Database Expert | `database-expert` | 1 | Medium |
| Sr Frontend Developer | `sr-frontend-developer` | 5 | Medium |
| Sr Backend Developer | `sr-backend-developer` | 5 | Medium |
| QA / Test Engineer | `qa-test-engineer` | 8 | Medium |
| DevOps / Infrastructure Engineer | `devops-infrastructure-engineer` | 19 | Medium to complex |
| Platform Engineer | `platform-engineer` | 5 | Medium to complex |
| Data Engineer | `data-engineer` | 7 | Medium |
| Security Engineer | `security-engineer` | 10 | Medium to complex |
| AI / ML Engineer | `ai-ml-engineer` | 7 | Medium to complex |

### Execution Sequence

1. **Research**: Web research on engineering disciplines (deep dives per sub-domain)
2. **Ethos**: Write `departments/engineering/ideal-engineering.md`
3. **Leadership first**: VP Engineering → Tech Architect → Tech Lead
4. **Core builders**: Sr Frontend → Sr Backend → Database Expert
5. **Quality & ops**: QA → DevOps → Platform Engineer
6. **Specialized**: Data Engineer → Security Engineer → AI/ML Engineer
7. **Cross-references**: Link Engineering ↔ Product (handoffs), Engineering ↔ Design (handoffs)
8. **Validate**: Run validation across all Engineering skills
9. **Update**: status.md + org chart

---

## Phase 4: Revenue + Governance (112 skills, 20 agents)

**Goal**: Enrich the departments that scale and protect the business — data-driven growth, financial operations, legal compliance, and sales execution.

### Research Required

- **Data & Growth**: Growth engineering frameworks (Reforge), experimentation platforms, analytics instrumentation (Segment, Amplitude patterns), retention analysis methodologies, referral program design.
- **Finance**: Startup financial management (SaaS metrics, unit economics), FP&A best practices, revenue recognition (ASC 606), investor relations, cap table management, fundraising processes.
- **Legal & Compliance**: Contract lifecycle management, privacy regulations (GDPR, CCPA), open-source license compliance, corporate governance, IP portfolio management, AI regulation landscape.
- **Sales**: Modern sales methodologies (MEDDIC, Challenger, SPIN), pipeline management, deal qualification frameworks, solutions engineering, sales development (SDR playbooks), pricing strategy.

### Departments & Agents

**Data & Growth** (4 agents, 39 skills):

| Agent | Dir | Skills |
|-------|-----|--------|
| Analytics Lead | `analytics-lead` | 10 |
| Data Analyst | `data-analyst` | 10 |
| Growth Lead | `growth-lead` | 10 |
| Growth Engineer | `growth-engineer` | 9 |

**Finance** (5 agents, 32 skills):

| Agent | Dir | Skills |
|-------|-----|--------|
| CFO / VP Finance | `vp-finance` | 4 |
| Finance Manager | `finance-manager` | 4 |
| FP&A Analyst | `fpa-analyst` | 8 |
| Controller / Accounting | `controller-accounting` | 7 |
| Investor Relations Manager | `investor-relations-manager` | 9 |

**Legal & Compliance** (4 agents, 24 skills):

| Agent | Dir | Skills |
|-------|-----|--------|
| General Counsel | `general-counsel` | 4 |
| Corporate Counsel | `corporate-counsel` | 8 |
| Product Counsel | `product-counsel` | 7 |
| Security & Compliance Programme Manager | `security-compliance-programme-manager` | 5 |

**Sales** (7 agents, 17 skills):

| Agent | Dir | Skills |
|-------|-----|--------|
| VP Sales | `vp-sales` | 3 |
| Sales Manager | `sales-manager` | 4 |
| Account Executive | `account-executive` | 3 |
| Sales Development Rep (SDR) | `sales-development-rep` | 1 |
| Business Development | `business-development` | 2 |
| Solutions Engineering Manager | `solutions-engineering-manager` | 2 |
| Solutions Engineer | `solutions-engineer` | 2 |

### Execution Sequence

1. **Research**: Web research on growth, finance, legal, and sales domains
2. **Ethos**: Write `ideal-data-growth.md`, `ideal-finance.md`, `ideal-legal.md`, `ideal-sales.md`
3. **Data & Growth**: Analytics Lead → Data Analyst → Growth Lead → Growth Engineer
4. **Finance**: CFO → Finance Manager → FP&A → Controller → Investor Relations
5. **Legal**: General Counsel → Corporate Counsel → Product Counsel → Compliance Manager
6. **Sales**: VP Sales → Sales Manager → AE → SDR → BizDev → SE Manager → SE
7. **Cross-references**: Link Sales ↔ Product ↔ Marketing, Legal ↔ Product, Finance ↔ Sales
8. **Validate**: Run validation across all Phase 4 departments
9. **Update**: status.md + org chart

---

## Phase 5: Operations + Customer Lifecycle (82 skills, 24 agents)

**Goal**: Enrich the departments that run the day-to-day machine — agent operations, customer-facing teams, support, and operational infrastructure.

### Research Required

- **Agent Operations**: AI agent management patterns, prompt engineering best practices, skill architecture design, agent evaluation methodologies, multi-agent orchestration patterns.
- **Customer Success**: Customer health scoring models, QBR best practices, onboarding frameworks, churn prediction, expansion playbooks, customer advocacy programs.
- **Customer Support**: Support operations (Zendesk/Intercom patterns), ticket triage frameworks, knowledge base management, SLA monitoring, escalation protocols.
- **Technical Operations**: IT operations (ITIL frameworks), vendor management, procurement processes, IT asset management, identity/access management.
- **Revenue Operations**: CRM administration best practices (Salesforce/HubSpot), revenue data governance, sales process optimization, lead routing, commission plan design.
- **Applied Research**: Research-to-product translation, applied research methodologies, prototype-driven research.
- **Account Management**: Account planning, renewal negotiation, upsell/cross-sell strategies, account risk management.
- **Implementation**: Implementation methodologies, data migration best practices, customer environment configuration.

### Departments & Agents

**Agent Operations** (6 agents, 23 skills):

| Agent | Dir | Skills |
|-------|-----|--------|
| VP Agent Operations | `vp-agent-operations` | 4 |
| Agent Operations Manager | `agent-operations-manager` | 4 |
| Skill Builder Lead | `skill-builder-lead` | 2 |
| Skill Builder | `skill-builder` | 1 |
| Agent Trainer / Skill Optimizer | `agent-trainer-skill-optimizer` | 5 |
| Agent Configuration Manager | `agent-configuration-manager` | 7 |

**Customer Success** (6 agents, 21 skills):

| Agent | Dir | Skills |
|-------|-----|--------|
| Head of Customer Success | `head-of-customer-success` | 5 |
| CS Manager | `cs-manager` | 4 |
| Customer Success Manager (CSM) | `customer-success-manager` | 4 |
| UAT Coordinator (CS) | `uat-coordinator` | 1 |
| Customer Programs Manager | `customer-programs-manager` | 4 |
| Technical Account Manager (TAM) | `technical-account-manager` | 3 |

**Customer Support** (2 agents, 9 skills):

| Agent | Dir | Skills |
|-------|-----|--------|
| Support Manager | `support-manager` | 4 |
| Support Agent | `support-agent` | 5 |

**Technical Operations** (3 agents, 9 skills):

| Agent | Dir | Skills |
|-------|-----|--------|
| IT Operations Manager | `it-operations-manager` | 4 |
| IT Support Specialist | `it-support-specialist` | 1 |
| Vendor Management / Procurement | `vendor-management-procurement` | 4 |

**Revenue Operations** (1 agent, 6 skills):

| Agent | Dir | Skills |
|-------|-----|--------|
| Revenue Operations (RevOps) | `revenue-operations-manager` | 6 |

**Applied Research** (1 agent, 5 skills):

| Agent | Dir | Skills |
|-------|-----|--------|
| Applied Research Lead | `applied-research-lead` | 5 |

**Account Management** (2 agents, 5 skills):

| Agent | Dir | Skills |
|-------|-----|--------|
| Account Management Lead | `account-management-lead` | 3 |
| Account Manager | `account-manager` | 2 |

**Implementation** (2 agents, 4 skills):

| Agent | Dir | Skills |
|-------|-----|--------|
| Implementation Lead | `implementation-lead` | 2 |
| Implementation Engineer | `implementation-engineer` | 2 |

### Execution Sequence

1. **Research**: Web research on ops, CS, support, and specialized domains
2. **Ethos**: Write ethos profiles for all 8 departments
3. **Agent Operations**: VP → Ops Manager → Skill Builder Lead → Skill Builder → Trainer → Config Manager
4. **Customer Success**: Head of CS → CS Manager → CSM → UAT → Programs → TAM
5. **Customer Support**: Support Manager → Support Agent
6. **Smaller departments**: Tech Ops → RevOps → Applied Research → Account Management → Implementation
7. **Cross-references**: Complete all remaining cross-department links
8. **Validate**: Run validation across entire repo (all 472 skills)
9. **Final update**: status.md + org chart (mark 100% complete)

---

## Post-Phase: Finalization

After all 5 phases are complete:

1. **Full repo validation**: Run `scripts/validate.py` against all 472 skills
2. **Cross-reference audit**: Verify all `related-skills` paths resolve bidirectionally
3. **Handoff documentation**: Document at least 5 end-to-end workflows (SC-005)
4. **Skill index generation**: Generate the searchable catalog from frontmatter (FR-017)
5. **README update**: Write a comprehensive README for the enriched repo
6. **Final status.md update**: Mark all departments complete

---

## Context Lookup Chain

When an AI agent invokes a skill, context loads in this order:

1. **Always loaded**: Skill frontmatter (~100 words) — for trigger evaluation
2. **On trigger**: Skill body (500–1,500 words) + department ethos profile (500 words)
3. **On demand**: Skill-level `references/` → agent-level `references/` → department-level `references/` → `_shared/references/`

Most specific wins — if a resource exists at both skill and agent level, the skill-level version is used.

---

## Per-Phase Workflow

Every phase follows the same sequence:

```
1. WEB RESEARCH
   - Research best practices for each domain in the phase
   - Study how top practitioners in the field actually work
   - Identify frameworks, methodologies, and anti-patterns from real-world sources
   - Take time — depth of research directly determines quality of skills

2. ETHOS PROFILES
   - Write ideal-<dept>.md for each department in the phase
   - Max 500 words, opinionated, specific
   - Must pass the "would a hiring manager nod at this?" test

3. SKILL ENRICHMENT (per agent, per skill)
   - Create skill subdirectory: mkdir + git mv
   - Add YAML frontmatter with pushy description
   - Write all 9 sections following the template
   - Add supporting context (references/, examples/, scripts/, assets/) where valuable
   - Stay within word limits (500/1,000/1,500 by complexity)

4. CROSS-REFERENCES
   - Link related skills within the department
   - Link to skills in previously-enriched departments
   - Document handoff protocols where skills produce/consume artifacts

5. VALIDATION
   - Run scripts/validate.py on all skills in the phase
   - Fix any errors (frontmatter, word limits, broken references)

6. STATUS UPDATE
   - Update status.md with enrichment counts
   - Update org chart if paths changed
```
