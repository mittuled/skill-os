# Project Scaffold Specification

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Tech Architect name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | tech-scaffolder |
| Service Name | [Repository / service name] |
| Service Type | [REST API / Worker / Frontend / Library] |
| Target Runtime | [Node 20 / Python 3.12 / Go 1.22 / etc.] |
| Deployment Target | [Kubernetes / Lambda / Vercel / ECS] |

## Executive Summary

[2–3 sentences covering the service's purpose, the chosen stack, and the handoff state of the scaffold.

GUIDANCE: Good — "The notification-worker scaffold is a Go 1.22 event-driven service deployed on Kubernetes, preconfigured with structured logging, SQS consumer, and a green CI pipeline. Engineers can begin feature development immediately after `git clone && make run`." Bad — "We set up the project with all the standard things."]

## Stack Decisions

| Concern | Choice | Rationale |
|---------|--------|-----------|
| Language | [Language + version] | [Why this language for this service] |
| Web / Queue framework | [Framework] | [Why this framework] |
| Database / Storage | [Database + ORM/driver] | [Why this database] |
| Test framework | [Framework] | [Why this test framework] |
| CI/CD platform | [GitHub Actions / GitLab CI / etc.] | [Why this platform] |
| Container base image | [image:tag] | [Why this base image] |

GUIDANCE: Good — "PostgreSQL 16 with `sqlc` for type-safe query generation; chosen over an ORM to keep query performance visible." Bad — "Postgres because that's what we use."

## Directory Structure

```
[Paste the actual directory tree output from `tree -L 3` or equivalent]
```

GUIDANCE: Every top-level directory must have an inline comment explaining its purpose. Reviewers should be able to understand the structure without reading code.

## Foundational Code Inventory

| Component | File Path | Status | Notes |
|-----------|-----------|--------|-------|
| Entry point | [path] | [ ] Complete | [Any caveats] |
| Health check | [path] | [ ] Complete | [Endpoint: GET /health] |
| Structured logging | [path] | [ ] Complete | [Library: ...] |
| Config loading | [path] | [ ] Complete | [Required env vars: ...] |
| Sample passing test | [path] | [ ] Complete | [Run: make test] |
| Graceful shutdown | [path] | [ ] Complete | [Handles: SIGTERM] |

## CI/CD Configuration

| Pipeline Stage | Tool | Config File | Status |
|----------------|------|-------------|--------|
| Lint | [tool] | [path] | [ ] Green |
| Type check | [tool or N/A] | [path] | [ ] Green |
| Unit tests | [tool] | [path] | [ ] Green |
| Build | [tool] | [path] | [ ] Green |
| Integration tests | [tool] | [path] | [ ] Green |

GUIDANCE: Every stage must be green before the scaffold is handed off. A scaffold with a red CI is not a scaffold — it's a starting point for debugging.

## Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `PORT` | Yes | `8080` | HTTP server port |
| `LOG_LEVEL` | No | `info` | Logging verbosity (debug/info/warn/error) |
| `DATABASE_URL` | Yes | None | PostgreSQL connection string |
| [Add all required vars] | | | |

GUIDANCE: The app must fail fast with a clear error message if a required variable is absent. Include a `.env.example` file with placeholder values for every variable.

## Architecture Decision Record

[ADR 001 covering the scaffold decisions — follow template at `references/framework.md`]

## Recommendations

**P1 — Before first feature development begins:**
- [ ] Verify CI is green on main branch
- [ ] Confirm health check responds in staging environment
- [ ] Share scaffold with first developer for 30-minute orientation

**P2 — Within first sprint:**
- [ ] Add integration test for the first business endpoint
- [ ] Configure branch protection rules on the repository

**P3 — Before first production deployment:**
- [ ] Add production Dockerfile optimised for image size
- [ ] Configure secret scanning in CI pipeline

## Appendices

### A. Methodology

Scaffold created using `tech-scaffolder` skill. Directory patterns sourced from `references/framework.md`. All tooling versions pinned; see lockfiles for exact versions.

### B. Getting Started

```bash
# Clone and install
git clone <repo-url>
cd <service-name>
make install

# Run locally
make run

# Run tests
make test

# Run linter
make lint
```
