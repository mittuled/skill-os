# CI/CD Pipeline Configuration: [Service Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | DevOps / Infrastructure Engineer |
| Service | [Service name and team] |
| Platform | [GitHub Actions / GitLab CI / CircleCI / Jenkins] |
| Skill | ci-cd-pipeline-builder |
| Version | [1.0] |
| Status | [Draft / Active] |

## Pipeline Overview

**Pipeline type**: [Trunk-based / Feature-branch / GitFlow]
**Deployment targets**: [dev → staging → production]
**Average pipeline duration (target)**: [< X minutes]
**On-call for pipeline failures**: [Role / Team]

## Stage Definitions

### Stage 1: Build

| Step | Tool | Trigger | Pass Criteria | Fail Action |
|------|------|---------|--------------|-------------|
| Dependency install | [npm ci / pip install / go mod] | Every push | Exit code 0 | Fail fast |
| Compile / Transpile | [tsc / webpack / go build] | Every push | Exit code 0 | Fail fast |
| Docker build | [Docker buildx] | Every push | Image built, no layer errors | Fail fast |
| Artifact upload | [Registry / S3] | Main branch + tags | Artifact URL returned | Fail fast |

**Target duration**: [< 3 min]
**Caching**: [node_modules / Go module cache / pip cache] keyed on [lock file hash]

### Stage 2: Test

| Step | Tool | Scope | Pass Criteria | Fail Action |
|------|------|-------|--------------|-------------|
| Unit tests | [Jest / pytest / go test] | All | 100% pass, ≥ 80% coverage | Fail fast |
| Integration tests | [Supertest / httpx / testcontainers] | API contracts | 100% pass | Fail fast |
| Lint | [ESLint / ruff / golangci-lint] | Changed files | 0 errors, 0 warnings | Fail fast |
| Type check | [tsc / mypy] | All | 0 type errors | Fail fast |
| SAST scan | [Semgrep / Snyk / CodeQL] | All | 0 Critical/High findings | Fail fast |
| Dependency audit | [npm audit / pip-audit / govulncheck] | lock file | 0 Critical/High CVEs | Fail fast |

**Target duration**: [< 8 min]
**Parallelism**: [Unit + Lint run in parallel; Integration after unit pass]

### Stage 3: Review Gate (PRs only)

| Check | Required | Auto-pass Condition |
|-------|----------|---------------------|
| Build passes | Yes | Stage 1 green |
| All tests pass | Yes | Stage 2 green |
| Coverage ≥ 80% | Yes | Coverage report artifact |
| No new SAST findings | Yes | Semgrep baseline comparison |
| PR description complete | Recommended | Template filled |
| 1+ approving review | Yes (main branch) | GitHub review approval |

### Stage 4: Staging Deploy

| Step | Tool | Trigger | Rollback Trigger |
|------|------|---------|-----------------|
| Database migration | [Flyway / Alembic / Liquibase] | Auto on merge to main | Schema rollback script |
| Deploy to staging | [ArgoCD / Helm / kubectl] | Auto on merge to main | Previous Helm release |
| Smoke test | [k6 / Playwright / curl] | Post-deploy | Auto-rollback if fail |
| Synthetic monitoring check | [Datadog / Checkly] | Post-deploy (5 min soak) | Page on-call if fail |

**Target duration**: [< 5 min]
**Environment parity**: staging mirrors production [Yes / No — list deltas]

### Stage 5: Production Deploy

| Step | Tool | Trigger | Rollback Trigger |
|------|------|---------|-----------------|
| Approval gate | [GitHub Environment / Jira workflow] | Manual — release manager | n/a |
| Pre-deploy backup | [DB snapshot / config export] | Auto pre-deploy | If migration fails |
| Canary deploy | [ArgoCD Rollout / Flagger] | Auto post-approval | Error rate or latency spike |
| Progressive traffic shift | [5% → 25% → 50% → 100%] | Automated | Rollback metric breach |
| Post-deploy validation | [Smoke tests + SLO check] | Auto at 100% | Rollback if SLO breached |

**Canary bake time**: [30 min at each stage]
**Rollback SLO**: [< 5 min MTTR target]

## Environment Variables and Secrets

| Variable | Source | Used In Stages | Rotation |
|----------|--------|---------------|----------|
| DATABASE_URL | [Vault / AWS Secrets Manager] | 4, 5 | [90 days] |
| API_KEY_[SERVICE] | [Vault] | 4, 5 | [30 days] |
| SENTRY_DSN | [Vault] | 4, 5 | [N/A — public endpoint] |

**Secret access pattern**: Secrets injected at runtime via [tool]; never stored in CI environment variables.

## Pipeline Health Metrics

| Metric | Target | Alert Threshold |
|--------|--------|----------------|
| Build success rate | ≥ 95% | < 90% over 24h |
| Mean pipeline duration | < [X] min | > [X+3] min p90 |
| MTTR for broken builds | < 30 min | > 2h |
| Deployment frequency | ≥ [1/day] | < [1/week] |
| Change failure rate | < 5% | > 10% over 7d |

## Failure Runbook

| Failure | First Action | Escalation |
|---------|-------------|-----------|
| Build fails on dependency install | Check lock file and registry status | Escalate to [team] if registry outage |
| SAST scan finds new Critical | Block merge; page security engineer | Security engineer assesses within 2h |
| Staging deploy fails | Check migration logs; verify image tag | Revert to last known-good image |
| Canary error rate spike | Auto-rollback triggers; verify in Datadog | Page on-call if auto-rollback fails |
| Production deploy frozen | Check ArgoCD sync status | Manual kubectl rollout undo |
