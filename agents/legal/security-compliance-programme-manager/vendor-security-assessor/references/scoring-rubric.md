# Scoring Rubric: vendor-security-assessor

Evaluates the completeness and rigour of a vendor security assessment covering tiering, questionnaire review, gap analysis, and monitoring planning.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Vendor Tiering | 15% | Accuracy of risk tier classification based on data access, system access, and business criticality |
| 2 | Security Posture Review | 30% | Depth of questionnaire analysis, certification review, and security practice evaluation |
| 3 | Gap Analysis | 30% | Quality of identifying gaps against organizational security requirements with risk ratings |
| 4 | Decision and Monitoring | 25% | Rigour of approve/conditional/reject decision with ongoing monitoring plan |

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
| A+ | 9.0 – 10.0 | Exceptional | Vendor correctly tiered, security posture thoroughly reviewed, all gaps identified with risk ratings, clear decision with monitoring plan | Approve vendor with standard monitoring |
| A | 8.0 – 8.9 | Strong | Tiering accurate, posture reviewed, major gaps identified, decision documented | Approve with monitoring plan |
| B | 7.0 – 7.9 | Good | Tiering reasonable, questionnaire reviewed, most gaps identified | Approve with conditions and enhanced monitoring |
| C | 5.0 – 6.9 | Adequate | Tiering done, questionnaire partially reviewed, gap analysis incomplete | Request additional information before decision |
| D | 3.0 – 4.9 | Weak | Tiering unclear, superficial review, significant gaps missed | Re-assess with complete questionnaire and documentation |
| F | 0.0 – 2.9 | Failing | No meaningful vendor security assessment performed | Block vendor onboarding until assessment complete |

## Signal Tables

### Vendor Tiering

| Score | Evidence |
|-------|----------|
| 9-10 | Vendor classified on all three dimensions (data access: none/metadata/PII/sensitive PII; system access: none/read-only/read-write/admin; business criticality: replaceable/important/critical). Tier determines assessment depth. Tiering rationale documented. |
| 7-8 | Tiering covers data access and system access, business criticality assessed |
| 5-6 | Tiering performed but only considers one dimension (e.g., data access without system access) |
| 3-4 | Vendor categorized generically ("high risk" / "low risk") without structured criteria |
| 0-2 | No vendor tiering performed |

### Security Posture Review

| Score | Evidence |
|-------|----------|
| 9-10 | Security questionnaire reviewed in full, SOC 2 report reviewed (scope, exceptions, complementary user entity controls), ISO 27001 certificate verified (scope, validity), penetration test summary reviewed, security policies assessed, insurance coverage confirmed |
| 7-8 | Questionnaire and primary certification reviewed, most security domains assessed |
| 5-6 | Questionnaire reviewed but certifications accepted at face value without scope/exception review |
| 3-4 | Partial questionnaire review, certifications noted but not reviewed |
| 0-2 | No security posture review performed |

### Gap Analysis

| Score | Evidence |
|-------|----------|
| 9-10 | Vendor posture compared against organizational requirements for: encryption (at rest, in transit), access controls, incident response, business continuity, data handling, sub-processor management. Each gap rated by risk level. Compensating controls identified where applicable. |
| 7-8 | Major security domains compared against requirements, gaps rated |
| 5-6 | Some gaps identified but not systematically compared against requirements |
| 3-4 | Generic concerns noted without structured gap analysis |
| 0-2 | No gap analysis performed |

### Decision and Monitoring

| Score | Evidence |
|-------|----------|
| 9-10 | Clear approve/conditional/reject decision with documented rationale. For conditional: specific remediation requirements with deadlines. Monitoring plan: annual reassessment, certification renewal tracking, breach monitoring, scope change triggers. Contractual security requirements defined. |
| 7-8 | Decision documented with rationale, monitoring cadence defined |
| 5-6 | Decision made but monitoring plan incomplete or conditions vague |
| 3-4 | Informal decision without documentation or monitoring |
| 0-2 | No decision or monitoring plan |
