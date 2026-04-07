# Scoring Rubric: Accessibility Checker (Engineering)

Evaluates the quality of in-development accessibility checks on PR-level code changes against WCAG 2.1 AA standards.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Lint Coverage | 20% | Completeness of automated a11y linting across changed files |
| 2 | Semantic Validation | 25% | Correctness of HTML semantics, heading hierarchy, landmarks, and ARIA usage |
| 3 | Keyboard Interaction | 25% | Verification that all interactive elements are keyboard-operable with visible focus |
| 4 | Finding Specificity | 30% | Precision of reported issues with element references, WCAG criteria, and fix suggestions |
| **Total** | | **100%** | |

## Scale

Each criterion is scored **0-10**:
- **0**: No evidence / completely absent
- **5**: Partially present with significant gaps
- **10**: Fully present, comprehensive, no gaps

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 – 10.0 | Exceptional | All changed components linted, semantics verified, keyboard tested, findings specific with code fixes | Approve PR with a11y sign-off |
| A | 8.0 – 8.9 | Strong | Lint and semantic checks complete; keyboard tested on primary interactions; findings actionable | Approve PR; minor a11y notes as follow-up |
| B | 7.0 – 7.9 | Good | Linting complete; semantic review done; keyboard testing partial; findings mostly specific | Request fixes for keyboard gaps before merge |
| C | 5.0 – 6.9 | Adequate | Linting run but semantic review incomplete; keyboard testing limited; findings lack specificity | Request revisions; expand review scope |
| D | 3.0 – 4.9 | Weak | Partial linting only; no semantic or keyboard review; findings vague | Block PR; full a11y check required |
| F | 0.0 – 2.9 | Failing | No accessibility checking performed on the changeset | Reject PR; a11y review is mandatory |

## Signal Tables

### Lint Coverage
| Score | Evidence |
|-------|----------|
| 9-10 | eslint-plugin-jsx-a11y or equivalent run on all changed files; zero suppressions without justification; custom rules for project-specific patterns |
| 7-8 | Linting run on all changed files; a few suppressions documented with rationale |
| 5-6 | Linting run on most files; some changed components not covered; suppressions present without documentation |
| 3-4 | Linting run on a single file or component; majority of changeset not checked |
| 0-2 | No linting executed or lint results not reviewed |

### Semantic Validation
| Score | Evidence |
|-------|----------|
| 9-10 | Heading hierarchy verified (no skipped levels); landmark regions present; ARIA roles match WAI-ARIA authoring practices; no div/span used where semantic element exists |
| 7-8 | Heading hierarchy correct; landmarks present; ARIA usage mostly correct with minor issues noted |
| 5-6 | Heading structure checked but landmarks not verified; ARIA usage not reviewed against authoring practices |
| 3-4 | Basic HTML reviewed but no semantic analysis; ARIA attributes present but not validated |
| 0-2 | No semantic review performed |

### Keyboard Interaction
| Score | Evidence |
|-------|----------|
| 9-10 | All interactive elements (buttons, links, inputs, custom widgets) focusable and operable via keyboard; focus order logical; focus indicators visible; focus traps managed |
| 7-8 | Primary interactive elements keyboard-tested; focus order reasonable; focus indicators present |
| 5-6 | Tab-through tested on main flow; custom widgets not keyboard-tested; focus indicators not verified |
| 3-4 | Basic tab navigation checked; no custom widget or focus trap testing |
| 0-2 | No keyboard testing performed |

### Finding Specificity
| Score | Evidence |
|-------|----------|
| 9-10 | Each finding references specific element (CSS selector or JSX path), WCAG success criterion, severity, and includes a code-level fix suggestion |
| 7-8 | Findings reference elements and WCAG criteria; fix suggestions provided for critical issues |
| 5-6 | Findings reference WCAG guidelines but not specific criteria; element references vague (e.g., "the form") |
| 3-4 | Generic findings like "improve accessibility" without element or criterion references |
| 0-2 | No findings documented or only lint output without interpretation |
