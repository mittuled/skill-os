# Deployment Automation Design

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Agent role / engineer name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | deployment-automation |
| Service | [Service name] |
| Environment | [staging / production] |

## Executive Summary

[2-3 sentences summarizing what is being automated, the current manual pain points being eliminated, and the deployment strategy chosen.
GUIDANCE: Lead with the impact — "Eliminates 12 manual deployment steps reducing error risk and cutting deploy time from 45 minutes to 8 minutes." Do not describe the methodology before the outcome.]

## Current State: Deployment Map

[Document every manual step in the current deployment process.

GUIDANCE:
- Good: "Step 7: Engineer SSH into prod-app-01, runs `./deploy.sh v1.2.3`, waits 5 minutes, verifies health manually via curl"
- Bad: "Deploy the application to production"
- Format: Numbered list with: step number, action, actor (human or system), time estimate, failure mode
- Flag each step as: Automatable | Requires human judgment | Compliance gate]

| Step | Action | Actor | Time | Failure Mode | Automation Candidate |
|------|--------|-------|------|--------------|---------------------|
| 1 | [action] | [human/system] | [Xmin] | [failure mode] | [Yes/No/Gate] |

## Strategy Selection

**Selected Strategy**: [Blue-Green / Canary / Rolling Update / Feature Flag]

**Rationale**: [1-2 sentences explaining why this strategy fits the service characteristics (stateful/stateless, traffic volume, rollback requirements). Reference the framework at `references/framework.md`.]

**Infrastructure Requirements**: [List any new infrastructure needed: load balancer rules, Kubernetes controllers, feature flag platform configuration]

## Automated Pipeline Configuration

[Define each pipeline stage with its inputs, actions, and pass/fail criteria.

GUIDANCE:
- Good: "Stage: Pre-deploy gates — runs terraform plan, artifact SHA validation, dependency health probe. Fails if drift detected or any probe returns non-200."
- Bad: "Stage: Validate"
- Format: Table with stage name, tool, trigger condition, pass criteria, failure action]

| Stage | Tool | Trigger | Pass Criteria | Failure Action |
|-------|------|---------|---------------|----------------|
| Pre-deploy gates | Terraform + health probes | Pipeline start | Zero drift, all probes healthy | Block |
| Deploy | [ArgoCD / Helm / Ansible] | Gates passed | Health check green within 2 min | Auto-rollback |
| Post-deploy validation | Smoke test suite | Deploy complete | 100% critical paths pass within 10 min bake | Auto-rollback |
| Notify | Slack webhook | Pipeline complete | — | — |

## Health Check Configuration

[Define readiness, liveness, and startup probe settings for this service.

GUIDANCE:
- Good: "Readiness: GET /healthz, checks PostgreSQL connectivity and Redis availability, 200 = ready. initialDelaySeconds: 15, periodSeconds: 5, failureThreshold: 3"
- Bad: "Health check endpoint: /healthz"]

## Human Gate Policy

[List the deployment types for this service that require human approval and specify the approval mechanism.

GUIDANCE:
- Good: "Database schema migrations: require approval from the DBA and the lead engineer via Slack approval workflow before proceeding. Timeout: 4 hours, then auto-block."
- Bad: "Migrations require approval"]

## Recommendations

[Prioritized list of automation gaps and improvements.

GUIDANCE: Each item should be specific and actionable.
- P1: [Action to eliminate the riskiest remaining manual step, assigned to a specific team]
- P2: [Enhancement to reduce bake time or add a missing validation gate]
- P3: [Optimization to improve pipeline speed or reduce noise]]

## Appendices

### A. Rollback Procedure

[How to trigger rollback for this service: command, expected time to revert, validation steps post-rollback]

### B. Pipeline Metrics Baseline

[Current deployment frequency, lead time, MTTR, and change failure rate (DORA metrics) before automation. Use as before/after comparison once automation is live.]
