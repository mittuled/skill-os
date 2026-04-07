# Identity Access Management — Example Input

## Scenario

Meridian AI has grown to 22 employees and is preparing for a SOC 2 Type II audit in Q3. The IT Manager is running an IAM compliance audit to identify MFA gaps, SSO non-enrollment, stale accounts, and privileged access reviews that are overdue. Two new hires haven't completed MFA setup yet, and one contractor's account hasn't been used in 95 days.

## Input JSON

```json
{
  "company_name": "Meridian AI",
  "company_size_tier": "startup_small",
  "users": [
    {"username": "alex.chen", "name": "Alex Chen", "department": "Executive", "access_level": "admin", "mfa_enabled": true, "sso_enrolled": true, "is_active": true, "days_since_login": 1, "days_since_access_review": 45},
    {"username": "priya.nair", "name": "Priya Nair", "department": "Engineering", "access_level": "admin", "mfa_enabled": true, "sso_enrolled": true, "is_active": true, "days_since_login": 1, "days_since_access_review": 45},
    {"username": "jordan.lee", "name": "Jordan Lee", "department": "Product", "access_level": "standard", "mfa_enabled": true, "sso_enrolled": true, "is_active": true, "days_since_login": 2, "days_since_access_review": 120},
    {"username": "marcus.webb", "name": "Marcus Webb", "department": "Engineering", "access_level": "production", "mfa_enabled": true, "sso_enrolled": true, "is_active": true, "days_since_login": 1, "days_since_access_review": 200},
    {"username": "diana.torres", "name": "Diana Torres", "department": "Design", "access_level": "standard", "mfa_enabled": true, "sso_enrolled": true, "is_active": true, "days_since_login": 3, "days_since_access_review": 120},
    {"username": "sarah.chen", "name": "Sarah Chen", "department": "Engineering", "access_level": "production", "mfa_enabled": false, "sso_enrolled": true, "is_active": true, "days_since_login": 5, "days_since_access_review": 5},
    {"username": "new.hire2", "name": "New Hire 2", "department": "Sales", "access_level": "standard", "mfa_enabled": false, "sso_enrolled": false, "is_active": true, "days_since_login": 10, "days_since_access_review": 10},
    {"username": "contractor.ext", "name": "External Contractor", "department": "Engineering", "access_level": "staging", "mfa_enabled": true, "sso_enrolled": false, "is_active": true, "days_since_login": 95, "days_since_access_review": 180},
    {"username": "kevin.park", "name": "Kevin Park", "department": "Operations", "access_level": "billing", "mfa_enabled": true, "sso_enrolled": true, "is_active": true, "days_since_login": 7, "days_since_access_review": 195}
  ]
}
```
