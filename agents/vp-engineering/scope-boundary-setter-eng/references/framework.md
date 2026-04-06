# Framework: scope-boundary-setter-eng

Defines the methodology for establishing, communicating, and enforcing engineering scope boundaries throughout a delivery.

## Scope Boundary Categories

Every scope definition must address four layers:

| Layer | What to Define | Example |
|-------|---------------|---------|
| **Feature scope** | Which features and capabilities are included/excluded | "Single-currency only; multi-currency excluded" |
| **User scope** | Which user segments, tiers, or regions are included/excluded | "B2B customers only; consumer app excluded" |
| **Integration scope** | Which integrations and API connections are included/excluded | "Stripe integration only; PayPal deferred to Phase 3" |
| **Quality scope** | What quality standards apply and which are explicitly deferred | "E2E tests for happy path only; edge case tests deferred" |

## In/Out-of-Scope Clarity Standards

An in-scope item is sufficiently defined when:
- It references a specific spec section, ticket ID, or named feature
- It specifies the depth of implementation (full / MVP / partial — with description of what partial means)
- It has an engineering effort estimate associated

An out-of-scope item is sufficiently defined when:
- It names the specific capability being excluded (not just "everything else")
- It states the reason for exclusion
- It states where/when it will be addressed (Phase N, future roadmap, or not planned)

## Change Control Gate Model

### Request Evaluation Criteria

When a scope change arrives, evaluate against four gates:

| Gate | Question | Pass Condition |
|------|---------|---------------|
| 1. Necessity | Is this required for the delivery to succeed, or is it a preference? | Required for core functionality or commitment |
| 2. Impact | What is the engineering effort cost? | Estimate provided; effort acceptable within timeline |
| 3. Risk | Does this change introduce new dependencies or technical risk? | Risk assessed and mitigation plan exists |
| 4. Trade-off | What must be cut or extended to accommodate this? | An explicit trade-off is identified and accepted |

A request that fails any gate is rejected or deferred. No exceptions for "quick adds."

### Effort-to-Value Classification

Use this matrix to guide approval decisions for scope change requests:

| Effort | High Business Value | Low Business Value |
|--------|--------------------|--------------------|
| **Low (< 2 days)** | Approve — add to current phase | Defer — add to future backlog |
| **High (> 2 days)** | Phase trade-off required — approve only if something else is cut | Reject — do not add to current phase |

### Change Documentation Requirements

Every approved change must be recorded with:
- Date of request and decision
- Requestor name and role
- Engineering effort estimate (story points or days)
- What was cut, deferred, or extended to accommodate it
- Approval authority (Tech Lead / VP Eng / joint Product-Engineering)

## Scope Creep Signals

Watch for these leading indicators that scope boundaries are eroding:

| Signal | Response |
|--------|---------|
| Tickets added to the sprint without going through change control | Immediately surface; require retroactive change control decision |
| "Small asks" from stakeholders that bypass the formal request process | Direct to change control; no ad-hoc acceptance |
| Acceptance criteria expanding after spec sign-off | Require product sign-off on any AC additions; treat as scope change |
| Engineering estimates consistently increasing sprint over sprint without new work | Audit for undocumented scope additions |

## Communication Template for Scope Rejections

> "I've reviewed the request for [item]. This is out of scope for the current phase because [reason]. Adding it would require [effort] and would impact [timeline/quality/other item].
>
> This item is logged and will be reviewed for [Phase N / next planning cycle]. If this is urgent, I need [stakeholder] to confirm what we should cut or defer in exchange before I can approve it."

Never reject a scope request without: (1) acknowledging it, (2) explaining the impact, and (3) stating where it goes next.
