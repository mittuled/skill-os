# Regression Test Report — Product v4.2 Release Candidate

| Field | Value |
|---|---|
| Date | 2026-03-31 |
| Author | QA Test Engineer |
| Suite Type | Full |
| Pass Rate | 71.4% (5/7) |
| Recommendation | HOLD RELEASE |
| Skill | regression-test-runner |

## Recommendation

**HOLD RELEASE** — 1 blocking HIGH severity regression found in the checkout flow. The cart reducer has an off-by-one error that causes the order total to exclude the last item. This would result in customer under-charges and must be fixed before release.

---

## Test Summary

| Metric | Value |
|---|---|
| Total Tests | 7 |
| Passed | 5 |
| Genuine Regressions | 1 (HIGH severity) |
| Flaky Tests | 1 |
| Pass Rate | 71.4% |

---

## Blocking Defects

### checkout_multiple_items — HIGH SEVERITY REGRESSION

**Test:** checkout_multiple_items
**Severity:** HIGH
**Expected:** Order total matches the sum of all items in cart
**Actual:** Order total excludes the last item — off-by-one error in cart reducer

**Impact:** Any customer purchasing 2+ items will be undercharged. This creates financial exposure and incorrect order records.

**Root cause hypothesis:** Off-by-one error in cart reducer's summing logic — likely introduced in the checkout refactor in this release.

**Action:** File P1 bug ticket immediately. Release is blocked until this defect is resolved and regression test passes.

---

## Flaky Tests

### order_history_pagination

Intermittent failure — not a genuine regression. Re-run in isolation. If flake rate exceeds 20%, investigate test data ordering assumption.

---

## Release Hold Criteria

Release is blocked until:
1. `checkout_multiple_items` test passes cleanly on a fixed build
2. Fix is reviewed by a second engineer
3. Regression suite re-run confirms no new failures introduced by the fix
