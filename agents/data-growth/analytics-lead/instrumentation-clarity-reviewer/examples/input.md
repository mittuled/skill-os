# Scenario: Reviewing Instrumentation Spec for New Checkout Flow

The analytics lead is reviewing the instrumentation spec submitted by the growth engineer for the new checkout flow. Some events need clarity review before the engineer implements tracking.

## Input Parameters

```json
{
  "spec_name": "Checkout Flow Instrumentation Spec v1",
  "events": [
    {
      "name": "checkout_started",
      "properties": [
        {"name": "user_id", "type": "string"},
        {"name": "timestamp", "type": "datetime"},
        {"name": "session_id", "type": "string"},
        {"name": "platform", "type": "string"},
        {"name": "cart_value_usd", "type": "float"},
        {"name": "item_count", "type": "integer"}
      ]
    },
    {
      "name": "PaymentClicked",
      "properties": [
        {"name": "user_id", "type": "string"},
        {"name": "payment_method"},
        {"name": "cart_value_usd", "type": "float"}
      ]
    },
    {
      "name": "purchase",
      "properties": [
        {"name": "order_id", "type": "string"},
        {"name": "revenue_usd", "type": "float"}
      ]
    }
  ]
}
```
