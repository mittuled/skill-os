# Scoring Rubric: prd-nfr-compliance

Evaluates the completeness of a PRD non-functional compliance review covering requirement identification, NFR specificity, and integration quality.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Compliance Area Coverage | 30% | Completeness of identifying applicable compliance areas (privacy, accessibility, security, regulatory disclosures, audit logging) |
| 2 | NFR Specificity | 40% | Whether injected NFRs are testable with concrete acceptance criteria rather than vague compliance references |
| 3 | Integration Quality | 30% | Effectiveness of PRD integration including PM acknowledgment and engineering assignment |

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
| A+ | 9.0 – 10.0 | Exceptional | All compliance areas identified, every NFR has testable acceptance criteria, PRD fully integrated with PM sign-off | PRD ready for engineering |
| A | 8.0 – 8.9 | Strong | Major compliance areas covered, most NFRs testable, PRD integration complete | PRD ready with minor NFR refinements |
| B | 7.0 – 7.9 | Good | Core compliance areas identified, some NFRs need specificity improvement | Refine NFRs before engineering sprint planning |
| C | 5.0 – 6.9 | Adequate | Compliance areas partially identified, NFRs too vague for implementation | Revise: rewrite NFRs with testable criteria |
| D | 3.0 – 4.9 | Weak | Significant compliance gaps, NFRs not actionable | Block: major compliance review needed |
| F | 0.0 – 2.9 | Failing | No compliance review of PRD performed | Block: full review required before engineering |

## Signal Tables

### Compliance Area Coverage

| Score | Evidence |
|-------|----------|
| 9-10 | All applicable areas assessed: data privacy (GDPR consent, CCPA opt-out, data minimization, retention, deletion), accessibility (WCAG 2.1 AA), security (encryption, authentication, authorization), regulatory disclosures (terms acceptance, cookie consent, age verification), audit logging, and sector-specific requirements |
| 7-8 | Major compliance areas identified (privacy, accessibility, security), most sector-specific requirements captured |
| 5-6 | Core areas (privacy, security) addressed, accessibility or audit logging missed |
| 3-4 | Only obvious compliance areas noted (e.g., privacy only) |
| 0-2 | No systematic compliance area identification |

### NFR Specificity

| Score | Evidence |
|-------|----------|
| 9-10 | Every NFR has a concrete acceptance criterion (e.g., "Must provide data export endpoint returning user data in JSON within 30 days of request" not "Must comply with GDPR"). Each criterion is testable by QA. Measurable thresholds where applicable. |
| 7-8 | Most NFRs have testable criteria, minor items need specificity |
| 5-6 | Some NFRs testable, others still reference regulations without specific behaviors |
| 3-4 | NFRs reference regulations ("must comply with GDPR") without product-specific behaviors |
| 0-2 | No testable NFRs written |

### Integration Quality

| Score | Evidence |
|-------|----------|
| 9-10 | NFRs embedded in PRD with traceability to regulatory source, assigned to engineering team, PM has acknowledged and signed off, compliance NFR appendix attached |
| 7-8 | NFRs in PRD appendix, PM acknowledged, most items assigned to engineering |
| 5-6 | NFRs drafted but not yet integrated into PRD or not acknowledged by PM |
| 3-4 | NFRs delivered as a separate document without PRD integration |
| 0-2 | No integration with PRD or product process |
