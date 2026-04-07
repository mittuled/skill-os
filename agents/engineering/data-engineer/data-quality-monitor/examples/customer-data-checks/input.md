# Scenario: Customer Data Quality Checks

Create data quality checks for a `customers` table that:

1. Verify no null values in required fields (email, name, created_at)
2. Validate email format
3. Check for duplicate customer records
4. Ensure referential integrity with the `orders` table
5. Alert when data freshness exceeds 24 hours
