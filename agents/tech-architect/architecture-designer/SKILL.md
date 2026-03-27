---
name: architecture-designer
description: >
  This skill designs the overall system architecture including components, data flows,
  and integrations. Use when asked to design a system, create an architecture diagram,
  or define the technical structure for a new product. Also consider when the current
  architecture cannot support upcoming product requirements. Suggest when the user is
  building features without an architecture that accounts for scale and maintainability.
department: engineering
agent: tech-architect
version: 1.0.0
complexity: complex
related-skills:
  - ../api-contract-definer/SKILL.md
  - ../technical-feasibility-check/SKILL.md
triggers:
  - "design the system architecture"
  - "create an architecture diagram"
  - "how should we structure this system"
  - "plan the technical architecture"
---

# architecture-designer

## Agent: Tech Architect

L2 technical architect (1x) responsible for feasibility assessment, system design, API contract definition, and infrastructure planning. Ensures technical decisions support product goals and scale requirements.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

Designs the overall system architecture by defining components, their responsibilities, data flows, integration patterns, and technology choices to create a system that meets functional requirements while supporting scale, reliability, and maintainability.

## When to Use

- When a new product or major feature requires a greenfield system design before development begins.
- When the existing architecture cannot support upcoming product requirements (scale, new capabilities, new integrations) and needs redesign.
- When multiple teams need a shared understanding of system structure to build their components in parallel.

## Workflow

1. **Requirements Synthesis**: Gather functional requirements (what the system must do), non-functional requirements (performance, availability, security, compliance), and constraints (timeline, team size, existing systems, budget). Deliverable: architecture requirements document.
2. **Component Design**: Decompose the system into components with clear responsibilities and boundaries. Define the interaction patterns between components (synchronous, asynchronous, event-driven). Select the appropriate granularity (monolith, modular monolith, microservices) based on team size and operational maturity. Deliverable: component diagram with responsibility descriptions.
3. **Data Architecture**: Design the data layer: storage technologies, data models, data flow between components, consistency requirements, and caching strategy. Address data ownership, replication, and eventual consistency trade-offs. Deliverable: data architecture document.
4. **Technology Selection**: Select technologies for each component based on requirements, team expertise, ecosystem maturity, and operational cost. Document the rationale for each choice and the alternatives considered. Deliverable: technology selection document with rationale.
5. **Cross-Cutting Concerns**: Design solutions for cross-cutting concerns: authentication and authorization, observability (logging, metrics, tracing), error handling, configuration management, and deployment strategy. Deliverable: cross-cutting concerns specification.
6. **Architecture Review**: Present the architecture to engineering leadership and senior engineers for review. Defend trade-off decisions, incorporate feedback, and finalize the design. Deliverable: reviewed and approved architecture document.

## Anti-Patterns

- **Resume-driven architecture**: Choosing technologies because the architect wants to learn them rather than because they fit the requirements. *Why*: technology choices should serve the product and team; novel technologies introduce risk and slow teams unfamiliar with them.
- **Premature microservices**: Decomposing into microservices before the team has the operational maturity, deployment infrastructure, and service mesh to manage distributed systems. *Why*: microservices without operational foundations create reliability and debugging nightmares worse than the monolith they replaced.
- **Architecture without constraints**: Designing the ideal system without considering timeline, team size, and operational budget. *Why*: an architecture the team cannot build, deploy, and operate is not a design but a fantasy; constraints produce practical architectures.
- **Big bang migration**: Planning to replace the entire existing system at once rather than incrementally. *Why*: big bang migrations have high failure rates; incremental migration allows learning, rollback, and continuous delivery.

## Output

**On success**: Produces an architecture document with component diagrams, data architecture, technology selections, cross-cutting concerns specification, and review notes. Delivered before development begins.

**On failure**: Report which architectural decisions could not be finalized (unresolved requirements, conflicting constraints), what partial design exists, and what decisions must be made before development can proceed.

## Related Skills

- [`api-contract-definer`](../api-contract-definer/SKILL.md) -- API contracts formalize the interfaces between components defined in the architecture.
- [`technical-feasibility-check`](../technical-feasibility-check/SKILL.md) -- Feasibility checks validate that the architecture can be built within constraints.
