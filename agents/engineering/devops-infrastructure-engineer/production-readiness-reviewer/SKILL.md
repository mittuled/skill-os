---
name: production-readiness-reviewer
description: >
  This skill reviews whether a system meets production readiness criteria before
  go-live. Use when asked to conduct a production readiness review, validate
  launch readiness, or audit operational maturity. Also consider when a new
  service is approaching deployment without formal review. Suggest when the user
  is planning a launch without a readiness checklist.
department: engineering
agent: devops-infrastructure-engineer
version: 1.0.0
complexity: complex
related-skills:
  - ../infrastructure-requirements-extractor/SKILL.md
  - ../runbook-drafter/SKILL.md
  - ../performance-monitor/SKILL.md
triggers:
  - "check if we're production ready"
  - "run a production readiness review"
  - "is this service ready for launch"
  - "audit operational maturity"
---

# production-readiness-reviewer

## Agent: DevOps / Infrastructure Engineer

L2 DevOps and infrastructure engineer (1x) responsible for CI/CD pipelines, deployment automation, cloud infrastructure, monitoring, alerting, incident response, and rollout management.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Reviews whether a service or system meets production readiness criteria across reliability, observability, security, performance, and operational domains before approving go-live deployment.

## When to Use

- When a new service or major feature is approaching production deployment and needs formal validation against readiness criteria.
- When an existing service is undergoing significant architectural changes that affect its operational posture.
- When an incident reveals operational gaps and the service needs re-evaluation against readiness standards.

## Workflow

1. **Checklist Assembly**: Assemble the production readiness checklist covering all domains: reliability (redundancy, failover, disaster recovery), observability (logging, metrics, tracing, alerting), security (authentication, authorization, secrets management, vulnerability scanning), performance (load testing, capacity planning, SLOs), and operations (runbooks, on-call, deployment procedures, rollback plans). Tailor the checklist to the service's criticality tier. Deliverable: tailored production readiness checklist.
2. **Architecture Review**: Review the service architecture for single points of failure, dependency risks, and blast radius. Verify that the service degrades gracefully under partial failures. Assess data durability and backup strategies. Deliverable: architecture review findings.
3. **Observability Audit**: Verify that the service has structured logging with correlation IDs, metrics covering the RED method (rate, errors, duration), distributed tracing, and alerts for SLO violations. Confirm that dashboards exist and are accurate. Deliverable: observability audit report.
4. **Security Review**: Verify secrets management (no hardcoded credentials), authentication and authorization enforcement, TLS configuration, dependency vulnerability scanning, and compliance with security policies. Deliverable: security review findings.
5. **Performance Validation**: Review load test results against production traffic projections. Verify auto-scaling configuration, resource limits, and capacity headroom. Confirm SLOs are defined and measurable. Deliverable: performance validation report.
6. **Operational Readiness**: Verify that runbooks exist for common failure modes, on-call rotation is established, deployment and rollback procedures are documented and tested, and the team has conducted a failure injection exercise (game day). Deliverable: operational readiness assessment.
7. **Go/No-Go Decision**: Compile findings into a readiness scorecard. Classify each domain as pass, conditional pass (with remediation timeline), or fail. Make the go/no-go recommendation with clear rationale. Deliverable: production readiness scorecard with recommendation.

## Anti-Patterns

- **Checkbox compliance without depth**: Marking checklist items as complete based on existence rather than quality (e.g., "runbook exists" without verifying it is accurate and actionable). *Why*: a checklist that measures existence rather than effectiveness provides false confidence and fails during real incidents.
- **Reviewing only the new service**: Assessing the new service in isolation without reviewing its impact on dependent and upstream services. *Why*: a production-ready service that overwhelms its database or saturates a shared message queue causes outages in other services.
- **Skipping the review under deadline pressure**: Bypassing or shortening the production readiness review to meet a launch date. *Why*: the review exists to prevent production incidents; launching without it trades short-term speed for incident risk that costs more time than the review would have taken.
- **One-time review without follow-up**: Treating production readiness as a gate rather than an ongoing standard. *Why*: services degrade over time as dependencies change, traffic patterns shift, and operational knowledge decays; periodic re-review maintains readiness.

## Output

**On success**: Produces a production readiness scorecard with domain-by-domain assessment, findings, and go/no-go recommendation. Delivered to the engineering team, VP Engineering, and stakeholders.

**On failure**: Report which domains could not be assessed (e.g., load tests not yet run, security scan pending), what the partial readiness status is, and what must be completed before the review can conclude. Block deployment until critical items are resolved.

## Related Skills

- [`infrastructure-requirements-extractor`](../infrastructure-requirements-extractor/SKILL.md) -- Infrastructure requirements inform the capacity and architecture aspects of the readiness review.
- [`runbook-drafter`](../runbook-drafter/SKILL.md) -- Runbooks are a required artifact for the operational readiness domain.
- [`performance-monitor`](../performance-monitor/SKILL.md) -- Monitoring and alerting are validated as part of the observability audit.
