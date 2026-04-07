# Scenario: Unit Test Run for Pricing Calculation Refactor

Developer refactored the pricing calculator module and needs CI unit test validation before merge.

## Input Parameters

```json
{
  "suite_name": "pricing-calculator unit tests",
  "passed": 87,
  "failed": 2,
  "coverage_pct": 78.5,
  "coverage_threshold_pct": 80,
  "coverage_delta_pct": -3.2,
  "failing_tests": [
    {"test": "calculate_discount_for_annual_plan", "error": "AssertionError: Expected 0.20 discount, got 0.15"},
    {"test": "apply_promo_code_stacks_with_tier_discount", "error": "AttributeError: 'NoneType' has no attribute 'discount_rate' — promo code fixture returns None in test setup"}
  ]
}
```
