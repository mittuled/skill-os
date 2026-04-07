# Support Readiness Sign-Off

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Support Agent name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | support-readiness-confirmer |
| Release | [Release version or name] |
| Launch Date | [YYYY-MM-DD] |

## Executive Summary

[2-3 sentences stating the readiness verdict (GO / CONDITIONAL GO / NO-GO), the composite readiness score, and any conditions or blocking gaps. Example: "The support team is CONDITIONAL GO for the v3.2 launch. Composite readiness score is 8.2/10. All agents passed knowledge checks and runbooks are updated; two help articles are pending final accuracy verification and must be published before the 9am launch window."]

## Readiness Verdict

| Verdict | Composite Score | Conditions |
|---------|----------------|------------|
| ☐ GO | ≥ 8.0 — all criteria met or minor gaps only | None |
| ☐ CONDITIONAL GO | 6.0 – 7.9 — gaps exist but do not block customer handling | [List conditions] |
| ☐ NO-GO | < 6.0 — blocking gaps that would cause customer-facing failures | [List blockers] |

**Verdict: [ ]**

## Knowledge Assessment Results

[Agent-by-agent results from the knowledge check.

GUIDANCE:
- Good: A table showing each agent's score on key knowledge questions, with any gaps noted and remediation assigned.
- Bad: "Agents were briefed and most understood the release."
- Format: Table with Agent Name | Knowledge Score | Key Gaps | Remediation Status]

| Agent | Score | Key Gaps | Remediation |
|-------|-------|----------|-------------|
| [Name] | [Pass/Fail/Score] | [Specific gap if any] | [Completed / Pending] |

## Tooling and Content Verification

[Checklist confirming each readiness component.

GUIDANCE: Mark each item as Verified, Partial, or Missing. Partial and Missing items require notes.]

| Component | Status | Notes |
|-----------|--------|-------|
| Runbooks updated for new ticket types | [Verified / Partial / Missing] | [Notes] |
| Macros deployed and tested | [Verified / Partial / Missing] | [Notes] |
| Help articles live and accurate | [Verified / Partial / Missing] | [Notes] |
| Agent tooling access confirmed | [Verified / Partial / Missing] | [Notes] |
| Escalation path communicated | [Verified / Partial / Missing] | [Notes] |

## Composite Readiness Score

| Criterion | Weight | Score (0-10) | Weighted Score |
|-----------|--------|--------------|----------------|
| Agent Knowledge | 30% | [0-10] | [calc] |
| Runbook and Macro Readiness | 25% | [0-10] | [calc] |
| Help Article Accuracy | 25% | [0-10] | [calc] |
| Tooling Access | 10% | [0-10] | [calc] |
| Escalation Path Clarity | 10% | [0-10] | [calc] |
| **Total** | **100%** | | **[composite]** |

## Recommendations

[Prioritised list of actions required before or immediately after launch.

GUIDANCE: Each item should specify the action, owner, and deadline.
- P1 (before launch): Must be resolved before the launch window opens
- P2 (within 24h): Can launch but must be resolved during hypercare
- P3 (within sprint): Non-blocking improvements for next release cycle]

## Appendices

### A. Knowledge Assessment Questions

[The questions used to assess agent knowledge for this release, with expected correct answers.]

### B. Readiness Briefing Delivery Confirmation

[Record of briefing delivery: date, channel (sync meeting / async doc / video), attendance list or read-receipt count.]
