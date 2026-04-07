# QA Instrumentation Verification — Checkout Funnel v2

| Field | Value |
|---|---|
| Date | 2026-03-31 |
| Author | QA Test Engineer |
| Feature | Checkout Funnel v2 Instrumentation |
| Recommendation | BLOCK PROMOTION |
| Skill | instrumentation-verifier-qa |

## Recommendation

**BLOCK PROMOTION** — 1 signal not firing (`checkout.payment.failed`). Error paths without instrumentation will be invisible in production. Fix before promoting to staging.

---

## Signal Verification Summary

| Signal | Type | Status | Notes |
|---|---|---|---|
| checkout.step.started | Metric | PASS | |
| checkout.step.completed | Metric | PASS | |
| checkout.payment.initiated | Log Entry | PASS | |
| checkout.payment.failed | Log Entry | **MISSING** | Error path not instrumented |
| checkout.funnel.trace | Trace Span | PAYLOAD ISSUE | user_id attribute is null in Jaeger |

---

## Missing Signals

### checkout.payment.failed

The payment failure code path was not instrumented. When a payment fails (declined card, network error), no log entry is emitted. In production, this means payment failures will not appear in logs, making it impossible to diagnose payment failure rates or debug customer-reported issues.

**Fix required:** Add structured log entry to the payment failure handler with fields: `event=checkout.payment.failed`, `error_code`, `payment_method`, `user_id`, `order_id`.

---

## Payload Issues

### checkout.funnel.trace — null user_id

The checkout funnel trace span fires correctly but the `user_id` attribute is null. Downstream trace queries filtered by user_id will return no results, making per-user debugging impossible.

**Fix required:** Pass `user_id` from the checkout context to the span creation call. Verify in Jaeger after fix.

---

## Re-verification Required

After both fixes are deployed to QA:
1. Run the payment failure test scenario and confirm `checkout.payment.failed` log entry appears
2. Inspect the `checkout.funnel.trace` span in Jaeger and confirm `user_id` is populated
