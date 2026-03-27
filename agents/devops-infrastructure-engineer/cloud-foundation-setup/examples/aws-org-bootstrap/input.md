# Scenario: AWS Organization Bootstrap

Create a Terraform configuration that:

1. Sets up an AWS Organization with consolidated billing
2. Creates dev, staging, and production accounts
3. Enables CloudTrail across all accounts
4. Enforces SCPs that deny root user actions and restrict regions
