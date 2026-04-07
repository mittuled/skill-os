# Scoring Rubric: sprint-reviewer-eng

Evaluates the quality of an engineering sprint's output across delivery completeness, estimation accuracy, blocker management, velocity trend, and process adherence.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Delivery Completeness | 35% | Percentage of sprint-committed work that fully met its acceptance criteria by sprint end |
| 2 | Estimation Accuracy | 25% | Ratio of planned points to delivered points; reflects how reliably the team sizes work |
| 3 | Blocker Management | 20% | Speed and thoroughness with which blockers were identified, escalated, and resolved |
| 4 | Velocity Trend | 10% | Direction of velocity over the last 3–5 sprints; identifies capacity or scope drift |
| 5 | Process Adherence | 10% | Compliance with agreed team practices: PR review SLAs, definition of done, retrospective action follow-through |
| **Total** | | **100%** | |

## Scale

Each criterion scored **0–10**: 0 = completely absent or broken, 5 = partially met with significant gaps, 10 = fully met with no gaps

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0–10.0 | Exceptional | > 95% delivery completeness; estimation within ±10%; zero unresolved blockers; velocity stable or improving | Maintain cadence; candidates for process reference by other teams |
| A | 8.0–8.9 | Strong | > 90% completeness; estimation within ±15%; blockers resolved same day; velocity consistent | Minor process improvements; maintain current practices |
| B | 7.0–7.9 | Good | 80–90% completeness; estimation within ±25%; most blockers resolved within 48h; velocity slightly variable | Address top carryover cause; refine sizing for consistently mis-estimated task types |
| C | 5.0–6.9 | Adequate | 65–79% completeness; estimation off by ±30–40%; some blockers unresolved at sprint end; velocity declining | Structured retrospective required; root cause analysis on top 3 incomplete items |
| D | 3.0–4.9 | Weak | 40–64% completeness; estimation consistently off by > 40%; blockers sat for multiple days; velocity trending down | Sprint process overhaul; reduce commitment by 30% next sprint; identify systemic blockers |
| F | 0.0–2.9 | Failing | < 40% completeness; no meaningful velocity signal; repeated blockers with no resolution; process not followed | Immediate escalation; team retrospective with engineering leadership; reset sprint structure |

## Signal Tables

### Delivery Completeness

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | ≥ 95% of committed story points delivered; all acceptance criteria verified with test evidence or demo recording; zero tasks marked "done" without meeting AC |
| 7–8 | 85–94% of committed points delivered; 1–2 tasks partially complete with documented reason; no tasks marked done without evidence |
| 5–6 | 70–84% completeness; 3–5 tasks incomplete or partially complete; some AC left unverified; carryover list exists but root causes are not documented |
| 3–4 | 50–69% completeness; > 5 tasks incomplete; tasks marked done without meeting AC; carryover not formally tracked |
| 0–2 | < 50% completeness; sprint effectively failed; unclear which tasks are complete vs. in-progress vs. abandoned |

### Estimation Accuracy

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Actual delivered points within ±10% of committed points for 3+ consecutive sprints; no task required re-sizing mid-sprint |
| 7–8 | Actual within ±15–25%; occasional re-size mid-sprint (1–2 tasks); team discusses estimation errors in retrospective |
| 5–6 | Actual off by ±25–35%; 3–4 tasks required re-sizing or were split mid-sprint; estimation not discussed in retrospective |
| 3–4 | Actual off by ±35–50%; > 5 tasks re-sized; team consistently over-commits or under-commits; no improvement pattern visible |
| 0–2 | Estimation has no predictive value; actual delivered varies > ±50% sprint over sprint; team does not estimate before committing |

### Blocker Management

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Blockers identified within 4 hours of arising; all resolved within 24 hours or a workaround applied; blocker log updated in real time |
| 7–8 | Blockers identified same day; most resolved within 48 hours; 1 blocker carried > 48 hours with documented escalation path |
| 5–6 | Blockers raised at stand-up but resolution delayed 2–4 days; some blockers not formally logged; escalation ad hoc |
| 3–4 | Blockers not raised until they caused missed commitments; no formal blocker tracking; resolution reactive and slow |
| 0–2 | Blockers discovered only at sprint review; no proactive identification; multiple tasks failed due to unmanaged dependencies |

### Velocity Trend

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Velocity stable (within ±10%) or improving over last 5 sprints; team capacity and output are predictable |
| 7–8 | Velocity within ±20% over last 5 sprints; one anomaly sprint explained by known cause (holiday, incident) |
| 5–6 | Velocity declining 10–20% over last 3 sprints without clear cause; capacity inconsistency not addressed |
| 3–4 | Velocity declining > 20% or highly erratic (±40%+); team does not track velocity trends between sprints |
| 0–2 | No velocity baseline exists; team has never tracked points delivered per sprint; no predictability signal available |

### Process Adherence

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | All PRs reviewed within agreed SLA; definition of done applied to every task; retrospective action items tracked and closed; stand-ups attended by all team members |
| 7–8 | 90%+ PRs reviewed within SLA; DoD applied with 1–2 documented exceptions; most retrospective actions closed |
| 5–6 | 70–89% PRs reviewed within SLA; DoD inconsistently applied; retrospective actions carried multiple sprints without resolution |
| 3–4 | PR review SLA frequently missed (> 30% of PRs); DoD applied only to high-priority items; retrospective actions not tracked |
| 0–2 | No PR review SLA; no definition of done; retrospectives not held or actions never closed; process entirely informal |
