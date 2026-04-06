# Threat Model Sketch

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Agent role / human name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | threat-model-sketch |
| Feature / System | [Feature name and owning team] |
| Design Document | [Link to PRD or design doc] |
| Escalation Required | [Yes — proceed to full STRIDE model / No] |

## Executive Summary

[2-3 sentences covering the highest-risk threat, its potential impact, and the top recommended mitigation.
GUIDANCE: Lead with the most severe finding. Example: "The highest-risk threat is unauthorized access to payment method tokens via IDOR in the payment API (Score 9). Immediate mitigation: enforce ownership validation on every payment method lookup. Full STRIDE threat model recommended before production launch due to PCI-DSS scope."]

## Scope

[Define the boundary of this sketch.

GUIDANCE:
- Good: "Scope: new file upload feature in the content service. In scope: upload endpoint `/api/v1/uploads`, S3 storage bucket, virus scan integration, and file URL generation. Out of scope: downstream consumers of uploaded files — separate sketch required."
- Bad: "The file upload feature."
- Format: Bullet list of in-scope components and explicit out-of-scope boundaries]

**In scope:**
- [Component or endpoint 1]
- [Component or endpoint 2]

**Out of scope:**
- [Component explicitly excluded and why]

## Data Flow Diagram

[Simple data flow description or ASCII diagram showing the primary flows.

GUIDANCE: For a sketch, a text description of the key flows is sufficient. Use arrows to show data direction. Mark trust boundaries with a double line (=====).]

```
[User Browser] → HTTPS → [API Gateway] ===TRUST BOUNDARY=== [Upload Service] → [S3 Bucket]
                                                              ↓
                                                       [Virus Scanner]
```

## Attack Surface Inventory

[List all entry points and classify each.

GUIDANCE:
- Good: "POST /api/v1/uploads — Authenticated API; accepts multipart form data; max 10 MB. S3 pre-signed URL endpoint — Unauthenticated; URL signed for 15 minutes; exposes direct bucket access."
- Bad: "The upload API."
- Format: Table with entry point, type, auth state, and key risk note]

| Entry Point | Type | Auth State | Key Risk |
|-------------|------|------------|----------|
| [Endpoint or component] | [Unauthenticated API / Authenticated API / File upload / etc.] | [None / JWT / API Key] | [Primary attack vector] |

## Top Threats

[Identify 3–5 highest-risk threats using STRIDE categorization.

GUIDANCE:
- Good: "Threat 1 — Malicious File Upload (T/I). Attack: Attacker uploads a disguised executable (.exe renamed to .jpg) to the upload API. Impact: Malware served to other users via CDN. Score: 8 (Impact 3 × Likelihood 3 − 1). Mitigation: MIME-type validation server-side (not client-provided Content-Type); antivirus scan before serving; block file extensions by allowlist."
- Bad: "Files could be malicious."
- Format: One entry per threat with all required fields]

### Threat 1 — [Title] ([STRIDE Category])

| Field | Value |
|-------|-------|
| Attack | [How an attacker would carry this out] |
| Impact | [What data or service is affected, what damage results] |
| Priority Score | [Impact (1-3) × Likelihood (1-3) = N] |
| Affected Component | [Which component or boundary] |

**Proposed Mitigation**: [Specific control — not generic. "Add input validation" is not acceptable; "Validate file MIME type using magic bytes, not Content-Type header" is acceptable.]

---

### Threat 2 — [Title] ([STRIDE Category])

| Field | Value |
|-------|-------|
| Attack | [How an attacker would carry this out] |
| Impact | [Impact description] |
| Priority Score | [N] |
| Affected Component | [Component] |

**Proposed Mitigation**: [Specific control]

---

### Threat 3 — [Title] ([STRIDE Category])

*(Repeat structure for threats 4 and 5 if needed)*

## Threat-Mitigation Matrix

[Summary table linking each threat to its mitigation for quick review.

GUIDANCE: Use this as the action list for the development team.]

| # | Threat | STRIDE | Score | Mitigation | Owner | Priority |
|---|--------|--------|-------|------------|-------|----------|
| 1 | [Threat title] | [S/T/R/I/D/E] | [N] | [Control] | [Team] | [P1/P2/P3] |
| 2 | [Threat title] | [S/T/R/I/D/E] | [N] | [Control] | [Team] | [P1/P2/P3] |

## Escalation Assessment

[Determine whether a full STRIDE threat model is required.

GUIDANCE: Be explicit about the trigger. If any of the escalation criteria are met, state it clearly.]

| Escalation Trigger | Present? |
|-------------------|----------|
| Score 9 threat identified | [Yes / No] |
| 3+ service components in scope | [Yes / No] |
| Regulated data in scope (PII, PHI, payment) | [Yes / No] |
| Multiple trust boundaries | [Yes / No] |
| **Full STRIDE model required** | **[Yes / No]** |

If yes: Assign full threat model to: [security engineer] by: [YYYY-MM-DD]

## Recommendations

- **P1 — [Mitigation]**: [Implement before this feature enters code review — specific control, owner]
- **P2 — [Mitigation]**: [Implement before staging deployment — specific control, owner]
- **P3 — [Follow-up]**: [Full STRIDE model or additional security review if required]

## Appendices

### A. Assumptions

[List any assumptions made due to incomplete design information. Assumptions must be validated with the feature team before the sketch is considered final.]
