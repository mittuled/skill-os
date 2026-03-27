# Scenario: Threat Model Sketch for Microservice Authentication

Sketch a threat model diagram for a microservice architecture where:

1. A mobile app authenticates via OAuth2 through an API Gateway
2. The API Gateway validates JWTs and routes to internal services
3. Internal services communicate via gRPC with mTLS
4. User data is stored in a PostgreSQL database
5. Sessions are cached in Redis
