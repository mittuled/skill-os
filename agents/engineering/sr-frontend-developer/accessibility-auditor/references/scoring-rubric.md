# Scoring Rubric: Accessibility Auditor

Evaluates the completeness and quality of a WCAG 2.1 AA accessibility audit across automated scanning, manual testing, finding classification, and remediation guidance.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Automated Scan Coverage | 20% | Completeness of automated tooling execution across all in-scope pages and components |
| 2 | Manual Testing Depth | 25% | Thoroughness of keyboard navigation, screen reader, and assistive technology testing |
| 3 | Finding Classification | 20% | Accuracy of WCAG criterion mapping, severity rating, and affected user group identification |
| 4 | Remediation Quality | 20% | Specificity and actionability of fix recommendations with code examples |
| 5 | Report Completeness | 15% | Presence of all required report sections with clear pass/fail verdict and release recommendation |
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
| A+ | 9.0 – 10.0 | Exceptional | All pages scanned and manually tested; every finding mapped to WCAG criterion with code-level fix; report includes clear verdict | Approve release with accessibility attestation |
| A | 8.0 – 8.9 | Strong | High scan coverage; thorough manual testing; most findings have specific remediation; minor report gaps | Approve release; address minor gaps in next cycle |
| B | 7.0 – 7.9 | Good | Scans complete but manual testing has gaps; findings classified but some remediation is generic | Conditionally approve; require manual testing completion |
| C | 5.0 – 6.9 | Adequate | Partial scan coverage; limited manual testing; findings lack WCAG criterion precision | Block release; expand audit scope before re-evaluation |
| D | 3.0 – 4.9 | Weak | Minimal automated scanning; no assistive technology testing; vague findings | Block release; restart audit with proper tooling and methodology |
| F | 0.0 – 2.9 | Failing | No audit performed or audit covers less than 20% of scope | Reject; full audit required before any release consideration |

## Signal Tables

### Automated Scan Coverage
| Score | Evidence |
|-------|----------|
| 9-10 | axe-core and Lighthouse run on 100% of in-scope pages; all component states (default, hover, error, disabled) scanned; results include severity and element selectors |
| 7-8 | Scans run on all primary pages; most component states covered; minor pages or modals may be missed |
| 5-6 | Scans run on critical pages only; dynamic content and modal dialogs not scanned; results lack element-level detail |
| 3-4 | Single scan tool run on homepage and one other page; no state-specific scanning |
| 0-2 | No automated scans executed or scan results not captured |

### Manual Testing Depth
| Score | Evidence |
|-------|----------|
| 9-10 | Full keyboard navigation tested on all flows; VoiceOver and NVDA screen reader testing completed; focus order, heading hierarchy, landmark regions, and ARIA attributes verified |
| 7-8 | Keyboard navigation tested on critical flows; one screen reader tested; focus management and heading hierarchy verified |
| 5-6 | Keyboard navigation tested on primary flow only; no screen reader testing; focus indicators visually checked |
| 3-4 | Tab-through-page test only; no assistive technology testing; no focus order verification |
| 0-2 | No manual testing performed |

### Finding Classification
| Score | Evidence |
|-------|----------|
| 9-10 | Every finding mapped to specific WCAG success criterion (e.g., 1.3.1, 2.4.7); severity rated as critical/major/minor with justification; affected user groups identified (blind, motor-impaired, cognitive) |
| 7-8 | Findings mapped to WCAG criteria; severity assigned; user group impact noted for critical findings |
| 5-6 | Findings reference WCAG guidelines broadly (e.g., "Perceivable") but not specific criteria; severity assigned without clear rationale |
| 3-4 | Findings listed without WCAG references; severity based on developer judgment rather than standard |
| 0-2 | Raw tool output with no classification or interpretation |

### Remediation Quality
| Score | Evidence |
|-------|----------|
| 9-10 | Every finding has a specific fix with before/after code examples; effort estimates provided; fixes reference ARIA authoring practices or MDN documentation |
| 7-8 | Critical and major findings have code-level fixes; minor findings have descriptive guidance; effort estimates for critical fixes |
| 5-6 | Findings have descriptive fix suggestions but no code examples; effort not estimated |
| 3-4 | Generic recommendations like "fix accessibility" or "add ARIA labels" without specifics |
| 0-2 | No remediation guidance provided |

### Report Completeness
| Score | Evidence |
|-------|----------|
| 9-10 | Report includes scope definition, automated results, manual results, classified findings, remediation plan, overall verdict, and release recommendation with stakeholder notification |
| 7-8 | All major sections present; verdict and recommendation clear; minor formatting or completeness gaps |
| 5-6 | Results and findings present but verdict is ambiguous; release recommendation missing or unclear |
| 3-4 | Partial report with either automated or manual results but not both; no clear verdict |
| 0-2 | No structured report; only raw tool output or verbal summary |
