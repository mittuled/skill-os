# Zubair-Trabzada Deep Comparison: Marketing, Sales, Legal

**Date**: 2026-03-27
**Scope**: skill-os (54 Marketing, 17 Sales, 36 Legal skills) vs. zubair-trabzada's 3 repos (14 Marketing, 14 Sales, 13 Legal skills + agents)

---

## Executive Summary

zubair-trabzada's repos are **runtime agent prompts** — each skill is a 4,000-6,000 word operational playbook designed to execute a complete workflow end-to-end with scoring, templates, and multi-agent orchestration. skill-os skills are **structured knowledge units** — 500-1,500 word enriched definitions designed to be loaded into any AI agent's context.

**They solve different problems.** zubair builds 14 deep skills per domain. skill-os builds 54 broad skills per domain. The right comparison isn't "which is better" but "what does each have that the other doesn't?"

---

## Coverage Comparison

### Marketing

| Capability | skill-os (54 skills) | zubair (14 skills) | Gap |
|-----------|---------------------|-------------------|-----|
| Full marketing audit | No orchestrator | `market-audit` — 5 parallel agents, weighted scoring | **skill-os gap**: no multi-agent audit orchestrator |
| Copywriting analysis | No dedicated skill | `market-copy` — headline formulas, voice dimensions, swipe file | **skill-os gap**: no copy analysis/generation |
| Email sequences | `onboarding-sequence-designer`, `nurture-campaign-builder`, `retention-email-designer`, `transactional-email-designer`, `email-performance-optimiser` (5 skills) | `market-emails` — 4 complete sequence templates with full copy | **Parity** — skill-os has broader coverage, zubair has deeper copy |
| Social media | `social-content-calendar-manager`, `social-listening-analyst`, `influencer-coordination-manager`, `ugc-programme-designer` (4 skills) | `market-social` — 30-day calendar with platform-specific hooks | **Parity** — different strengths |
| Ad campaigns | No dedicated skill | `market-ads` — Google/Meta/LinkedIn/TikTok/Twitter with retargeting funnels | **skill-os gap**: no ad campaign skill |
| Funnel optimization | No dedicated skill | `market-funnel` — page-by-page 5-dimension CRO scoring | **skill-os gap**: no funnel analysis |
| Competitive intel | No dedicated marketing CI | `market-competitors` — SWOT, positioning maps, switching narratives | **Partial gap** — skill-os has `competitive-response-monitor-pmm` but it's PMM-scoped, not marketing-wide |
| Landing page CRO | No dedicated skill | `market-landing` — 7-point CRO framework with section weights | **skill-os gap**: no landing page analysis |
| Launch playbook | No dedicated marketing launch | `market-launch` — 8-week timeline, day-by-day launch week | **Partial gap** — skill-os has `launch-plan-owner` under PMM but it's strategy, not tactical execution |
| SEO audit | No dedicated skill | `market-seo` — 11-step audit with E-E-A-T, Core Web Vitals | **skill-os gap**: no SEO skill |
| Brand voice | No dedicated skill | `market-brand` — 4 voice dimensions, 5 archetypes, messaging hierarchy | **skill-os gap**: no brand voice analysis |
| Client proposals | No dedicated marketing proposal | `market-proposal` — 11-section proposal with 3-tier pricing | **Partial gap** — skill-os has `enablement-brief-writer` but not a full proposal generator |
| PDF reports | No | `market-report-pdf` — branded PDF with charts | N/A — presentation layer |
| PR/comms | `press-release-writer`, `crisis-communications-planner`, `media-relationship-builder`, `thought-leadership-programme-runner`, `earned-media-monitor` (5 skills) | No | **zubair gap** |
| MarOps | `martech-stack-manager`, `lead-scoring-model-builder`, `campaign-analytics-reporter`, `marketing-attribution-modeller`, `email-deliverability-manager` (5 skills) | No | **zubair gap** |
| Events | 6 event marketing skills | No | **zubair gap** |
| Analyst relations | 5 analyst relations skills | No | **zubair gap** |
| Community | 5 community skills | No | **zubair gap** |
| DevRel | 7 developer relations skills | No | **zubair gap** |

**Marketing verdict**: skill-os has **3.9x more skills** (54 vs 14) with much broader departmental coverage (PR, events, community, DevRel, analyst relations — none of which zubair covers). But zubair has **7 capabilities skill-os completely lacks**: full audit orchestrator, copywriting, ad campaigns, funnel optimization, landing page CRO, SEO, and brand voice analysis. These are the most operationally valuable marketing skills.

---

### Sales

| Capability | skill-os (17 skills) | zubair (14 skills) | Gap |
|-----------|---------------------|-------------------|-----|
| Prospect analysis | No orchestrator | `sales-prospect` — 5 parallel agents, composite scoring | **skill-os gap**: no multi-agent prospect analysis |
| Company research | No dedicated skill | `sales-research` — 8 dimensions, revenue estimation | **skill-os gap**: no deep company research |
| Lead qualification | No dedicated skill | `sales-qualify` — BANT + MEDDIC with signal tables | **skill-os gap**: no formal qualification framework |
| Contact mapping | No dedicated skill | `sales-contacts` — buying committee, multi-threading | **skill-os gap**: no decision-maker intelligence |
| Cold outreach | No dedicated skill | `sales-outreach` — 5-email sequences with A/B variants | **skill-os gap**: no outreach sequence builder |
| Follow-up sequences | No dedicated skill | `sales-followup` — 5 scenario types with cadence matrix | **skill-os gap**: no follow-up sequences |
| Meeting prep | No dedicated skill | `sales-prep` — 11-section brief with cheat sheet | **skill-os gap**: no meeting prep |
| Proposals | No dedicated sales proposal | `sales-proposal` — 11-section with ROI math | **skill-os gap**: no proposal generator |
| Objection handling | `objection-handler-updater-sales` (1 skill) | `sales-objections` — 15 universal objections, dual framework | **zubair deeper** |
| ICP building | No dedicated skill | `sales-icp` — 6 dimensions, 100-point rubric, buyer personas | **skill-os gap**: no ICP builder |
| Competitive intel | No dedicated sales CI | `sales-competitors` — battle cards, switching cost matrix | **skill-os gap**: no sales-specific competitive intel |
| Pipeline report | No | `sales-report` — aggregate pipeline dashboard | N/A |
| Sales strategy | `sales-strategy-setter`, `pricing-finaliser-sales` | Embedded in orchestrator | **Parity** |
| Pipeline management | `pipeline-reviewer`, `forecast-submitter` (via sales-manager) | No dedicated pipeline management | **zubair gap** |
| Solutions engineering | `proof-of-concept-runner`, `technical-feasibility-for-sales` | No | **zubair gap** |
| Business development | `partner-activation-planner`, `partner-activation-executor` | No | **zubair gap** |
| Hiring/coaching | `sales-hiring-bar-setter`, `sales-coaching-provider` | No | **zubair gap** |

**Sales verdict**: skill-os has **17 vs 14 skills** but zubair's are vastly deeper. zubair covers the entire **deal execution lifecycle** (prospect → research → qualify → contact → outreach → follow-up → prep → proposal → objection handling → ICP) with scoring rubrics and output templates. skill-os covers **sales management and operations** (pipeline, forecasting, hiring, coaching, solutions engineering, partnerships) which zubair doesn't touch. **10 critical execution skills are missing from skill-os.**

---

### Legal

| Capability | skill-os (36 skills) | zubair (13 skills) | Gap |
|-----------|---------------------|-------------------|-----|
| Contract review | No orchestrator | `legal review` — 5 parallel agents, Contract Safety Score | **skill-os gap**: no multi-agent contract review |
| Risk analysis | No dedicated skill | `legal risks` — clause-by-clause 1-10 scoring, hidden risk detection | **skill-os gap**: no deep risk analysis |
| Contract comparison | No dedicated skill | `legal compare` — side-by-side diff with favorability analysis | **skill-os gap**: no contract comparison |
| Plain English translation | No dedicated skill | `legal plain` — 8th-grade reading level, 5 flag types | **skill-os gap**: no plain English translator |
| Counter-proposals | No dedicated skill | `legal negotiate` — 3-tier priorities, concession strategy | **skill-os gap**: no negotiation strategy |
| Missing protections | No dedicated skill | `legal missing` — 7 contract-type checklists, 17 universal protections | **skill-os gap**: no missing protections finder |
| NDA generation | No dedicated skill | `legal nda` — 4 NDA variants, 15 sections | **skill-os gap**: no NDA generator |
| ToS generation | No dedicated skill | `legal terms` — 16-section ToS with GDPR/CCPA compliance | **skill-os gap**: no ToS generator |
| Privacy policy | No dedicated skill | `legal privacy` — website scanning, 50+ detection items | **skill-os gap**: no privacy policy generator |
| Business agreements | No dedicated skill | `legal agreement` — 10 agreement types, 15-section structure | **skill-os gap**: no agreement generator |
| Compliance audit | No dedicated skill | `legal compliance` — 57 checks across 7 frameworks | **skill-os gap**: no compliance audit |
| Freelancer review | No dedicated skill | `legal freelancer` — 14 lenses, IRS 20-Factor test | **skill-os gap**: no freelancer-specific review |
| Entity formation | `entity-formation` (1 skill) | No | **Parity** |
| IP management | `ip-assignment`, `founder-equity-issuance` | No | **zubair gap** |
| Corporate governance | `bylaws-and-board-setup`, `83b-election-coordinator` | No | **zubair gap** |
| AI regulation | `ai-risk-assessor`, `ai-regulation-monitor` (via product-counsel) | No | **zubair gap** |
| Data protection | `data-processing-agreement-negotiator`, `privacy-impact-assessor` | No | **zubair gap** |
| Compliance programme | 5 security-compliance-programme-manager skills | No | **zubair gap** |

**Legal verdict**: skill-os has **2.8x more skills** (36 vs 13) covering corporate counsel, product counsel, and compliance programme management that zubair doesn't touch. But zubair has **12 contract-focused capabilities skill-os completely lacks**: full contract review orchestrator, risk analysis, comparison, plain English translation, negotiation, missing protections, NDA/ToS/privacy/agreement generation, compliance audit, and freelancer review. These are the most immediately useful legal skills for any company.

---

## Quality Comparison (Where Both Cover Similar Ground)

| Dimension | skill-os | zubair |
|-----------|---------|--------|
| **Depth per skill** | 500-1,500 words (by complexity tier) | 3,000-6,500 words |
| **Scoring rubrics** | Qualitative (anti-patterns with rationale) | Quantitative (weighted 0-100 composites with grade bands) |
| **Output templates** | Format described in Output section | Full markdown templates with every section pre-defined |
| **Multi-agent orchestration** | None — single-skill execution | 5-agent parallel architecture for flagship skills |
| **Cross-references** | Bidirectional related-skills | Cross-skill data flow (skills read each other's output files) |
| **Error handling** | Failure reporting (what went wrong, what to try next) | Graceful degradation (neutral scores for failed agents) |
| **Structural consistency** | 9 sections, enforced by validation | Ad-hoc — each skill invents its own structure |
| **Department ethos** | 15 profiles influencing agent behavior | None |
| **Platform support** | Platform-agnostic YAML + markdown | Claude-specific |
| **Breadth** | 495 skills across 16 departments | 14 skills in 1 department per repo |

---

## Specific Skills Missing from skill-os

### Must-Add (High Impact, No Coverage)

**Marketing** (7 skills to add):
1. `marketing-audit-orchestrator` — full-site marketing audit with multi-agent scoring
2. `copywriting-analyst` — website copy scoring, headline formulas, swipe file generation
3. `ad-campaign-builder` — Google/Meta/LinkedIn/TikTok ad creation with retargeting
4. `funnel-optimizer` — page-by-page CRO with 5-dimension scoring
5. `landing-page-auditor` — 7-point CRO framework with section weighting
6. `seo-auditor` — on-page, E-E-A-T, Core Web Vitals, content gaps, schema
7. `brand-voice-analyst` — voice dimensions, archetypes, messaging hierarchy

**Sales** (10 skills to add):
1. `prospect-analyst-orchestrator` — multi-agent prospect research and scoring
2. `company-researcher` — 8-dimension firmographic deep dive
3. `lead-qualifier` — BANT + MEDDIC from public signals
4. `decision-maker-mapper` — buying committee identification, multi-threading
5. `cold-outreach-builder` — 5-email sequences with A/B variants
6. `follow-up-sequence-builder` — 5 scenario types with cadence matrix
7. `meeting-prep-builder` — 11-section brief with cheat sheet
8. `sales-proposal-builder` — 11-section proposal with ROI math
9. `icp-builder` — 6-dimension ICP with 100-point scoring rubric
10. `sales-competitive-intel` — battle cards, switching costs, win/loss patterns

**Legal** (12 skills to add):
1. `contract-review-orchestrator` — multi-agent contract analysis with safety score
2. `contract-risk-analyst` — clause-by-clause scoring, hidden risk detection
3. `contract-comparator` — side-by-side diff with favorability analysis
4. `plain-english-translator` — legalese to 8th-grade reading level
5. `negotiation-strategist` — counter-proposals with concession strategy
6. `missing-protections-finder` — contract-type checklists, universal protections
7. `nda-generator` — 4 NDA variants with plain English annotations
8. `terms-of-service-generator` — GDPR/CCPA-compliant ToS from website scan
9. `privacy-policy-generator` — detection-based privacy policy creation
10. `business-agreement-generator` — 10 agreement types, 15-section structure
11. `compliance-auditor` — 57 checks across 7 regulatory frameworks
12. `freelancer-contract-reviewer` — 14 freelancer-specific analysis lenses

### Should-Add (Scoring/Template Enhancements to Existing Skills)

These aren't new skills but upgrades to existing ones:

1. Add **weighted scoring rubrics** to all assessment skills (zubair's 0-100 composites with grade bands are far superior to our qualitative assessments)
2. Add **full output templates** to high-use skills (zubair's templates are immediately usable; ours describe the format but don't provide the template)
3. Add **multi-agent orchestration patterns** for complex workflows spanning 3+ skills

---

## Recommendations

1. **Create a new feature spec** (`003-competitive-gap-skills`) to add the 29 missing skills identified above. These should be the highest-quality skills in the repo — matching or exceeding zubair's depth while maintaining skill-os's structural consistency.

2. **Adopt scoring rubrics broadly**. zubair's quantitative scoring (weighted composites, grade bands, signal tables) is genuinely better than our qualitative anti-patterns for any skill that evaluates or assesses. This aligns with US7 in the `002-skill-quality-improvements` spec.

3. **Design orchestration patterns**. zubair's 5-agent parallel architecture for flagship skills (audit, review, prospect) is a proven pattern. skill-os should define a standard orchestration pattern for multi-skill workflows.

4. **Don't try to match depth per skill**. zubair's skills are 4,000-6,500 words — effectively full agent prompts. skill-os's value is breadth (495 skills) + consistency (9-section format) + organizational context (ethos, seniority). Keep skills lean and use `references/` for the depth that zubair puts inline.

5. **Prioritize the 29 new skills by department**: Legal (12) has the most gaps and the most immediate business value. Sales (10) closes the deal execution lifecycle. Marketing (7) adds the most commonly requested capabilities.
