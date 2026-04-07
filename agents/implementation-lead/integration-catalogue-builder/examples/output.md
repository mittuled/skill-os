# Integration Catalogue — Workday HRIS

| Field | Value |
|---|---|
| Date | 2026-03-31 |
| Integration | Workday HRIS |
| Category | HRIS |
| Status | GA |
| Platform Version | v3.2+ |
| Support | integrations-support@company.com |
| Skill | integration-catalogue-builder |

## Description

Syncs employee roster data from Workday to the platform, keeping user records, department assignments, and manager hierarchies current without manual CSV imports.

## Prerequisites

Before beginning setup, confirm all prerequisites are met:

1. Workday tenant must be on version 33 or later
2. Customer must have a Workday Integration System User (ISU) with permissions: `Get_Workers`, `Get_Organizations`
3. Customer IT admin must whitelist the platform's IP range (provided by implementation engineer)
4. Platform tenant must be provisioned before configuring the integration

## Authentication

**Method:** Workday SOAP API with ISU username and password (Basic Auth over TLS)

## Setup Steps

1. In the platform admin panel, navigate to **Integrations > HRIS > Workday**
2. Enter the customer's Workday tenant URL: `https://{tenant}.workday.com/ccx/service/{tenant_id}`
3. Enter the ISU username and password provided by the customer
4. Click **Test Connection** — verify green status before proceeding
5. Configure sync scope: select fields to sync (First Name, Last Name, Email, Department, Manager, Job Title, Start Date)
6. Set sync frequency (recommended: every 4 hours for mid-market, every 1 hour for enterprise)
7. Run initial full sync — monitor progress in the sync log
8. Verify record count matches Workday active employee count
9. Enable ongoing scheduled sync

## Data Mapping

| Workday Field | Platform Field |
|---|---|
| `Worker_ID` | `external_id` |
| `Legal_Name.First_Name` | `first_name` |
| `Legal_Name.Last_Name` | `last_name` |
| `Work_Email` | `email` |
| `Primary_Job.Position.Supervisory_Organization` | `department` |
| `Primary_Job.Manager_as_of_last_detected_manager_change` | `manager_email` |

## Known Limitations

1. Workday tenant versions below 33 are not supported — customer must upgrade first
2. Terminated employees are deactivated within 1 sync cycle, not immediately
3. Custom Workday fields are not supported — only the standard fields listed in data mapping
4. Maximum 10,000 active employees per sync run — enterprise customers above this limit must contact support

## Known Errors and Fixes

| Error | Cause | Fix |
|---|---|---|
| Authentication failure (401) | ISU password expired or permissions revoked | Ask customer to reset ISU password and verify Get_Workers / Get_Organizations permissions |
| Sync timeout | Workday tenant response time exceeded 30s (common for large orgs) | Switch to off-peak sync schedule (e.g., 2am customer local time) |

## Maintenance Notes

This catalogue entry covers Platform v3.2+. Review this entry when the platform ships a new major version or when Workday announces API changes in their release notes (published quarterly). Next scheduled review: June 2026.
