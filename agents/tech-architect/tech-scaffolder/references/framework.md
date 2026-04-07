# Framework: tech-scaffolder

Defines the structural methodology for creating production-quality project scaffolds that teams can build on immediately.

## Scaffold Quality Dimensions

A production-quality scaffold must satisfy four dimensions before handoff:

| Dimension | Test | Pass Criteria |
|-----------|------|---------------|
| Runnable | `make run` or equivalent starts the process | Process starts, health check responds |
| Green CI | CI pipeline completes on first push | Build, lint, test all pass |
| Documented | `README.md` covers run/test/deploy | Developer new to the repo can start in < 10 min |
| Configurable | All environment-specific values in env vars | No hardcoded hosts, ports, or secrets |

## Directory Structure Patterns by Service Type

### REST API Service

```
<service-name>/
├── src/
│   ├── handlers/        # HTTP route handlers (one file per resource)
│   ├── services/        # Business logic (no HTTP concerns)
│   ├── repositories/    # Data access (no business logic)
│   ├── middleware/       # Auth, logging, rate limiting
│   ├── models/          # Data types / schemas
│   └── main.<ext>       # Entry point
├── tests/
│   ├── unit/            # Pure function tests
│   ├── integration/     # Tests with real DB / external services
│   └── fixtures/        # Test data
├── migrations/          # DB schema migrations (if applicable)
├── docs/                # OpenAPI spec, ADRs
├── .github/workflows/   # CI/CD pipeline definitions
├── Dockerfile
├── Makefile             # Standard targets: run, test, lint, build, migrate
└── README.md
```

### Event-Driven Worker

```
<worker-name>/
├── src/
│   ├── consumers/       # Message handlers per event type
│   ├── producers/       # Outbound message publishing
│   ├── processors/      # Core processing logic
│   └── main.<ext>
├── tests/
├── .github/workflows/
├── Dockerfile
├── Makefile
└── README.md
```

### Frontend Application

```
<app-name>/
├── src/
│   ├── pages/ or app/   # Route-level components
│   ├── components/      # Reusable UI components
│   ├── hooks/           # Custom hooks
│   ├── lib/             # Utilities, API clients
│   └── types/           # Type definitions
├── public/
├── tests/
│   ├── unit/
│   └── e2e/
├── .storybook/          # Component development environment
├── .github/workflows/
└── README.md
```

## Foundational Code Requirements

Every scaffold must include these working implementations on day one:

| Component | Purpose | Acceptance Test |
|-----------|---------|-----------------|
| Entry point | Starts the process with configured port/queue | `curl localhost:8080/health` returns `{"status":"ok"}` |
| Health check endpoint | Kubernetes / load-balancer readiness probe | Returns 200 within 200ms with no dependencies |
| Structured logging | JSON logs with request ID, level, timestamp | Log output parseable by standard log aggregators |
| Config loading | All config from environment variables | App fails fast with clear message if required var missing |
| Sample test | Validates the scaffold's test runner works | Test suite runs and passes on clean checkout |
| Graceful shutdown | Handles SIGTERM without data loss | Process exits cleanly within 5 seconds of signal |

## Tooling Selection Matrix

| Concern | TypeScript/Node | Python | Go | Java |
|---------|----------------|--------|----|------|
| Build | `tsc` / `esbuild` | `pyproject.toml` + `build` | `go build` | Gradle / Maven |
| Linter | `eslint` | `ruff` | `golangci-lint` | Checkstyle |
| Formatter | `prettier` | `black` | `gofmt` | google-java-format |
| Test runner | `jest` / `vitest` | `pytest` | `go test` | JUnit 5 |
| Dependency lock | `package-lock.json` | `uv.lock` / `poetry.lock` | `go.sum` | `gradle.lockfile` |
| Pre-commit hooks | `husky` + `lint-staged` | `pre-commit` | `pre-commit` | `pre-commit` |

## CI/CD Baseline Pipeline Stages

Every CI pipeline must include these stages in order:

1. **Dependency install** — restore from cache, install pinned versions
2. **Lint** — fail on lint errors; warnings acceptable
3. **Type check** (if typed language) — zero type errors
4. **Unit tests** — must pass; coverage report generated
5. **Build** — produce deployable artifact (Docker image / binary / bundle)
6. **Integration tests** — run against ephemeral test services (Docker Compose or GitHub Actions services)
7. **Artifact publish** — push image/artifact to registry on `main` branch only

## ADR Template for Scaffold Decisions

Record the initial architectural decisions in `docs/adr/001-initial-scaffold.md`:

```markdown
# ADR 001: Initial Scaffold Decisions

## Status: Accepted

## Context
[Why this service exists; what it will do]

## Technology Choices
| Concern | Choice | Alternatives Considered | Rationale |
|---------|--------|------------------------|-----------|
| Language | ... | ... | ... |
| Web framework | ... | ... | ... |
| Database | ... | ... | ... |
| Message broker | ... | ... | ... |

## Constraints
[Timeline, team expertise, infrastructure, org standards that shaped the choices]

## Consequences
[What becomes easier and what becomes harder with these choices]
```
