# Framework: Golden Path Definition Standards

Reference for defining, documenting, and maintaining golden paths — the opinionated, supported routes for common development tasks.

## Golden Path Principles

A golden path is not a mandate, but it must be the path of least resistance:

| Principle | Description | Anti-Pattern |
|-----------|-------------|-------------|
| Opinionated | One obvious choice per problem | Presenting 5 equally-valid options with no guidance |
| Self-service | Usable without platform team intervention | Requiring a Jira ticket to create a new service |
| Batteries-included | Works end-to-end for the target use case out of the box | Missing monitoring, CI, or secrets management by default |
| Paved, not required | Teams can deviate with a documented RFC process | Mandating use and blocking non-compliant teams |
| Maintained | Platform team owns updates; users get improvements automatically | Golden paths that drift stale within 6 months |

## Golden Path Catalog Structure

Each golden path entry must include:

| Field | Description | Example |
|-------|-------------|---------|
| Path name | Short descriptive name | `new-http-service` |
| Purpose | What problem it solves | Bootstrapping a production-ready REST API service |
| Target user | Who it is designed for | Backend engineers creating a new microservice |
| Scope | What it includes end-to-end | Repo, CI/CD, monitoring, secrets, service catalog registration |
| Entrypoint | How to invoke it | `platform create service --template http` |
| Documentation | Link to full guide | Internal developer portal path |
| Owner | Platform team responsible | Platform Engineering |
| SLA | Response time for golden path issues | 1 business day |
| Last updated | Date of last meaningful update | [YYYY-MM-DD] |

## Standard Golden Paths (Coverage Checklist)

The following golden paths should exist in any mature platform:

### Service Creation

| Path | Status | Maturity |
|------|--------|---------|
| New HTTP/REST service | [Exists / Planned / Not started] | [GA / Beta / Alpha] |
| New async worker / job | [Exists / Planned / Not started] | |
| New event-driven consumer | [Exists / Planned / Not started] | |
| New frontend / SPA | [Exists / Planned / Not started] | |
| New data pipeline | [Exists / Planned / Not started] | |
| New ML model service | [Exists / Planned / Not started] | |

### Development Workflow

| Path | Status | Maturity |
|------|--------|---------|
| Local development environment setup | [Exists / Planned] | |
| CI/CD pipeline | [Exists / Planned] | |
| Secret management | [Exists / Planned] | |
| Feature flagging | [Exists / Planned] | |
| Database migrations | [Exists / Planned] | |
| Distributed tracing instrumentation | [Exists / Planned] | |

### Operations

| Path | Status | Maturity |
|------|--------|---------|
| Service observability (logs, metrics, traces) | [Exists / Planned] | |
| Alerting and on-call setup | [Exists / Planned] | |
| Runbook creation | [Exists / Planned] | |
| Incident response | [Exists / Planned] | |
| Service catalog registration | [Exists / Planned] | |

## Golden Path Maturity Model

| Level | Label | Criteria |
|-------|-------|---------|
| L0 | Not started | No golden path exists; teams do this ad-hoc |
| L1 | Alpha | Works for at least one team; not production-hardened |
| L2 | Beta | Used by 3+ teams; known gaps exist; maintained |
| L3 | GA | Used by majority of teams; comprehensive docs; SLA defined |
| L4 | Managed | Automated health checks; auto-updated dependencies; DX metrics tracked |

**Target**: All core golden paths at L3+ within 2 platform quarters.

## Deviation Process

Teams that cannot use a golden path must follow this process:

1. **Document**: Record the reason for deviation in the team's ADR or tech doc.
2. **Notify**: Inform the platform team via the platform RFC channel.
3. **Assess**: Platform team responds within 1 business day with one of:
   - "Valid deviation — adopt as exception" (team maintains their solution)
   - "We can adapt the golden path to support this" (platform adds support)
   - "This should block — use the golden path" (with specific rationale)
4. **Review**: Deviations reviewed quarterly; valid ones may feed future golden path updates.

**Deviation tracking**: Maintain a deviation register. High deviation rates signal a golden path that does not meet real needs.

## Golden Path Health Metrics

| Metric | Target | Measurement |
|--------|--------|------------|
| Adoption rate (new services using path) | ≥ 80% | % of new services created from golden path template |
| Time to create new service (via path) | < 30 minutes | Measure from `platform create` to first PR up |
| Deviation rate | < 20% | % of applicable use cases using non-standard approach |
| Golden path issue response time | < 1 business day | Time from issue filed to first platform team response |
| Documentation freshness | < 90 days since last review | Last-reviewed date in each path's docs |
| User satisfaction score | ≥ 4.0/5.0 | Quarterly DX survey question on golden paths |

## Golden Path Review Cadence

| Activity | Frequency | Owner |
|----------|-----------|-------|
| Dependency version updates | Monthly (automated) | Platform |
| Security patch validation | On CVE notification | Platform |
| Functionality review (docs + accuracy) | Quarterly | Platform |
| User feedback synthesis (survey + issues) | Quarterly | Platform |
| Deprecation assessment | Semi-annually | Platform |

## Deprecation Protocol

When a golden path is deprecated:

1. Announce deprecation 90 days in advance in the developer portal.
2. Notify all teams currently using the path directly.
3. Provide a migration guide to the replacement path.
4. Keep the deprecated path functional until the migration deadline.
5. Remove only after 100% of teams have migrated or filed documented exceptions.
