# Scoring Rubric: product-legal-reviewer

Evaluates the completeness of a product legal review covering feature intake, regulatory mapping, risk assessment, and clearance quality.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Feature Intake Quality | 15% | Completeness of feature understanding including purpose, data handling, monetization, and target users |
| 2 | Regulatory Mapping | 30% | Thoroughness of identifying all applicable regulations by jurisdiction for the feature |
| 3 | Risk Assessment | 30% | Quality of compliance gap identification with severity classification and likelihood evaluation |
| 4 | Recommendation and Clearance | 25% | Actionability of recommendations with compliant alternatives and clear clearance status |

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
| A+ | 9.0 – 10.0 | Exceptional | Feature fully understood, all regulations mapped, gaps identified with alternatives, clearance issued with documented scope | Feature cleared for launch |
| A | 8.0 – 8.9 | Strong | Thorough review with minor gaps in international regulation coverage | Clear with minor conditions |
| B | 7.0 – 7.9 | Good | Major regulations mapped, most gaps identified, recommendations provided | Clear with conditions: address gaps within defined window |
| C | 5.0 – 6.9 | Adequate | Core regulations identified, risk assessment incomplete, some recommendations generic | Hold: complete risk assessment before clearance |
| D | 3.0 – 4.9 | Weak | Significant regulatory gaps, risk assessment superficial | Block: major review revision required |
| F | 0.0 – 2.9 | Failing | No systematic product legal review performed | Block: full review required |

## Signal Tables

### Feature Intake Quality

| Score | Evidence |
|-------|----------|
| 9-10 | Feature specification reviewed, user flows mapped, data practices documented, monetization approach understood, target user segments identified, geographic reach confirmed |
| 7-8 | Feature purpose and data practices understood, most user flows reviewed |
| 5-6 | High-level feature understanding without detailed data flow or user flow review |
| 3-4 | Minimal feature understanding from brief description only |
| 0-2 | No feature intake performed |

### Regulatory Mapping

| Score | Evidence |
|-------|----------|
| 9-10 | All applicable regulations identified by jurisdiction: consumer protection, privacy (GDPR, CCPA), accessibility (ADA, WCAG), advertising, financial services, health (HIPAA), sector-specific rules. Regulatory applicability matrix produced with specific article references. |
| 7-8 | Major regulations identified for primary jurisdictions, applicability matrix produced |
| 5-6 | Core US/EU regulations identified, sector-specific or emerging market regulations missed |
| 3-4 | Generic regulatory awareness without jurisdiction-specific mapping |
| 0-2 | No regulatory mapping performed |

### Risk Assessment

| Score | Evidence |
|-------|----------|
| 9-10 | Each applicable requirement assessed against feature design with specific gap identification. Gaps classified as blocking/recommended/advisory with likelihood and severity. Ambiguous items flagged for General Counsel escalation. |
| 7-8 | Major gaps identified and classified, most items assessed against feature design |
| 5-6 | Some gaps identified but classification inconsistent or likelihood not evaluated |
| 3-4 | Generic risk concerns without specific gap identification |
| 0-2 | No risk assessment performed |

### Recommendation and Clearance

| Score | Evidence |
|-------|----------|
| 9-10 | Actionable recommendation for each gap with compliant alternative that achieves the product goal. Clearance issued with documented scope, assumptions, and conditions. Blocking items clearly distinguished from advisory. |
| 7-8 | Recommendations provided for most gaps with alternatives, clearance status clear |
| 5-6 | Recommendations provided but alternatives incomplete or clearance scope undefined |
| 3-4 | Issues flagged without alternatives or clearance decision |
| 0-2 | No recommendations or clearance provided |
