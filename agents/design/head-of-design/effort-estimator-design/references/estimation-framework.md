# Design Effort Estimation Framework

A structured model for estimating design work with consistent sizing, complexity factors, and confidence levels.

## Core Methodology

Design effort estimation decomposes a feature into discrete deliverables, applies complexity multipliers, adds a review buffer, and outputs a range (optimistic / expected / pessimistic) with a confidence level.

**Formula:**
> Effort = (Base Hours × Complexity Multiplier) + Review Buffer

---

## Deliverable Inventory — Base Hours

| Deliverable Type | Low Complexity | Medium Complexity | High Complexity |
|-----------------|---------------|------------------|-----------------|
| User flow (per flow) | 2–4 h | 4–8 h | 8–16 h |
| Wireframes (per screen) | 1–2 h | 2–4 h | 4–8 h |
| Visual design (per screen) | 2–4 h | 4–8 h | 8–16 h |
| Prototype (interactive, per flow) | 4–8 h | 8–16 h | 16–32 h |
| Design system update (new component) | 4–8 h | 8–16 h | 16–40 h |
| Design system update (new variant) | 1–2 h | 2–4 h | 4–8 h |
| Handoff spec / redlines | 1–2 h | 2–4 h | 4–8 h |
| Content / copy for UI | 1–3 h | 3–6 h | 6–12 h |

---

## Complexity Factors

Apply the highest applicable multiplier. Do not stack multipliers.

| Factor | Multiplier | When to Apply |
|--------|-----------|---------------|
| Existing component reuse only | 0.7× | All screens use existing design system components without modification |
| Baseline (new layout, reusing patterns) | 1.0× | Mix of new layouts with existing components |
| Novel interaction pattern | 1.5× | Requires new interaction paradigm not in current system |
| Multi-platform (2 platforms) | 1.4× | Design targets web + mobile, or iOS + Android |
| Multi-platform (3+ platforms) | 1.8× | Design targets web + iOS + Android or more |
| Accessibility-first (WCAG AAA) | 1.2× | Higher than standard AA compliance required |
| Complex animation / motion | 1.3× | Detailed motion specs, micro-interaction design included |

---

## Review Buffer

Add buffer for feedback and iteration cycles based on project type:

| Project Type | Review Rounds | Buffer |
|-------------|---------------|--------|
| Internal tool / admin | 1–2 | +20% |
| B2B SaaS feature | 2–3 | +30% |
| Consumer-facing / high visibility | 3–4 | +40% |
| Full redesign / rebrand | 4+ | +50% |

---

## T-Shirt Size Reference

| Size | Hour Range | Typical Scope |
|------|------------|---------------|
| XS | < 4 h | Single component variant or micro-interaction |
| S | 4–8 h | One screen, one flow segment |
| M | 8–24 h | Full feature flow (3–6 screens) |
| L | 24–60 h | Multi-flow feature with system updates |
| XL | 60–120 h | Major feature area with new components |
| XXL | 120+ h | Platform-wide redesign or new product area |

---

## Confidence Levels

| Level | Conditions |
|-------|-----------|
| High | Requirements are fully defined; user flows exist; component scope is known |
| Medium | Requirements mostly defined; some edge cases unclear; component scope partially known |
| Low | Requirements are conceptual; user flows not yet designed; significant unknowns remain |

At Low confidence, present estimate as a range (±40%) and flag the assumptions that would collapse uncertainty.

---

## Design Debt Factor

When a feature touches areas with known design debt (inconsistent patterns, deprecated components, incomplete state coverage), apply an additional design debt factor:

| Debt Level | Additional Overhead |
|------------|-------------------|
| None | 0% |
| Minor (a few inconsistencies) | +10% |
| Moderate (systemic inconsistency in this area) | +20% |
| Severe (area needs refactoring before feature work) | +30–50% (separate cleanup ticket recommended) |

---

## Estimation Checklist

Before submitting an estimate, verify:
- [ ] Feature decomposed into individual deliverable types
- [ ] Complexity factor selected per deliverable
- [ ] Review buffer applied per project type
- [ ] Design debt factor assessed
- [ ] Responsive breakpoints counted (each adds ~20% to screen-level estimates)
- [ ] Confidence level declared with assumptions listed
- [ ] Estimate presented as a range (optimistic / expected / pessimistic)
