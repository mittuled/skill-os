# Scenario: Writing Instrumentation Spec for User Signup Flow

The analytics lead is writing the instrumentation spec for the new user signup flow covering 3 events: signup page viewed, signup form submitted, and account created.

## Input Parameters

```json
{
  "spec_name": "User Signup Flow Instrumentation Spec",
  "feature_name": "User Signup",
  "events": [
    {
      "name": "signup_page_viewed",
      "trigger": "Fired when the user navigates to or loads the page",
      "firing_location": "client",
      "properties": [
        {"name": "referrer_source", "type": "string", "required": false, "description": "UTM source or referrer domain"},
        {"name": "variant", "type": "string", "required": false, "description": "A/B test variant shown"}
      ]
    },
    {
      "name": "signup_form_submitted",
      "trigger": "Fired when the user submits the form successfully (after client validation passes)",
      "firing_location": "client",
      "properties": [
        {"name": "signup_method", "type": "string", "required": true, "description": "email | google | github"},
        {"name": "plan_selected", "type": "string", "required": false, "description": "Plan tier selected at signup"}
      ]
    },
    {
      "name": "account_created",
      "trigger": "Fired server-side when the API endpoint responds with a success status",
      "firing_location": "server",
      "properties": [
        {"name": "user_id", "type": "string", "required": true, "description": "Newly created user ID"},
        {"name": "plan_tier", "type": "string", "required": true, "description": "Assigned plan tier"}
      ]
    }
  ]
}
```
