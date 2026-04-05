# Scoring Rubric: design-implementer-review

Evaluates the fidelity and completeness of an engineering implementation against approved design specifications.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Visual Fidelity | 25% | Spacing, typography, colour tokens, border radii, elevation match Figma redlines |
| 2 | Interaction Completeness | 25% | All states rendered correctly: hover, focus, active, disabled, error, loading, empty |
| 3 | Responsive Behaviour | 20% | Layout reflow and component adaptation correct at all specified breakpoints |
| 4 | Accessibility Implementation | 20% | Focus order, ARIA labels, keyboard navigation, colour contrast verified in live DOM |
| 5 | Design System Compliance | 10% | Correct components used per mapping; no detached or improvised implementations |
| **Total** | | **100%** | |

## Scale: 0–10. Composite = Σ(score × weight)

## Grade Bands

| Grade | Score | Label | Description | Action |
|-------|-------|-------|-------------|--------|
| A+ | 9.0–10.0 | Exceptional | Implementation matches design with zero blocking deviations | Approve; file cosmetic notes as tickets |
| A | 8.0–8.9 | Strong | One or two minor deviations; no interaction or accessibility gaps | Approve; file deviations as tickets |
| B | 7.0–7.9 | Good | A few noticeable deviations; all states present | Conditional approve; fix deviations before release |
| C | 5.0–6.9 | Adequate | Multiple visual or state gaps; some states missing | Needs revision; file blocking tickets |
| D | 3.0–4.9 | Weak | Significant visual drift; key states missing; accessibility failures | Do not release; rework required |
| F | 0.0–2.9 | Failing | Implementation does not resemble design; major accessibility or functionality issues | Full reimplementation needed |

## Signal Tables

### Visual Fidelity

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Spacing within 2px of spec; token values exact; typography weight, size, and line-height match |
| 7–8 | Minor spacing deviations (4px or less); typography and colour tokens correct |
| 5–6 | Noticeable spacing drift (8px+ in places); some colours not from token set |
| 3–4 | Layout noticeably different from spec; hard-coded values used for colour or spacing |
| 0–2 | Implementation visually unrecognisable from design; no token usage |

### Interaction Completeness

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Every state present and correct: happy, loading, error, empty, disabled, hover, focus, active |
| 7–8 | All primary states correct; one minor state (tooltip, pressed) missing or imprecise |
| 5–6 | Happy path and error states present; loading or empty states improvised or missing |
| 3–4 | Only happy path implemented; error and empty states missing or placeholder |
| 0–2 | Multiple states missing; implementation is happy-path-only |

### Accessibility Implementation

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Focus order logical; all ARIA labels present; colour contrast passes AA; keyboard nav complete |
| 7–8 | ARIA labels present; minor focus order issue; keyboard nav works |
| 5–6 | Some ARIA labels missing; focus visible but order not fully logical |
| 3–4 | Focus management broken; ARIA labels largely absent; contrast issues present |
| 0–2 | No focus management; inaccessible to keyboard or screen reader users |
