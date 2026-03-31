# Hardware Lifecycle Manager — Example Input

## Scenario

Meridian AI has 18 devices across the company. The IT Manager is doing the annual fleet audit to identify devices due for refresh and flag any expiring warranties before the Q2 budget planning cycle. Several of the early employee laptops are approaching or past their refresh cycle.

## Input JSON

```json
{
  "company_name": "Meridian AI",
  "action": "audit",
  "assets": [
    {"asset_id": "MBP-001", "device_type": "macbook_pro", "model": "MacBook Pro 16\" M1", "assigned_to": "Alex Chen (CEO)", "age_years": 2, "status": "deployed", "warranty_months_remaining": 10},
    {"asset_id": "MBP-002", "device_type": "macbook_pro", "model": "MacBook Pro 14\" M1", "assigned_to": "Priya Nair (CTO)", "age_years": 2, "status": "deployed", "warranty_months_remaining": 10},
    {"asset_id": "MBA-001", "device_type": "macbook_air", "model": "MacBook Air M2", "assigned_to": "Jordan Lee (CPO)", "age_years": 1, "status": "deployed", "warranty_months_remaining": 23},
    {"asset_id": "MBP-003", "device_type": "macbook_pro", "model": "MacBook Pro 13\" Intel", "assigned_to": "Marcus Webb (Sr. Engineer)", "age_years": 4, "status": "deployed", "warranty_months_remaining": 0},
    {"asset_id": "MBP-004", "device_type": "macbook_pro", "model": "MacBook Pro 13\" Intel", "assigned_to": "Diana Torres (Design)", "age_years": 4, "status": "deployed", "warranty_months_remaining": 0},
    {"asset_id": "MBP-005", "device_type": "macbook_pro", "model": "MacBook Pro 13\" Intel", "assigned_to": "Kevin Park (Ops)", "age_years": 5, "status": "deployed", "warranty_months_remaining": 0},
    {"asset_id": "MBA-002", "device_type": "macbook_air", "model": "MacBook Air Intel", "assigned_to": "Unassigned", "age_years": 4, "status": "in_storage", "warranty_months_remaining": 0},
    {"asset_id": "MON-001", "device_type": "monitor", "model": "LG 27\" 4K", "assigned_to": "Alex Chen (CEO)", "age_years": 3, "status": "deployed", "warranty_months_remaining": 2},
    {"asset_id": "MON-002", "device_type": "monitor", "model": "LG 27\" 4K", "assigned_to": "Priya Nair (CTO)", "age_years": 3, "status": "deployed", "warranty_months_remaining": 2},
    {"asset_id": "IPH-001", "device_type": "iphone", "model": "iPhone 14 Pro", "assigned_to": "Alex Chen (CEO)", "age_years": 2, "status": "deployed", "warranty_months_remaining": 1}
  ]
}
```
