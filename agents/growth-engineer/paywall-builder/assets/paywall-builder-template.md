# Paywall Implementation Spec

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Growth Engineer name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | paywall-builder |
| Product | [Product / feature being gated] |
| Paywall Type | [Feature gate / Usage metering / Trial / Reverse trial] |

## Executive Summary

[2-3 sentences describing the paywall strategy, primary gate, and expected conversion impact.
GUIDANCE: Example — "A usage-metered paywall gates the report export feature at 3 exports/month on the free tier. The gate appears after the activation moment (first report created), and the Pro plan unlocks unlimited exports at $49/month. Expected freemium-to-paid conversion: 4% based on industry benchmark of 2–5% for PLG SaaS."]

## Entitlement Matrix

[Map every product feature to free/paid tiers. Must confirm the activation moment feature is not gated.
GUIDANCE:
- Good: Explicit table showing Free/Pro/Enterprise access level for every feature, with footnotes indicating usage limits.
- Bad: "Pro users get more features than free users."
- Format: Three-column table. Mark the activation moment feature with (*)]

| Feature | Free | Pro | Enterprise |
|---------|------|-----|-----------|
| [Activation moment feature*] | Full access | Full access | Full access |
| [Feature 2] | [N uses / Blocked / Full] | [Access level] | [Access level] |
| [Feature 3] | | | |

*Activation moment feature — must never be gated.

## Gate Implementation Plan

[Describe each gate: what triggers the upgrade prompt, what happens (hard block or soft limit), and the upgrade CTA.
GUIDANCE:
- Good: "When a free user attempts a 4th report export in a month, the export action shows an upgrade modal with the message: 'You've used your 3 free exports this month. Upgrade to Pro for unlimited exports.' CTA: 'Upgrade to Pro — $49/month'."
- Bad: "Show an upgrade prompt when users hit the limit."
- Format: One row per gate]

| Gate | Trigger | Type | Prompt Copy | CTA | Funnel Position |
|------|---------|------|------------|-----|----------------|
| [Feature gate name] | [User action that triggers it] | [Hard block / Soft limit] | [Prompt text] | [Button text + destination] | [Pre/Post activation] |

## Upgrade Flow Specification

[Describe the complete upgrade flow from upgrade prompt to confirmed subscription.
GUIDANCE:
- Good: "Step 1: Upgrade modal (pre-filled plan recommendation based on current usage). Step 2: Plan comparison page with annual billing pre-selected (20% discount). Step 3: Stripe checkout pre-filled with user email. Step 4: Confirmation page with success message and immediate feature unlock."
- Bad: "Redirect users to the pricing page."
- Format: Numbered steps with deliverables at each step]

1. **Upgrade modal**: [Description, pre-filled defaults, dismiss behaviour]
2. **Plan comparison page**: [Plans shown, pricing display, billing toggle, pre-selected option]
3. **Checkout**: [Provider, pre-filled fields, payment options]
4. **Confirmation**: [Message, immediate unlock behaviour, next action]

## Instrumentation Requirements

[List every event the paywall must fire for analytics.
GUIDANCE: All events must link to user_id, plan, and gate context (which feature triggered the paywall).]

| Event | Trigger | Properties |
|-------|---------|-----------|
| paywall_impression | Upgrade prompt displayed | user_id, gate_name, plan, feature |
| paywall_click | User clicks CTA | user_id, gate_name, cta_text |
| upgrade_page_view | Plan comparison page loads | user_id, source_gate |
| checkout_started | User enters payment details | user_id, plan, price, billing_cycle |
| subscription_created | Payment confirmed | user_id, plan, mrr |
| paywall_dismissed | User closes prompt | user_id, gate_name |

## A/B Test Roadmap

[Define planned experiments for paywall optimization.
GUIDANCE: List experiments in priority order. Each experiment needs a hypothesis, success metric, and minimum sample size.]

| Priority | Experiment | Hypothesis | Success Metric | Sample Size |
|----------|-----------|-----------|---------------|------------|
| 1 | [e.g., Annual billing pre-selected] | [If annual is default, more users choose it] | [Annual plan take rate] | [N per variant] |
| 2 | [Next experiment] | | | |

## Recommendations

[Prioritized list of implementation decisions and optimizations.
GUIDANCE: P1 = required for launch; P2 = first 30-day optimization; P3 = quarterly review]

| Priority | Recommendation | Expected Impact | Owner |
|----------|---------------|----------------|-------|
| P1 | [e.g., Confirm activation moment feature is not gated before launch] | [Prevents activation drop] | [Growth Lead review] |

## Appendices

### A. Methodology

[Entitlement decisions based on: activation signal definition, growth pricing review, competitive analysis. Benchmark data sources: Reforge PLG benchmarks, OpenView SaaS survey.]

### B. Supporting Data

[Baseline metrics: current free user count, current paid conversion rate, top feature usage by free tier users (to inform gate placement).]
