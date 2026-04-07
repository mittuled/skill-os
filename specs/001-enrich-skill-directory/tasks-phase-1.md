# Tasks — Phase 1: Product (82 skills, 5 agents)

**Input**: Design documents from `/specs/001-enrich-skill-directory/`
**Prerequisites**: Phase 0 complete (ETHOS.md, departments/, _shared/, validate.py)

**Goal**: Fully enrich the Product department as the reference implementation. Gold standard for all subsequent phases.

**Commit discipline**: Every skill = 1 commit. Format: `Enrich skill: <skill-slug> for <Agent Role>`

---

## Phase 1.0: Research & Ethos

- [ ] T024 Research product management best practices — PM frameworks (RICE, MoSCoW, JTBD, Opportunity Solution Trees), how top PMs at Stripe/Linear/Notion operate, sprint planning, backlog management, stakeholder communication patterns, roadmapping approaches, experiment design, feature flagging strategies. Save as working context.
- [ ] T025 Research product marketing frameworks — April Dunford positioning, messaging hierarchies, competitive intelligence (Klue/Crayon patterns), launch planning playbooks, sales enablement content, win/loss analysis, market segmentation, pricing communication.
- [ ] T026 Research product operations — process auditing, OKR tracking tools and frameworks, knowledge base curation, workflow automation, metrics dashboards, product data pipelines.
- [ ] T027 Write `departments/product/ideal-product.md` — ethos profile (max 500 words). Use ethos template from `contracts/ethos-template.md`. Must be opinionated: what does an ideal product practitioner care about? 1 commit.

---

## Phase 1.1: VP Product (18 skills)

Agent: VP Product (`vp-product`) — L3 executive setting product vision, strategy, and org-wide product culture.

- [ ] T028 Enrich `product-vision-setter` — migrate `agents/vp-product/product-vision-setter.md` → `agents/vp-product/product-vision-setter/SKILL.md`, write 9-section enriched format with YAML frontmatter (complexity: complex). 1 commit.
- [ ] T029 Enrich `roadmap-owner` — migrate + enrich at `agents/vp-product/roadmap-owner/SKILL.md` (complexity: complex). 1 commit.
- [ ] T030 Enrich `stakeholder-alignment-driver` — migrate + enrich at `agents/vp-product/stakeholder-alignment-driver/SKILL.md` (complexity: complex). 1 commit.
- [ ] T031 Enrich `product-council-chair` — migrate + enrich at `agents/vp-product/product-council-chair/SKILL.md` (complexity: medium). 1 commit.
- [ ] T032 Enrich `product-ops-sponsor` — migrate + enrich at `agents/vp-product/product-ops-sponsor/SKILL.md` (complexity: medium). 1 commit.
- [ ] T033 Enrich `gtm-strategy-co-owner` — migrate + enrich at `agents/vp-product/gtm-strategy-co-owner/SKILL.md` (complexity: complex). 1 commit.
- [ ] T034 Enrich `pricing-strategist` — migrate + enrich at `agents/vp-product/pricing-strategist/SKILL.md` (complexity: complex). 1 commit.
- [ ] T035 Enrich `platform-vs-feature-arbitrator` — migrate + enrich at `agents/vp-product/platform-vs-feature-arbitrator/SKILL.md` (complexity: complex). 1 commit.
- [ ] T036 Enrich `technical-debt-prioritiser` — migrate + enrich at `agents/vp-product/technical-debt-prioritiser/SKILL.md` (complexity: medium). 1 commit.
- [ ] T037 Enrich `product-analytics-reviewer` — migrate + enrich at `agents/vp-product/product-analytics-reviewer/SKILL.md` (complexity: medium). 1 commit.
- [ ] T038 Enrich `competitive-landscape-monitor` — migrate + enrich at `agents/vp-product/competitive-landscape-monitor/SKILL.md` (complexity: medium). 1 commit.
- [ ] T039 Enrich `product-culture-evangelist` — migrate + enrich at `agents/vp-product/product-culture-evangelist/SKILL.md` (complexity: medium). 1 commit.
- [ ] T040 Enrich `board-product-update-author` — migrate + enrich at `agents/vp-product/board-product-update-author/SKILL.md` (complexity: simple). 1 commit.
- [ ] T041 Enrich `beta-programme-sponsor` — migrate + enrich at `agents/vp-product/beta-programme-sponsor/SKILL.md` (complexity: medium). 1 commit.
- [ ] T042 Enrich `partnership-product-evaluator` — migrate + enrich at `agents/vp-product/partnership-product-evaluator/SKILL.md` (complexity: complex). 1 commit.
- [ ] T043 Enrich `customer-advisory-board-liaison` — migrate + enrich at `agents/vp-product/customer-advisory-board-liaison/SKILL.md` (complexity: medium). 1 commit.
- [ ] T044 Enrich `regulatory-product-navigator` — migrate + enrich at `agents/vp-product/regulatory-product-navigator/SKILL.md` (complexity: complex). 1 commit.
- [ ] T045 Enrich `ai-product-ethics-reviewer` — migrate + enrich at `agents/vp-product/ai-product-ethics-reviewer/SKILL.md` (complexity: complex). 1 commit.

---

## Phase 1.2: Product Manager (30 skills)

Agent: Product Manager (`product-manager`) — L2 IC owning backlog, sprints, user stories, and cross-team execution.

- [ ] T046 Enrich `backlog-groomer` — migrate + enrich at `agents/product-manager/backlog-groomer/SKILL.md` (complexity: medium). 1 commit.
- [ ] T047 Enrich `sprint-planner` — migrate + enrich at `agents/product-manager/sprint-planner/SKILL.md` (complexity: medium). 1 commit.
- [ ] T048 Enrich `user-story-writer` — migrate + enrich at `agents/product-manager/user-story-writer/SKILL.md` (complexity: medium). 1 commit.
- [ ] T049 Enrich `acceptance-criteria-definer` — migrate + enrich at `agents/product-manager/acceptance-criteria-definer/SKILL.md` (complexity: medium). 1 commit.
- [ ] T050 Enrich `stakeholder-communicator` — migrate + enrich at `agents/product-manager/stakeholder-communicator/SKILL.md` (complexity: medium). 1 commit.
- [ ] T051 Enrich `release-note-drafter` — migrate + enrich at `agents/product-manager/release-note-drafter/SKILL.md` (complexity: simple). 1 commit.
- [ ] T052 Enrich `roadmap-contributor` — migrate + enrich at `agents/product-manager/roadmap-contributor/SKILL.md` (complexity: medium). 1 commit.
- [ ] T053 Enrich `customer-feedback-synthesiser` — migrate + enrich at `agents/product-manager/customer-feedback-synthesiser/SKILL.md` (complexity: medium). 1 commit.
- [ ] T054 Enrich `competitive-intel-gatherer` — migrate + enrich at `agents/product-manager/competitive-intel-gatherer/SKILL.md` (complexity: medium). 1 commit.
- [ ] T055 Enrich `analytics-interpreter` — migrate + enrich at `agents/product-manager/analytics-interpreter/SKILL.md` (complexity: medium). 1 commit.
- [ ] T056 Enrich `experiment-designer` — migrate + enrich at `agents/product-manager/experiment-designer/SKILL.md` (complexity: complex). 1 commit.
- [ ] T057 Enrich `feature-flag-manager` — migrate + enrich at `agents/product-manager/feature-flag-manager/SKILL.md` (complexity: simple). 1 commit.
- [ ] T058 Enrich `cross-team-dependency-tracker` — migrate + enrich at `agents/product-manager/cross-team-dependency-tracker/SKILL.md` (complexity: medium). 1 commit.
- [ ] T059 Enrich `prd-author` — migrate + enrich at `agents/product-manager/prd-author/SKILL.md` (complexity: complex). 1 commit.
- [ ] T060 Enrich `technical-spec-reviewer` — migrate + enrich at `agents/product-manager/technical-spec-reviewer/SKILL.md` (complexity: medium). 1 commit.
- [ ] T061 Enrich `ux-review-participant` — migrate + enrich at `agents/product-manager/ux-review-participant/SKILL.md` (complexity: simple). 1 commit.
- [ ] T062 Enrich `bug-triage-lead` — migrate + enrich at `agents/product-manager/bug-triage-lead/SKILL.md` (complexity: medium). 1 commit.
- [ ] T063 Enrich `post-mortem-contributor` — migrate + enrich at `agents/product-manager/post-mortem-contributor/SKILL.md` (complexity: medium). 1 commit.
- [ ] T064 Enrich `onboarding-flow-designer` — migrate + enrich at `agents/product-manager/onboarding-flow-designer/SKILL.md` (complexity: complex). 1 commit.
- [ ] T065 Enrich `pricing-tier-mapper` — migrate + enrich at `agents/product-manager/pricing-tier-mapper/SKILL.md` (complexity: medium). 1 commit.
- [ ] T066 Enrich `api-consumer-advocate` — migrate + enrich at `agents/product-manager/api-consumer-advocate/SKILL.md` (complexity: medium). 1 commit.
- [ ] T067 Enrich `localisation-coordinator` — migrate + enrich at `agents/product-manager/localisation-coordinator/SKILL.md` (complexity: simple). 1 commit.
- [ ] T068 Enrich `accessibility-champion` — migrate + enrich at `agents/product-manager/accessibility-champion/SKILL.md` (complexity: medium). 1 commit.
- [ ] T069 Enrich `data-privacy-requirement-writer` — migrate + enrich at `agents/product-manager/data-privacy-requirement-writer/SKILL.md` (complexity: medium). 1 commit.
- [ ] T070 Enrich `partner-integration-specifier` — migrate + enrich at `agents/product-manager/partner-integration-specifier/SKILL.md` (complexity: medium). 1 commit.
- [ ] T071 Enrich `sla-definer` — migrate + enrich at `agents/product-manager/sla-definer/SKILL.md` (complexity: medium). 1 commit.
- [ ] T072 Enrich `capacity-planner` — migrate + enrich at `agents/product-manager/capacity-planner/SKILL.md` (complexity: medium). 1 commit.
- [ ] T073 Enrich `documentation-reviewer` — migrate + enrich at `agents/product-manager/documentation-reviewer/SKILL.md` (complexity: simple). 1 commit.
- [ ] T074 Enrich `incident-communication-drafter` — migrate + enrich at `agents/product-manager/incident-communication-drafter/SKILL.md` (complexity: simple). 1 commit.
- [ ] T075 Enrich `dogfooding-coordinator` — migrate + enrich at `agents/product-manager/dogfooding-coordinator/SKILL.md` (complexity: simple). 1 commit.

---

## Phase 1.3: Product Operations Analyst (12 skills)

Agent: Product Operations Analyst (`product-operations-analyst`) — L2 IC maintaining product processes, tooling, and data pipelines.

- [ ] T076 Enrich `process-auditor` — migrate + enrich at `agents/product-operations-analyst/process-auditor/SKILL.md` (complexity: medium). 1 commit.
- [ ] T077 Enrich `tool-administrator` — migrate + enrich at `agents/product-operations-analyst/tool-administrator/SKILL.md` (complexity: simple). 1 commit.
- [ ] T078 Enrich `product-data-pipeline-maintainer` — migrate + enrich at `agents/product-operations-analyst/product-data-pipeline-maintainer/SKILL.md` (complexity: medium). 1 commit.
- [ ] T079 Enrich `okr-tracker` — migrate + enrich at `agents/product-operations-analyst/okr-tracker/SKILL.md` (complexity: medium). 1 commit.
- [ ] T080 Enrich `launch-checklist-enforcer` — migrate + enrich at `agents/product-operations-analyst/launch-checklist-enforcer/SKILL.md` (complexity: medium). 1 commit.
- [ ] T081 Enrich `cross-team-ritual-facilitator` — migrate + enrich at `agents/product-operations-analyst/cross-team-ritual-facilitator/SKILL.md` (complexity: medium). 1 commit.
- [ ] T082 Enrich `product-knowledge-base-curator` — migrate + enrich at `agents/product-operations-analyst/product-knowledge-base-curator/SKILL.md` (complexity: simple). 1 commit.
- [ ] T083 Enrich `workflow-automation-builder` — migrate + enrich at `agents/product-operations-analyst/workflow-automation-builder/SKILL.md` (complexity: medium). 1 commit.
- [ ] T084 Enrich `product-metrics-dashboard-owner` — migrate + enrich at `agents/product-operations-analyst/product-metrics-dashboard-owner/SKILL.md` (complexity: medium). 1 commit.
- [ ] T085 Enrich `vendor-evaluation-supporter` — migrate + enrich at `agents/product-operations-analyst/vendor-evaluation-supporter/SKILL.md` (complexity: simple). 1 commit.
- [ ] T086 Enrich `template-standardiser` — migrate + enrich at `agents/product-operations-analyst/template-standardiser/SKILL.md` (complexity: simple). 1 commit.
- [ ] T087 Enrich `onboarding-buddy-for-new-pms` — migrate + enrich at `agents/product-operations-analyst/onboarding-buddy-for-new-pms/SKILL.md` (complexity: simple). 1 commit.

---

## Phase 1.4: PMM — Product Marketing Manager (16 skills)

Agent: PMM — Product Marketing Manager (`pmm-product-marketing-manager`) — L2 IC owning positioning, messaging, launches, and competitive intelligence.

- [ ] T088 Enrich `positioning-architect` — migrate + enrich at `agents/pmm-product-marketing-manager/positioning-architect/SKILL.md` (complexity: complex). 1 commit.
- [ ] T089 Enrich `messaging-framework-builder` — migrate + enrich at `agents/pmm-product-marketing-manager/messaging-framework-builder/SKILL.md` (complexity: complex). 1 commit.
- [ ] T090 Enrich `launch-plan-owner` — migrate + enrich at `agents/pmm-product-marketing-manager/launch-plan-owner/SKILL.md` (complexity: complex). 1 commit.
- [ ] T091 Enrich `competitive-battle-card-author` — migrate + enrich at `agents/pmm-product-marketing-manager/competitive-battle-card-author/SKILL.md` (complexity: medium). 1 commit.
- [ ] T092 Enrich `sales-enablement-content-creator` — migrate + enrich at `agents/pmm-product-marketing-manager/sales-enablement-content-creator/SKILL.md` (complexity: medium). 1 commit.
- [ ] T093 Enrich `analyst-briefing-preparer` — migrate + enrich at `agents/pmm-product-marketing-manager/analyst-briefing-preparer/SKILL.md` (complexity: medium). 1 commit.
- [ ] T094 Enrich `customer-story-producer` — migrate + enrich at `agents/pmm-product-marketing-manager/customer-story-producer/SKILL.md` (complexity: medium). 1 commit.
- [ ] T095 Enrich `product-naming-advisor` — migrate + enrich at `agents/pmm-product-marketing-manager/product-naming-advisor/SKILL.md` (complexity: medium). 1 commit.
- [ ] T096 Enrich `market-segmentation-analyst` — migrate + enrich at `agents/pmm-product-marketing-manager/market-segmentation-analyst/SKILL.md` (complexity: complex). 1 commit.
- [ ] T097 Enrich `win-loss-analyst` — migrate + enrich at `agents/pmm-product-marketing-manager/win-loss-analyst/SKILL.md` (complexity: complex). 1 commit.
- [ ] T098 Enrich `pricing-communicator` — migrate + enrich at `agents/pmm-product-marketing-manager/pricing-communicator/SKILL.md` (complexity: medium). 1 commit.
- [ ] T099 Enrich `demo-script-writer` — migrate + enrich at `agents/pmm-product-marketing-manager/demo-script-writer/SKILL.md` (complexity: simple). 1 commit.
- [ ] T100 Enrich `internal-evangelism-driver` — migrate + enrich at `agents/pmm-product-marketing-manager/internal-evangelism-driver/SKILL.md` (complexity: simple). 1 commit.
- [ ] T101 Enrich `partner-co-marketing-planner` — migrate + enrich at `agents/pmm-product-marketing-manager/partner-co-marketing-planner/SKILL.md` (complexity: medium). 1 commit.
- [ ] T102 Enrich `content-calendar-strategist` — migrate + enrich at `agents/pmm-product-marketing-manager/content-calendar-strategist/SKILL.md` (complexity: medium). 1 commit.
- [ ] T103 Enrich `feature-adoption-campaign-designer` — migrate + enrich at `agents/pmm-product-marketing-manager/feature-adoption-campaign-designer/SKILL.md` (complexity: complex). 1 commit.

---

## Phase 1.5: PMM Analyst / Content Strategist (6 skills)

Agent: PMM Analyst / Content Strategist (`pmm-analyst-content-strategist`) — L1 IC managing SEO, content performance, and editorial calendars.

- [ ] T104 Enrich `seo-keyword-researcher` — migrate + enrich at `agents/pmm-analyst-content-strategist/seo-keyword-researcher/SKILL.md` (complexity: medium). 1 commit.
- [ ] T105 Enrich `content-performance-analyst` — migrate + enrich at `agents/pmm-analyst-content-strategist/content-performance-analyst/SKILL.md` (complexity: medium). 1 commit.
- [ ] T106 Enrich `editorial-calendar-manager` — migrate + enrich at `agents/pmm-analyst-content-strategist/editorial-calendar-manager/SKILL.md` (complexity: simple). 1 commit.
- [ ] T107 Enrich `content-repurposer` — migrate + enrich at `agents/pmm-analyst-content-strategist/content-repurposer/SKILL.md` (complexity: simple). 1 commit.
- [ ] T108 Enrich `audience-persona-researcher` — migrate + enrich at `agents/pmm-analyst-content-strategist/audience-persona-researcher/SKILL.md` (complexity: medium). 1 commit.
- [ ] T109 Enrich `content-gap-identifier` — migrate + enrich at `agents/pmm-analyst-content-strategist/content-gap-identifier/SKILL.md` (complexity: medium). 1 commit.

---

## Phase 1.6: Validate & Finalize

- [ ] T110 Run `python scripts/validate.py agents/vp-product/ agents/product-manager/ agents/product-operations-analyst/ agents/pmm-product-marketing-manager/ agents/pmm-analyst-content-strategist/` — fix any errors. 1 commit per fix.
- [ ] T111 Add cross-references between related Product skills — update `related-skills` frontmatter and Related Skills sections bidirectionally (FR-015). 1 commit per skill updated.
- [ ] T112 Update `status.md` — mark Product department as complete (82/82 enriched, ethos profile done). 1 commit.
- [ ] T113 Update `AGENTS.md` — reflect new `<skill>/SKILL.md` paths for all Product agents. 1 commit.

**Checkpoint**: Product complete. Review before Phase 2:
- Do word limits work in practice?
- Is the ethos profile influencing skill content meaningfully?
- Are cross-references within Product resolving?
- Adjust templates/process based on learnings.

---

## Dependencies

- T024–T026 (research) can run in parallel — no file output
- T027 (ethos) depends on T024–T026 research
- T028–T109 (skill enrichment) depend on T027 (ethos must exist before skills reference it)
- Within each agent section, skills can run in parallel [P] (different directories)
- T110 (validate) depends on all skill tasks completing
- T111 (cross-refs) depends on T110 (validate first, then add refs)
- T112–T113 (status/org chart) depend on T111

## Task Count

| Section | Tasks | Skills |
|---------|-------|--------|
| Research & Ethos | 4 | — |
| VP Product | 18 | 18 |
| Product Manager | 30 | 30 |
| Product Operations Analyst | 12 | 12 |
| PMM | 16 | 16 |
| PMM Analyst | 6 | 6 |
| Validate & Finalize | 4 | — |
| **Total** | **90** | **82** |
