# Tasks: Production-Grade Skill Depth

**Input**: Design documents from `/specs/003-production-grade-depth/`
**Prerequisites**: plan.md (required), spec.md (required), data-model.md, contracts/, research.md, quickstart.md

**Commit discipline**: Each skill (new or deepened) = 1 commit. Org chart/status updates = separate commits.

**Artifact guide**: Assessment skills → `references/scoring-rubric.md` + `assets/<name>-report-template.md`. Output skills → `assets/<output>-template.md` + at least one `references/` file. Workflow skills → at least one `references/` file (framework, checklist, or signal table). Follow contracts at `contracts/scoring-rubric-contract.md` and `contracts/output-template-contract.md`.

---

## Phase 1: Setup & Research

**Purpose**: Domain-cluster research and upgrade of existing 002 artifacts. Must complete before skill creation/deepening.

- [x] T001 Upgrade 10 existing scoring rubrics from 002 to 003 standard — add signal tables, complete grade bands (A+ through F), domain-specific frameworks. Skills: threat-modelling, go-live-approver, accessibility-auditor-design, and 7 others in `agents/*/references/scoring-rubric.md`. 1 commit per rubric.
- [x] T002 [P] Conduct domain-cluster research for Sales skill families (qualification, prospecting, outreach, execution, management). Produce research notes used by T004-T013 and T030-T036. No commit — working notes only.
- [x] T003 [P] Conduct domain-cluster research for Legal skill families (contract analysis, contract generation, compliance, legal risk). Produce research notes used by T014-T025 and T037-T040. No commit — working notes only.

**Checkpoint**: Research complete. 002 rubrics upgraded. New skill creation can begin.

---

## Phase 2: US2 — New Sales Skills (Priority: P2, but created first per FR-012)

**Goal**: Create 10 new Sales skills at production-grade depth from day one.

**Independent Test**: Each skill passes `python3 scripts/validate.py`, has scoring rubric or output template, and matches zubair's depth for equivalent capabilities.

### New Sales Skills

- [x] T004 [P] [US2] Create `agents/sales/sales-development-rep/prospect-analyst-orchestrator/` — SKILL.md (complex) + `references/scoring-rubric.md` (multi-agent prospect scoring) + `assets/prospect-report-template.md`. 1 commit.
- [x] T005 [P] [US2] Create `agents/sales/sales-development-rep/company-researcher/` — SKILL.md (medium) + `references/framework.md` (8-dimension firmographic analysis) + `assets/company-profile-template.md`. 1 commit.
- [x] T006 [P] [US2] Create `agents/sales/sales-development-rep/lead-qualifier/` — SKILL.md (complex) + `references/scoring-rubric.md` (BANT + MEDDIC scoring with signal tables) + `assets/qualification-report-template.md`. 1 commit.
- [x] T007 [P] [US2] Create `agents/sales/sales-development-rep/decision-maker-mapper/` — SKILL.md (medium) + `references/framework.md` (buying committee theory, org chart mapping) + `assets/stakeholder-map-template.md`. 1 commit.
- [x] T008 [P] [US2] Create `agents/sales/sales-development-rep/cold-outreach-builder/` — SKILL.md (complex) + `references/framework.md` (AIDA, PAS, BAB frameworks, cadence science) + `assets/outreach-sequence-template.md`. 1 commit.
- [x] T009 [P] [US2] Create `agents/sales/sales-development-rep/follow-up-sequence-builder/` — SKILL.md (medium) + `references/framework.md` (5 scenario types with cadence matrix) + `assets/follow-up-sequence-template.md`. 1 commit.
- [x] T010 [P] [US2] Create `agents/sales/account-executive/meeting-prep-builder/` — SKILL.md (medium) + `references/framework.md` (11-section brief structure) + `assets/meeting-brief-template.md`. 1 commit.
- [x] T011 [P] [US2] Create `agents/sales/account-executive/sales-proposal-builder/` — SKILL.md (complex) + `references/framework.md` (11-section proposal with ROI math) + `assets/sales-proposal-template.md`. 1 commit.
- [x] T012 [P] [US2] Create `agents/sales/sales-manager/icp-builder/` — SKILL.md (complex) + `references/scoring-rubric.md` (6-dimension ICP with 100-point scoring) + `assets/icp-profile-template.md`. 1 commit.
- [x] T013 [P] [US2] Create `agents/sales/sales-manager/sales-competitive-intel/` — SKILL.md (medium) + `references/framework.md` (battle card methodology, switching costs) + `assets/battle-card-template.md`. 1 commit.

---

## Phase 3: US2 — New Legal Skills (Priority: P2)

**Goal**: Create 12 new Legal skills at production-grade depth.

**Independent Test**: Each skill passes validation, includes domain-specific frameworks (GDPR, CCPA, SOC 2, etc.), and matches zubair's depth.

### New Legal Skills

- [x] T014 [P] [US2] Create `agents/legal/corporate-counsel/contract-review-orchestrator/` — SKILL.md (complex) + `references/scoring-rubric.md` (contract safety score, clause taxonomy) + `assets/contract-review-report-template.md`. 1 commit.
- [x] T015 [P] [US2] Create `agents/legal/corporate-counsel/contract-risk-analyst/` — SKILL.md (complex) + `references/scoring-rubric.md` (clause-by-clause risk scoring) + `references/risk-categories.md` + `assets/risk-analysis-report-template.md`. 1 commit.
- [x] T016 [P] [US2] Create `agents/legal/corporate-counsel/contract-comparator/` — SKILL.md (medium) + `references/framework.md` (side-by-side diff methodology, favorability analysis) + `assets/comparison-report-template.md`. 1 commit.
- [x] T017 [P] [US2] Create `agents/legal/corporate-counsel/plain-english-translator/` — SKILL.md (simple) + `references/framework.md` (readability scoring, 8th-grade target, legalese patterns) + `assets/plain-english-output-template.md`. 1 commit.
- [x] T018 [P] [US2] Create `agents/legal/corporate-counsel/negotiation-strategist/` — SKILL.md (complex) + `references/framework.md` (counter-proposal strategies, concession planning) + `assets/negotiation-strategy-template.md`. 1 commit.
- [x] T019 [P] [US2] Create `agents/legal/corporate-counsel/missing-protections-finder/` — SKILL.md (medium) + `references/checklist.md` (contract-type-specific protection checklists, universal protections) + `assets/protections-gap-report-template.md`. 1 commit.
- [x] T020 [P] [US2] Create `agents/legal/corporate-counsel/nda-generator/` — SKILL.md (medium) + `references/framework.md` (4 NDA variants, standard clauses) + `assets/nda-template.md` (with plain English annotations). 1 commit.
- [x] T021 [P] [US2] Create `agents/legal/product-counsel/terms-of-service-generator/` — SKILL.md (complex) + `references/checklist.md` (GDPR/CCPA compliance checklist) + `assets/terms-of-service-template.md`. 1 commit.
- [x] T022 [P] [US2] Create `agents/legal/product-counsel/privacy-policy-generator/` — SKILL.md (complex) + `references/checklist.md` (data collection detection, regulatory requirements) + `assets/privacy-policy-template.md`. 1 commit.
- [x] T023 [P] [US2] Create `agents/legal/corporate-counsel/business-agreement-generator/` — SKILL.md (complex) + `references/framework.md` (10 agreement types, 15-section structure) + `assets/business-agreement-template.md`. 1 commit.
- [x] T024 [P] [US2] Create `agents/legal/security-compliance-programme-manager/compliance-auditor/` — SKILL.md (complex) + `references/checklist.md` (57 checks across SOC 2, HIPAA, GDPR, CCPA, ISO 27001, PCI DSS, SOX) + `assets/compliance-audit-report-template.md`. 1 commit.
- [x] T025 [P] [US2] Create `agents/legal/corporate-counsel/freelancer-contract-reviewer/` — SKILL.md (medium) + `references/framework.md` (14 freelancer-specific analysis lenses, IRS 20-factor test) + `assets/freelancer-review-report-template.md`. 1 commit.

---

## Phase 4: US1 — Deepen Sales Department (Priority: P1)

**Goal**: Deepen all 17 existing Sales skills to production-grade quality.

**Independent Test**: Every Sales skill has at least one `references/` file. Assessment skills have scoring rubrics. Output skills have templates. Workflow steps are specific with named frameworks.

- [x] T026 [P] [US1] Deepen 3 skills for vp-sales: `sales-hiring-bar-raiser`, `pipeline-review-cadence-setter`, `territory-strategy-designer`. Add `references/` (framework or checklist per skill type). 1 commit per skill.
- [x] T027 [P] [US1] Deepen 4 skills for sales-manager: `forecast-submitter`, `deal-desk-coordinator`, `rep-coaching-session-runner`, `quota-territory-assigner`. Add `references/scoring-rubric.md` for forecast-submitter, `references/framework.md` for others. 1 commit per skill.
- [x] T028 [P] [US1] Deepen 3 skills for account-executive: `deal-qualifier`, `proposal-builder`, `contract-negotiator`. Add `references/scoring-rubric.md` for deal-qualifier, `assets/` templates for proposal-builder and contract-negotiator. 1 commit per skill.
- [x] T029 [P] [US1] Deepen 1 skill for sales-development-rep: `outbound-prospecting-executor`. Has refs/. 1 commit. *(assets still needed)*
- [x] T030 [P] [US1] Deepen 2 skills for business-development: `partner-activation-planner` (done), `partner-activation-executor` (refs only). Add `references/framework.md` per skill. 1 commit per skill.
- [x] T031 [P] [US1] Deepen 2 skills for solutions-engineering-manager: `solutions-playbook-builder` (done), `technical-buyer-signal-extractor` (assets only). 1 commit per skill.
- [x] T032 [P] [US1] Deepen 2 skills for solutions-engineer: `proof-of-concept-runner` (done), `technical-feasibility-for-sales` (done). 1 commit per skill.

---

## Phase 5: US1 — Deepen Legal Department (Priority: P1)

**Goal**: Deepen all 24 existing Legal skills to production-grade quality.

**Independent Test**: Every Legal skill has domain-specific references with regulatory framework details. Assessment skills have rubrics with legal-specific signal tables.

- [x] T033 [P] [US1] Deepen skills for general-counsel: `entity-type-decision` (done), `ip-assignment` (refs only), `legal-idea-reviewer` (done), `stock-plan-setup` (done). 1 commit per skill. *(ip-assignment needs assets)*
- [x] T034 [P] [US1] Deepen skills for corporate-counsel: all 17 skills have refs/; most have assets/. Stragglers: `83b-election-coordinator` (refs only), `entity-formation` (refs only). 1 commit per skill. *(2 need assets)*
- [x] T035 [P] [US1] Deepen skills for product-counsel: all 16 skills have refs/; most have assets/. Straggler: `prd-nfr-compliance` (refs only). 1 commit per skill. *(1 needs assets)*
- [ ] T036 [P] [US1] Deepen skills for security-compliance-programme-manager: `compliance-auditor` (done), `disaster-recovery-drill-runner` (done), `policy-document-owner` (done), `risk-register-maintainer` (done), `vendor-security-assessor` (done). **Still need assets**: `audit-programme-manager`, `compliance-framework-implementer`, `gdpr-ccpa-compliance-manager`, `penetration-test-programme-manager`, `security-awareness-training-runner`, `soc2-programme-manager`. 1 commit per skill.

---

## Phase 6: US2 + US1 — Marketing Department

**Goal**: Create 7 new Marketing skills and deepen all 54 existing Marketing skills.

**Independent Test**: New skills match zubair's marketing depth. Existing skills have domain-specific references with marketing frameworks.

### Phase 6a: Research

- [x] T037 Conduct domain-cluster research for Marketing skill families — complete (embedded in research.md).

### Phase 6b: New Marketing Skills (US2)

- [x] T038 [P] [US2] Create `agents/marketing/vp-marketing/marketing-audit-orchestrator/` — done (refs + assets). 1 commit.
- [x] T039 [P] [US2] Create `agents/marketing/content-marketer/copywriting-analyst/` — done (refs + assets). 1 commit.
- [x] T040 [P] [US2] Create `agents/marketing/demand-gen-manager/ad-campaign-builder/` — done (refs + assets). 1 commit.
- [ ] T041 [P] [US2] Create `agents/marketing/demand-gen-manager/funnel-optimizer/` — not yet created.
- [ ] T042 [P] [US2] Create `agents/marketing/demand-gen-manager/landing-page-auditor/` — not yet created.
- [ ] T043 [P] [US2] Create `agents/marketing/marketing-operations-manager/seo-auditor/` — not yet created.
- [ ] T044 [P] [US2] Create `agents/design/brand-designer/brand-voice-analyst/` — not yet created.

### Phase 6c: Deepen Existing Marketing Skills (US1)

- [ ] T045 [P] [US1] Deepen vp-marketing: `demand-gen-planner` (none), `gtm-activation-marketing` (none), `gtm-planner-marketing` (none). 1 commit per skill.
- [ ] T046 [P] [US1] Deepen demand-gen-manager: `content-engine-builder-marketing` (none), `roadmap-timing-input` (none), `channel-signal-analyst` (refs only). 1 commit per skill.
- [ ] T047 [P] [US1] Deepen content-marketer: `content-marketing-operations` (none). 1 commit.
- [ ] T048 [P] [US1] Deepen pr-communications-manager: `crisis-communications-planner` (none), `media-relationship-builder` (refs only), `press-release-writer` (none), `thought-leadership-programme-runner` (refs only). earned-media-monitor has refs. 1 commit per skill.
- [ ] T049 [P] [US1] Deepen marketing-operations-manager: `email-deliverability-manager` (none), `lead-scoring-model-builder` (none), `marketing-attribution-modeller` (none), `martech-stack-manager` (none). campaign-analytics-reporter has refs. 1 commit per skill.
- [ ] T050 [P] [US1] Deepen social-media-manager: `influencer-coordination-manager` (refs only), `social-content-calendar-manager` (none), `social-listening-analyst` (none), `ugc-programme-designer` (refs only). 1 commit per skill.
- [x] T051 [P] [US1] Deepen lifecycle-email-marketing-manager: onboarding-sequence-designer (done), nurture-campaign-builder (done), retention-email-designer (done), transactional-email-designer (done). email-performance-optimiser has refs only.
- [ ] T052 [P] [US1] Deepen event-marketing-manager: `company-offsite-producer` (none), `conference-presence-manager` (none), `sales-kickoff-producer` (none), `user-conference-producer` (none), `webinar-and-virtual-event-manager` (none). event-calendar-planner has refs. 1 commit per skill.
- [ ] T053 [P] [US1] Deepen analyst-relations-manager: `analyst-inquiry-responder` (none), `analyst-report-monitor` (none), `magic-quadrant-strategy` (none), `peer-review-platform-manager` (none). analyst-briefing-scheduler has refs. 1 commit per skill.
- [ ] T054 [P] [US1] Deepen community-manager: all 5 skills have examples+scripts but NO refs/. Add refs + assets per skill. 1 commit per skill.
- [ ] T055 [P] [US1] Deepen developer-relations-lead: `api-developer-experience-reviewer` (refs in progress), `developer-community-grower` (none), `developer-community-signal-extractor` (none), `developer-experience-reviewer` (none), `developer-feedback-synthesiser` (none), `developer-gtm-planner` (none), `developer-launch-packager` (none). 1 commit per skill.
- [ ] T056 [P] [US1] Deepen technical-writer: all 5 skills have no refs/. 1 commit per skill.

---

## Phase 7: US1 — Deepen Product Department

**Goal**: Deepen all 82 existing Product skills.

**Independent Test**: All Product skills have references/. Assessment skills (20) have scoring rubrics. Output skills (22) have templates. RICE, MoSCoW, Kano, and other product frameworks embedded.

### Phase 7a: Research

- [ ] T057 Conduct domain-cluster research for Product skill families (strategy, execution, analytics, operations, product marketing, content). Produce research notes.

### Phase 7b: Deepen Product Skills (US1)

- [ ] T058 [P] [US1] Deepen 9 skills for vp-product (batch 1 of 2): `product-vision-setter`, `roadmap-owner`, `stakeholder-alignment-driver`, `product-council-chair`, `product-ops-sponsor`, `gtm-strategy-co-owner`, `pricing-strategist`, `platform-vs-feature-arbitrator`, `technical-debt-prioritiser`. 1 commit per skill.
- [ ] T059 [P] [US1] Deepen 9 skills for vp-product (batch 2 of 2): `product-analytics-reviewer`, `competitive-landscape-monitor`, `product-culture-evangelist`, `board-product-update-author`, `beta-programme-sponsor`, `partnership-product-evaluator`, `customer-advisory-board-liaison`, `regulatory-product-navigator`, `ai-product-ethics-reviewer`. 1 commit per skill.
- [ ] T060 [P] [US1] Deepen 10 skills for product-manager (batch 1 of 3): `backlog-groomer`, `prd-author`, `user-story-writer`, `acceptance-criteria-definer`, `sprint-planning-facilitator`, `release-note-drafter`, `analytics-interpreter`, `experiment-designer`, `customer-feedback-synthesiser`, `stakeholder-demo-presenter`. 1 commit per skill.
- [ ] T061 [P] [US1] Deepen 10 skills for product-manager (batch 2 of 3): `bug-triage-lead`, `onboarding-flow-designer`, `documentation-reviewer`, `beta-programme-coordinator`, `competitive-feature-analyst`, `product-spec-reviewer`, `go-live-approver`, `localisation-coordinator`, `pricing-experiment-runner`, `accessibility-champion`. 1 commit per skill.
- [ ] T062 [P] [US1] Deepen 10 skills for product-manager (batch 3 of 3): `technical-requirements-translator`, `dogfooding-programme-runner`, `data-privacy-requirements-author`, `dependency-tracker`, `product-area-on-call`, `cross-team-dependency-negotiator`, `customer-escalation-handler`, `feature-deprecation-manager`, `internal-tool-product-owner`, `product-debt-register-maintainer`. 1 commit per skill.
- [ ] T063 [P] [US1] Deepen 12 skills for product-operations-analyst. 1 commit per skill.
- [ ] T064 [P] [US1] Deepen 8 skills for pmm-product-marketing-manager (batch 1 of 2): `messaging-framework-builder`, `launch-plan-owner`, `sales-enablement-content-creator`, `win-loss-analyst`, `competitive-battle-card-author`, `market-segmentation-analyst`, `demo-script-writer`, `customer-reference-programme-manager`. 1 commit per skill.
- [ ] T065 [P] [US1] Deepen 8 skills for pmm-product-marketing-manager (batch 2 of 2): `content-calendar-strategist`, `feature-adoption-campaign-designer`, `analyst-briefing-contributor`, `pricing-page-optimiser`, `partner-co-marketing-coordinator`, `product-webinar-host`, `competitive-intelligence-subscriber`, `market-sizing-researcher`. 1 commit per skill.
- [ ] T066 [P] [US1] Deepen 6 skills for pmm-analyst-content-strategist. 1 commit per skill.

---

## Phase 8: US1 — Deepen Engineering Department

**Goal**: Deepen all 100 existing Engineering skills.

**Independent Test**: All Engineering skills have references/. Security skills have OWASP/STRIDE/DREAD frameworks. DevOps skills have DORA metrics and deployment strategies. QA skills have test pyramid references.

### Phase 8a: Research

- [ ] T067 Conduct domain-cluster research for Engineering skill families (architecture, code quality, backend, frontend, DevOps, security, data/ML, QA). Produce research notes.

### Phase 8b: Deepen Engineering Skills (US1)

- [ ] T068 [P] [US1] Deepen 12 skills for vp-engineering. 1 commit per skill.
- [ ] T069 [P] [US1] Deepen 9 skills for tech-architect. 1 commit per skill.
- [ ] T070 [P] [US1] Deepen 12 skills for tech-lead-pr-reviewer. 1 commit per skill.
- [ ] T071 [P] [US1] Deepen 1 skill for database-expert: `query-optimiser`. 1 commit.
- [ ] T072 [P] [US1] Deepen 5 skills for sr-frontend-developer. 1 commit per skill.
- [ ] T073 [P] [US1] Deepen 5 skills for sr-backend-developer. 1 commit per skill.
- [ ] T074 [P] [US1] Deepen 8 skills for qa-test-engineer. 1 commit per skill.
- [ ] T075 [P] [US1] Deepen 10 skills for devops-infrastructure-engineer (batch 1 of 2). 1 commit per skill.
- [ ] T076 [P] [US1] Deepen 9 skills for devops-infrastructure-engineer (batch 2 of 2). 1 commit per skill.
- [ ] T077 [P] [US1] Deepen 5 skills for platform-engineer. 1 commit per skill.
- [ ] T078 [P] [US1] Deepen 7 skills for data-engineer. 1 commit per skill.
- [ ] T079 [P] [US1] Deepen 10 skills for security-engineer. 1 commit per skill.
- [ ] T080 [P] [US1] Deepen 7 skills for ai-ml-engineer. 1 commit per skill.

---

## Phase 9: US1 — Deepen Remaining Departments

**Goal**: Deepen all remaining skills across Design (42), Data & Growth (39), Finance (32), Agent Ops (27), Customer Success (21), Customer Support (9), Tech Ops (9), RevOps (6), Applied Research (5), Account Mgmt (5), Implementation (4).

### Phase 9a: Research

- [ ] T081 Conduct domain-cluster research for remaining departments (design craft, UX research, financial planning, customer success, agent operations, support, tech ops). Produce research notes.

### Phase 9b: Design (42 skills)

- [ ] T082 [P] [US1] Deepen 8 skills for head-of-design. 1 commit per skill.
- [ ] T083 [P] [US1] Deepen 8 skills for ux-ui-designer. 1 commit per skill.
- [ ] T084 [P] [US1] Deepen 2 skills for visual-interaction-designer. 1 commit per skill.
- [ ] T085 [P] [US1] Deepen 5 skills for brand-designer. 1 commit per skill.
- [ ] T086 [P] [US1] Deepen 6 skills for ux-research-lead. 1 commit per skill.
- [ ] T087 [P] [US1] Deepen 4 skills for ux-researcher. 1 commit per skill.
- [ ] T088 [P] [US1] Deepen 5 skills for content-design-lead. 1 commit per skill.
- [ ] T089 [P] [US1] Deepen 4 skills for content-designer-ux-writer. 1 commit per skill.

### Phase 9c: Data & Growth (39 skills)

- [ ] T090 [P] [US1] Deepen 10 skills for analytics-lead. 1 commit per skill.
- [ ] T091 [P] [US1] Deepen 10 skills for data-analyst. 1 commit per skill.
- [ ] T092 [P] [US1] Deepen 10 skills for growth-lead. 1 commit per skill.
- [ ] T093 [P] [US1] Deepen 9 skills for growth-engineer. 1 commit per skill.

### Phase 9d: Finance (32 skills)

- [ ] T094 [P] [US1] Deepen 4 skills for cfo-vp-finance. 1 commit per skill.
- [ ] T095 [P] [US1] Deepen 4 skills for finance-manager. 1 commit per skill.
- [ ] T096 [P] [US1] Deepen 8 skills for fpa-analyst. 1 commit per skill.
- [ ] T097 [P] [US1] Deepen 7 skills for controller-accounting. 1 commit per skill.
- [ ] T098 [P] [US1] Deepen 9 skills for investor-relations-manager. 1 commit per skill.

### Phase 9e: Agent Operations (27 skills)

- [ ] T099 [P] [US1] Deepen 4 skills for vp-agent-operations. 1 commit per skill.
- [ ] T100 [P] [US1] Deepen 5 skills for agent-operations-manager (including tool-health-checker from 002). 1 commit per skill.
- [ ] T101 [P] [US1] Deepen 2 skills for skill-builder-lead. 1 commit per skill.
- [ ] T102 [P] [US1] Deepen 2 skills for skill-builder (including mcp-server-builder from 002). 1 commit per skill.
- [ ] T103 [P] [US1] Deepen 5 skills for agent-trainer-skill-optimizer. 1 commit per skill.
- [ ] T104 [P] [US1] Deepen 9 skills for agent-configuration-manager (including company-tooling-onboarder and tool-policy-manager from 002). 1 commit per skill.

### Phase 9f: Customer Success (21 skills)

- [ ] T105 [P] [US1] Deepen 5 skills for head-of-customer-success. 1 commit per skill.
- [ ] T106 [P] [US1] Deepen 4 skills for cs-manager. 1 commit per skill.
- [ ] T107 [P] [US1] Deepen 4 skills for customer-success-manager. 1 commit per skill.
- [ ] T108 [P] [US1] Deepen 1 skill for uat-coordinator-cs. 1 commit.
- [ ] T109 [P] [US1] Deepen 4 skills for customer-programs-manager. 1 commit per skill.
- [ ] T110 [P] [US1] Deepen 3 skills for technical-account-manager. 1 commit per skill.

### Phase 9g: Small Departments

- [ ] T111 [P] [US1] Deepen 9 skills for Customer Support (support-manager: 4, support-agent: 5). 1 commit per skill.
- [ ] T112 [P] [US1] Deepen 9 skills for Technical Operations (it-operations-manager: 4, it-support-specialist: 1, vendor-management-procurement: 4). 1 commit per skill.
- [ ] T113 [P] [US1] Deepen 6 skills for Revenue Operations (revenue-operations-manager: 6). 1 commit per skill.
- [ ] T114 [P] [US1] Deepen 5 skills for Applied Research (applied-research-lead: 5). 1 commit per skill.
- [ ] T115 [P] [US1] Deepen 5 skills for Account Management (account-management-lead: 3, account-manager: 2). 1 commit per skill.
- [ ] T116 [P] [US1] Deepen 4 skills for Implementation (implementation-lead: 2, implementation-engineer: 2). 1 commit per skill.

---

## Phase 10: Polish & Cross-Cutting Concerns

**Purpose**: Org chart updates, status tracking, validation, final quality check.

- [ ] T117 Update `AGENTS.md` — add all 29 new skills to their respective agent skill lists, update total skill count to 528. 1 commit.
- [ ] T118 Update `status.md` — reflect 528 total skills, production-grade depth status per department. 1 commit.
- [ ] T119 Run full repo validation: `python3 scripts/validate.py` — confirm 0 errors across all 528 skills. Fix any errors. 1 commit per fix.
- [ ] T120 Spot-check 10 skills (2 per key department: Sales, Legal, Marketing, Product, Engineering) against zubair equivalents. Document comparison results. Confirm SC-003 (match or exceed on depth). 1 commit.
- [ ] T121 Update `CLAUDE.md` — add depth artifact guidance, reference/asset conventions. 1 commit.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: No dependencies — start immediately
- **Phases 2-3 (Sales+Legal new skills)**: Depend on Phase 1 research (T002, T003)
- **Phases 4-5 (Sales+Legal deepening)**: Depend on Phases 2-3 (new skills set the depth standard)
- **Phase 6 (Marketing)**: Depends on Phase 1 completion. Independent of Sales/Legal phases.
- **Phase 7 (Product)**: Depends on Phase 1 completion. Independent of other department phases.
- **Phase 8 (Engineering)**: Depends on Phase 1 completion. Independent of other department phases.
- **Phase 9 (Remaining)**: Depends on Phase 1 completion. Independent of other department phases.
- **Phase 10 (Polish)**: Depends on ALL previous phases

### Within Each Phase

- Research tasks complete before skill creation/deepening
- New skills (US2) complete before deepening existing skills (US1) in same department
- All [P] tasks within a phase can run in parallel
- Each skill is a separate commit regardless of task grouping

### Parallel Opportunities

- T002 + T003 (Sales and Legal research) can run in parallel
- T004-T013 (all 10 new Sales skills) can run in parallel
- T014-T025 (all 12 new Legal skills) can run in parallel
- T026-T032 (all Sales deepening) can run in parallel
- T033-T036 (all Legal deepening) can run in parallel
- Phases 6, 7, 8, 9 can all run in parallel (different departments, no file conflicts)
- Within any deepening phase, all agent-level tasks can run in parallel

---

## Parallel Example: Phase 2 (New Sales Skills)

```bash
# All 10 new Sales skills can be created in parallel:
Agent 1: "Create prospect-analyst-orchestrator at agents/sales/sales-development-rep/prospect-analyst-orchestrator/"
Agent 2: "Create company-researcher at agents/sales/sales-development-rep/company-researcher/"
Agent 3: "Create lead-qualifier at agents/sales/sales-development-rep/lead-qualifier/"
Agent 4: "Create decision-maker-mapper at agents/sales/sales-development-rep/decision-maker-mapper/"
Agent 5: "Create cold-outreach-builder at agents/sales/sales-development-rep/cold-outreach-builder/"
# ... (all 10 in parallel, different directories)
```

## Parallel Example: Phase 8 (Engineering Deepening)

```bash
# All 13 agent-level tasks can run in parallel:
Agent 1: "Deepen 12 vp-engineering skills"
Agent 2: "Deepen 9 tech-architect skills"
Agent 3: "Deepen 12 tech-lead-pr-reviewer skills"
Agent 4: "Deepen 5 sr-frontend-developer skills"
# ... (all 13 agents in parallel, different directories)
```

---

## Implementation Strategy

### MVP First (Sales + Legal)

1. Phase 1: Setup & research
2. Phases 2-3: Create 22 new Sales + Legal skills
3. Phases 4-5: Deepen 41 existing Sales + Legal skills
4. **STOP and VALIDATE**: Run validation, spot-check against zubair

### Incremental Delivery

1. Phases 1-5 → Sales + Legal complete (63 skills at production-grade depth)
2. Phase 6 → Marketing complete (61 skills)
3. Phase 7 → Product complete (82 skills)
4. Phase 8 → Engineering complete (100 skills)
5. Phase 9 → All remaining departments (222 skills)
6. Phase 10 → Polish, validate, compare

### Parallel Team Strategy

With sufficient context capacity:
- After Phase 1, run Phases 2+3 in parallel (Sales and Legal new skills)
- After Phases 2+3, run Phases 4+5+6+7+8+9 in parallel (all departments deepen simultaneously)
- Phase 10 after all complete

---

## Task Count

| Phase | Tasks | Skills Covered | Description |
|-------|-------|---------------|-------------|
| 1 | 3 | 10 (upgrades) | Setup & research |
| 2 | 10 | 10 (new) | New Sales skills |
| 3 | 12 | 12 (new) | New Legal skills |
| 4 | 7 | 17 (deepen) | Deepen Sales |
| 5 | 4 | 24 (deepen) | Deepen Legal |
| 6 | 20 | 61 (7 new + 54 deepen) | Marketing |
| 7 | 10 | 82 (deepen) | Product |
| 8 | 14 | 100 (deepen) | Engineering |
| 9 | 36 | 222 (deepen) | Remaining departments |
| 10 | 5 | — | Polish & validate |
| **Total** | **121** | **528** | |

Estimated commits: 528 skill commits + ~10 org chart/status/CLAUDE.md commits = ~538 total.
