# Scenario: Full Regression Suite Before v4.2 Release

QA engineer runs the full regression suite for the v4.2 release candidate which includes changes to the checkout flow.

## Input Parameters

```json
{
  "release_name": "Product v4.2 Release Candidate",
  "suite_type": "full",
  "test_results": [
    {"test_name": "user_registration_flow", "passed": true},
    {"test_name": "checkout_single_item", "passed": true},
    {"test_name": "checkout_multiple_items", "passed": false, "failure_type": "genuine_regression", "severity": "high", "expected": "Order total matches sum of items", "actual": "Order total excludes last item — off-by-one in cart reducer"},
    {"test_name": "coupon_code_application", "passed": true},
    {"test_name": "order_history_pagination", "passed": false, "failure_type": "flaky_test"},
    {"test_name": "email_notification_on_order", "passed": true},
    {"test_name": "admin_refund_processing", "passed": true}
  ]
}
```
