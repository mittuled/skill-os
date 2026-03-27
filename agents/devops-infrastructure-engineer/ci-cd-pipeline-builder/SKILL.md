---
name: ci-cd-pipeline-builder
description: Builds reliable CI/CD pipelines that turn every commit into a deployable, tested artifact.
department: engineering
agent: devops-infrastructure-engineer
version: 1.0.0
complexity: complex
related-skills: []
triggers:
  - "set up CI/CD"
  - "build the deployment pipeline"
  - "configure continuous integration"
  - "automate the build and deploy process"
---

# ci-cd-pipeline-builder

## Agent

L2 DevOps and infrastructure engineer responsible for CI/CD pipelines, deployment automation, cloud infrastructure, monitoring, alerting, incident response, and rollout management.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

The DevOps / Infrastructure Engineer builds and configures continuous integration and continuous deployment pipelines.

## When to Use

- A new project or service needs a CI/CD pipeline from scratch.
- An existing pipeline is unreliable, slow, or missing stages (lint, test, security scan, deploy).
- The team is migrating to a new CI/CD platform or changing deployment targets.
- A post-incident review identified pipeline gaps that allowed a defect into production.

## Workflow

1. Gather requirements: target environments, deployment cadence, test suites, security scan requirements, and artifact storage.
2. Design the pipeline stages: source checkout, dependency install, lint, unit test, integration test, security scan, build, artifact publish, deploy to staging, deploy to production.
3. Configure the CI platform (GitHub Actions, GitLab CI, etc.) with pipeline-as-code definitions.
4. Implement caching strategies for dependencies and build artifacts to minimize pipeline duration.
5. Add quality gates: fail the pipeline on lint errors, test failures, security vulnerabilities above threshold, or coverage drops.
6. Configure environment-specific deployment steps with secrets managed through the CI platform's secret store.
7. Implement notification hooks for pipeline failures (Slack, email, PagerDuty).
8. Add pipeline metrics: track build duration, success rate, and flaky test frequency.
9. Test the full pipeline end-to-end with a representative change.
10. Document the pipeline architecture, stage responsibilities, and troubleshooting guide.
    - **Deliverable**: A working CI/CD pipeline with all stages, quality gates, notifications, and documentation.

## Anti-Patterns

- **Building pipelines without quality gates.** *Why*: A pipeline that deploys regardless of test results is an automated way to ship bugs faster.
- **Hardcoding secrets in pipeline definitions.** *Why*: Secrets in code are visible to anyone with repo access and persist in version history forever.
- **Ignoring pipeline performance.** *Why*: Slow pipelines reduce deployment frequency, encourage batching changes, and increase the blast radius of each deploy.
- **Skipping the staging deploy step.** *Why*: Deploying directly to production removes the last safety net for catching environment-specific failures.
- **Not monitoring pipeline health.** *Why*: A silently degrading pipeline (increasing flakiness, slower builds) erodes developer trust and slows delivery.

## Output

**Success**: A fully operational CI/CD pipeline that builds, tests, scans, and deploys code through staging to production with quality gates at each stage.

**Failure**: A pipeline assessment listing which stages are missing or broken, with a remediation plan and priority order.

## Related Skills

*None defined yet.*
