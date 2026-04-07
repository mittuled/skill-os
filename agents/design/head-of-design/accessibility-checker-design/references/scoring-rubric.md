# Scoring Rubric: Accessibility Checker Design

Evaluates the thoroughness of a pre-handoff accessibility check across contrast compliance, interaction state coverage, content accessibility, finding documentation, and gate-decision clarity.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Contrast & Sizing Compliance | 25% | Verification of WCAG colour contrast ratios and minimum touch target sizes across all components |
| 2 | Interaction State Coverage | 25% | Completeness of focus, hover, active, disabled, and error state documentation |
| 3 | Content Accessibility | 20% | Alt text specs, ARIA label annotations, heading hierarchy, and error message adjacency |
| 4 | Finding Documentation | 15% | Specificity of each finding with WCAG criterion, affected component, and recommended fix |
| 5 | Gate Decision Clarity | 15% | Clear pass/conditional/fail verdict with required fixes listed for conditional passes |
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
| A+ | 9.0 – 10.0 | Exceptional | Every component verified for contrast, all states documented, ARIA annotations complete | Approve for dev handoff |
| A | 8.0 – 8.9 | Strong | Minor gaps in edge-case state coverage or content annotations | Approve with minor fixes before handoff |
| B | 7.0 – 7.9 | Good | Core checks pass but interaction states or ARIA annotations incomplete for some components | Conditional pass; complete missing state documentation |
| C | 5.0 – 6.9 | Adequate | Contrast checks done but interaction states or content accessibility largely unchecked | Revise check; expand coverage before handoff |
| D | 3.0 – 4.9 | Weak | Only superficial contrast check; most accessibility dimensions uncovered | Rework check with full WCAG criteria |
| F | 0.0 – 2.9 | Failing | No meaningful accessibility checking performed | Block handoff until check is completed |

## Signal Tables

### Contrast & Sizing Compliance
| Score | Evidence |
|-------|----------|
| 9-10 | All text/background pairs verified at 4.5:1 (normal) and 3:1 (large); all touch targets confirmed at 44x44pt minimum; colour-only indicators flagged and alternatives specified |
| 7-8 | Primary text pairs verified; most touch targets checked; one or two colour-only indicators noted |
| 5-6 | Key screens checked for contrast but not exhaustive; touch target verification inconsistent |
| 3-4 | Spot-check of obvious contrast issues; no systematic touch target verification |
| 0-2 | No contrast or sizing verification performed |

### Interaction State Coverage
| Score | Evidence |
|-------|----------|
| 9-10 | Every interactive element has documented focus, hover, active, disabled, and error states with focus order annotations following logical reading order |
| 7-8 | Most interactive elements have all states; minor gaps in focus order documentation |
| 5-6 | Primary buttons and inputs have states; secondary elements or complex components missing state documentation |
| 3-4 | Only default and hover states documented; focus, disabled, and error states absent |
| 0-2 | No interaction state documentation |

### Content Accessibility
| Score | Evidence |
|-------|----------|
| 9-10 | Alt text specified for all images, ARIA labels for all icons and controls, heading hierarchy documented, error messages descriptive and field-adjacent |
| 7-8 | Alt text and ARIA labels present for most elements; minor gaps in heading hierarchy documentation |
| 5-6 | Some alt text specified; ARIA labels missing for icon-only buttons; heading hierarchy informal |
| 3-4 | Sporadic alt text; no ARIA annotations; heading hierarchy not documented |
| 0-2 | No content accessibility specifications |

### Finding Documentation
| Score | Evidence |
|-------|----------|
| 9-10 | Each issue cites specific WCAG criterion, identifies the affected component/screen, and provides a concrete recommended fix |
| 7-8 | Findings reference WCAG criteria with component identification; fixes suggested for most issues |
| 5-6 | Findings listed but WCAG criteria not consistently cited; fixes are general suggestions |
| 3-4 | Issues noted informally without WCAG references or structured documentation |
| 0-2 | No findings documented |

### Gate Decision Clarity
| Score | Evidence |
|-------|----------|
| 9-10 | Clear pass/conditional-pass/fail verdict communicated to designer and product; conditional passes list every required fix |
| 7-8 | Verdict issued with most required fixes listed; minor ambiguity in conditional requirements |
| 5-6 | Verdict given but required fixes for conditional pass are vague or incomplete |
| 3-4 | No formal verdict; findings shared without a clear decision |
| 0-2 | No gate decision communicated |
