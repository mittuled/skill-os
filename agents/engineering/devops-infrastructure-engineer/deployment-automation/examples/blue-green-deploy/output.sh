#!/usr/bin/env bash
set -euo pipefail

CLUSTER="$1"
SERVICE="$2"
IMAGE="$3"
ALB_LISTENER_ARN="$4"
GREEN_TG_ARN="$5"
BLUE_TG_ARN="$6"

echo "==> Registering new task definition with image: $IMAGE"
TASK_DEF=$(aws ecs describe-task-definition --task-definition "$SERVICE" --query 'taskDefinition')
NEW_TASK_DEF=$(echo "$TASK_DEF" | jq --arg IMG "$IMAGE" \
  '.containerDefinitions[0].image = $IMG | del(.taskDefinitionArn, .revision, .status, .requiresAttributes, .compatibilities, .registeredAt, .registeredBy)')
NEW_ARN=$(aws ecs register-task-definition --cli-input-json "$NEW_TASK_DEF" --query 'taskDefinition.taskDefinitionArn' --output text)

echo "==> Deploying green service with task: $NEW_ARN"
aws ecs update-service --cluster "$CLUSTER" --service "${SERVICE}-green" \
  --task-definition "$NEW_ARN" --desired-count 2

echo "==> Waiting for green service to stabilize..."
aws ecs wait services-stable --cluster "$CLUSTER" --services "${SERVICE}-green"

echo "==> Health check on green target group"
for i in {1..30}; do
  HEALTH=$(aws elbv2 describe-target-health --target-group-arn "$GREEN_TG_ARN" \
    --query 'TargetHealthDescriptions[*].TargetHealth.State' --output text)
  if echo "$HEALTH" | grep -qv "healthy"; then
    echo "    Attempt $i: targets not yet healthy, waiting 10s..."
    sleep 10
  else
    echo "    All green targets healthy."
    break
  fi
  [ "$i" -eq 30 ] && { echo "ERROR: Green targets never became healthy"; exit 1; }
done

echo "==> Switching ALB listener to green target group"
aws elbv2 modify-listener --listener-arn "$ALB_LISTENER_ARN" \
  --default-actions Type=forward,TargetGroupArn="$GREEN_TG_ARN"

echo "==> Draining blue (waiting 30s for in-flight requests)"
sleep 30

echo "==> Scaling down blue service"
aws ecs update-service --cluster "$CLUSTER" --service "${SERVICE}-blue" --desired-count 0

echo "==> Blue-green deployment complete."
