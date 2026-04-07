# Compliance Scan Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | Corporate Counsel |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | compliance-scanner |

## Executive Summary

[2-3 sentences summarizing the compliance posture, number of regulations assessed, critical gaps found, and overall grade.
GUIDANCE: Lead with the overall posture. Example: "The company has 14 applicable regulatory frameworks across 3 jurisdictions. Current posture: Grade B (7.4/10). Two critical gaps identified in data privacy (missing DPAs with 3 sub-processors) and one moderate gap in California biometric data handling. Remediation plan targets full compliance within 60 days."]

## Regulatory Scope Matrix

[Mapping of business activities to regulatory domains and applicable jurisdictions.

GUIDANCE:
- Good: Matrix showing each business activity (data collection, payments, marketing, employment) mapped to applicable regulations per jurisdiction with threshold analysis
- Bad: "GDPR and CCPA apply"
- Format: Table with business activity rows and jurisdiction/regulation columns]

| Business Activity | US Federal | [State 1] | [State 2] | EU/UK | Other |
|-------------------|-----------|-----------|-----------|-------|-------|
| Personal data collection | FTC Act Section 5 | CCPA/CPRA | [Law] | GDPR/UK GDPR | [Law] |
| Payment processing | PCI-DSS | [Law] | [Law] | PSD2 | [Law] |
| Email marketing | CAN-SPAM | [Law] | [Law] | ePrivacy Directive | [Law] |
| Employment | FLSA, Title VII | [State labor laws] | [Law] | [Law] | [Law] |
| [Activity] | [Regulation] | [Regulation] | [Regulation] | [Regulation] | [Regulation] |

## Regulation Applicability Register

[Detailed register of each applicable regulation with requirements, thresholds, and exemptions.

GUIDANCE:
- Good: Each regulation listed with applicability trigger, key requirements, current exemptions, and penalty range. "CCPA: Applies if annual revenue > $25M, or process data of 100K+ consumers, or derive 50% of revenue from data sales. Key requirements: privacy notice, opt-out right, DSAR within 45 days. Penalty: $2,500/violation (unintentional), $7,500/violation (intentional)."
- Bad: "CCPA may apply."
- Format: Detailed table with regulation, applicability test, key requirements, exemption status, and penalty exposure]

| Regulation | Applicability Test | Applies? | Key Requirements | Exemptions | Max Penalty |
|------------|-------------------|----------|-----------------|------------|-------------|
| [Regulation] | [Threshold] | [Yes/No/TBD] | [Requirements] | [Exemptions] | [Penalty] |

## Gap Analysis

[Comparison of current practices against each applicable regulatory requirement.

GUIDANCE:
- Good: Each requirement mapped to current practice with gap severity. "GDPR Art. 28: Require DPA with each processor. Current: DPAs executed with 5/8 processors. Gap: 3 processors lack DPA. Severity: CRITICAL — regulatory exposure per missing DPA."
- Bad: "Some privacy gaps exist."
- Format: Table with requirement, current practice, gap description, and severity rating]

| Regulation | Requirement | Current Practice | Gap | Severity |
|------------|------------|-----------------|-----|----------|
| [Regulation] | [Specific requirement] | [What we do today] | [Specific gap] | [Critical/Moderate/Low] |

## Remediation Roadmap

[Prioritized plan to close compliance gaps.

GUIDANCE: Each remediation should be:
- Specific: "Execute DPA with Processor X using standard contractual clauses template"
- Actionable: Assigned to a specific person with cost estimate
- Prioritized: By penalty exposure and likelihood of enforcement]

| Priority | Gap | Remediation Action | Owner | Deadline | Est. Cost | Regulation |
|----------|-----|-------------------|-------|----------|-----------|------------|
| P1 | [Gap] | [Action] | [Name] | [Date] | [$] | [Regulation] |

## Recommendations

[Strategic compliance recommendations beyond gap closure.

GUIDANCE: Each recommendation should be:
- Specific: "Implement automated DSAR response workflow to meet 45-day CCPA deadline at scale"
- Actionable: Assignable with cost/benefit analysis
- Prioritized: P1 (critical compliance risk), P2 (enforcement risk), P3 (best practice)]

| Priority | Recommendation | Rationale | Est. Investment |
|----------|---------------|-----------|-----------------|
| P1 | [Recommendation] | [Rationale] | [$] |

## Appendices

### A. Methodology

[Scoring rubric applied per `references/scoring-rubric.md`. Jurisdictions scanned, regulatory databases consulted, product documentation reviewed, stakeholder interviews conducted.]

### B. Monitoring Schedule

[Re-scan cadence, trigger events for ad hoc scans, regulatory watch list sources, responsible parties]

| Scan Type | Cadence | Trigger | Owner |
|-----------|---------|---------|-------|
| Full re-scan | Quarterly | Scheduled | Corporate Counsel |
| Ad hoc scan | As needed | New market, product, or M&A | Corporate Counsel |
| Regulatory watch | Ongoing | New legislation or enforcement action | Corporate Counsel |
