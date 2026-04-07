# Interaction Flow Specification

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [UX/UI Designer] |
| Feature | [Feature name] |
| User Journey | [Journey name — e.g. "Checkout: guest payment"] |
| Figma Flow Diagram | [Link] |
| Version | [1.0] |
| Status | [Draft / Review / Approved] |

## Flow Overview

[Describe the user journey this flow covers in 2-3 sentences. State the entry point, exit point, and primary goal the user is trying to accomplish.]

- **Entry point**: [e.g. User taps "Checkout" from cart screen]
- **Exit point**: [e.g. Order confirmation screen displayed]
- **User goal**: [e.g. Complete purchase without creating an account]
- **Estimated steps**: [X steps in happy path]

## Step-by-Step Flow

[Document every step in the flow. Include branching logic and decision points.]

| Step # | Screen / State | User Action | System Response | Next Step | Branching Conditions |
|--------|---------------|-------------|-----------------|-----------|---------------------|
| 1 | Cart — default | Taps "Checkout" | Validates cart has items; shows loading | 2 | If cart empty → Empty state; redirect to browse |
| 2 | Checkout — Guest or sign in | Taps "Continue as guest" | Records guest session; advances | 3 | If taps "Sign in" → Auth flow |
| 3 | Address entry | Fills in address; taps "Continue" | Validates address fields | 4 | If validation fails → Inline errors on failed fields |
| 4 | Payment selection | Selects payment method; taps "Continue" | Stores selection in session | 5 | If no payment method saved → Show add card flow |
| 5 | Order review | Reviews order; taps "Place order" | Shows loading spinner; calls payment API | 6 | If API error → Error state (Step 5a) |
| 5a | Order review — error | Reads error message | Shows retry option | 5 | If payment declined → Specific decline message |
| 6 | Order confirmation | Views confirmation | Sends confirmation email; clears cart | End | – |

## Decision Points

[Detail each branching decision point in the flow.]

### Decision Point 1: [e.g. Guest vs Sign In at Checkout Entry]

| Condition | Branch | Design Response |
|-----------|--------|-----------------|
| [User is not signed in] | Show guest/sign-in toggle | Two equal-weight CTAs: "Continue as guest" and "Sign in" |
| [User is already signed in] | Skip step 2 | Auto-advance to address entry |
| [User taps "Sign in"] | Auth flow branch | Navigate to sign-in screen; deep link back to checkout on success |

### Decision Point 2: [e.g. Payment Method at Payment Step]

| Condition | Branch | Design Response |
|-----------|--------|-----------------|
| [User has saved payment method] | Show saved method selected by default | Allow change; show "Add new method" option |
| [No saved payment method] | Show empty state | Direct to "Add payment method" modal |
| [Payment declined] | Error state on Order Review | Show specific decline reason; offer retry or different method |

## Micro-Interaction Specifications

[Specify animations, transitions, and feedback moments for key interactions in the flow.]

| Trigger | Animation / Feedback | Duration | Notes |
|---------|---------------------|----------|-------|
| [Taps "Continue" on valid form] | [Button loading spinner, screen slide-left transition] | [300ms transition] | [Use standard screen transition] |
| [Validation error on blur] | [Inline error text fades in; field border turns red] | [200ms fade] | [Do not delay until form submit] |
| [Order placement loading] | [Full-screen loading overlay with progress indicator] | [Until API resolves] | [Avoid timeout under 10s] |
| [Order confirmation reveal] | [Confirmation icon scales in with ease-out] | [400ms] | [Celebratory but not distracting] |

## Edge Cases Covered

| Edge Case | Handling |
|-----------|---------|
| [Empty cart at checkout entry] | [Redirect to browse with empty cart message] |
| [Payment API timeout] | [Show timeout error with "Try again" CTA; do not double-charge] |
| [Address autocomplete unavailable] | [Fallback to manual address entry without autocomplete] |
| [User navigates back mid-flow] | [Preserve entered data; do not reset form on back navigation] |
| [Session expires mid-flow] | [Show session expiry modal; offer re-auth without losing cart] |

## Open Questions

| # | Question | Owner | Due |
|---|----------|-------|-----|
| Q1 | [e.g. Should we save guest address for future sessions via cookie?] | [PM] | [Date] |
| Q2 | [e.g. What is the timeout threshold before showing the payment error state?] | [Engineering] | [Date] |
