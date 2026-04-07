# Scoring Rubric: Accessibility Auditor Design

Evaluates the rigour and completeness of an accessibility audit across automated coverage, manual testing depth, finding classification, remediation quality, and report clarity.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Automated Coverage | 15% | Breadth and accuracy of automated accessibility scanning across all scoped surfaces |
| 2 | Manual Testing Depth | 25% | Thoroughness of assistive technology testing including keyboard, screen reader, magnification, and reduced motion |
| 3 | Finding Classification | 20% | Accuracy of WCAG criterion mapping, severity rating, and affected-population assessment per finding |
| 4 | Remediation Specificity | 25% | Actionability of remediation recommendations with design-level fixes, owner assignments, and effort estimates |
| 5 | Report Clarity | 15% | Structured presentation with executive summary, compliance scorecard, and stakeholder-appropriate communication |
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
| A+ | 9.0 – 10.0 | Exceptional | All WCAG principles covered with assistive tech validation; every finding has specific design-level remediation | Approve and schedule periodic re-audit at 6-month cadence |
| A | 8.0 – 8.9 | Strong | Comprehensive coverage with minor gaps in edge-case assistive technology combinations | Approve with follow-up on flagged AT gaps within next sprint |
| B | 7.0 – 7.9 | Good | Solid automated and manual coverage but remediation lacks design specificity or effort estimates | Approve conditionally; strengthen remediation plan before handoff |
| C | 5.0 – 6.9 | Adequate | Core WCAG criteria checked but manual testing limited to one AT; findings lack precise criterion mapping | Revise audit; expand manual testing before releasing findings |
| D | 3.0 – 4.9 | Weak | Automated-only audit or significant WCAG principles untested; generic remediation recommendations | Rework with dedicated assistive technology testing sessions |
| F | 0.0 – 2.9 | Failing | No systematic audit performed; findings are anecdotal or untraceable to WCAG | Halt and commission a full accessibility audit engagement |

## Signal Tables

### Automated Coverage
| Score | Evidence |
|-------|----------|
| 9-10 | axe-core, Lighthouse, and colour-contrast analyser run on every scoped page; all violations logged with WCAG criterion, element selector, and screenshot |
| 7-8 | Two automated tools used across most pages; minor pages or dynamically-loaded content omitted with justification |
| 5-6 | Single tool run on key pages only; dynamic content and modal overlays not scanned |
| 3-4 | Automated scan run on homepage or a few representative pages; most surfaces unscanned |
| 0-2 | No automated scanning performed |

### Manual Testing Depth
| Score | Evidence |
|-------|----------|
| 9-10 | Keyboard navigation, VoiceOver, NVDA, TalkBack, magnification (200%), reduced motion, and high-contrast mode all tested on scoped flows |
| 7-8 | Keyboard and two screen readers tested; magnification or reduced motion tested on critical flows only |
| 5-6 | Keyboard-only testing completed; one screen reader tested superficially |
| 3-4 | Keyboard testing on primary happy path only; no screen reader testing |
| 0-2 | No manual assistive technology testing performed |

### Finding Classification
| Score | Evidence |
|-------|----------|
| 9-10 | Every finding maps to a specific WCAG 2.1 success criterion; severity rated by impact on task completion, affected population size, and workaround availability |
| 7-8 | Findings mapped to WCAG criteria with severity ratings; minor inconsistencies in population impact assessment |
| 5-6 | Findings reference WCAG principles (Perceivable, Operable) but not specific success criteria; severity ratings present but not consistently justified |
| 3-4 | Findings listed without WCAG mapping; severity based on subjective assessment |
| 0-2 | Findings are vague descriptions without criterion or severity |

### Remediation Specificity
| Score | Evidence |
|-------|----------|
| 9-10 | Every critical/major finding has a named design change (updated colour token, focus ring spec, ARIA label text), assigned owner, and effort estimate |
| 7-8 | Remediation specified for most findings with design-level detail; effort estimates present for critical items |
| 5-6 | Remediation described in general terms without specific token values or component references |
| 3-4 | Generic recommendations without design-level guidance |
| 0-2 | No remediation recommendations provided |

### Report Clarity
| Score | Evidence |
|-------|----------|
| 9-10 | Executive summary with pass/fail verdict, compliance scorecard per WCAG principle, prioritised issue register, and remediation timeline — all audience-appropriate |
| 7-8 | Structured report with summary and scorecard; minor gaps in stakeholder-appropriate framing |
| 5-6 | Findings documented but no executive summary or compliance scorecard; raw findings list only |
| 3-4 | Informal notes or spreadsheet of issues without structure or summary |
| 0-2 | No structured report produced |
