# Platform Scale Preparation — Example Input

## Scenario

Meridian AI is planning an AI workflow feature launch to 100% of Pro and Enterprise users (projected 10x traffic spike). The CTO asks the platform team to run a scale readiness assessment before the launch. The platform currently handles 200 RPS; the launch is expected to peak at 2,000 RPS. The database is a known bottleneck with a single PostgreSQL instance and no read replicas.

## Input JSON

```json
{
  "system_name": "Meridian AI AI Workflow Platform",
  "current_rps": 200,
  "target_load_multiplier": 10,
  "dimensions": [
    {
      "dimension": "stateless_services",
      "score": 8,
      "is_single_point_of_failure": false,
      "notes": "All API services are stateless. Session state managed in Redis.",
      "mitigations": ["Kubernetes HPA configured for API pods"]
    },
    {
      "dimension": "database_scalability",
      "score": 3,
      "is_single_point_of_failure": true,
      "notes": "Single RDS PostgreSQL instance. No read replicas. Connection pool limit is 100. At current load (200 RPS) we hit 80% pool utilization.",
      "mitigations": []
    },
    {
      "dimension": "caching_strategy",
      "score": 6,
      "is_single_point_of_failure": false,
      "notes": "Redis cache for session and hot data. AI model results are not cached — each request hits the AI API.",
      "mitigations": ["Redis cluster (3 nodes) deployed"]
    },
    {
      "dimension": "async_processing",
      "score": 7,
      "is_single_point_of_failure": false,
      "notes": "AI workflow jobs run via SQS + Lambda worker pool. Workers can scale to 500 concurrent.",
      "mitigations": ["SQS dead letter queue configured", "Lambda concurrency limit set"]
    },
    {
      "dimension": "auto_scaling",
      "score": 7,
      "is_single_point_of_failure": false,
      "notes": "Kubernetes HPA scales API pods. Lambda scales automatically. RDS does not auto-scale.",
      "mitigations": ["HPA configured: min 3, max 20 API pods"]
    },
    {
      "dimension": "load_testing",
      "score": 2,
      "is_single_point_of_failure": false,
      "notes": "No load tests have been run. Last capacity review was 8 months ago.",
      "mitigations": []
    }
  ]
}
```
