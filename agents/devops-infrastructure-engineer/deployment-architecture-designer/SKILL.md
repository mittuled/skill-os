---
name: deployment-architecture-designer
description: Designs the deployment topology that determines how code reaches users reliably and efficiently.
department: engineering
agent: devops-infrastructure-engineer
version: 1.0.0
complexity: complex
related-skills: []
---

# deployment-architecture-designer

## Agent

L2 DevOps and infrastructure engineer responsible for CI/CD pipelines, deployment automation, cloud infrastructure, monitoring, alerting, incident response, and rollout management.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

The DevOps / Infrastructure Engineer designs the deployment architecture including environments, networking, and service topology.

## When to Use

- A new product is being architected and needs a deployment strategy from the start.
- The team is migrating from monolith to microservices and the deployment model must change.
- Scaling requirements have outgrown the current deployment architecture.
- A post-incident review revealed architectural weaknesses in the deployment topology.

## Workflow

1. Gather requirements: service count, traffic patterns, latency targets, availability SLOs, compliance constraints, and team structure.
2. Define the environment topology: development, staging, production, and any region-specific deployments.
3. Design the service topology: how services communicate (sync vs. async), load balancing strategy, and service discovery.
4. Select the deployment model: containers (Kubernetes), serverless, VMs, or hybrid, with justification.
5. Design the networking layer: ingress, egress, inter-service communication, and network policies.
6. Plan for high availability: redundancy, failover, health checks, and multi-region if required.
7. Define the artifact flow: how build artifacts move from CI to each environment.
8. Document the architecture with diagrams, decision records (ADRs), and operational constraints.
9. Validate the design against the SLOs and failure scenarios with a tabletop exercise.
10. Present the architecture to engineering leadership for review and approval.
    - **Deliverable**: A deployment architecture document with diagrams, ADRs, and SLO validation results.

## Anti-Patterns

- **Designing for peak scale on day one.** *Why*: Over-engineering the initial architecture wastes resources and adds complexity that slows iteration when the product is still finding fit.
- **Ignoring network policy design.** *Why*: Flat networks where every service can talk to every other service create a massive blast radius for any compromise.
- **Choosing technology based on resume appeal.** *Why*: The deployment architecture must match team capabilities and operational maturity, not industry trends.
- **Skipping failure scenario validation.** *Why*: An architecture that has not been stress-tested on paper will be stress-tested in production at the worst possible time.

## Output

**Success**: A reviewed and approved deployment architecture document with environment topology, service topology, networking design, ADRs, and SLO validation.

**Failure**: A list of unresolved architectural risks with their potential impact and recommended mitigations, escalated to engineering leadership.

## Related Skills

*None defined yet.*
