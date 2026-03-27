# Scenario: Database Failover Runbook

Draft a runbook for failing over a PostgreSQL RDS primary to its read replica when:

1. The primary becomes unresponsive
2. Replication lag has been confirmed as minimal
3. Application connections need to be redirected
4. Data integrity must be verified post-failover
