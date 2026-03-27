# Scenario: Blue-Green Deployment Script

Create a bash deployment script for an AWS ECS service that:

1. Deploys a new task definition (green) alongside the existing one (blue)
2. Waits for the green service to become healthy
3. Switches the ALB target group to green
4. Drains connections from the blue target group
5. Tears down the blue service after successful cutover
