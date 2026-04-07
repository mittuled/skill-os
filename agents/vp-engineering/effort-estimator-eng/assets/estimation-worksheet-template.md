# Effort Estimation Worksheet: [Feature / Epic Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Estimator | VP Engineering / Tech Lead |
| Feature | [Feature or epic name] |
| Estimation Method | [T-shirt sizing / Story points / Three-point (PERT)] |
| Estimation Session | [Async / Planning poker / Expert judgment] |
| Skill | effort-estimator-eng |
| Confidence | [High (±10%) / Medium (±25%) / Low (±50%)] |

## Feature Summary

**What is being built?**
[2–3 sentences describing the feature scope. Be specific enough that each work item below can be tied back to this description.]

**Assumptions**
1. [Explicit assumption that the estimate depends on, e.g., "Auth system already exists; we are adding OAuth provider only"]
2. [Another assumption]

**Out of scope (explicit)**
1. [What is NOT included in this estimate]

## Work Breakdown

### Backend

| Task | Complexity | Points | Low | Likely | High | Owner |
|------|-----------|--------|-----|--------|------|-------|
| [API endpoint: POST /resource] | [M] | [3] | [2] | [3] | [5] | [Backend] |
| [Database schema change + migration] | [S] | [2] | [1] | [2] | [3] | [Backend] |
| [Service layer logic] | [L] | [5] | [3] | [5] | [8] | [Backend] |
| [Unit + integration tests] | [M] | [3] | [2] | [3] | [5] | [Backend] |
| **Backend subtotal** | | **[13]** | **[8]** | **[13]** | **[21]** | |

### Frontend

| Task | Complexity | Points | Low | Likely | High | Owner |
|------|-----------|--------|-----|--------|------|-------|
| [UI component: FormComponent] | [M] | [3] | [2] | [3] | [5] | [Frontend] |
| [Page / view implementation] | [L] | [5] | [3] | [5] | [8] | [Frontend] |
| [State management integration] | [S] | [2] | [1] | [2] | [3] | [Frontend] |
| [Accessibility + responsive] | [S] | [2] | [1] | [2] | [3] | [Frontend] |
| [Component tests] | [S] | [2] | [1] | [2] | [3] | [Frontend] |
| **Frontend subtotal** | | **[14]** | **[8]** | **[14]** | **[22]** | |

### Infrastructure / DevOps

| Task | Complexity | Points | Low | Likely | High | Owner |
|------|-----------|--------|-----|--------|------|-------|
| [Environment config / secrets] | [S] | [1] | [1] | [1] | [2] | [DevOps] |
| [CI/CD pipeline changes] | [S] | [1] | [1] | [1] | [2] | [DevOps] |
| **Infra subtotal** | | **[2]** | **[2]** | **[2]** | **[4]** | |

### QA

| Task | Complexity | Points | Low | Likely | High | Owner |
|------|-----------|--------|-----|--------|------|-------|
| [Test plan creation] | [S] | [1] | [1] | [1] | [2] | [QA] |
| [Manual regression pass] | [M] | [2] | [1] | [2] | [3] | [QA] |
| **QA subtotal** | | **[3]** | **[2]** | **[3]** | **[5]** | |

## PERT Summary

| Component | Low (O) | Likely (M) | High (P) | PERT = (O + 4M + P) / 6 |
|-----------|---------|-----------|----------|--------------------------|
| Backend | [8] | [13] | [21] | [13.2] |
| Frontend | [8] | [14] | [22] | [14.0] |
| Infra | [2] | [2] | [4] | [2.3] |
| QA | [2] | [3] | [5] | [3.2] |
| **Total** | **[20]** | **[32]** | **[52]** | **[32.7]** |

**PERT formula**: (Optimistic + 4 × Most Likely + Pessimistic) / 6

**Standard deviation** = (Pessimistic − Optimistic) / 6 = [52 − 20] / 6 = [5.3 pts]

## Sprint Capacity Mapping

| Sprint | Capacity (pts) | Allocated Work | Remaining Estimate |
|--------|---------------|----------------|--------------------|
| Sprint [N] | [X pts] | [Backend API + DB] = [8 pts] | [24.7 pts] |
| Sprint [N+1] | [X pts] | [Frontend + tests] = [14 pts] | [10.7 pts] |
| Sprint [N+2] | [X pts] | [QA + polish] = [5 pts] | Done |

**Projected completion**: Sprint [N+2] (week of [YYYY-MM-DD])

## Risk Factors Affecting Estimate

| Risk | Likelihood | If realized, impact on estimate |
|------|-----------|--------------------------------|
| [Third-party API undocumented behavior] | Medium | +3–5 pts (spike needed) |
| [Design not finalized for edge case] | High | +2 pts if design change mid-sprint |
| [Key engineer unavailable] | Low | +5–8 pts (knowledge transfer time) |

## Estimation Confidence

**Confidence level**: [High / Medium / Low]
**Range**: [Low estimate] to [High estimate] story points
**Recommended commitment**: [PERT estimate × confidence buffer]

> Confidence guide:
> - High: Requirements fully defined, team has done similar work, no unknowns
> - Medium: Core requirements clear; 1–2 open design decisions
> - Low: Significant unknowns; spike or discovery needed first
