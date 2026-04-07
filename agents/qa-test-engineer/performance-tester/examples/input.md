# Scenario: Performance Test for /api/search Endpoint Refactor

The search endpoint was refactored to use a new index. Performance tests are required before release.

## Input Parameters

```json
{
  "endpoint": "/api/search",
  "budget": {
    "p50_latency_ms": 80,
    "p95_latency_ms": 250,
    "p99_latency_ms": 800,
    "throughput_rps": 300,
    "error_rate_pct": 0.5
  },
  "measured": {
    "p50_latency_ms": 65,
    "p95_latency_ms": 380,
    "p99_latency_ms": 750,
    "throughput_rps": 340,
    "error_rate_pct": 0.2
  },
  "baseline_regression": {
    "p95_change_pct": 52,
    "context": "p95 increased 52% vs previous baseline of 250ms — likely due to missing query cache warm-up"
  }
}
```
