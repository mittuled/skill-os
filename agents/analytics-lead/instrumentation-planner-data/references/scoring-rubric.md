# Scoring Rubric: Instrumentation Planner

Evaluates the quality of an instrumentation rollout plan across platform coverage, tooling architecture, phase sequencing, verification gates, and engineering coordination.

## Criteria

| Criterion | Weight | Scale | Description |
|-----------|--------|-------|-------------|
| Platform Coverage | 20% | 0-10 | Completeness of instrumentation across all product surfaces: client, server, mobile, API |
| Tooling & Architecture | 20% | 0-10 | Appropriateness of SDK selection, event routing design, and data pipeline architecture |
| Phase Sequencing | 20% | 0-10 | Logical ordering of rollout phases with clear scope and verification gates between them |
| Verification Gates | 20% | 0-10 | Presence and rigour of data quality validation checkpoints at each phase boundary |
| Engineering Coordination | 20% | 0-10 | Clarity of per-team task assignments, sprint alignment, and cross-team dependencies |
| **Total** | **100%** | | |

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 – 10.0 | Exceptional | All platforms instrumented with verified pipelines; phased rollout with automated gates; engineering tasks assigned per-sprint | Approve plan and begin Phase 1 implementation |
| A | 8.0 – 8.9 | Strong | Major platforms covered with clear architecture; phases sequenced logically; minor gaps in verification automation | Approve with manual verification checkpoints for Phase 1 |
| B | 7.0 – 7.9 | Good | Primary platform covered but secondary surfaces deferred; verification gates exist but are informal | Approve conditionally; document deferred surfaces and add gate checklists |
| C | 5.0 – 6.9 | Adequate | Single-platform plan with vague phasing; tooling decisions not justified; engineering coordination is high-level only | Revise plan to address coverage gaps and add concrete verification steps |
| D | 3.0 – 4.9 | Weak | No phasing or verification; tooling chosen without evaluation; no engineering buy-in | Rework plan with engineering and data teams before proceeding |
| F | 0.0 – 2.9 | Failing | No systematic instrumentation plan; ad-hoc event tracking with no architecture or coordination | Start over with platform inventory and stakeholder alignment |

## Signal Tables

### Platform Coverage
| Score | Evidence |
|-------|----------|
| 9-10 | All product surfaces (web, mobile, server, API) have instrumentation plans; client-side and server-side events complement each other; coverage gaps explicitly documented with justification |
| 7-8 | Major platforms covered; minor surfaces (e.g., admin tools, internal APIs) deferred with rationale; no critical coverage gaps |
| 5-6 | Primary platform covered but secondary platforms have incomplete plans; some client-only or server-only blind spots |
| 3-4 | Only one platform planned; significant surfaces unaddressed; coverage gaps not acknowledged |
| 1-2 | No systematic platform inventory; instrumentation planned ad-hoc without surface-level analysis |

### Tooling & Architecture
| Score | Evidence |
|-------|----------|
| 9-10 | SDK selection justified with trade-off analysis; event routing documented (trigger to warehouse); buffering, batching, retry, and deduplication behaviour specified; architecture handles ad-blocker data loss |
| 7-8 | SDK selected with rationale; event routing documented at high level; most pipeline concerns addressed |
| 5-6 | SDK chosen but trade-offs not documented; event routing partially described; pipeline reliability concerns unaddressed |
| 3-4 | SDK selection is default/inherited without evaluation; no event routing documentation; pipeline is a black box |
| 1-2 | No tooling decisions made; plan assumes instrumentation "just works" without architectural consideration |

### Phase Sequencing
| Score | Evidence |
|-------|----------|
| 9-10 | Clear phase breakdown (core funnel, engagement, edge-case/error); phases ordered by data criticality; each phase has defined scope, timeline, and entry/exit criteria |
| 7-8 | Phases defined with logical ordering; most phases have scope and timeline; entry criteria exist but exit criteria are informal |
| 5-6 | Phases exist but ordering rationale is unclear; scope per phase is approximate; timelines are aspirational |
| 3-4 | Only 2 phases (do it all then fix it); no data-criticality ordering; no timeline |
| 1-2 | No phasing; plan is a single big-bang deployment |

### Verification Gates
| Score | Evidence |
|-------|----------|
| 9-10 | Each phase boundary has a verification checklist: event firing validation, property correctness, volume sanity checks, and data warehouse arrival confirmation; automated verification where possible |
| 7-8 | Verification gates defined for each phase; mostly manual but checklist-based; key validation criteria documented |
| 5-6 | Verification gates exist for some phases; validation criteria are general ("check events fire"); no automation |
| 3-4 | One verification step at the end of all phases; no intermediate checkpoints; validation is ad-hoc |
| 1-2 | No verification gates; plan assumes correct implementation without validation |

### Engineering Coordination
| Score | Evidence |
|-------|----------|
| 9-10 | Per-team task lists with event names, trigger points, and property sources; sprint allocation confirmed; cross-team dependencies mapped and sequenced; single owner per event |
| 7-8 | Task lists exist per team; sprint allocation discussed; most dependencies identified; minor gaps in property source documentation |
| 5-6 | Tasks assigned at team level but not broken down to individual events; sprint alignment assumed but not confirmed |
| 3-4 | Tasks loosely assigned; no sprint alignment; cross-team dependencies not mapped |
| 1-2 | No engineering coordination; plan exists in analytics team only without engineering buy-in |
