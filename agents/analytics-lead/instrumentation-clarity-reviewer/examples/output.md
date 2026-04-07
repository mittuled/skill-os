# Instrumentation Spec Review: Checkout Flow v1

| Field | Value |
|-------|-------|
| Date | 2026-03-31 |
| Analytics Lead | Analytics Lead |
| Spec | Checkout Flow Instrumentation Spec v1 |
| Events Reviewed | 3 |
| Average Score | 5.8 / 10 |
| Verdict | CONDITIONAL PASS — fix critical issues before implementation |
| Skill | instrumentation-clarity-reviewer |

## Event Scores

| Event | Score | Issues |
|-------|-------|--------|
| checkout_started | 10.0 | None — well-formed |
| PaymentClicked | 5.5 | 2 issues |
| purchase | 4.0 | 3 issues |

## Issues Found

### Critical Issues (Must Fix)

| Event | Issue |
|-------|-------|
| PaymentClicked | Name should be snake_case: rename to `payment_method_clicked` |
| PaymentClicked | Missing required universal property: `timestamp` |
| PaymentClicked | Missing required universal property: `session_id` |
| PaymentClicked | Missing required universal property: `platform` |
| PaymentClicked | Property `payment_method` has no type defined |
| purchase | Name `purchase` should follow object_action format: rename to `order_completed` |
| purchase | Missing required universal property: `user_id` |
| purchase | Missing required universal property: `timestamp` |
| purchase | Missing required universal property: `session_id` |
| purchase | Missing required universal property: `platform` |

## Naming Issues

| Current Name | Problem | Suggested Name |
|-------------|---------|----------------|
| `PaymentClicked` | Not snake_case | `payment_method_clicked` |
| `purchase` | Not object_action format; no past tense | `order_completed` |

## Revised Event List

| Original | Revised |
|----------|---------|
| checkout_started | No change |
| PaymentClicked | `payment_method_clicked` |
| purchase | `order_completed` |

## Required Actions Before Implementation

1. Rename `PaymentClicked` → `payment_method_clicked`
2. Rename `purchase` → `order_completed`
3. Add `timestamp`, `session_id`, `platform` to `payment_method_clicked`
4. Add `user_id`, `timestamp`, `session_id`, `platform` to `order_completed`
5. Add type definition to `payment_method` property in `payment_method_clicked`
