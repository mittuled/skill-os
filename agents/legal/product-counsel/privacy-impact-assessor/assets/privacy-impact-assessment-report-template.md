# Privacy Impact Assessment Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Product Counsel] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | privacy-impact-assessor |

## Executive Summary

[2-3 sentences summarizing the processing activity assessed, overall privacy risk level, and primary recommendation.
GUIDANCE: Lead with the risk verdict and whether GDPR Article 35 DPIA triggers are met. State the most significant privacy risk identified.]

## Data Flow Diagram and Processing Inventory

[Complete data lifecycle documentation.

GUIDANCE:
- Good: "User registration collects: name, email, company (contractual necessity). Analytics service receives: anonymized usage events (legitimate interest). AWS eu-west-1 stores: all PII with 2-year retention. Stripe processes: payment data under separate controller relationship."
- Bad: "We collect user data"
- Format: Data flow diagram plus table with Data Category, Source, Processing Activity, Storage Location, Retention, Recipients, Legal Basis]

## Legal Basis Analysis

[Per-activity legal basis determination.

GUIDANCE:
- Good: Table with Processing Activity, Data Categories, Legal Basis (GDPR Art. 6), Justification, CCPA Category
- Bad: "We rely on consent"
- Format: Per-activity analysis with specific GDPR article and justification]

## Necessity and Proportionality Assessment

[Data minimization and alternatives analysis.

GUIDANCE:
- Good: "Email collection: necessary for account authentication and communication (no alternative). Phone number: collected for MFA — alternative: authenticator app. Recommendation: make phone number optional, offer authenticator as primary MFA."
- Bad: "All data is necessary"
- Format: Per-data-element assessment with necessity justification and alternatives considered]

## Privacy Risk Register

[Identified privacy risks with likelihood and severity ratings.

GUIDANCE:
- Good: Table with Risk ID, Description, Dimension (unauthorized access/function creep/re-identification/cross-border/DSR compliance), Likelihood (High/Medium/Low), Severity (High/Medium/Low), Residual Risk Rating, Existing Controls
- Bad: "There are some privacy risks"
- Format: Risk register with ratings]

## Mitigation Plan

[Specific mitigations for each identified risk.

GUIDANCE:
- Good: "Risk R-003 (re-identification of anonymized analytics): Technical: implement k-anonymity (k>=5) for all analytics exports. Organizational: quarterly re-identification testing by security team. Legal: update privacy notice to describe anonymization methodology. Owner: Data Engineering. Deadline: Pre-launch."
- Bad: "Implement privacy measures"
- Format: Table with Risk ID, Mitigation Type (Technical/Organizational/Legal), Mitigation Description, Owner, Deadline]

## DPO Consultation Record

[Documentation of DPO or supervisory authority consultation.

GUIDANCE:
- Good: "DPO consulted on [date]. DPO assessed: DPIA not required to be submitted to supervisory authority as residual risk is medium after mitigations. Condition: implement all P1 mitigations before launch."
- Bad: "DPO was informed"
- Format: Consultation date, DPO assessment, conditions, supervisory authority filing requirement]

## Recommendations

[Prioritized privacy recommendations.
GUIDANCE: Each recommendation should be:
- Specific (not "improve privacy" but "implement data subject access request API endpoint with 30-day response SLA")
- Actionable (assignable to a person/team)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[Scoring rubric applied per `references/scoring-rubric.md`. Assessment performed per GDPR Articles 35-36 DPIA requirements. ICO DPIA guidance and CNIL PIA methodology referenced. Risk rated per ISO 29134 privacy risk framework.]

### B. Supporting Data

[Data flow diagrams, consent mechanism mockups, anonymization methodology documentation, DPO correspondence, legitimate interest balancing test worksheets.]
