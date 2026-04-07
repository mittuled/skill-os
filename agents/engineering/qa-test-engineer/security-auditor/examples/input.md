# Scenario: Security Audit of API Gateway Before Compliance Review

QA engineer conducts a security audit of the new API gateway before an SOC 2 compliance review.

## Input Parameters

```json
{
  "audit_scope": "API Gateway v2 — pre-SOC2 review",
  "findings": [
    {
      "title": "JWT tokens never expire — no expiry claim set",
      "severity": "critical",
      "category": "authentication",
      "exploitation_scenario": "Stolen token remains valid indefinitely, enabling persistent unauthorized access",
      "affected_component": "AuthMiddleware.verify_token"
    },
    {
      "title": "SQL query in user search uses string concatenation",
      "severity": "high",
      "category": "injection",
      "exploitation_scenario": "Attacker injects malicious SQL via search parameter, exposing all user records",
      "affected_component": "UserRepository.search"
    },
    {
      "title": "Rate limiting absent on /auth/login endpoint",
      "severity": "medium",
      "category": "authentication",
      "exploitation_scenario": "Brute force attack on credentials without throttling",
      "affected_component": "AuthController.login"
    },
    {
      "title": "Error messages expose stack traces to API consumers",
      "severity": "low",
      "category": "configuration",
      "exploitation_scenario": "Stack traces reveal internal framework versions and file paths",
      "affected_component": "GlobalErrorHandler"
    }
  ]
}
```
