# Framework: Developer Experience (DX) Standards

Reference for measuring, improving, and sustaining developer experience across tooling, onboarding, feedback loops, and golden paths.

## DX Quality Dimensions (SPACE Framework)

The SPACE framework measures developer productivity and experience across five dimensions:

| Dimension | What It Measures | Key Metrics |
|-----------|-----------------|-------------|
| **S**atisfaction | Developer wellbeing and engagement | eNPS, survey scores, tool satisfaction ratings |
| **P**erformance | Quality and impact of output | Defect escape rate, customer-reported bugs, deployment success rate |
| **A**ctivity | Volume of completed tasks | PRs merged, deploys, builds, test runs |
| **C**ommunication | Collaboration and knowledge sharing | PR review turnaround, documentation freshness, pair programming rate |
| **E**fficiency | Ability to work without friction and interruption | Build time, CI wait time, local setup time, context-switch events |

**Measurement rule**: Never use Activity alone as a proxy for productivity. Use at minimum one metric from Satisfaction, Efficiency, and Performance together.

## Key DX Metrics Catalog

### Build and CI Metrics

| Metric | Benchmark | Good | Needs Work | Critical |
|--------|-----------|------|-----------|---------|
| Local build time | Industry: 30–90s | < 60s | 60–180s | > 3 min |
| CI pipeline duration (PR feedback) | Industry: 5–15 min | < 10 min | 10–20 min | > 20 min |
| CI queue wait time | Industry: 0–3 min | < 2 min | 2–10 min | > 10 min |
| Flaky test rate | Industry: < 1% | < 0.5% | 0.5–2% | > 2% |
| Build success rate | Industry: 90–95% | ≥ 95% | 85–95% | < 85% |

### Onboarding Metrics

| Metric | Target | How to Measure |
|--------|--------|---------------|
| Time to first commit | ≤ 1 day | Onboarding survey + git log |
| Time to first production deployment | ≤ 2 weeks | Deploy log timestamps |
| Onboarding satisfaction score | ≥ 4.0/5.0 | 30-day new hire survey |
| Documentation completeness | 100% of critical paths | Onboarding checklist completion rate |
| "First stuck" event time | ≥ 4 hours without blocker | Onboarding buddy check-in cadence |

### Developer Toil Metrics

| Toil Category | Measurement | Target |
|--------------|-------------|--------|
| Manual environment setup steps | Count per onboarding | 0 (fully automated) |
| Manual deployment steps | Count per deploy | 0 (fully automated) |
| Context switches per day (unplanned) | Survey | < 3/day |
| Flaky test investigation time | Hours/week per engineer | < 30 min/week |
| Meeting overhead | % of working hours | < 20% |

## Developer Journey Stages

Map interventions to the stage where friction occurs:

| Stage | Description | Common Friction Points | Platform Interventions |
|-------|-------------|----------------------|----------------------|
| Discover | Finding the right tool/service/doc | Fragmented documentation, no service catalog | Internal developer portal, searchable service catalog |
| Onboard | Setting up the environment | Manual steps, stale README, broken setup scripts | Automated dev environment (Devcontainers, Nix), golden path CLI |
| Develop | Writing and testing code | Slow builds, poor IDE integration, missing scaffolding | Template repositories, fast local builds, dev proxy |
| Integrate | Merging and reviewing code | Slow CI, flaky tests, unclear PR requirements | Fast CI, quality gates, PR templates |
| Deploy | Releasing to production | Manual release steps, unclear deploy status | Automated CD, deployment observability |
| Operate | Monitoring and debugging in production | Missing runbooks, poor log UX, alert noise | Developer-facing dashboards, pre-built runbooks |

## DX Improvement Prioritization Matrix

| Issue | Frequency | Impact per Occurrence | Priority |
|-------|-----------|----------------------|----------|
| [Slow CI (> 20 min)] | [X times/day × N engineers] | [Breaks flow state] | [P1] |
| [Broken local setup script] | [Every new hire] | [1–2 days lost] | [P1] |
| [Flaky tests] | [X times/week] | [15–30 min investigation] | [P2] |
| [No standard PR template] | [Every PR] | [5 min cognitive overhead] | [P3] |

**Scoring**: Priority = Frequency × Impact. Fix P1s before building new features.

## Developer Survey Cadence

| Survey Type | Frequency | Length | Audience | Key Questions |
|------------|-----------|--------|----------|--------------|
| Developer NPS (eNPS) | Quarterly | 2 questions | All engineers | "How likely are you to recommend working here?" + open follow-up |
| Tooling satisfaction | Quarterly | 10–15 questions | All engineers | Rate each tool 1–5; identify top 3 friction points |
| Onboarding experience | At 30 days | 8–10 questions | New engineers | Time to first commit, first blocker, documentation quality |
| DX incident review | After each major DX incident | 5 questions | Affected engineers | What happened, how long it blocked, what would prevent it |

## Golden Path Compliance Metrics

Track adoption of platform-provided golden paths:

| Golden Path Component | Adoption Target | Measurement |
|----------------------|----------------|-------------|
| Template repositories (new services) | 100% of new services | % of repos created from template |
| Automated dev environment | ≥ 80% of engineers | % using Devcontainer or platform tooling |
| Standard CI/CD pipeline | 100% of services | % of services using platform CI template |
| Centralized secrets management | 100% | % of services with zero hardcoded secrets |
| Internal service catalog registration | 100% | % of production services in catalog |

## Anti-Patterns to Monitor

| Anti-Pattern | Signal | Remediation |
|-------------|--------|------------|
| "Just works on my machine" | Onboarding issues > 1/quarter | Reproduce + fix dev environment setup |
| Shadow tooling | Engineers using non-standard tools not in catalog | Acknowledge the need; either adopt or provide equivalent |
| Documentation debt | Stale docs reported > 1/month | Rotate doc ownership; add doc freshness checks |
| Alert fatigue | Engineers ignoring alerts | Audit alert signal-to-noise; tune or eliminate low-signal alerts |
| Platform abandonment | Engineers manually bypassing golden paths | Conduct DX interviews; remove friction in golden path |
