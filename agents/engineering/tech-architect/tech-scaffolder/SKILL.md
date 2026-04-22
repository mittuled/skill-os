---
name: tech-scaffolder
description: >
  This skill creates the initial technical scaffold and project structure for a new system. Use
  when asked to bootstrap a new service, set up a project skeleton, or define the initial folder
  and configuration layout. Also consider when a team is starting a greenfield build without
  agreed conventions. Suggest when engineers are about to create a new repository without a template.
department: engineering
agent: tech-architect
version: 1.0.0
complexity: medium
related-skills:
  - ../../../engineering/tech-architect/architecture-designer/SKILL.md
  - ../../../engineering/tech-architect/api-contract-definer/SKILL.md
  - performance-budget-setter-eng
  - scale-infrastructure-planner
triggers:
  - "scaffold the project"
  - "set up the repo structure"
  - "bootstrap a new service"
  - "create the project skeleton"
---

# tech-scaffolder

## Agent: Tech Architect

L2 technical architect (1x) responsible for feasibility assessment, system design, API contract definition, and infrastructure planning. Ensures technical decisions support product goals and scale requirements.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Creates the initial technical scaffold, project structure, tooling configuration, and foundational code for a new system or service.

## When to Use

- When a new service, library, or application needs to be bootstrapped from scratch with consistent conventions.
- When the architecture design is complete and the team needs a working skeleton to begin implementation against.
- When multiple teams are starting new projects and need a standardized starting point to ensure consistency across the codebase.

## Workflow

1. **Gather requirements**: Collect the technology stack decisions, target runtime, deployment model, and team conventions from the architecture design. Deliverable: scaffold requirements checklist.
2. **Define directory structure**: Design the folder layout including source directories, test directories, configuration, CI/CD templates, and documentation stubs. Deliverable: directory tree specification.
3. **Configure tooling**: Set up build system, linter, formatter, test runner, and dependency management. Pin dependency versions and configure pre-commit hooks. Deliverable: configuration files (e.g., tsconfig, eslint, Makefile, pyproject.toml).
4. **Create foundational code**: Write the entry point, health-check endpoint, structured logging setup, and a sample test to validate the scaffold works end-to-end. Deliverable: runnable project skeleton.
5. **Set up CI/CD baseline**: Configure the CI pipeline to build, lint, test, and produce a deployable artifact. Include a minimal deployment configuration for the target environment. Deliverable: CI/CD pipeline definition file.
6. **Document and hand off**: Write a README covering how to run, test, and deploy the project locally. Record architectural decisions in an ADR. Deliverable: README and initial ADR.

## Anti-Patterns

- **Scaffold bloat**: Including every possible library, middleware, and configuration option upfront. *Why*: over-scaffolding creates cognitive overhead and maintenance burden for features the team may never use.
- **Copy-paste from last project**: Cloning an old project and stripping it down instead of building from deliberate choices. *Why*: inherited configuration carries assumptions and technical debt from a different context.
- **No working CI on day one**: Scaffolding the project without a green CI pipeline. *Why*: a broken or missing pipeline from the start normalizes red builds and delays feedback loops.

## Output

**On success**: Produces a runnable project skeleton with directory structure, tooling configuration, foundational code, CI/CD pipeline, and documentation. Delivered as an initialized repository ready for the team to begin feature development.

**On failure**: Report which scaffold elements could not be created (e.g., missing stack decisions, unavailable base images), what decisions are blocking, and recommended steps to unblock.

## Related Skills

- [`architecture-designer`](../../../engineering/tech-architect/architecture-designer/SKILL.md) -- the architecture design drives the stack and structure choices that the scaffold implements.
- [`api-contract-definer`](../../../engineering/tech-architect/api-contract-definer/SKILL.md) -- API contracts determine which endpoints and interfaces the scaffold must stub out.
- [`performance-budget-setter-eng`](../performance-budget-setter-eng/SKILL.md) — sibling skill under the same agent — combine with performance-budget-setter-eng for end-to-end coverage
- [`scale-infrastructure-planner`](../scale-infrastructure-planner/SKILL.md) — sibling skill under the same agent — combine with scale-infrastructure-planner for end-to-end coverage
