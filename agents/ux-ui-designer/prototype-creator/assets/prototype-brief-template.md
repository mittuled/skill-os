# Prototype Brief

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [UX/UI Designer] |
| Feature | [Feature name] |
| Prototype Type | [Lo-fi clickthrough / Mid-fi flow / Hi-fi interactive / Micro-interaction demo] |
| Prototype Link | [Figma prototype URL] |
| Version | [1.0] |
| Status | [In Build / Ready for Review / Ready for Testing] |

## Prototype Purpose

[State clearly what this prototype is for and what questions it needs to answer. GUIDANCE: The prototype purpose determines what fidelity is needed and what interactions must be wired. Do not over-build.]

**Primary use**: [Usability testing / Stakeholder review / Engineering handoff reference / Internal demo]
**Key question to answer**: [e.g. "Can users find and complete the address entry step without assistance?"]
**Secondary questions**: [List if applicable]

## Scope

[Define exactly what is wired and what is not. Unscoped areas should be clearly marked as "not interactive" in the prototype.]

### In Scope (wired interactions)

- [ ] [e.g. Full happy path: Cart → Checkout → Address → Payment → Confirmation]
- [ ] [e.g. Validation error state on address form]
- [ ] [e.g. Payment declined error state]
- [ ] [e.g. Back navigation from all steps]

### Out of Scope (not interactive in this prototype)

- [ ] [e.g. Sign-in flow — not being tested]
- [ ] [e.g. Order history screen]
- [ ] [e.g. Profile settings]

## Prototype Structure

[Document all screens and their wired connections.]

| Screen # | Screen Name | Entry From | Exits To | Interactions Wired |
|----------|------------|-----------|---------|-------------------|
| S1 | [Cart — default] | [External] | [S2 on "Checkout" tap] | [Tap "Checkout" CTA] |
| S2 | [Checkout entry — Guest/Sign in] | [S1] | [S3 on "Guest" tap / Auth flow on "Sign in"] | [Tap "Continue as guest", Tap "Sign in"] |
| S3 | [Address entry] | [S2] | [S4 on valid submit / S3e on error] | [Tap "Continue", Tap back arrow] |
| S3e | [Address entry — validation error] | [S3] | [S3 on correction] | [Tap "Continue" after error shown] |
| S4 | [Payment selection] | [S3] | [S5 on "Continue"] | [Tap payment method, Tap "Continue"] |
| S5 | [Order review] | [S4] | [S6 on "Place order"] | [Tap "Place order"] |
| S6 | [Order confirmation] | [S5] | [End] | [Static — no further interaction] |

## Fidelity Rationale

[Explain why this fidelity level was chosen for the stated purpose.]

| Dimension | Decision | Rationale |
|-----------|----------|-----------|
| Visual fidelity | [Lo-fi / Mid-fi / Hi-fi] | [e.g. Hi-fi needed — testing visual design of confirmation screen] |
| Animation / transitions | [Included / Not included] | [e.g. Transitions included — testing if users notice screen change] |
| Real copy | [Real / Placeholder] | [e.g. Real copy required — testing comprehension of error messages] |
| Real images | [Real / Grey boxes] | [e.g. Real product images — testing if image quality affects purchase intent] |

## Test Task Script (if for usability testing)

[If prototype will be used in a usability test, include the task instruction and success criteria here.]

**Task instruction for participant**:
> "[e.g. Imagine you want to buy the blue jacket in your cart. Please go ahead and complete the purchase using your regular payment method.]"

**Success criteria**:
- [ ] Participant reaches order confirmation screen
- [ ] Participant does not request help
- [ ] Participant completes within [X minutes]

**Failure indicators**:
- Participant takes wrong path (navigates away from checkout flow)
- Participant asks "what do I tap next?"
- Participant expresses confusion at address entry

## Prototype QA Checklist

Before handing off for testing or review:

- [ ] All in-scope interactions are wired
- [ ] Out-of-scope areas are marked "Not part of this test" with an overlay
- [ ] Back navigation works on all screens
- [ ] Prototype starts from the correct entry screen
- [ ] Figma link is set to "Anyone with link can view"
- [ ] Mobile prototype is set to the correct device frame (if testing on mobile)
- [ ] Presenter has rehearsed the walkthrough path
