#!/usr/bin/env bash
set -euo pipefail

NAMESPACE="${1:-production}"
STABLE_DEPLOY="api-stable"
CANARY_DEPLOY="api-canary"
SLACK_WEBHOOK="$SLACK_ROLLBACK_WEBHOOK_URL"

echo "==> Capturing canary diagnostics before rollback"
kubectl logs -n "$NAMESPACE" -l app=api,track=canary --tail=500 > "/tmp/canary-logs-$(date +%s).txt"
kubectl describe deploy "$CANARY_DEPLOY" -n "$NAMESPACE" > "/tmp/canary-describe-$(date +%s).txt"

echo "==> Scaling canary deployment to 0"
kubectl scale deploy "$CANARY_DEPLOY" -n "$NAMESPACE" --replicas=0
kubectl rollout status deploy "$CANARY_DEPLOY" -n "$NAMESPACE" --timeout=60s

echo "==> Routing 100% traffic to stable"
kubectl patch virtualservice api-vs -n "$NAMESPACE" --type=json -p='[
  {"op": "replace", "path": "/spec/http/0/route", "value": [
    {"destination": {"host": "api-stable", "port": {"number": 8080}}, "weight": 100}
  ]}
]'

echo "==> Verifying stable deployment health"
kubectl rollout status deploy "$STABLE_DEPLOY" -n "$NAMESPACE" --timeout=120s
READY=$(kubectl get deploy "$STABLE_DEPLOY" -n "$NAMESPACE" -o jsonpath='{.status.readyReplicas}')
echo "    Stable replicas ready: $READY"

echo "==> Sending Slack notification"
curl -s -X POST "$SLACK_WEBHOOK" -H 'Content-Type: application/json' -d "{
  \"text\": \":rotating_light: Canary rollback completed in \`$NAMESPACE\`. Stable deployment serving 100% traffic. Diagnostics saved to /tmp/.\"
}"

echo "==> Rollback complete."
