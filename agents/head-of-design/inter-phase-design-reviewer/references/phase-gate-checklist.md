# Phase Gate Checklist: Design Phase Transitions

Defines the exit criteria and quality bar for each design phase before progression to the next.

---

## Phase 1 → Phase 2: Discovery to Definition

**Goal of Discovery:** Understand the problem space, user needs, and constraints before committing to a design direction.

### Required Deliverables

| Deliverable | Exit Criteria |
|-------------|--------------|
| Research synthesis | At least one round of user research completed; key insights documented with evidence |
| JTBD or problem statement | User jobs/problems articulated; validated with at least minimal data |
| Competitor or analogous examples | At least 3 references reviewed; design principles extracted |
| Technical feasibility check | Engineering reviewed for major constraints |
| Scope alignment | Product, design, and engineering agree on what is in/out of scope |

### Quality Gates

- [ ] Research insights are actionable (not just observations)
- [ ] Problem statement is specific enough to evaluate design solutions against
- [ ] No major technical blockers unresolved
- [ ] Stakeholder alignment confirmed (no open "should we do this?" questions)

**Advisory (track, not block):**
- Quantitative baseline data for the problem area (analytics, surveys)
- Competitive positioning notes

---

## Phase 2 → Phase 3: Definition to Production

**Goal of Definition:** Produce validated information architecture and wireframes that establish structure before investing in visual design.

### Required Deliverables

| Deliverable | Exit Criteria |
|-------------|--------------|
| User flows | All primary, error, and edge case paths documented |
| Wireframes | All in-scope screens covered at all required breakpoints |
| Content inventory | Key content and copy requirements identified |
| Component mapping | Existing components mapped; new components or variants identified |
| Usability test or design review | At least one validation round completed (test or structured review) |

### Quality Gates

- [ ] All interaction states specified (happy path, empty, error, loading, disabled)
- [ ] Responsive breakpoints defined and wireframed
- [ ] Component gaps resolved or tracked as tickets
- [ ] Design brief acceptance criteria checked against wireframes
- [ ] Accessibility requirements identified (WCAG level, key interaction patterns)

**Advisory (track, not block):**
- Prototype tested with users (5+ participants preferred)
- Content copy drafted (not just labelled)

---

## Phase 3 → Handoff: Production to Handoff

**Goal of Production:** Deliver pixel-ready, annotated designs that engineering can implement without guessing.

### Required Deliverables

| Deliverable | Exit Criteria |
|-------------|--------------|
| Visual designs | All screens and states designed at final fidelity |
| Redlines / design tokens | Spacing, typography, colour tokens annotated per screen |
| Interaction specs | Transitions, timing, easing, and gesture specs documented |
| Accessibility annotations | Focus order, ARIA roles, contrast ratios annotated |
| Design system sync | New components published to Figma library; tokens updated |
| Prototype for handoff | Interactive prototype covering primary flows |

### Quality Gates

- [ ] All interaction states present: happy path, empty, error, loading, disabled
- [ ] All responsive breakpoints designed
- [ ] Design system components used correctly (no detached instances without rationale)
- [ ] Colour contrast passes WCAG 2.1 AA (4.5:1 text, 3:1 UI)
- [ ] Accessibility annotations complete
- [ ] Content design spec compliance verified (no placeholder copy in production designs)
- [ ] Design review completed; all blocking issues resolved

**Advisory (track, not block):**
- Motion / animation specs
- Edge case documentation beyond primary error states

---

## Verdict Definitions

| Verdict | Meaning | Next Action |
|---------|---------|-------------|
| **Approved** | All required deliverables present; all quality gates pass | Proceed to next phase immediately |
| **Conditionally Approved** | Required deliverables present; 1–3 quality gates have tracked issues with owners and due dates | Proceed to next phase; resolve tracked issues within agreed timeframe |
| **Blocked** | One or more required deliverables missing or quality gates contain unresolved critical issues | Do not proceed; rework required before re-review |

---

## Re-Review Trigger Conditions

Schedule a phase gate re-review when:
- New scope is added after the original gate review
- A major technical constraint changes the feasible design space
- User research invalidates the approved direction
- More than 30% of screens are revised post-gate
