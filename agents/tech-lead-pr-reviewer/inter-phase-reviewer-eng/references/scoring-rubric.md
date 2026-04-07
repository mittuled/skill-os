# Scoring Rubric: inter-phase-reviewer-eng

Evaluates readiness to advance from one engineering project phase to the next by assessing deliverable completeness, quality, documentation, and carried-forward debt.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Deliverable Completeness | 35% | Percentage of phase deliverables that fully meet their defined exit criteria |
| 2 | Quality Standard Adherence | 25% | Test coverage, code review compliance, and absence of P1/P2 defects in deliverables |
| 3 | Documentation Completeness | 20% | ADRs, runbooks, API specs, and design docs produced and reviewed during the phase |
| 4 | Carried-Forward Debt | 20% | Volume and severity of incomplete items, deferred decisions, and known technical debt entering the next phase |
| **Total** | | **100%** | |

## Scale

Each criterion scored **0–10**: 0 = completely absent or failed, 5 = partially met with significant gaps, 10 = fully met with no gaps

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0–10.0 | Pass — Exceptional | 100% deliverables complete; no P1/P2 defects; all docs reviewed; zero unmitigated debt | Advance immediately; no conditions |
| A | 8.0–8.9 | Pass — Strong | ≥ 95% deliverables complete; minor test gap; docs mostly complete; debt logged and accepted | Advance with documented debt; assign remediation in next phase |
| B | 7.0–7.9 | Conditional Pass | 85–94% deliverables complete; 1–2 P2 defects mitigated; some docs outstanding | Conditional advance; outstanding docs and defects must resolve within first week of next phase |
| C | 5.0–6.9 | Hold | 70–84% complete; P2 defects unresolved; documentation gaps affecting next phase inputs | Hold; 3–5 day remediation sprint before advancing |
| D | 3.0–4.9 | Fail — Weak | 50–69% complete; P1 defects or critical documentation absent; significant unresolved debt | Fail; restructure remaining phase scope; re-evaluate in 1 week |
| F | 0.0–2.9 | Fail — Critical | < 50% deliverables complete; P1 defects in shipped code; next phase prerequisites unmet | Fail; do not advance; immediate escalation to engineering leadership |

## Signal Tables

### Deliverable Completeness

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | 100% of phase deliverables meet their exit criteria with verified evidence; no items in "in-progress" at phase end |
| 7–8 | 90–99% of deliverables complete; 1–2 minor items incomplete with agreed completion date within next phase's first week |
| 5–6 | 75–89% complete; 3–5 items incomplete; some items are next-phase prerequisites, creating rework risk |
| 3–4 | 50–74% complete; multiple prerequisites for the next phase are undelivered; next phase cannot start cleanly |
| 0–2 | < 50% of deliverables complete; phase effectively did not achieve its stated goals; next phase inputs are absent |

### Quality Standard Adherence

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | All PRs reviewed before merge; test coverage ≥ 80% across all changed code; zero P1 or P2 defects in deliverables; all CI checks green at phase close |
| 7–8 | 90%+ PRs reviewed; coverage 70–79%; zero P1 defects; 1–2 P2 defects documented with accepted mitigation |
| 5–6 | 80%+ PRs reviewed; coverage 60–69%; zero P1 defects; 3–5 P2 defects with partial mitigation |
| 3–4 | Some PRs merged without review; coverage 50–59%; 1 P1 defect in non-critical path with documented workaround |
| 0–2 | Significant PRs unreviewed; coverage < 50%; P1 defects in critical user paths; CI checks failing at phase close |

### Documentation Completeness

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | All ADRs written and reviewed; API specs complete and published; runbooks current; design docs approved by relevant stakeholders |
| 7–8 | All ADRs written; API specs complete; 1–2 runbooks in draft state; design docs approved |
| 5–6 | Most ADRs written; API spec partially complete (critical endpoints documented); runbooks not yet written |
| 3–4 | ADRs for major decisions absent; API spec drafts only; no runbooks; design docs not reviewed |
| 0–2 | No ADRs; no published API specs; no runbooks; next phase team has insufficient documentation to begin work |

### Carried-Forward Debt

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Zero unmitigated debt entering next phase; all deferred items are non-blocking with logged tickets and assigned owners |
| 7–8 | 1–3 deferred items with documented rationale; none are next-phase prerequisites; tickets exist with priority labels |
| 5–6 | 4–6 deferred items; 1–2 are soft prerequisites for next phase; some items lack tickets or owners |
| 3–4 | 7–10 deferred items; 3+ are prerequisites for next phase; significant rework risk in next sprint |
| 0–2 | > 10 deferred items; multiple hard prerequisites unresolved; next phase will begin in a hole that compounds |
