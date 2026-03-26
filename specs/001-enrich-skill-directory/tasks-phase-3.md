# Tasks — Phase 3: Engineering (100 skills, 12 agents)

**Input**: Design documents from `/specs/001-enrich-skill-directory/`
**Prerequisites**: Phase 0 + Phase 1 complete

**Goal**: Enrich the largest single department. Highest density of intra-department cross-references.

**Commit discipline**: Every skill = 1 commit. Format: `Enrich skill: <skill-slug> for <Agent Role>`

---

## Phase 3.0: Research & Ethos

- [ ] T218 Research engineering best practices — code review (Google eng practices), ADRs, system design, CI/CD pipeline design, IaC (Terraform/Pulumi), Kubernetes, observability (OpenTelemetry), incident response (PagerDuty patterns), OWASP top 10, STRIDE threat modeling, data engineering (dimensional modeling, streaming/Kafka), MLOps, test pyramid, platform engineering (DORA/SPACE), developer experience.
- [ ] T219 Write `departments/engineering/ideal-engineering.md` — ethos profile (max 500 words). 1 commit.

---

## Phase 3.1: VP Engineering (12 skills)

- [ ] T220 Enrich `engineering-roadmap-owner` — migrate + enrich at `agents/vp-engineering/engineering-roadmap-owner/SKILL.md` (complexity: complex). 1 commit.
- [ ] T221 Enrich `hiring-bar-setter` — migrate + enrich at `agents/vp-engineering/hiring-bar-setter/SKILL.md` (complexity: medium). 1 commit.
- [ ] T222 Enrich `architecture-review-chair` — migrate + enrich at `agents/vp-engineering/architecture-review-chair/SKILL.md` (complexity: complex). 1 commit.
- [ ] T223 Enrich `incident-commander-escalation` — migrate + enrich at `agents/vp-engineering/incident-commander-escalation/SKILL.md` (complexity: complex). 1 commit.
- [ ] T224 Enrich `tech-debt-budget-allocator` — migrate + enrich at `agents/vp-engineering/tech-debt-budget-allocator/SKILL.md` (complexity: complex). 1 commit.
- [ ] T225 Enrich `platform-investment-sponsor` — migrate + enrich at `agents/vp-engineering/platform-investment-sponsor/SKILL.md` (complexity: complex). 1 commit.
- [ ] T226 Enrich `engineering-culture-builder` — migrate + enrich at `agents/vp-engineering/engineering-culture-builder/SKILL.md` (complexity: medium). 1 commit.
- [ ] T227 Enrich `vendor-technical-evaluator` — migrate + enrich at `agents/vp-engineering/vendor-technical-evaluator/SKILL.md` (complexity: medium). 1 commit.
- [ ] T228 Enrich `security-posture-owner` — migrate + enrich at `agents/vp-engineering/security-posture-owner/SKILL.md` (complexity: complex). 1 commit.
- [ ] T229 Enrich `cross-functional-liaison` — migrate + enrich at `agents/vp-engineering/cross-functional-liaison/SKILL.md` (complexity: medium). 1 commit.
- [ ] T230 Enrich `engineering-metrics-reviewer` — migrate + enrich at `agents/vp-engineering/engineering-metrics-reviewer/SKILL.md` (complexity: medium). 1 commit.
- [ ] T231 Enrich `open-source-strategy-setter` — migrate + enrich at `agents/vp-engineering/open-source-strategy-setter/SKILL.md` (complexity: medium). 1 commit.

## Phase 3.2: Tech Architect (9 skills)

- [ ] T232 [P] Enrich `system-design-author` — migrate + enrich at `agents/tech-architect/system-design-author/SKILL.md` (complexity: complex). 1 commit.
- [ ] T233 [P] Enrich `adr-writer` — migrate + enrich at `agents/tech-architect/adr-writer/SKILL.md` (complexity: medium). 1 commit.
- [ ] T234 [P] Enrich `technology-radar-maintainer` — migrate + enrich at `agents/tech-architect/technology-radar-maintainer/SKILL.md` (complexity: medium). 1 commit.
- [ ] T235 [P] Enrich `scalability-reviewer` — migrate + enrich at `agents/tech-architect/scalability-reviewer/SKILL.md` (complexity: complex). 1 commit.
- [ ] T236 [P] Enrich `api-contract-designer` — migrate + enrich at `agents/tech-architect/api-contract-designer/SKILL.md` (complexity: complex). 1 commit.
- [ ] T237 [P] Enrich `data-architecture-advisor` — migrate + enrich at `agents/tech-architect/data-architecture-advisor/SKILL.md` (complexity: complex). 1 commit.
- [ ] T238 [P] Enrich `migration-planner` — migrate + enrich at `agents/tech-architect/migration-planner/SKILL.md` (complexity: complex). 1 commit.
- [ ] T239 [P] Enrich `proof-of-concept-builder` — migrate + enrich at `agents/tech-architect/proof-of-concept-builder/SKILL.md` (complexity: medium). 1 commit.
- [ ] T240 [P] Enrich `architecture-debt-identifier` — migrate + enrich at `agents/tech-architect/architecture-debt-identifier/SKILL.md` (complexity: medium). 1 commit.

## Phase 3.3: Tech Lead / PR Reviewer (12 skills)

- [ ] T241 [P] Enrich `code-reviewer` — migrate + enrich at `agents/tech-lead-pr-reviewer/code-reviewer/SKILL.md` (complexity: complex). 1 commit.
- [ ] T242 [P] Enrich `pr-merge-gatekeeper` — migrate + enrich at `agents/tech-lead-pr-reviewer/pr-merge-gatekeeper/SKILL.md` (complexity: medium). 1 commit.
- [ ] T243 [P] Enrich `coding-standards-enforcer` — migrate + enrich at `agents/tech-lead-pr-reviewer/coding-standards-enforcer/SKILL.md` (complexity: medium). 1 commit.
- [ ] T244 [P] Enrich `mentorship-provider` — migrate + enrich at `agents/tech-lead-pr-reviewer/mentorship-provider/SKILL.md` (complexity: medium). 1 commit.
- [ ] T245 [P] Enrich `sprint-technical-advisor` — migrate + enrich at `agents/tech-lead-pr-reviewer/sprint-technical-advisor/SKILL.md` (complexity: medium). 1 commit.
- [ ] T246 [P] Enrich `refactoring-champion` — migrate + enrich at `agents/tech-lead-pr-reviewer/refactoring-champion/SKILL.md` (complexity: medium). 1 commit.
- [ ] T247 [P] Enrich `dependency-update-reviewer` — migrate + enrich at `agents/tech-lead-pr-reviewer/dependency-update-reviewer/SKILL.md` (complexity: simple). 1 commit.
- [ ] T248 [P] Enrich `test-coverage-advocate` — migrate + enrich at `agents/tech-lead-pr-reviewer/test-coverage-advocate/SKILL.md` (complexity: medium). 1 commit.
- [ ] T249 [P] Enrich `documentation-enforcer` — migrate + enrich at `agents/tech-lead-pr-reviewer/documentation-enforcer/SKILL.md` (complexity: simple). 1 commit.
- [ ] T250 [P] Enrich `on-call-rotation-manager` — migrate + enrich at `agents/tech-lead-pr-reviewer/on-call-rotation-manager/SKILL.md` (complexity: medium). 1 commit.
- [ ] T251 [P] Enrich `technical-interview-lead` — migrate + enrich at `agents/tech-lead-pr-reviewer/technical-interview-lead/SKILL.md` (complexity: medium). 1 commit.
- [ ] T252 [P] Enrich `knowledge-sharing-facilitator` — migrate + enrich at `agents/tech-lead-pr-reviewer/knowledge-sharing-facilitator/SKILL.md` (complexity: simple). 1 commit.

## Phase 3.4: Database Expert (1 skill)

- [ ] T253 [P] Enrich `query-optimiser` — migrate + enrich at `agents/database-expert/query-optimiser/SKILL.md` (complexity: medium). 1 commit.

## Phase 3.5: Sr Frontend Developer (5 skills)

- [ ] T254 [P] Enrich `builder` — migrate + enrich at `agents/sr-frontend-developer/builder/SKILL.md` (complexity: medium). 1 commit.
- [ ] T255 [P] Enrich `component-library-contributor` — migrate + enrich at `agents/sr-frontend-developer/component-library-contributor/SKILL.md` (complexity: medium). 1 commit.
- [ ] T256 [P] Enrich `performance-optimiser` — migrate + enrich at `agents/sr-frontend-developer/performance-optimiser/SKILL.md` (complexity: medium). 1 commit.
- [ ] T257 [P] Enrich `accessibility-implementer` — migrate + enrich at `agents/sr-frontend-developer/accessibility-implementer/SKILL.md` (complexity: medium). 1 commit.
- [ ] T258 [P] Enrich `design-system-consumer` — migrate + enrich at `agents/sr-frontend-developer/design-system-consumer/SKILL.md` (complexity: simple). 1 commit.

## Phase 3.6: Sr Backend Developer (5 skills)

- [ ] T259 [P] Enrich `builder` — migrate + enrich at `agents/sr-backend-developer/builder/SKILL.md` (complexity: medium). 1 commit.
- [ ] T260 [P] Enrich `api-implementer` — migrate + enrich at `agents/sr-backend-developer/api-implementer/SKILL.md` (complexity: medium). 1 commit.
- [ ] T261 [P] Enrich `background-job-developer` — migrate + enrich at `agents/sr-backend-developer/background-job-developer/SKILL.md` (complexity: medium). 1 commit.
- [ ] T262 [P] Enrich `data-model-implementer` — migrate + enrich at `agents/sr-backend-developer/data-model-implementer/SKILL.md` (complexity: medium). 1 commit.
- [ ] T263 [P] Enrich `integration-connector-builder` — migrate + enrich at `agents/sr-backend-developer/integration-connector-builder/SKILL.md` (complexity: medium). 1 commit.

## Phase 3.7: QA / Test Engineer (8 skills)

- [ ] T264 [P] Enrich `test-plan-author` — migrate + enrich at `agents/qa-test-engineer/test-plan-author/SKILL.md` (complexity: complex). 1 commit.
- [ ] T265 [P] Enrich `automated-test-writer` — migrate + enrich at `agents/qa-test-engineer/automated-test-writer/SKILL.md` (complexity: medium). 1 commit.
- [ ] T266 [P] Enrich `regression-suite-maintainer` — migrate + enrich at `agents/qa-test-engineer/regression-suite-maintainer/SKILL.md` (complexity: medium). 1 commit.
- [ ] T267 [P] Enrich `exploratory-tester` — migrate + enrich at `agents/qa-test-engineer/exploratory-tester/SKILL.md` (complexity: medium). 1 commit.
- [ ] T268 [P] Enrich `performance-test-runner` — migrate + enrich at `agents/qa-test-engineer/performance-test-runner/SKILL.md` (complexity: medium). 1 commit.
- [ ] T269 [P] Enrich `bug-report-writer` — migrate + enrich at `agents/qa-test-engineer/bug-report-writer/SKILL.md` (complexity: simple). 1 commit.
- [ ] T270 [P] Enrich `test-environment-manager` — migrate + enrich at `agents/qa-test-engineer/test-environment-manager/SKILL.md` (complexity: medium). 1 commit.
- [ ] T271 [P] Enrich `release-sign-off-tester` — migrate + enrich at `agents/qa-test-engineer/release-sign-off-tester/SKILL.md` (complexity: medium). 1 commit.

## Phase 3.8: DevOps / Infrastructure Engineer (19 skills)

- [ ] T272 [P] Enrich `ci-pipeline-builder` — migrate + enrich at `agents/devops-infrastructure-engineer/ci-pipeline-builder/SKILL.md` (complexity: complex). 1 commit.
- [ ] T273 [P] Enrich `cd-pipeline-builder` — migrate + enrich at `agents/devops-infrastructure-engineer/cd-pipeline-builder/SKILL.md` (complexity: complex). 1 commit.
- [ ] T274 [P] Enrich `infrastructure-as-code-author` — migrate + enrich at `agents/devops-infrastructure-engineer/infrastructure-as-code-author/SKILL.md` (complexity: complex). 1 commit.
- [ ] T275 [P] Enrich `monitoring-alert-configurator` — migrate + enrich at `agents/devops-infrastructure-engineer/monitoring-alert-configurator/SKILL.md` (complexity: medium). 1 commit.
- [ ] T276 [P] Enrich `log-aggregation-manager` — migrate + enrich at `agents/devops-infrastructure-engineer/log-aggregation-manager/SKILL.md` (complexity: medium). 1 commit.
- [ ] T277 [P] Enrich `container-orchestration-operator` — migrate + enrich at `agents/devops-infrastructure-engineer/container-orchestration-operator/SKILL.md` (complexity: complex). 1 commit.
- [ ] T278 [P] Enrich `secret-manager` — migrate + enrich at `agents/devops-infrastructure-engineer/secret-manager/SKILL.md` (complexity: medium). 1 commit.
- [ ] T279 [P] Enrich `ssl-certificate-manager` — migrate + enrich at `agents/devops-infrastructure-engineer/ssl-certificate-manager/SKILL.md` (complexity: simple). 1 commit.
- [ ] T280 [P] Enrich `disaster-recovery-planner` — migrate + enrich at `agents/devops-infrastructure-engineer/disaster-recovery-planner/SKILL.md` (complexity: complex). 1 commit.
- [ ] T281 [P] Enrich `cost-optimiser` — migrate + enrich at `agents/devops-infrastructure-engineer/cost-optimiser/SKILL.md` (complexity: medium). 1 commit.
- [ ] T282 [P] Enrich `network-configuration-manager` — migrate + enrich at `agents/devops-infrastructure-engineer/network-configuration-manager/SKILL.md` (complexity: medium). 1 commit.
- [ ] T283 [P] Enrich `load-balancer-manager` — migrate + enrich at `agents/devops-infrastructure-engineer/load-balancer-manager/SKILL.md` (complexity: medium). 1 commit.
- [ ] T284 [P] Enrich `database-backup-operator` — migrate + enrich at `agents/devops-infrastructure-engineer/database-backup-operator/SKILL.md` (complexity: medium). 1 commit.
- [ ] T285 [P] Enrich `feature-flag-infrastructure-provider` — migrate + enrich at `agents/devops-infrastructure-engineer/feature-flag-infrastructure-provider/SKILL.md` (complexity: medium). 1 commit.
- [ ] T286 [P] Enrich `service-mesh-configurator` — migrate + enrich at `agents/devops-infrastructure-engineer/service-mesh-configurator/SKILL.md` (complexity: complex). 1 commit.
- [ ] T287 [P] Enrich `cdn-manager` — migrate + enrich at `agents/devops-infrastructure-engineer/cdn-manager/SKILL.md` (complexity: simple). 1 commit.
- [ ] T288 [P] Enrich `dns-manager` — migrate + enrich at `agents/devops-infrastructure-engineer/dns-manager/SKILL.md` (complexity: simple). 1 commit.
- [ ] T289 [P] Enrich `infrastructure-drift-detector` — migrate + enrich at `agents/devops-infrastructure-engineer/infrastructure-drift-detector/SKILL.md` (complexity: medium). 1 commit.
- [ ] T290 [P] Enrich `capacity-forecaster` — migrate + enrich at `agents/devops-infrastructure-engineer/capacity-forecaster/SKILL.md` (complexity: medium). 1 commit.

## Phase 3.9: Platform Engineer (5 skills)

- [ ] T291 [P] Enrich `developer-experience-toolsmith` — migrate + enrich at `agents/platform-engineer/developer-experience-toolsmith/SKILL.md` (complexity: complex). 1 commit.
- [ ] T292 [P] Enrich `internal-platform-builder` — migrate + enrich at `agents/platform-engineer/internal-platform-builder/SKILL.md` (complexity: complex). 1 commit.
- [ ] T293 [P] Enrich `self-service-provisioner` — migrate + enrich at `agents/platform-engineer/self-service-provisioner/SKILL.md` (complexity: medium). 1 commit.
- [ ] T294 [P] Enrich `shared-library-maintainer` — migrate + enrich at `agents/platform-engineer/shared-library-maintainer/SKILL.md` (complexity: medium). 1 commit.
- [ ] T295 [P] Enrich `platform-documentation-author` — migrate + enrich at `agents/platform-engineer/platform-documentation-author/SKILL.md` (complexity: simple). 1 commit.

## Phase 3.10: Data Engineer (7 skills)

- [ ] T296 [P] Enrich `etl-pipeline-builder` — migrate + enrich at `agents/data-engineer/etl-pipeline-builder/SKILL.md` (complexity: complex). 1 commit.
- [ ] T297 [P] Enrich `data-warehouse-architect` — migrate + enrich at `agents/data-engineer/data-warehouse-architect/SKILL.md` (complexity: complex). 1 commit.
- [ ] T298 [P] Enrich `data-quality-monitor` — migrate + enrich at `agents/data-engineer/data-quality-monitor/SKILL.md` (complexity: medium). 1 commit.
- [ ] T299 [P] Enrich `streaming-pipeline-developer` — migrate + enrich at `agents/data-engineer/streaming-pipeline-developer/SKILL.md` (complexity: complex). 1 commit.
- [ ] T300 [P] Enrich `data-catalogue-maintainer` — migrate + enrich at `agents/data-engineer/data-catalogue-maintainer/SKILL.md` (complexity: medium). 1 commit.
- [ ] T301 [P] Enrich `analytics-infrastructure-provider` — migrate + enrich at `agents/data-engineer/analytics-infrastructure-provider/SKILL.md` (complexity: medium). 1 commit.
- [ ] T302 [P] Enrich `data-retention-policy-implementer` — migrate + enrich at `agents/data-engineer/data-retention-policy-implementer/SKILL.md` (complexity: medium). 1 commit.

## Phase 3.11: Security Engineer (10 skills)

- [ ] T303 [P] Enrich `threat-modelling` — migrate + enrich at `agents/security-engineer/threat-modelling/SKILL.md` (complexity: complex). 1 commit.
- [ ] T304 [P] Enrich `vulnerability-scanner-operator` — migrate + enrich at `agents/security-engineer/vulnerability-scanner-operator/SKILL.md` (complexity: medium). 1 commit.
- [ ] T305 [P] Enrich `penetration-test-coordinator` — migrate + enrich at `agents/security-engineer/penetration-test-coordinator/SKILL.md` (complexity: complex). 1 commit.
- [ ] T306 [P] Enrich `security-incident-responder` — migrate + enrich at `agents/security-engineer/security-incident-responder/SKILL.md` (complexity: complex). 1 commit.
- [ ] T307 [P] Enrich `access-control-auditor` — migrate + enrich at `agents/security-engineer/access-control-auditor/SKILL.md` (complexity: medium). 1 commit.
- [ ] T308 [P] Enrich `dependency-vulnerability-monitor` — migrate + enrich at `agents/security-engineer/dependency-vulnerability-monitor/SKILL.md` (complexity: medium). 1 commit.
- [ ] T309 [P] Enrich `security-training-facilitator` — migrate + enrich at `agents/security-engineer/security-training-facilitator/SKILL.md` (complexity: simple). 1 commit.
- [ ] T310 [P] Enrich `compliance-evidence-collector` — migrate + enrich at `agents/security-engineer/compliance-evidence-collector/SKILL.md` (complexity: medium). 1 commit.
- [ ] T311 [P] Enrich `encryption-implementation-reviewer` — migrate + enrich at `agents/security-engineer/encryption-implementation-reviewer/SKILL.md` (complexity: medium). 1 commit.
- [ ] T312 [P] Enrich `security-tooling-maintainer` — migrate + enrich at `agents/security-engineer/security-tooling-maintainer/SKILL.md` (complexity: simple). 1 commit.

## Phase 3.12: AI / ML Engineer (7 skills)

- [ ] T313 [P] Enrich `model-trainer` — migrate + enrich at `agents/ai-ml-engineer/model-trainer/SKILL.md` (complexity: complex). 1 commit.
- [ ] T314 [P] Enrich `feature-store-maintainer` — migrate + enrich at `agents/ai-ml-engineer/feature-store-maintainer/SKILL.md` (complexity: medium). 1 commit.
- [ ] T315 [P] Enrich `model-deployment-engineer` — migrate + enrich at `agents/ai-ml-engineer/model-deployment-engineer/SKILL.md` (complexity: complex). 1 commit.
- [ ] T316 [P] Enrich `experiment-tracker` — migrate + enrich at `agents/ai-ml-engineer/experiment-tracker/SKILL.md` (complexity: medium). 1 commit.
- [ ] T317 [P] Enrich `data-labelling-pipeline-builder` — migrate + enrich at `agents/ai-ml-engineer/data-labelling-pipeline-builder/SKILL.md` (complexity: medium). 1 commit.
- [ ] T318 [P] Enrich `model-monitoring-configurator` — migrate + enrich at `agents/ai-ml-engineer/model-monitoring-configurator/SKILL.md` (complexity: medium). 1 commit.
- [ ] T319 [P] Enrich `ai-ethics-reviewer` — migrate + enrich at `agents/ai-ml-engineer/ai-ethics-reviewer/SKILL.md` (complexity: complex). 1 commit.

---

## Phase 3.13: Validate & Finalize

- [ ] T320 Run `python scripts/validate.py` for all Engineering agents — fix errors. 1 commit per fix.
- [ ] T321 Add cross-references: intra-Engineering (DevOps ↔ Security ↔ Platform ↔ QA), Engineering ↔ Product (handoffs), Engineering ↔ Design (handoffs). 1 commit per skill updated.
- [ ] T322 Update `status.md` — mark Engineering (100/100) complete. 1 commit.
- [ ] T323 Update `restructured-org-chart-v3.md` — reflect new paths for Engineering agents. 1 commit.

**Checkpoint**: Engineering complete. 278/472 skills enriched (59%).

---

## Task Count

| Section | Tasks | Skills |
|---------|-------|--------|
| Research & Ethos | 2 | — |
| 12 Engineering agents | 100 | 100 |
| Validate & Finalize | 4 | — |
| **Total** | **106** | **100** |
