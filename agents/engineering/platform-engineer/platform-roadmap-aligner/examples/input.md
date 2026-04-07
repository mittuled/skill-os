# Platform Roadmap Aligner — Example Input

## Scenario

Meridian AI is planning Q2 2026. The product team has 4 features planned. Two features depend on platform work that may not land in time. The platform team needs to check whether their roadmap items arrive before the product features that depend on them.

## Input JSON

```json
{
  "team_name": "Meridian AI Engineering",
  "planning_period": "Q2 2026",
  "product_items": [
    {
      "id": "PROD-201",
      "name": "Multi-tenant workspace support",
      "target_sprint": "Q2-S3",
      "owner": "Squad Orion",
      "platform_dependencies": ["PLAT-101", "PLAT-102"],
      "notes": "High-impact enterprise feature. Needs SSO tenant isolation and DB row-level security."
    },
    {
      "id": "PROD-202",
      "name": "AI workflow v2 — streaming responses",
      "target_sprint": "Q2-S1",
      "owner": "Squad Nova",
      "platform_dependencies": ["PLAT-103"],
      "notes": "Streaming requires WebSocket support at API gateway level."
    },
    {
      "id": "PROD-203",
      "name": "Compliance report exporter",
      "target_sprint": "Q2-S2",
      "owner": "Squad Orion",
      "platform_dependencies": [],
      "notes": "No platform dependencies — fully self-contained."
    },
    {
      "id": "PROD-204",
      "name": "Real-time collaboration (beta)",
      "target_sprint": "Q2-S4",
      "owner": "Squad Nova",
      "platform_dependencies": ["PLAT-104"],
      "notes": "Needs low-latency pub/sub event bus."
    }
  ],
  "platform_items": [
    {
      "id": "PLAT-101",
      "name": "SSO tenant isolation (Okta multi-tenant config)",
      "target_sprint": "Q2-S2",
      "dependency_type": "blocking",
      "notes": "Engineering estimate: 3-week implementation."
    },
    {
      "id": "PLAT-102",
      "name": "Row-level security in PostgreSQL",
      "target_sprint": "Q2-S4",
      "dependency_type": "blocking",
      "notes": "Complex migration. Lower priority than PLAT-101."
    },
    {
      "id": "PLAT-103",
      "name": "WebSocket support at API gateway",
      "target_sprint": "Q2-S2",
      "dependency_type": "blocking",
      "notes": "AWS API Gateway configuration + load balancer changes."
    },
    {
      "id": "PLAT-104",
      "name": "Event bus (AWS EventBridge or Kafka)",
      "target_sprint": "Q2-S3",
      "dependency_type": "enabling",
      "notes": "Platform team evaluating Kafka vs. EventBridge."
    }
  ]
}
```
