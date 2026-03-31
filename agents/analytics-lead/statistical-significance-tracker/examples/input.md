# Scenario: Evaluating Onboarding A/B Test After 10 Days

The growth team is running an A/B test on the onboarding flow. After 10 days, the treatment shows higher conversion. The analytics lead is evaluating whether results are significant enough to ship.

## Input Parameters

```json
{
  "experiment_name": "Onboarding Flow v2 vs v1",
  "confidence_level": 0.95,
  "expected_treatment_ratio": 0.5,
  "days_running": 10,
  "min_duration_days": 14,
  "control": {
    "n": 1850,
    "conversions": 629
  },
  "treatment": {
    "n": 1823,
    "conversions": 712
  }
}
```
