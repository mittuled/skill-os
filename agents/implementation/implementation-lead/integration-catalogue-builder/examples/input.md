# Scenario: Add Workday HRIS Integration to the Catalogue

The product team has shipped GA support for Workday HRIS integration. Implementation engineers have been configuring it ad hoc for the past two months and are getting repeated questions from customers. The Implementation Lead needs to document the integration in the catalogue so setup is self-serve.

## Input Parameters

```json
{
  "integration_name": "Workday HRIS",
  "category": "HRIS",
  "status": "GA",
  "description": "Syncs employee roster data from Workday to the platform, keeping user records, department assignments, and manager hierarchies current without manual CSV imports.",
  "prerequisites": [
    "Workday tenant must be on version 33 or later",
    "Customer must have a Workday Integration System User (ISU) with the following permissions: Get_Workers, Get_Organizations",
    "Customer IT admin must whitelist the platform's IP range (provided by implementation engineer)",
    "Platform tenant must be provisioned before configuring the integration"
  ],
  "authentication_method": "Workday SOAP API with ISU username and password (Basic Auth over TLS)",
  "setup_steps": [
    "1. In the platform admin panel, navigate to Integrations > HRIS > Workday",
    "2. Enter the customer's Workday tenant URL (format: https://{tenant}.workday.com/ccx/service/{tenant_id})",
    "3. Enter the ISU username and password provided by the customer",
    "4. Click 'Test Connection' — verify green status before proceeding",
    "5. Configure sync scope: select which fields to sync (First Name, Last Name, Email, Department, Manager, Job Title, Start Date)",
    "6. Set sync frequency (recommended: every 4 hours for mid-market, every 1 hour for enterprise)",
    "7. Run initial full sync — monitor progress in the sync log",
    "8. Verify record count matches Workday active employee count",
    "9. Enable ongoing scheduled sync"
  ],
  "data_mapping": [
    {"workday_field": "Worker_ID", "platform_field": "external_id"},
    {"workday_field": "Legal_Name.First_Name", "platform_field": "first_name"},
    {"workday_field": "Legal_Name.Last_Name", "platform_field": "last_name"},
    {"workday_field": "Work_Email", "platform_field": "email"},
    {"workday_field": "Primary_Job.Position.Supervisory_Organization", "platform_field": "department"},
    {"workday_field": "Primary_Job.Manager_as_of_last_detected_manager_change", "platform_field": "manager_email"}
  ],
  "limitations": [
    "Workday tenant versions below 33 are not supported — customer must upgrade first",
    "Terminated employees are deactivated in the platform within 1 sync cycle, not immediately",
    "Custom Workday fields are not supported — only the standard fields listed in data mapping",
    "Maximum 10,000 active employees per sync run — enterprise customers with more must contact support"
  ],
  "known_errors": [
    {"error": "Authentication failure (401)", "cause": "ISU password expired or permissions revoked", "fix": "Ask customer to reset ISU password and verify permissions"},
    {"error": "Sync timeout", "cause": "Workday tenant response time exceeded 30s (common for large orgs)", "fix": "Switch to off-peak sync schedule (e.g., 2am customer timezone)"}
  ],
  "product_versions": "Platform v3.2+",
  "support_contact": "integrations-support@company.com",
  "last_reviewed": "2026-03-31"
}
```
