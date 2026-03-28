# Scoring Rubric: compliance-scanner

Evaluates the company's regulatory compliance posture across all applicable frameworks for a given product, business model, and operational footprint.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Regulatory Identification Coverage | 25% | Whether all applicable regulations have been identified for the company's jurisdictions, industries, and data types |
| 2 | Gap Analysis Depth | 25% | Quality of gap analysis comparing current practices against regulatory requirements |
| 3 | Data Privacy Compliance | 20% | Compliance with applicable data privacy frameworks (GDPR, CCPA, COPPA, HIPAA, state biometric laws) |
| 4 | Remediation Plan Quality | 20% | Whether compliance gaps have actionable remediation plans with owners, priorities, and timelines |
| 5 | Monitoring and Currency | 10% | Whether ongoing monitoring processes exist and the assessment reflects current regulatory landscape |
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
| A+ | 9.0 – 10.0 | Fully Compliant | All applicable regulations identified, gaps assessed and remediated, ongoing monitoring in place | Maintain current cadence; prepare for due diligence or audit |
| A | 8.0 – 8.9 | Substantially Compliant | Most regulations covered with minor gaps in one domain; remediation underway | Close remaining gaps within 30 days; document for next review |
| B | 7.0 – 7.9 | Mostly Compliant | Major frameworks covered but state-level or niche regulations partially assessed; remediation plan exists | Expand scan to cover all jurisdictions; prioritize gaps by penalty exposure |
| C | 5.0 – 6.9 | Partially Compliant | Well-known regulations identified but gap analysis is superficial; remediation plan lacks owners or timelines | Conduct deeper gap analysis with assigned owners; escalate critical gaps |
| D | 3.0 – 4.9 | Minimally Compliant | Only obvious regulations identified (e.g., GDPR for EU data); many gaps unassessed; no remediation plan | Engage compliance specialist; prioritize by penalty severity; halt expansion into new jurisdictions |
| F | 0.0 – 2.9 | Non-Compliant | No systematic compliance assessment; operating without awareness of regulatory obligations | Immediate compliance audit required; consider pausing regulated activities until baseline established |

## Signal Tables

### Regulatory Identification Coverage

| Score | Evidence |
|-------|----------|
| 9-10 | Regulatory scope matrix covers all operating jurisdictions; industry-specific regulations identified (FINRA, HIPAA, FERPA); state-level requirements mapped (BIPA, CPRA, SHIELD Act); thresholds and exemptions analyzed |
| 7-8 | Major federal and international regulations identified; most state regulations covered; 1-2 niche requirements may be missing (e.g., state biometric laws, COPPA if minor users possible) |
| 5-6 | Well-known regulations identified (GDPR, CCPA, SOC 2) but no systematic jurisdictional analysis; industry-specific requirements partially covered |
| 3-4 | Only the most prominent regulations mentioned (e.g., "we need to be GDPR compliant"); no state-level or industry-specific analysis |
| 0-2 | No regulatory identification performed; operating without knowledge of applicable requirements |

### Gap Analysis Depth

| Score | Evidence |
|-------|----------|
| 9-10 | Each applicable requirement mapped to current practice; gaps categorized as critical/moderate/low with specific deficiency descriptions; evidence collected for compliant areas |
| 7-8 | Gap analysis covers major requirements with specific findings; severity ratings applied; some requirements assessed at policy level without operational verification |
| 5-6 | Gaps identified at a high level ("we lack a privacy policy") without mapping to specific regulatory requirements or severity |
| 3-4 | Gap analysis limited to obvious deficiencies; no systematic comparison of requirements vs. practices |
| 0-2 | No gap analysis performed; compliance status unknown |

### Data Privacy Compliance

| Score | Evidence |
|-------|----------|
| 9-10 | Data inventory complete; legal basis for each processing activity documented; privacy notices published; DSAR procedures operational; DPA executed with all processors; cross-border transfer mechanisms in place (SCCs, adequacy decisions); breach notification procedures tested |
| 7-8 | Privacy policies and consent flows implemented; DPAs with major processors; DSAR process defined but not tested; cross-border transfers addressed for primary jurisdictions |
| 5-6 | Privacy policy exists but may not cover all data types; consent collection in place but legal basis analysis incomplete; DPAs missing for some processors |
| 3-4 | Basic privacy policy published; no data inventory; no DPAs; consent flows incomplete; DSAR process undefined |
| 0-2 | No privacy compliance measures; personal data collected without legal basis, privacy notice, or processor agreements |

### Remediation Plan Quality

| Score | Evidence |
|-------|----------|
| 9-10 | Each gap has a specific remediation action, assigned owner, deadline, estimated cost, and priority ranking; dependencies mapped; progress tracking in place |
| 7-8 | Most gaps have assigned remediation actions with owners and timelines; some gaps pending external counsel or specialist input |
| 5-6 | Remediation actions defined at a high level ("implement a privacy policy") without specific owners, deadlines, or cost estimates |
| 3-4 | Gaps identified but no formal remediation plan; verbal commitments to "address compliance" without specifics |
| 0-2 | No remediation planning; gaps acknowledged but not actioned |

### Monitoring and Currency

| Score | Evidence |
|-------|----------|
| 9-10 | Quarterly re-scan cadence established; regulatory watch list maintained for all relevant jurisdictions; trigger events defined for ad hoc scans (new product, new market, M&A); assessment reflects regulations enacted within last 90 days |
| 7-8 | Re-scan cadence defined (semi-annual or quarterly); major regulatory developments tracked; assessment current within 6 months |
| 5-6 | Initial scan completed; no formal re-scan cadence; regulatory developments monitored informally |
| 3-4 | One-time scan performed more than 6 months ago; no monitoring process; regulatory changes since scan not incorporated |
| 0-2 | No monitoring process; compliance assessment is a point-in-time artifact with no update mechanism |
