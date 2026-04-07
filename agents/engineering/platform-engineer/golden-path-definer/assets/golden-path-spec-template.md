# Golden Path Specification

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Agent role / human name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | golden-path-definer |

## Executive Summary

[2-3 sentences summarizing the golden path: what task it covers, how many teams it impacts, and key tooling decisions.
GUIDANCE: Lead with the problem this path solves. State the expected velocity improvement.]

## Current State Audit

[Document how teams currently handle this task and the variants discovered.

GUIDANCE:
- Good: "Service creation: Team A uses custom Yeoman generator (2 years old, unmaintained). Team B copies from last service (no template updates). Team C has a Bash script that scaffolds from internal template. Variant count: 3. Common pain: all teams manually configure CI, observability, and database connections."
- Bad: "Teams do things differently."
- Format: Table with team, current approach, pros, cons, and maintenance status]

| Team | Current Approach | Pros | Cons | Maintained |
|------|-----------------|------|------|-----------|
| [Name] | [Description] | [What works] | [What doesn't] | [Y/N, last update] |

## Golden Path Definition

[Define the recommended approach with tooling, templates, and guardrails.

GUIDANCE:
- Good: "Service creation golden path: `platform create-service --name <name> --type <api|worker|cron>`. Generates: project structure, Dockerfile, CI pipeline, Terraform module, OpenTelemetry config, health check endpoint, README. Opinionated: TypeScript, Express, PostgreSQL. Escapable: teams can override any generated file; deviations tracked in `.platform-overrides`."
- Bad: "Use our template."
- Format: Step-by-step path with tooling, defaults, and escape hatches]

## Templates and Tooling

[List the concrete artifacts that implement the golden path.

GUIDANCE:
- Good: "CLI: `@platform/create-service` (npm package, v1.0.0). Templates: service-api (Express+Postgres), service-worker (Bull+Redis), service-cron (node-cron). CI: `.github/workflows/golden-pipeline.yml`. IaC: `modules/golden-service` Terraform module."
- Bad: "Templates exist."
- Format: Table with artifact type, name, version, and location]

## Migration Guide

[For services not on the golden path, define how to migrate.

GUIDANCE:
- Good: "Step 1: Run `platform migrate-service --from <current> --to golden`. Step 2: Review generated diff. Step 3: Update CI to use golden pipeline. Step 4: Verify in staging. Priority: migrate services with highest change frequency first."
- Bad: "Migrate old services."
- Format: Step-by-step guide with priority criteria]

## Recommendations

[Prioritized list of implementation and rollout steps.
GUIDANCE: Each recommendation should be:
- Specific (not "roll out golden path" but "pilot with Team B on their next new service, collect feedback for 2 sprints")
- Actionable (assignable to a person/team)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[How current state was audited: teams interviewed, repos inspected, developer survey results]

### B. Supporting Data

[Full variant inventory, developer survey raw data, pilot team feedback]
