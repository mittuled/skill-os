# Scenario: AWS Auto Scaling with Terraform

Create a Terraform configuration that:

1. Defines an ECS service with auto-scaling between 2 and 10 tasks
2. Scales up when average CPU exceeds 70%
3. Scales down when average CPU drops below 30%
4. Includes a cooldown period to prevent thrashing
