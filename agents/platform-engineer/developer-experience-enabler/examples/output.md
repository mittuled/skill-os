# Developer Experience Assessment — Meridian AI Engineering

| Field | Value |
|---|---|
| Team | Meridian AI Engineering |
| Team Size | 14 engineers |
| DX Score | 58/100 |
| Grade | C |
| Verdict | ACCEPTABLE_DX |
| High-Friction Areas | 3 (CI speed, deployment self-service, docs) |
| Estimated Productivity Drag | ~13% |
| Skill | developer-experience-enabler |

## DX Dimension Scores

| Dimension | Score | Weight | Weighted | Benchmark | Severity |
|---|---|---|---|---|---|
| Onboarding Speed | 5/10 | 20 | 10 | <1 day | MEDIUM |
| Local Dev Parity | 7/10 | 15 | 11 | >90% parity | LOW |
| Build & Test Speed | 3/10 | 20 | **6** | <10 min CI | **HIGH** |
| Deployment Self-Service | 4/10 | 20 | **8** | Fully self-service | **HIGH** |
| Docs Discoverability | 4/10 | 10 | **4** | Findable in <5 min | **HIGH** |
| Tooling Satisfaction | 6/10 | 15 | 9 | >7/10 satisfaction | MEDIUM |
| **Total** | | **100** | **48** | | |

## High-Friction Areas

### Build & Test Speed — HIGH (3/10)
**Problem:** 15-minute CI baseline plus 5-10 minutes of flaky test reruns = 20-25 minutes per PR cycle. At 14 engineers, this creates a constant throughput bottleneck.

**Estimated impact:** At 5 PRs/engineer/week × 14 engineers, 70 PRs/week × 20 min wait = **23 hours of lost engineering time per week.**

**Improvements:**
1. **Parallelize CI jobs** — Run test suites in parallel across multiple GitHub Actions runners (GitHub Actions matrix strategy)
2. **Split test suites** — Separate unit tests (<3 min) from integration tests; run unit tests on every PR, integration tests only on main merge
3. **Cache dependencies** — Ensure node_modules / pip packages are cached in GitHub Actions
4. **Fix flaky tests** — Identify top 5 flaky tests by failure rate; fix or quarantine. Target: eliminate reruns within 2 sprints.
5. **Target:** <8 minutes CI time

### Deployment Self-Service — HIGH (4/10)
**Problem:** Every staging deploy requires a Slack message to the platform team. This creates a platform team bottleneck and forces engineers to context-switch.

**Improvements:**
1. **Expose ArgoCD self-service** — Grant engineers ArgoCD UI access for staging namespace with commit-triggered deploys
2. **GitOps trigger:** Any merge to `develop` branch auto-deploys to staging via ArgoCD (no manual step)
3. **Slack command fallback:** `/deploy [service] staging [branch]` Slack command via GitHub Actions webhook
4. **Target:** Engineers deploy to staging without platform team involvement

### Docs Discoverability — HIGH (4/10)
**Problem:** Docs are split across Notion, Confluence (legacy), and GitHub wikis. Engineers can't find runbooks. New hire onboarding checklist is 3 months outdated.

**Improvements:**
1. **Single source of truth:** Migrate all docs to Notion (or adopt Backstage TechDocs). Archive Confluence and GitHub wikis.
2. **Tag all runbooks** consistently: service name, domain, alert name
3. **Update onboarding checklist** this sprint
4. **Add local Redis setup doc** to developer setup guide
5. **Create doc-finding convention:** `/docs [search term]` Slack command via Notion API

## Pain Points Summary

| Pain Point | Priority | Effort | Impact |
|---|---|---|---|
| 15-min CI killing PR velocity | P0 | Medium | HIGH — 23 hrs/week lost |
| No self-service staging deploys | P0 | Low | HIGH — platform team bottleneck |
| Runbooks not findable | P1 | Low | MEDIUM — incident response risk |
| Onboarding checklist outdated | P1 | Low | MEDIUM — 3-day onboarding instead of 1 |
| Local Redis undocumented | P2 | Low | LOW — affects new hires |

## Q2 DX Improvement Plan

| Week | Action | Owner | Expected DX Gain |
|---|---|---|---|
| 1-2 | Grant ArgoCD staging access + GitOps auto-deploy | Platform | +3 pts deployment |
| 1-2 | Update onboarding checklist + add Redis setup doc | Platform | +2 pts onboarding |
| 2-4 | Parallelize CI + cache dependencies | Platform + Backend | +3 pts CI speed |
| 3-4 | Identify and fix top 5 flaky tests | All teams | +2 pts CI speed |
| 3-5 | Consolidate docs to single source (Notion) | Platform + Tech Lead | +3 pts docs |

**Projected score after Q2 improvements: ~73/100 (B — Good DX)**
