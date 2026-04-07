# Component Inventory & Gap Analysis

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [UX/UI Designer] |
| Feature | [Feature or surface name] |
| Design System Version | [e.g. v2.4.1] |
| Figma Library | [Link to design system Figma file] |
| Version | [1.0] |
| Status | [Draft / Review / Approved] |

## Summary

[1-2 sentences stating the overall coverage result — how many elements are needed, how many exist in the design system, and how many are gaps requiring new component work. GUIDANCE: e.g. "22 UI elements required for the checkout redesign; 17 (77%) are covered by existing design system components. 5 new components or variants are needed before production design can begin."]

## Component Audit Table

[List every UI element required for the feature, mapped to its design system counterpart.]

| # | UI Element Required | DS Component Name | DS Status | Variant Available | Action Required |
|---|--------------------|--------------------|-----------|------------------|-----------------|
| 1 | [e.g. Primary action button] | [Button / Primary] | [Exists] | [Yes — default + loading + disabled] | [Use as-is] |
| 2 | [e.g. Quantity stepper with +/- controls] | [Stepper] | [Exists] | [Yes — compact variant] | [Use compact variant] |
| 3 | [e.g. Product image carousel] | [None] | [Missing] | [N/A] | [New component needed] |
| 4 | [e.g. Inline validation error text] | [Form / Error text] | [Exists] | [Yes] | [Use as-is] |
| 5 | [e.g. Order summary card] | [Card / Summary] | [Partial] | [No — needs new condensed variant] | [New variant needed] |
| 6 | [e.g. Payment method selector row] | [None] | [Missing] | [N/A] | [New component needed] |
| 7 | [e.g. Progress stepper (3 steps)] | [None] | [Missing] | [N/A] | [New component needed — design first] |
| 8 | [e.g. Toast notification — success] | [Toast / Success] | [Exists] | [Yes] | [Use as-is] |
| 9 | [Description] | [DS name] | [Status] | [Yes/No] | [Action] |
| 10 | [Description] | [DS name] | [Status] | [Yes/No] | [Action] |

**DS Status options**: Exists | Partial | Missing

## Coverage Summary

| Category | Count |
|----------|-------|
| Elements audited | [X] |
| Covered by existing components | [X] |
| Covered by adding a new variant to existing component | [X] |
| Require net-new components | [X] |
| **Coverage rate** | **[X%]** |

## New Component Specifications

[For each component that needs to be created, provide the brief for the component build.]

### [New Component 1]: [Component Name]

**Rationale**: [Why this cannot be satisfied by an existing DS component]
**Proposed location in DS**: [e.g. Navigation > Stepper]
**Variants required**: [List variants needed — e.g. 2-step, 3-step, 4-step; horizontal, vertical]
**States required**: [Default, active step, completed step, error]
**Reference UI**: [Link or description of analogous pattern from another product / DS]
**Design owner**: [Designer name]
**Target sprint**: [Sprint]

---

### [New Component 2]: [Component Name]

**Rationale**: [Reason]
**Proposed location in DS**: [Category > Name]
**Variants required**: [List]
**States required**: [List]
**Reference UI**: [Link or description]
**Design owner**: [Name]
**Target sprint**: [Sprint]

---

## Deviations from Design System

[Document any intentional deviations from the design system for this feature, with rationale and approval status.]

| Element | DS Guideline | Deviation | Rationale | Approved By |
|---------|-------------|-----------|-----------|-------------|
| [e.g. Primary button — colour] | [Blue #0057FF] | [Green #00A36C for checkout flow] | [Green = payment convention; reduces cognitive dissonance in checkout] | [Head of Design] |

## Next Steps

- [ ] Submit new component briefs to design system owner by [date]
- [ ] Confirm DS team capacity for new component builds
- [ ] Unblock production design tickets that depend on new components
- [ ] Update component inventory on completion of each new component
