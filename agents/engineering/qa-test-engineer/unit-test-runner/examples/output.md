# Unit Test Report — pricing-calculator

| Field | Value |
|---|---|
| Date | 2026-03-31 |
| Author | QA Test Engineer |
| Suite | pricing-calculator unit tests |
| Passed / Total | 87 / 89 |
| Coverage | 78.5% (threshold: 80%) |
| Verdict | FAIL |
| Skill | unit-test-runner |

## Recommendation

**FAIL** — 2 tests failing and coverage 78.5% is below the 80% threshold. Both must be resolved before merge.

---

## Summary

| Metric | Value | Status |
|---|---|---|
| Total Tests | 89 | — |
| Passed | 87 | — |
| Failed | 2 | FAIL |
| Coverage | 78.5% | FAIL (threshold: 80%) |
| Coverage Delta | -3.2% | Down from previous |

---

## Failing Tests

### calculate_discount_for_annual_plan

**Error:** `AssertionError: Expected 0.20 discount, got 0.15`
**Diagnosis:** Likely a genuine logic error — the annual plan discount multiplier was changed in the refactor. Verify the correct discount rate in the pricing configuration and update the implementation (not the test).

### apply_promo_code_stacks_with_tier_discount

**Error:** `AttributeError: 'NoneType' has no attribute 'discount_rate' — promo code fixture returns None`
**Diagnosis:** Test setup issue — the promo code fixture is returning `None` instead of a promo code object. Check fixture initialization; may be a missing factory call after the refactor renamed the promo code model.

---

## Coverage

Coverage dropped 3.2% to 78.5% — below the 80% threshold. The uncovered paths are likely in the new discount stacking logic added in this refactor. Add unit tests for:
1. Annual plan + promo code combination scenarios
2. Edge case: promo code that pushes total discount below zero

Merge is blocked until coverage returns to ≥80%.
