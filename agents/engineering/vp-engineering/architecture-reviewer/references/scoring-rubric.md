# Scoring Rubric: Architecture Reviewer

Evaluates architecture decision records and design proposals across structural soundness, scalability, standards alignment, operational readiness, and simplicity.

## Criteria

| Criterion | Weight | Scale | Description |
|-----------|--------|-------|-------------|
| Structural Soundness | 25% | 0-10 | Component boundaries, data flow correctness, failure domains, and blast radius containment |
| Scalability Posture | 20% | 0-10 | Horizontal/vertical scaling design, capacity headroom, and load projection alignment |
| Standards Alignment | 20% | 0-10 | Adherence to technology radar, observability requirements, and security posture |
| Operational Readiness | 20% | 0-10 | Deployment complexity, rollback strategy, data migration, and on-call burden |
| Architectural Simplicity | 15% | 0-10 | Appropriate complexity for the problem; avoidance of premature abstraction and unnecessary components |
| **Total** | **100%** | | |

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 – 10.0 | Exceptional | Clean component boundaries; 3x+ scaling headroom; full standards alignment; automated deployment with tested rollback; minimal complexity | Approve ADR and proceed to implementation |
| A | 8.0 – 8.9 | Strong | Well-isolated components; adequate scaling; mostly standards-aligned; deployment automated with minor operational gaps | Approve with follow-up on flagged operational items |
| B | 7.0 – 7.9 | Good | Component boundaries clear but some coupling; scaling approach defined for primary paths; observability partially designed | Approve conditionally; address coupling and observability before sprint 2 |
| C | 5.0 – 6.9 | Adequate | Leaky abstractions; scaling untested; off-radar technology without justification; manual deployment | Return for revision; schedule architecture pairing session |
| D | 3.0 – 4.9 | Weak | Tightly coupled components; no scaling design; no observability or security analysis; over-engineered | Reject; require fundamental redesign with architectural guidance |
| F | 0.0 – 2.9 | Failing | Monolithic with no isolation; no deployment strategy; no standards adherence; team cannot operate proposed system | Reject; assign architecture sponsor and restart design from requirements |

## Signal Tables

### Structural Soundness
| Score | Evidence |
|-------|----------|
| 9-10 | Clear component boundaries with well-defined interfaces; no single points of failure; failure domains isolated; blast radius contained to individual components; data flow paths are explicit and documented |
| 7-8 | Component boundaries are clear; most failure domains isolated; minor single-point-of-failure risks documented with mitigations; data flows documented |
| 5-6 | Component boundaries exist but some are leaky; failure domains partially identified; some undocumented data flow paths |
| 3-4 | Components are tightly coupled; failure in one component cascades broadly; data flows are implicit and undocumented |
| 1-2 | Monolithic design with no component isolation; complete system failure on any component fault; no data flow documentation |

### Scalability Posture
| Score | Evidence |
|-------|----------|
| 9-10 | Horizontal scaling designed for all stateless components; 3x+ headroom beyond projected load; scaling triggers automated; capacity plan accounts for growth trajectory |
| 7-8 | Scaling approach defined for primary components; 2-3x headroom; manual scaling triggers documented; growth projections referenced |
| 5-6 | Scaling approach exists for some components; headroom is 1-2x; scaling is manual and untested; growth projections vague |
| 3-4 | Scaling discussed but not designed; no headroom analysis; architecture assumes current load indefinitely |
| 1-2 | No scaling consideration; architecture is sized for current load only; vertical scaling is the only option |

### Standards Alignment
| Score | Evidence |
|-------|----------|
| 9-10 | All technology choices on the approved radar; structured logging, metrics, and distributed tracing designed in; threat model present; auth flows documented; ADR follows organizational template |
| 7-8 | Technology choices mostly on radar with justified exceptions; observability mostly covered; security posture documented; ADR format followed |
| 5-6 | Some technology choices off-radar without justification; observability partially designed; threat model absent but security basics covered |
| 3-4 | Multiple off-radar choices; observability an afterthought; no security analysis; ADR format not followed |
| 1-2 | Technology choices made without reference to standards; no observability, security, or documentation standards met |

### Operational Readiness
| Score | Evidence |
|-------|----------|
| 9-10 | Deployment is automated with blue-green or canary strategy; rollback tested and under 15 minutes; data migration is reversible; on-call runbook exists; operational burden assessed |
| 7-8 | Deployment automated; rollback documented; data migration planned; on-call considerations noted; minor gaps in runbook |
| 5-6 | Deployment partially automated; rollback possible but untested; data migration planned but irreversible; no runbook |
| 3-4 | Deployment is manual; rollback strategy unclear; data migration risky; on-call burden not assessed |
| 1-2 | No deployment strategy; no rollback capability; data migration would cause downtime; operational concerns not considered |

### Architectural Simplicity
| Score | Evidence |
|-------|----------|
| 9-10 | Architecture uses the minimum number of components to solve the problem; no premature abstractions; technology choices match team expertise; complexity is justified by requirements |
| 7-8 | Architecture is mostly simple with minor over-engineering; new technologies introduced with clear justification; complexity proportional to problem |
| 5-6 | Some unnecessary components or abstractions present; one or two technologies introduced without strong justification; complexity slightly exceeds requirements |
| 3-4 | Over-engineered with multiple unnecessary services, queues, or caches; resume-driven technology choices; complexity far exceeds current requirements |
| 1-2 | Massively over-engineered; architecture designed for problems that do not exist; team cannot operate the proposed system |
