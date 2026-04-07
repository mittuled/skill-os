# Hardware Lifecycle Management Framework

Reference for the `hardware-lifecycle-manager` skill.

---

## 1. Asset Lifecycle Stages

```
Procurement → Configuration → Deployment → In-Service → Maintenance → End-of-Life
```

| Stage | Activities | Key Output |
|-------|-----------|-----------|
| **Procurement** | Needs assessment, vendor selection, purchase order | PO confirmation, delivery ETA |
| **Configuration** | OS imaging, security software, user account setup | Configured device ready for deployment |
| **Deployment** | Shipping or in-person handoff, user onboarding | Signed asset receipt, asset registered |
| **In-Service** | Warranty tracking, performance monitoring | Current asset registry |
| **Maintenance** | Repairs, OS updates, peripherals replacement | Maintenance log |
| **End-of-Life** | Retrieval, data wipe, redeploy or dispose | Data-wipe certificate, disposition record |

---

## 2. Standard Hardware Configurations

### Laptop Tiers

| Tier | Target Role | Spec Level | Refresh Cycle |
|------|------------|-----------|--------------|
| **Tier A — Developer** | Engineering, Data, Design | High (16GB+ RAM, 512GB+ SSD) | 3 years |
| **Tier B — Power User** | Marketing, Product, Finance | Mid (16GB RAM, 256GB SSD) | 3–4 years |
| **Tier C — Standard** | Operations, Support, Sales | Standard (8GB RAM, 256GB SSD) | 4 years |
| **Tier D — Executive** | C-Level | Premium (as requested) | 3 years |

### Accessories — Standard Kit

- External monitor (27" or larger) for office-based roles
- Keyboard and mouse (wired or wireless based on preference)
- USB-C hub / docking station for laptop users
- Headset for customer-facing and remote roles

---

## 3. Procurement Decision Matrix

| Scenario | Recommended Action | Approval Required |
|----------|--------------------|------------------|
| New hire before start date | Order new device based on tier | Auto-approved for budgeted headcount |
| Refresh — warranty expiring <90 days | Order replacement; plan parallel deployment | IT Manager approval |
| Device failure — warranty active | File warranty claim; loan device if needed | None — use loan pool |
| Device failure — warranty expired | Assess: repair vs. replace based on TCO | IT Manager approval if >$500 |
| Role change requiring tier upgrade | Order upgrade device; redeploy old | Manager approval |
| Leaver — device return | Wipe and re-add to redeployment pool | No new purchase |

---

## 4. Total Cost of Ownership (TCO) Model

When deciding between repair and replace, calculate TCO:

```
TCO = Purchase Price + Configuration Cost + Annual Support + End-of-Life Disposal
    - Residual Value at Disposal
```

| Factor | Typical Value |
|--------|-------------|
| Laptop purchase price | $1,200 – $2,500 depending on tier |
| Configuration time | 2–4 hours @ internal IT rate |
| Annual warranty / support | $150 – $300/year |
| End-of-life disposal | $0 (resell) to $50 (certified destruction) |
| Residual value at 3 years | 15–25% of purchase price |

**Rule of thumb**: If repair cost exceeds 40% of the replacement cost for a device older than 2 years, replace.

---

## 5. Device Refresh Triggers

| Trigger | Action |
|---------|--------|
| Warranty expires within 90 days | Initiate refresh procurement |
| Device age exceeds tier refresh cycle | Add to next refresh batch |
| Recurring hardware failures (3+ in 12 months) | Flag for early refresh |
| Employee role change requiring higher tier | Upgrade procurement |
| OS no longer supported by vendor | Mandatory refresh |

---

## 6. End-of-Life Disposition Matrix

| Device Condition | Age | Disposition |
|-----------------|-----|------------|
| Functional, <3 years old | — | Redeploy to new hire or role change |
| Functional, 3–4 years old | Moderate | Redeploy to standard tier if spec meets current requirements |
| Functional, >4 years old | Aged | Resell to certified refurbisher |
| Damaged, repairable | Any | Repair and redeploy if cost-effective |
| Damaged, non-repairable | Any | Certified e-waste recycling with data destruction certificate |
| Sensitive data device | Any | Certified data destruction before any disposition |

---

## 7. Data Wipe Standards

| Method | Standard | Use Case | Certificate Required? |
|--------|---------|---------|----------------------|
| Software overwrite (NIST 800-88 Clear) | 3-pass overwrite | Standard redeployment | No |
| Software wipe (NIST 800-88 Purge) | DoD 5220.22-M | Sensitive data, regulated industries | Yes |
| Physical destruction | NIST 800-88 Destroy | Damaged, non-recoverable SSDs | Yes |
| Remote wipe via MDM | Apple MDM / Intune | Lost or stolen devices | Log MDM wipe confirmation |

**Requirement**: Any device leaving company control must have a documented wipe or destruction record.

---

## 8. Asset Registry — Required Fields

| Field | Type | Notes |
|-------|------|-------|
| `asset_id` | String | Internal asset tag ID |
| `make_model` | String | e.g., "MacBook Pro 14 M3" |
| `serial_number` | String | From device underside or BIOS |
| `purchase_date` | Date | From invoice |
| `purchase_price` | Currency | Excluding tax |
| `warranty_expiry` | Date | From vendor confirmation |
| `assigned_user` | Email | Current assigned user |
| `assignment_date` | Date | When assigned to current user |
| `location` | String | Office / Remote — City |
| `os_version` | String | Current OS build |
| `status` | Enum | `Active / Loan / In-Repair / EOL / Disposed` |
| `disposition_date` | Date | When retired (if applicable) |
| `wipe_certificate_ref` | String | Reference to wipe record (if applicable) |

---

*Reference version 1.0 — Technical Operations / IT Operations Manager*
