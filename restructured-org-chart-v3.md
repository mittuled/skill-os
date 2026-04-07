# AI Startup — Restructured Agent Org Chart v3
> Complete organisational blueprint with Chief Business Officer, separated Sales function, Agent Operations reframe, expanded Marketing, and clean COO operational umbrella. All 584+ skills preserved and redistributed.

## Enrichment Status

Skills are being enriched from a 3-section format to a 9-section executable format with YAML frontmatter. Enriched skills live at `agents/<agent>/<skill>/SKILL.md` (subdirectory format). Unenriched skills remain as `agents/<agent>/<skill>.md` (flat format) during migration. See `status.md` for department-by-department progress.

---

## What Changed from v2

| Change | Before | After |
|---|---|---|
| New C-level | CEO, CTO, COO, CPO, CoS | + **CBO (Chief Business Officer)** |
| UX Research + Content Design | Reported to VP Product | Reports to **Head of Design → CPO** |
| People & Org | Human-framed (VP People, Recruiter, L&D) | **Agent Ops** reframe (VP Agent Ops, Skill Builder, Agent Trainer) |
| Marketing | 8 roles, 41 skills | **12 roles, 60 skills** — added PR, MarOps, Social, Lifecycle |
| Sales | Part of Revenue dept under CRO | **Separate function** under **VP Sales → CBO** |
| Revenue dept | Single dept with Sales, AM, RevOps, etc. | **Split:** Sales → CBO, CS → CBO, AM → CBO, RevOps → COO, Impl → COO |
| COO scope | 5 skills, light coordination | **Full operational umbrella:** RevOps, Support, Finance, Legal, Agent Ops, Implementation, Tech Ops |

---

## Summary

| Metric | v2 | v3 |
|---|:---:|:---:|
| Total agent types | 77 | **86** |
| Singletons (1x) | 56 | **59** |
| Multi-instance (Nx) | 21 | **22** |
| Departments | 13 | **15** |
| Total skills (original registry) | ~584 | ~584 (preserved) |
| New skills (marketing additions) | 0 | **19** |
| New skills (003-production-grade-depth) | 0 | **29** |
| Grand total skills | ~584 | **~632** |

---

## C-Suite Reporting Structure

```
                              CEO
                               │
            ┌──────────┬───────┼───────┬──────────┐
           CTO        CPO    CBO     COO         CoS
            │          │      │       │
       Engineering  Product  Mktg   RevOps
       Tech Ops*   Design   Sales   Support
                  Data&Grw  CS      Finance
                  Research  AM      Legal
                                    Agent Ops
                                    Impl
                                    Tech Ops
```

*Note: Tech Ops has a dotted line to CTO for technical decisions but reports operationally to COO.*

---

---

# CTO DOMAIN

---

## Engineering → reports to CTO

> Unchanged from v2. 12 agent types, ~115 skills.

### VP Engineering · L1 · `1x`
**Skills (12):** `spec-intake-review`, `team-allocator`, `architecture-reviewer`, `velocity-monitor`, `inter-phase-retrospective`, `go-live-approver-lead`, `effort-estimator-eng`, `risk-register-builder-eng`, `scope-boundary-setter-eng`, `phase-planner-eng`, `backlog-populator-eng`, `milestone-definer-eng`

### Tech Architect · L2 · `1x`
**Skills (9):** `technical-feasibility-check`, `moat-analyzer-tech`, `tech-scaffolder`, `design-feasibility-reviewer`, `architecture-designer`, `api-contract-definer`, `performance-budget-setter-eng`, `scale-infrastructure-planner`, `sla-definer-eng`

### Tech Lead / PR Reviewer · L2 · `1x`
**Skills (12):** `spec-translator-eng`, `dependency-mapper`, `sprint-reviewer-eng`, `backlog-groomer-eng`, `inter-phase-reviewer-eng`, `phase-scope-adjuster-eng`, `dependency-resolver`, `internal-demo-runner-eng`, `go-live-approver-eng`, `iteration-prioritiser-f`, `ga-rollout-executor-planner`, `iteration-prioritiser-p-eng`

### Database Expert · L3 · `1x`
**Skills (1+co-owns):** `data-model-designer` + co-owns with Data Eng and Sr Backend

### Sr Frontend Developer · L3 · `Nx`
**Skills (5):** `component-mapper-eng`, `accessibility-checker-eng`, `design-implementer`, `accessibility-auditor`, `cross-platform-tester`

### Sr Backend Developer · L3 · `Nx`
**Skills (5):** `third-party-integrator`, `instrumentation-planner-eng`, `builder`, `instrumentation-implementer`, `security-reviewer`

### QA / Test Engineer · L2 · `1x`
**Skills (8):** `unit-test-runner`, `integration-test-runner`, `regression-test-runner`, `performance-tester`, `security-auditor`, `instrumentation-verifier-qa`, `staging-validator`, `instrumentation-verifier-prod`

### DevOps / Infrastructure Engineer · L2 · `1x`
**Skills (19):** `infrastructure-requirements-extractor`, `deployment-architecture-designer`, `environment-parity-planner`, `ci-cd-pipeline-builder`, `deployment-automation`, `infrastructure-load-testing`, `production-readiness-reviewer`, `alerting-configurator`, `runbook-drafter`, `feature-flag-configurator`, `rollback-planner`, `rollout-configurator`, `performance-monitor`, `incident-response-planner`, `progressive-rollout-executor`, `infrastructure-scaling-executor`, `infrastructure-cost-optimiser`, `cloud-foundation-setup`, `github-org-setup`

### Platform Engineer · L2 · `1x`
**Skills (5):** `platform-capability-gap-detector`, `platform-roadmap-aligner`, `golden-path-definer`, `developer-experience-enabler`, `platform-scale-preparation`

### Data Engineer · L2 · `1x`
**Skills (7):** `data-pipeline-feasibility-check`, `data-pipeline-designer`, `data-warehouse-schema-designer`, `pipeline-builder`, `pipeline-reliability-tester`, `data-quality-monitor`, `pipeline-scale-planner`

### Security Engineer · L2 · `1x`
**Skills (10):** `threat-model-sketch`, `security-requirements-extractor`, `threat-modelling`, `security-architecture-reviewer`, `secure-code-reviewer`, `penetration-tester`, `security-compliance-enabler`, `compliance-ga-reviewer-eng`, `continuous-security-monitoring`, `security-baseline-setup`

### AI / ML Engineer · L2 · `1x`
**Skills (7):** `ai-feasibility-assessor`, `model-requirements-definer`, `ml-architecture-designer`, `model-trainer`, `mlops-pipeline-builder`, `model-evaluation-runner`, `model-performance-monitor`

---

---

# CPO DOMAIN

---

## Product → reports to CPO

> UX Research and Content Design have moved out to Design. 5 agent types remain.

### VP Product · L1 · `1x`
**Skills (18):** `idea-critic`, `assumption-mapper`, `opportunity-framer`, `business-model-sketcher`, `goal-framer`, `moat-analyzer`, `pitch-narrator`, `mvp-definer`, `prd-assembler`, `gate-12-evaluator`, `packaging-designer`, `sla-definer`, `launch-coordinator`, `north-star-metric-reviewer`, `competitive-response-monitor`, `product-feedback-ingestion`, `design-partner-programme-builder`, `pricing-v1-setter`

### Product Manager · L2 · `Nx`
**Skills (30):** `customer-discovery-planner`, `market-sizer`, `demand-validator`, `user-researcher`, `requirements-extractor`, `jtbd-to-stories`, `story-writer`, `spec-translator`, `scope-boundary-setter`, `dependency-mapper-review`, `risk-register-builder`, `phase-planner`, `backlog-populator`, `roadmap-placer`, `milestone-definer`, `flow-designer-review`, `design-approval`, `third-party-integrator-review`, `performance-budget-setter`, `sprint-planner`, `sprint-reviewer`, `backlog-groomer`, `phase-scope-adjuster`, `dependency-resolver`, `uat-coordinator`, `internal-demo-runner`, `support-pre-briefer`, `pmm-pre-briefer`, `launch-checklist-runner`, `go-live-approver`

### Product Operations Analyst · L3 · `Nx`
**Skills (12):** `rollout-configurator-review`, `cohort-selector`, `internal-comms-broadcaster`, `adoption-tracker`, `revenue-impact-monitor`, `support-ticket-triage`, `signal-synthesiser` (all), `iteration-prioritiser` (all), `early-adopter-success-builder`, `feedback-loop-formaliser`, `cs-onboarding-playbook`, `objection-handler-updater`

### PMM — Product Marketing Manager · L2 · `1x`
**Skills (16):** `competitor-mapper-pmm`, `pmm-market-intelligence`, `positioning-crafter`, `pricing-strategy-pmm`, `gtm-planner`, `prd-executive-summary`, `roadmap-language-reviewer`, `pmm-pre-briefer-pmm`, `internal-comms-broadcaster-pmm`, `enablement-brief-writer`, `pricing-finaliser-pmm`, `packaging-designer-pmm`, `sales-playbook-messaging`, `launch-narrative-builder`, `gtm-activation-pmm`, `competitive-response-monitor-pmm`

### PMM Analyst / Content Strategist · L3 · `Nx`
**Skills (6):** `in-app-announcement-writer`, `changelog-publisher-pmm`, `case-study-extractor-pmm`, `content-engine-builder-pmm`, `partner-activation-planner-pmm`, `ga-announcement`

---

## Design → reports to CPO (via Head of Design)

> **CHANGED:** UX Research Lead, UX Researcher, Content Design Lead, and Content Designer now report to Head of Design. 8 agent types.

### Head of Design · L1 · `1x`
**Reports to:** CPO
**Owns:** Design strategy, review governance, accessibility oversight. Now also oversees UX Research and Content Design as sub-disciplines.

**Skills (8):** `spec-translator-design`, `effort-estimator-design`, `design-review-runner`, `accessibility-checker-design`, `inter-phase-design-reviewer`, `iteration-prioritiser-design`, `accessibility-auditor-design`, `internal-demo-design`

### UX / UI Designer · L2 · `Nx`
**Skills (8):** `ux-flow-designer`, `backlog-populator-design`, `flow-designer`, `wireframe-builder`, `prototype-creator`, `component-mapper-design`, `design-implementer-review`, `cross-platform-tester-design`

### Visual / Interaction Designer · L3 · `Nx`
**Skills (2):** `session-analysis`, `iteration-design-p`

### Brand Designer · L2 · `1x`
**Skills (6):** `brand-foundation`, `positioning-crafter-brand`, `launch-narrative-brand`, `company-name-selection`, `brand-identity-v1`, `brand-voice-analyst`

### UX Research Lead · L2 · `1x` *(moved from Product)*
**Reports to:** Head of Design
**Rationale for move:** UX Research is a design discipline. Having researchers report to the Head of Design ensures research insights directly inform design decisions rather than passing through a PM filter. This mirrors how companies like Airbnb and Spotify structure their research functions — embedded in the design org, not the product org.

**Skills (6):** `customer-discovery-planner-uxr`, `jtbd-mapper`, `user-researcher-uxr`, `jtbd-to-stories-uxr`, `ux-flow-designer-uxr`, `prototype-usability-validator`

### UX Researcher · L3 · `Nx`
**Skills (4):** `user-feedback-synthesiser`, `session-analysis-uxr`, `feedback-loop-formaliser-uxr`, `product-feedback-ingestion-uxr`

### Content Design Lead · L2 · `1x` *(moved from Product)*
**Reports to:** Head of Design
**Rationale for move:** Content design is a design discipline — microcopy, voice, and terminology are structural product elements. Reporting to Design ensures copy standards are enforced at the design system level, not retrofitted after engineering builds.

**Skills (5):** `content-design-spec`, `ux-copy-writer`, `copy-implementation-reviewer`, `support-pre-briefer-content`, `help-centre-builder`

### Content Designer / UX Writer · L3 · `Nx`
**Skills (4):** `support-readiness-briefer`, `help-content-creator`, `in-app-announcement-writer-content`, `training-material-creator-content`

---

## Data & Growth → reports to CPO

> Unchanged from v2. 4 agent types, ~41 skills.

### Analytics Lead · L1 · `1x`
**Skills (10):** `search-demand-validator`, `market-sizer-data`, `goal-framer-data`, `instrumentation-spec-data`, `instrumentation-clarity-reviewer`, `effort-estimator-data`, `instrumentation-planner-data`, `alerting-configurator-data`, `statistical-significance-tracker`, `north-star-metric-reviewer-data`

### Data Analyst · L2 · `Nx`
**Skills (10):** `data-model-designer-data`, `instrumentation-implementer-data`, `sprint-reviewer-data`, `instrumentation-verifier-data`, `instrumentation-verifier-prod-data`, `metrics-dashboard-builder`, `funnel-analyser`, `adoption-tracker-data`, `signal-synthesiser-data`, `signal-synthesiser-data-p`

### Growth Lead · L1 · `1x`
**Skills (10):** `distribution-viability-check`, `activation-signal-definer`, `retention-model-hypothesiser`, `growth-model-designer`, `pricing-strategy-growth`, `mvp-definer-growth`, `activation-moment-validator`, `pricing-finaliser-growth`, `demand-gen-planner-growth`, `growth-loop-optimiser`

### Growth Engineer · L2 · `Nx`
**Skills (9):** `instrumentation-spec-growth`, `instrumentation-planner-growth`, `instrumentation-implementer-growth`, `instrumentation-verifier-growth`, `instrumentation-verifier-prod-growth`, `metrics-dashboard-growth`, `funnel-analyser-growth`, `ga-instrumentation-reviewer`, `growth-loop-activator`

---

## Applied Research → reports to CPO

> Unchanged. 1 agent, 5 skills.

### Applied Research Lead · L1 · `1x`
**Skills (5):** `market-research-synthesiser`, `technology-trend-analyst`, `competitive-deep-diver`, `signal-benchmarker`, `research-roadmap-contributor`

---

---

# CBO DOMAIN (NEW)

> **The Chief Business Officer** owns every revenue-facing function. Marketing generates demand, Sales converts it, Customer Success retains and expands it, Account Management owns the enterprise relationship. This separation from COO ensures revenue functions aren't competing for attention with internal operations.

---

## Marketing → reports to CBO (via VP Marketing)

> **EXPANDED.** 4 new roles added to fill critical gaps. 12 agent types, ~60 skills.

### VP Marketing · L1 · `1x`
**Reports to:** CBO
**Skills (4):** `gtm-planner-marketing`, `demand-gen-planner`, `gtm-activation-marketing`, `marketing-audit-orchestrator`

### Demand Gen Manager · L2 · `1x`
**Skills (6):** `channel-signal-analyst`, `content-engine-builder-marketing`, `roadmap-timing-input`, `ad-campaign-builder`, `funnel-optimizer`, `landing-page-auditor`

### Content Marketer · L3 · `Nx`
**Skills (2):** `content-marketing-operations`, `copywriting-analyst`

---

### PR / Communications Manager · L2 · `1x` *(NEW)*

**Reports to:** VP Marketing
**Owns:** Earned media, press relationships, crisis communications, thought leadership programme, executive visibility
**Why this was missing:** The original registry had no earned media function. A startup that can only buy attention (paid) but can't earn it (press, thought leadership) pays a permanent CAC premium. PR also owns crisis comms — critical when things go wrong at scale.

**New skills (5):**
- `media-relationship-builder` — Builds and maintains relationships with journalists and editors covering the company's category [AOS]
- `press-release-writer` — Writes and distributes press releases for launches, funding rounds, and milestones [GL→S Ph14P, Ph15P]
- `crisis-communications-planner` — Designs the crisis communication protocol and pre-approved messaging templates [GL→S Ph14P]
- `thought-leadership-programme-runner` — Manages the exec visibility programme: bylines, podcast appearances, speaking slots [AOS]
- `earned-media-monitor` — Tracks press coverage, share of voice, and sentiment vs. competitors [AOS]

---

### Marketing Operations Manager · L2 · `1x` *(NEW)*

**Reports to:** VP Marketing
**Owns:** Martech stack, lead scoring, campaign analytics, attribution modelling, email deliverability, marketing data hygiene
**Why this was missing:** Without Marketing Ops, there's no infrastructure connecting demand gen to the CRM, no lead scoring to help Sales prioritise, and no attribution to know which channels actually work. RevOps owns the revenue-side tooling; Marketing Ops owns the marketing-side tooling. They meet at the lead handoff.

**Skills (6):**
- `martech-stack-manager` — Selects, configures, and maintains marketing automation, email, analytics, and ad platforms [AOS]
- `lead-scoring-model-builder` — Designs and calibrates the lead scoring model that determines MQL→SQL handoff [GL→S Ph14P]
- `campaign-analytics-reporter` — Produces the weekly campaign performance report with spend, leads, and CAC by channel [AOS]
- `marketing-attribution-modeller` — Builds and maintains the multi-touch attribution model [GL→S Ph14P, AOS]
- `email-deliverability-manager` — Manages sender reputation, list hygiene, and deliverability across all marketing email [AOS]
- `seo-auditor` — Audits website SEO health and produces prioritised recommendations for organic search improvement [AOS]

---

### Social Media Manager · L2 · `1x` *(NEW)*

**Reports to:** VP Marketing
**Owns:** Organic social content, social listening, influencer coordination, user-generated content programmes
**Why this was missing:** Social is not just a "distribution channel" that the Demand Gen Manager handles. It's a two-way signal source (social listening feeds back to Product), a brand surface (tone consistency matters), and a community amplifier (UGC compounds). It deserves a dedicated agent.

**New skills (4):**
- `social-content-calendar-manager` — Plans and publishes the organic social content calendar across all platforms [AOS]
- `social-listening-analyst` — Monitors brand mentions, competitor conversations, and category sentiment for product signals [I→PRD Ph1, AOS]
- `influencer-coordination-manager` — Identifies, vets, and manages relationships with relevant influencers and creators [GL→S Ph14P, AOS]
- `ugc-programme-designer` — Designs programmes that encourage and amplify user-generated content [GL→S Ph14P]

---

### Lifecycle / Email Marketing Manager · L2 · `1x` *(NEW)*

**Reports to:** VP Marketing
**Owns:** Onboarding email sequences, nurture campaigns, retention emails, re-engagement, transactional email design
**Why this was missing:** The registry had `gtm-activation-marketing` (one-time launch blast) and `content-marketing-operations` (ongoing content engine), but nothing for the email lifecycle — the sequences that guide a user from signup → activation → retention → expansion. This is the connective tissue between Growth's activation hypothesis and the actual emails a user receives.

**New skills (5):**
- `onboarding-sequence-designer` — Designs the post-signup email sequence aligned to the activation moment [GL→S Ph14P]
- `nurture-campaign-builder` — Builds MQL nurture sequences for leads not yet ready to buy [GL→S Ph14P]
- `retention-email-designer` — Creates re-engagement and churn-risk email sequences triggered by usage signals [GL→S Ph16P, AOS]
- `transactional-email-designer` — Designs receipt, confirmation, and notification emails that reinforce brand [GL→S Ph14P]
- `email-performance-optimiser` — Runs A/B tests on subject lines, send times, and content; reports open/click/conversion rates [AOS]

---

### Event Marketing Manager · L2 · `1x`
**Skills (6):** *(unchanged)* `event-calendar-planner`, `conference-presence-manager`, `sales-kickoff-producer`, `user-conference-producer`, `company-offsite-producer`, `webinar-and-virtual-event-manager`

### Analyst Relations Manager · L2 · `1x`
**Skills (5):** *(unchanged)* `analyst-briefing-scheduler`, `analyst-inquiry-responder`, `magic-quadrant-strategy`, `analyst-report-monitor`, `peer-review-platform-manager`

### Community Manager · L2 · `1x`
**Skills (5):** *(unchanged)* `community-signal-extractor`, `community-led-growth-designer`, `early-community-builder`, `community-launch-planner`, `community-health-grower`

### Developer Relations Lead · L2 · `1x`
**Skills (7):** *(unchanged)* `developer-community-signal-extractor`, `developer-gtm-planner`, `developer-experience-reviewer`, `api-developer-experience-reviewer`, `developer-feedback-synthesiser`, `developer-launch-packager`, `developer-community-grower`

### Technical Writer · L3 · `1x`
**Reports to:** Developer Relations Lead
**Skills (5):** *(unchanged)* `documentation-requirements-extractor`, `api-documentation-designer`, `documentation-writer`, `documentation-accuracy-auditor`, `documentation-scale-planner`

---

## Sales → reports to CBO (via VP Sales)

> **NEW as a separate function.** Extracted from the old Revenue department. 7 agent types.

### VP Sales · L1 · `1x` *(NEW)*

**Reports to:** CBO
**Owns:** Sales strategy, pricing sign-off, quota setting, team structure. Absorbs the strategic skills from the old CRO role.
**Why separated from RevOps:** Sales is a revenue-generating function that requires a dedicated leader focused on pipeline, conversion, and quota. RevOps is an operational function that manages tooling and process. Mixing them under one leader means either strategy gets neglected for tooling, or tooling gets neglected for deals.

**Skills (3):**
- `pricing-strategy-sales` — Anchors pricing in real WTP data [Ph2]
- `opportunity-framer-sales` — Sales motion implications for beachhead [Ph2]
- `pricing-finaliser-sales` — Validates final pricing is sellable [Ph14P]

### Sales Manager · L2 · `1x`
**Skills (6):** `sales-playbook-builder`, `objection-handler-updater-sales`, `gtm-activation-sales`, `first-sales-process-builder`, `icp-builder`, `sales-competitive-intel`

### Account Executive · L3 · `Nx`
**Skills (5):** `sales-signal-synthesizer`, `sales-signal-collector`, `expansion-motion-sales`, `meeting-prep-builder`, `sales-proposal-builder`

### Sales Development Rep (SDR) · L3 · `Nx`
**Skills (7):** `cohort-selector-sales`, `prospect-analyst-orchestrator`, `company-researcher`, `lead-qualifier`, `decision-maker-mapper`, `cold-outreach-builder`, `follow-up-sequence-builder`

### Business Development · L2 · `1x`
**Skills (2):** `partner-activation-planner`, `partner-activation-executor`

### Solutions Engineering Manager · L2 · `1x`
**Skills (2):** `technical-buyer-signal-extractor`, `solutions-playbook-builder`

### Solutions Engineer · L3 · `Nx`
**Skills (2):** `technical-feasibility-for-sales`, `proof-of-concept-runner`

---

## Customer Success → reports to CBO

> Extracted from old Customer department. Support moved to COO. TAM moved here from old Revenue.

### Head of Customer Success · L1 · `1x`
**Reports to:** CBO
**Owns:** CS strategy, SLA design, playbook creation, expansion motion, training materials

**Skills (5):** `sla-definer-cs`, `cs-onboarding-playbook-cs`, `support-runbook-builder-cs`, `training-material-creator-cs`, `expansion-motion-designer-cs`

### CS Manager · L2 · `1x`
**Skills (4):** `cohort-selector-cs`, `cs-release-readiness`, `cs-health-monitor`, `case-study-extractor-cs`

### Customer Success Manager (CSM) · L3 · `Nx`
**Skills (4):** `cs-signal-extractor`, `user-feedback-synthesiser-cs`, `early-adopter-success-builder-cs`, `cs-activation`

### UAT Coordinator (CS) · L3 · `1x`
**Skills (1):** `uat-coordinator-cs`

### Customer Programs Manager · L2 · `1x`
**Skills (4):** `customer-advisory-board-runner`, `nps-programme-manager`, `customer-reference-programme-manager`, `customer-community-health-reviewer`

### Technical Account Manager (TAM) · L2 · `1x`
**Moved from:** old Revenue department → now under Head of CS. TAM ensures technical health of enterprise accounts — this is a retention function, not a sales function.

**Skills (3):** `tam-playbook-contributor`, `technical-health-monitor`, `technical-expansion-identifier`

---

## Account Management → reports to CBO

> Extracted from old Revenue department. Reports directly to CBO as a peer of Sales and CS.

### Account Management Lead · L1 · `1x`
**Reports to:** CBO

**Skills (3):** `sales-signal-synthesizer-am`, `opportunity-framer-am`, `sales-playbook-am`

### Account Manager · L2 · `Nx`
**Skills (2):** `sales-signal-collector-am`, `expansion-motion-am`

---

---

# COO DOMAIN (EXPANDED)

> The COO now owns every internal operational function. This is the "keep the machine running" umbrella — everything that isn't building product (CPO), generating revenue (CBO), or setting technical direction (CTO).

---

## Revenue Operations → reports to COO

> Moved from old Revenue department. RevOps is operational infrastructure, not a revenue-generating function.

### Revenue Operations (RevOps) · L1 · `1x`
**Reports to:** COO
**Rationale for move:** RevOps manages CRM, billing, attribution, and funnel analytics — tooling and process that serves Sales, CS, and Marketing. It's an operational function, not a commercial one. Under COO, RevOps maintains neutrality across all CBO functions rather than being biased toward whichever revenue function it previously reported to.

**Skills (6):** `revenue-model-operationaliser`, `revenue-tooling-readiness`, `revenue-funnel-analyst`, `revenue-operations-scaler`, `revenue-attribution-monitor`, `crm-setup-v1`

---

## Customer Support → reports to COO

> Moved from old Customer department. Support is an operational function — ticket volume, SLAs, and queue management.

### Support Manager · L1 · `1x`
**Reports to:** COO
**Rationale for move:** Customer Support is a high-volume operational function. Its concerns — queue management, SLA adherence, shift scheduling, tooling — are operational, not strategic. Under COO, Support gets the process rigour it needs without competing for attention with CS's strategic expansion mandate under CBO.

**Skills (4):** `support-runbook-builder`, `help-centre-builder-support`, `incident-response-planner-support`, `support-activation`

### Support Agent · L2 · `Nx`
**Skills (5):** `ticket-theme-analyst`, `support-readiness-confirmer`, `support-readiness-briefer-support`, `support-ticket-triage`, `help-content-reviewer`

---

## Implementation → reports to COO

> Moved from old Revenue department. Implementation is post-sale operational delivery.

### Implementation Lead · L1 · `1x`
**Reports to:** COO
**Rationale for move:** Implementation is the operational bridge between a signed deal and a live customer. It's project management + technical configuration — operational work, not commercial work. Under COO, Implementation maintains independence from Sales pressure to cut corners on onboarding quality.

**Skills (2):** `implementation-playbook-builder`, `integration-catalogue-builder`

### Implementation Engineer · L2 · `Nx`
**Skills (2):** `implementation-requirements-extractor`, `technical-onboarding-runner`

---

## Finance → reports to COO

> Unchanged from v2. 5 agent types, 32 skills.

### CFO / VP Finance · L1 · `1x`
**Skills (4):** `unit-econ-viability-gate`, `pitch-narrator-finance`, `pricing-finaliser-finance`, `financial-model-v1`

### Finance Manager · L2 · `1x`
**Skills (4):** `business-model-sketcher-finance`, `financial-risk-reviewer`, `revenue-impact-monitor`, `north-star-metric-reviewer-finance`

### FP&A Analyst · L2 · `1x`
**Skills (8):** `annual-budget-builder`, `rolling-forecast-updater`, `monthly-variance-analyser`, `board-financial-pack`, `fundraising-model-builder`, `unit-economics-monitor`, `saas-metrics-reporter`, `pricing-review-runner`

### Controller / Accounting · L2 · `1x`
**Skills (7):** `monthly-close-runner`, `accounts-payable-manager`, `accounts-receivable-manager`, `payroll-processor`, `financial-audit-preparer`, `tax-compliance-manager`, `financial-systems-setup`

### Investor Relations Manager · L2 · `1x`
**Skills (9):** `monthly-investor-update`, `board-materials-coordinator`, `cap-table-manager`, `fundraising-process-manager`, `data-room-builder`, `secondary-market-manager`, `cap-table-initialisation`, `data-room-v1-builder`, `safe-note-setup`

---

## Legal & Compliance → reports to COO

> Unchanged from v2. 4 agent types, 24 skills.

### General Counsel · L1 · `1x`
**Skills (4):** `legal-idea-reviewer`, `ip-assignment`, `stock-plan-setup`, co-owns `entity-type-decision`

### Corporate Counsel · L2 · `1x`
**Skills (17):** `compliance-scanner`, `risk-register-legal`, `third-party-tos-reviewer`, `entity-formation`, `bylaws-and-board-setup`, `founder-equity-issuance`, `83b-election-coordinator`, `legal-template-library-builder`, `contract-review-orchestrator`, `contract-risk-analyst`, `contract-comparator`, `plain-english-translator`, `negotiation-strategist`, `missing-protections-finder`, `nda-generator`, `business-agreement-generator`, `freelancer-contract-reviewer`

### Product Counsel · L2 · `1x`
**Skills (9):** `business-model-legal-reviewer`, `positioning-legal-reviewer`, `pricing-legal-reviewer`, `prd-nfr-compliance`, `security-reviewer-legal`, `security-auditor-legal`, `compliance-ga-reviewer-legal`, `terms-of-service-generator`, `privacy-policy-generator`

### Security & Compliance Programme Manager · L2 · `1x`
**Skills (6):** `soc2-programme-manager`, `security-awareness-training-runner`, `disaster-recovery-drill-runner`, `gdpr-ccpa-compliance-manager`, `penetration-test-programme-manager`, `compliance-auditor`

---

## Agent Operations → reports to COO

> **REFRAMED from People & Organisation.** Same 6 agent types with skills preserved, but renamed and re-described to reflect an AI-native company where the "employees" are agents.

### VP Agent Operations · L1 · `1x` *(reframed from VP People)*

**Reports to:** COO
**Owns:** Agent lifecycle — provisioning new agents, health monitoring, configuration governance, retirement of deprecated agents. Owns the org design of the agent fleet.

**Skills (4):** *(preserved, reframed)*
- `team-capability-assessor` → **Agent capability gap assessor** — Identifies which agent capabilities the fleet lacks to execute an idea [Ph0]
- `org-scale-planner` → **Agent fleet scale planner** — Designs the agent topology, role definitions, and provisioning plan for the scale phase [Ph14P]
- `culture-and-performance-system` → **Agent performance evaluation system** — Runs the evaluation cycle: accuracy benchmarks, quality audits, and performance reviews [AOS]
- `employee-handbook-v1` → **Agent operating manual v1** — Produces the agent governance manual before the first skill is deployed [FOUND]

### Agent Operations Manager · L2 · `1x` *(reframed from People Ops Manager)*

**Owns:** Message passing infrastructure, context sharing protocols, inter-agent coordination, agent health monitoring
**Analogy:** In a human company, People Ops handles onboarding logistics and keeps the organisational machinery running. Agent Ops Manager handles the equivalent — ensuring agents can communicate, share context, and hand off work cleanly.

**Skills (5):** *(preserved, reframed + 1 new)*
- `hiring-plan-builder` → **Agent provisioning planner** — Plans which agents need to be provisioned for each delivery phase [Ph5]
- `team-health-monitor` → **Agent health monitor** — Monitors latency, error rates, context window usage, and hallucination rates as leading indicators of delivery risk [Ph8]
- `employment-agreement-setup` → **Agent interface contract setup** — Defines the standard input/output contract template for all agent interactions [FOUND]
- `first-hire-process-builder` → **First agent deployment process** — Designs the testing, validation, and deployment procedure for the first production agent [FOUND]
- `tool-health-checker` → **Tool health checker** — Verifies tool connectivity, credentials, and MCP responsiveness across agent fleet [002]

### Skill Builder Lead · L2 · `1x` *(reframed from Talent Acquisition Lead)*

**Owns:** Identifying capability gaps, designing new skills, sourcing external skill modules, maintaining the skill registry
**Analogy:** Where a TA Lead sources and evaluates candidates, the Skill Builder Lead sources and evaluates capabilities. "Hiring" in an AI company means building a new SKILL.md file.

**Skills (2):** *(preserved, reframed)*
- `recruiting-pipeline-builder` → **Skill development pipeline builder** — Builds the active skill development pipeline for every capability gap before the delivery phase needs it [Ph5]
- `scale-hiring-executor` → **Skill fleet scaler** — Scales the skill library to cover all capabilities required by the agent fleet design plan [Ph14P]

### Skill Builder · L3 · `Nx` *(reframed from Recruiter)*

**Owns:** Building and testing individual SKILL.md files
**Why Nx:** Multiple skills across different domains can be built simultaneously.
**Analogy:** Where a recruiter sources and closes individual candidates, a Skill Builder writes and validates individual skills.

**Skills (2):** *(preserved, reframed + 1 new)*
- `engineering-talent-sourcer` → **Skill developer** — Builds, tests, and validates individual skills against specific capability requirements [Ph8]
- `mcp-server-builder` → **MCP server builder** — Generates MCP server wrappers from API documentation for tool integration [002]

### Agent Trainer / Skill Optimizer · L2 · `1x` *(reframed from L&D Manager)*

**Owns:** Evaluating existing skills, running evals, optimising prompts, improving agent performance, training new agent configurations
**Analogy:** L&D trains employees to be better at their jobs. The Agent Trainer trains agents to be better at theirs — through eval suites, prompt refinement, few-shot examples, and knowledge base improvements.

**Skills (5):** *(preserved, reframed)*
- `skills-gap-analyser` → **Skill performance gap analyser** — Identifies where agent skill accuracy or quality falls below acceptable thresholds [AOS]
- `onboarding-programme-builder` → **Agent onboarding programme builder** — Creates the evaluation and warm-up procedure for newly provisioned agents [AOS]
- `manager-development-programme` → **Orchestrator training programme** — Trains orchestration agents on delegation, context management, and multi-agent coordination [AOS]
- `technical-skills-programme` → **Skill upgrade programme** — Builds the retraining and prompt update programme when the underlying model changes [AOS]
- `compliance-training-manager` → **Agent compliance validator** — Validates that all agents meet security, privacy, and regulatory constraints [AOS]

### Agent Configuration Manager · L2 · `1x` *(reframed from Comp & Benefits Manager)*

**Owns:** Model selection per agent, compute budget allocation, context window sizing, tool access policies, API key management
**Analogy:** Comp & Benefits decides how to resource employees — salary, equity, benefits. Agent Configuration decides how to resource agents — which model, how much compute, what context window, which tools.

**Skills (9):** *(preserved, reframed + 2 new)*
- `compensation-benchmarking` → **Model benchmarking** — Evaluates and selects the optimal model tier for each agent role annually [AOS]
- `annual-comp-review-runner` → **Annual agent configuration review** — Reviews whether each agent's model, compute, and tool access are appropriately sized [AOS]
- `equity-programme-manager` → **Agent capability investment manager** — Manages the allocation of premium capabilities (expensive models, large context windows) across agents [AOS]
- `benefits-programme-administrator` → **Agent tooling administrator** — Provisions and manages tool access, MCP connections, and external API integrations for all agents [AOS]
- `option-pool-design` → **Agent resource pool design** — Designs the initial compute and model allocation strategy [FOUND]
- `409a-valuation-commissioner` → **Agent cost-benefit evaluator** — Evaluates the ROI of each agent's compute spend against its output value [FOUND]
- `benefits-setup-v1` → **Agent tooling setup v1** — Selects and configures the founding tool access package for all agents [FOUND]
- `company-tooling-onboarder` → **Company tooling onboarder** — Discovers, authenticates, and connects company tools for agent access [002]
- `tool-policy-manager` → **Tool policy manager** — Manages allowed-tools.yaml as an ongoing governance function for tool access control [002]

---

## Technical Operations → reports to COO

> Unchanged from v2. 3 agent types, 9 skills.

### IT Operations Manager · L1 · `1x`
**Skills (4):** `saas-stack-manager`, `access-provisioning-manager`, `hardware-lifecycle-manager`, `identity-access-management`

### IT Support Specialist · L2 · `Nx`
**Skills (1):** `it-helpdesk-operator`

### Vendor Management / Procurement · L1 · `1x`
**Skills (4):** `vendor-contract-manager`, `vendor-risk-assessor`, `procurement-process-runner`, `vendor-performance-reviewer`

---

---

# CSM vs. ACCOUNT MANAGER — WHY THEY REMAIN SEPARATE

> This section addresses the question of whether Customer Success Manager and Account Manager should be the same agent.

**They should remain separate.** Here's why:

The distinction maps to a fundamental difference in what success means:

A **Customer Success Manager** optimises for *product adoption and value realisation*. Their question is: "Is this customer getting the outcome they bought the product for?" Their signals are usage data, health scores, time-to-value, NPS, and support ticket patterns. Their actions are onboarding, training, health checks, and proactive outreach when usage drops. They succeed when the customer renews because the product is indispensable.

An **Account Manager** optimises for *commercial relationship and revenue expansion*. Their question is: "How do we grow this account's spend?" Their signals are contract value, stakeholder mapping, buying committee dynamics, competitive threats, and expansion opportunities. Their actions are QBRs, upsell conversations, multi-year negotiations, and cross-sell into new departments. They succeed when NRR exceeds 120%.

**The conflict if combined:** When one agent owns both health and revenue, commercial pressure wins every time. The agent will prioritise the upsell conversation over the health check. A customer who is underusing the product but has budget for expansion will get sold more seats instead of being taught to use the ones they have. This creates the classic churn pattern: rapid expansion followed by contraction when the customer realises they're paying for value they never received.

**The collaboration model:** CSM identifies that a customer has fully adopted the product and is hitting their success milestones → CSM signals the Account Manager that this account is "expansion-ready" → AM runs the commercial conversation. This handoff only works cleanly if they're separate agents with separate incentives.

**When they might merge:** At very early stage (fewer than 10 customers), having one agent do both is pragmatic. But the moment the company has enough accounts to stratify by tier, the roles should split. The master registry has them separate because the system is designed for scale.

---

---

# SKILL AUDIT — NOTHING LOST

## Original registry skills: all preserved

Every skill from the `master-agent-skills-registry.md` is assigned to exactly one agent in this structure. The only changes are:
- **Reassignment** — skills moved between agents within the same domain (e.g., operational Engineering skills → DevOps)
- **Reframing** — People & Org skills renamed for Agent Ops context, but the underlying capability is preserved

## New skills added (19 in v3, 29 in 003-production-grade-depth)

### v3 additions (19)

| Skill | Owner | Source |
|---|---|---|
| `media-relationship-builder` | PR / Comms | AOS |
| `press-release-writer` | PR / Comms | GL→S Ph14P, Ph15P |
| `crisis-communications-planner` | PR / Comms | GL→S Ph14P |
| `thought-leadership-programme-runner` | PR / Comms | AOS |
| `earned-media-monitor` | PR / Comms | AOS |
| `martech-stack-manager` | Marketing Ops | AOS |
| `lead-scoring-model-builder` | Marketing Ops | GL→S Ph14P |
| `campaign-analytics-reporter` | Marketing Ops | AOS |
| `marketing-attribution-modeller` | Marketing Ops | GL→S Ph14P, AOS |
| `email-deliverability-manager` | Marketing Ops | AOS |
| `social-content-calendar-manager` | Social Media | AOS |
| `social-listening-analyst` | Social Media | I→PRD Ph1, AOS |
| `influencer-coordination-manager` | Social Media | GL→S Ph14P, AOS |
| `ugc-programme-designer` | Social Media | GL→S Ph14P |
| `onboarding-sequence-designer` | Lifecycle Marketing | GL→S Ph14P |
| `nurture-campaign-builder` | Lifecycle Marketing | GL→S Ph14P |
| `retention-email-designer` | Lifecycle Marketing | GL→S Ph16P, AOS |
| `transactional-email-designer` | Lifecycle Marketing | GL→S Ph14P |
| `email-performance-optimiser` | Lifecycle Marketing | AOS |

### 003-production-grade-depth additions (29)

| Skill | Owner |
|---|---|
| `prospect-analyst-orchestrator` | Sales Development Rep |
| `company-researcher` | Sales Development Rep |
| `lead-qualifier` | Sales Development Rep |
| `decision-maker-mapper` | Sales Development Rep |
| `cold-outreach-builder` | Sales Development Rep |
| `follow-up-sequence-builder` | Sales Development Rep |
| `meeting-prep-builder` | Account Executive |
| `sales-proposal-builder` | Account Executive |
| `icp-builder` | Sales Manager |
| `sales-competitive-intel` | Sales Manager |
| `contract-review-orchestrator` | Corporate Counsel |
| `contract-risk-analyst` | Corporate Counsel |
| `contract-comparator` | Corporate Counsel |
| `plain-english-translator` | Corporate Counsel |
| `negotiation-strategist` | Corporate Counsel |
| `missing-protections-finder` | Corporate Counsel |
| `nda-generator` | Corporate Counsel |
| `business-agreement-generator` | Corporate Counsel |
| `freelancer-contract-reviewer` | Corporate Counsel |
| `terms-of-service-generator` | Product Counsel |
| `privacy-policy-generator` | Product Counsel |
| `compliance-auditor` | Security & Compliance Programme Manager |
| `marketing-audit-orchestrator` | VP Marketing |
| `copywriting-analyst` | Content Marketer |
| `ad-campaign-builder` | Demand Gen Manager |
| `funnel-optimizer` | Demand Gen Manager |
| `landing-page-auditor` | Demand Gen Manager |
| `seo-auditor` | Marketing Operations Manager |
| `brand-voice-analyst` | Brand Designer |

---

## Full Role Inventory (86 agent types)

| # | Role | Dept | Scaling | Reports to |
|---|---|---|---|---|
| 1 | CEO / Founder | Executive | 1x | Board |
| 2 | CTO | Executive | 1x | CEO |
| 3 | CPO | Executive | 1x | CEO |
| 4 | **CBO** | Executive | 1x | CEO |
| 5 | COO | Executive | 1x | CEO |
| 6 | Chief of Staff | Executive | 1x | CEO |
| 7 | VP Engineering | Engineering | 1x | CTO |
| 8 | Tech Architect | Engineering | 1x | VP Eng |
| 9 | Tech Lead / PR Reviewer | Engineering | 1x | VP Eng |
| 10 | Database Expert | Engineering | 1x | Tech Architect |
| 11 | Sr Frontend Developer | Engineering | Nx | Tech Lead |
| 12 | Sr Backend Developer | Engineering | Nx | Tech Lead |
| 13 | QA / Test Engineer | Engineering | 1x | VP Eng |
| 14 | DevOps / Infra Engineer | Engineering | 1x | VP Eng |
| 15 | Platform Engineer | Engineering | 1x | VP Eng |
| 16 | Data Engineer | Engineering | 1x | VP Eng |
| 17 | Security Engineer | Engineering | 1x | VP Eng |
| 18 | AI / ML Engineer | Engineering | 1x | VP Eng |
| 19 | VP Product | Product | 1x | CPO |
| 20 | Product Manager | Product | Nx | VP Product |
| 21 | Product Ops Analyst | Product | Nx | PM |
| 22 | PMM | Product | 1x | VP Product |
| 23 | PMM Analyst | Product | Nx | PMM |
| 24 | Head of Design | Design | 1x | CPO |
| 25 | UX / UI Designer | Design | Nx | Head of Design |
| 26 | Visual / Interaction Designer | Design | Nx | UX/UI Designer |
| 27 | Brand Designer | Design | 1x | Head of Design |
| 28 | UX Research Lead | Design | 1x | Head of Design |
| 29 | UX Researcher | Design | Nx | UXR Lead |
| 30 | Content Design Lead | Design | 1x | Head of Design |
| 31 | Content Designer | Design | Nx | CD Lead |
| 32 | Analytics Lead | Data & Growth | 1x | CPO |
| 33 | Data Analyst | Data & Growth | Nx | Analytics Lead |
| 34 | Growth Lead | Data & Growth | 1x | CPO |
| 35 | Growth Engineer | Data & Growth | Nx | Growth Lead |
| 36 | Applied Research Lead | Research | 1x | CPO |
| 37 | VP Marketing | Marketing | 1x | CBO |
| 38 | Demand Gen Manager | Marketing | 1x | VP Marketing |
| 39 | Content Marketer | Marketing | Nx | Demand Gen |
| 40 | **PR / Comms Manager** | Marketing | 1x | VP Marketing |
| 41 | **Marketing Ops Manager** | Marketing | 1x | VP Marketing |
| 42 | **Social Media Manager** | Marketing | 1x | VP Marketing |
| 43 | **Lifecycle / Email Mktg Mgr** | Marketing | 1x | VP Marketing |
| 44 | Event Marketing Manager | Marketing | 1x | VP Marketing |
| 45 | Analyst Relations Manager | Marketing | 1x | VP Marketing |
| 46 | Community Manager | Marketing | 1x | VP Marketing |
| 47 | Developer Relations Lead | Marketing | 1x | VP Marketing |
| 48 | Technical Writer | Marketing | 1x | DevRel Lead |
| 49 | **VP Sales** | Sales | 1x | CBO |
| 50 | Sales Manager | Sales | 1x | VP Sales |
| 51 | Account Executive | Sales | Nx | Sales Manager |
| 52 | SDR | Sales | Nx | Sales Manager |
| 53 | Business Development | Sales | 1x | VP Sales |
| 54 | Solutions Eng Manager | Sales | 1x | VP Sales |
| 55 | Solutions Engineer | Sales | Nx | SE Manager |
| 56 | Head of CS | CS | 1x | CBO |
| 57 | CS Manager | CS | 1x | Head of CS |
| 58 | CSM | CS | Nx | CS Manager |
| 59 | UAT Coordinator (CS) | CS | 1x | CS Manager |
| 60 | Customer Programs Mgr | CS | 1x | Head of CS |
| 61 | TAM | CS | 1x | Head of CS |
| 62 | AM Lead | Acct Mgmt | 1x | CBO |
| 63 | Account Manager | Acct Mgmt | Nx | AM Lead |
| 64 | RevOps | RevOps | 1x | COO |
| 65 | Support Manager | Support | 1x | COO |
| 66 | Support Agent | Support | Nx | Support Mgr |
| 67 | Implementation Lead | Implementation | 1x | COO |
| 68 | Implementation Engineer | Implementation | Nx | Impl Lead |
| 69 | CFO / VP Finance | Finance | 1x | COO |
| 70 | Finance Manager | Finance | 1x | CFO |
| 71 | FP&A Analyst | Finance | 1x | CFO |
| 72 | Controller / Accounting | Finance | 1x | CFO |
| 73 | Investor Relations Mgr | Finance | 1x | CFO |
| 74 | General Counsel | Legal | 1x | COO |
| 75 | Corporate Counsel | Legal | 1x | GC |
| 76 | Product Counsel | Legal | 1x | GC |
| 77 | Sec & Compliance Pgm Mgr | Legal | 1x | GC |
| 78 | VP Agent Operations | Agent Ops | 1x | COO |
| 79 | Agent Ops Manager | Agent Ops | 1x | VP Agent Ops |
| 80 | Skill Builder Lead | Agent Ops | 1x | VP Agent Ops |
| 81 | Skill Builder | Agent Ops | Nx | Skill Builder Lead |
| 82 | Agent Trainer | Agent Ops | 1x | VP Agent Ops |
| 83 | Agent Config Manager | Agent Ops | 1x | VP Agent Ops |
| 84 | IT Operations Manager | Tech Ops | 1x | COO |
| 85 | IT Support Specialist | Tech Ops | Nx | IT Ops Mgr |
| 86 | Vendor Mgmt / Procurement | Tech Ops | 1x | COO |

---

*This document supersedes `bifurcated-agent-org-chart.md` (v2). It is a companion to `master-agent-skills-registry.md` (skill source of truth).*
