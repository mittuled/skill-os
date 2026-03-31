# Scenario: Requirements Extraction — Bright Horizons Healthcare

Bright Horizons Healthcare signed a 2-year enterprise contract for the platform to replace their manual compliance tracking spreadsheets. The sales team has handed off the deal with a signed SOW covering 500 seats across 3 departments. The implementation engineer ran two discovery sessions with the customer's IT director and department leads and is compiling the requirements document for customer sign-off.

## Input Parameters

```json
{
  "customer_name": "Bright Horizons Healthcare",
  "sales_context": {
    "contract_value": "$240,000 ARR",
    "seats": 500,
    "term": "24 months",
    "departments": ["Compliance", "HR", "Clinical Operations"],
    "key_promise": "Replace spreadsheet-based compliance tracking by June 1"
  },
  "discovery_notes": {
    "functional_requirements": [
      "Track compliance certifications for 500 clinical staff with expiry alerts",
      "Generate monthly compliance reports for department heads",
      "Support custom compliance frameworks (HIPAA, OSHA, Joint Commission)",
      "Role-based dashboards: staff view (own certs), manager view (team status), admin view (org-wide)"
    ],
    "technical_environment": [
      "Azure Active Directory for SSO (SAML 2.0)",
      "Windows 11 workstations, Chrome browser",
      "No on-premise infrastructure — fully cloud-based preferred",
      "HIPAA Business Associate Agreement required before data ingestion"
    ],
    "integration_requirements": [
      "Azure AD — SSO and user provisioning via SCIM",
      "Workday — employee roster sync (department, role, start date)",
      "Email (Microsoft 365) — certification expiry notifications"
    ],
    "data_migration_requirements": [
      "Migrate 500 employee records from Excel spreadsheets",
      "Historical certification records (3 years) in CSV format",
      "Data mapping session required with HR to confirm field alignment"
    ],
    "user_and_access_requirements": [
      "3 admin accounts (IT Director, Compliance Lead, HR Director)",
      "50 manager accounts with team dashboard access",
      "447 staff accounts with self-service certification upload"
    ],
    "acceptance_criteria": [
      "All 500 employee records migrated and verified",
      "SSO login functional for 100% of users",
      "Workday sync updating employee roster within 24 hours of changes",
      "Compliance report generation tested by department heads",
      "Customer IT Director signs off on security configuration"
    ]
  },
  "open_items": [
    "BAA not yet signed — Legal review in progress, expected April 5",
    "Workday API access: Bright Horizons IT to provision API credentials (pending)"
  ],
  "sign_off_required": true
}
```
