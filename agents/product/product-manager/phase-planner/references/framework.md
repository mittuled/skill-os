# Framework: Phase Planning

## Core Model

Phase planning decomposes an initiative into sequential delivery phases, each with defined boundaries, activities, deliverables, and transition criteria.

## Phase Taxonomy

| Phase | Purpose | Typical Duration | Key Deliverables |
|-------|---------|-----------------|------------------|
| Discovery | Validate problem and solution direction | 1-3 weeks | Problem statement, user journey map, competitive landscape |
| Design | Define the solution shape | 1-2 weeks | Wireframes, technical architecture, API contracts |
| Build | Implement the solution | 2-6 weeks | Working software behind feature flag |
| Beta | Validate with real users | 1-2 weeks | UAT results, performance benchmarks |
| Launch | Ship to general availability | 1 week | Release notes, monitoring dashboards, support enablement |

## Entry/Exit Criteria Pattern

Every phase boundary requires:
- **Entry criteria**: Preconditions that must be true before the phase starts (artifacts from prior phase, approvals, resource availability)
- **Exit criteria**: Outcomes that must be demonstrated before advancing (validated hypothesis, passing tests, stakeholder sign-off)
- **Carry-over protocol**: How incomplete work from the current phase is handled in the next

## Risk Assessment per Phase

Each phase should identify the top 1-2 risks:
- **Likelihood**: Low / Medium / High
- **Impact**: Low / Medium / High
- **Mitigation**: Specific action to reduce likelihood or impact
- **Owner**: Named person responsible for executing the mitigation

## Estimation Approach

- Use historical velocity from similar initiatives when available
- Apply a 1.3x buffer to estimates for phases with high uncertainty (discovery, beta)
- Identify the critical path across phases to determine the minimum total duration
- Flag phases where parallel work is possible vs. strictly sequential

## Anti-Pattern Checklist

- [ ] No phase has entry/exit criteria defined only by calendar dates
- [ ] No phase exceeds 6 weeks without a checkpoint
- [ ] Feedback loops exist between adjacent phases (not pure waterfall)
- [ ] Carry-over from prior phase is explicitly accounted for in next phase scope
