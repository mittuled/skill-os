# Runbook: PostgreSQL RDS Failover

**Severity:** P1 — Data layer outage
**Estimated time:** 10-15 minutes
**Last tested:** Quarterly game day

## Prerequisites

- AWS CLI configured with `rds:PromoteReadReplica` permissions
- Access to the application's database connection config (SSM Parameter Store)
- PagerDuty incident already open

## Step 1: Confirm Primary is Unresponsive

```bash
# Check RDS instance status
aws rds describe-db-instances \
  --db-instance-identifier prod-primary \
  --query 'DBInstances[0].DBInstanceStatus'

# Attempt direct connection (timeout after 5s)
psql "host=prod-primary.xxxxx.us-east-1.rds.amazonaws.com \
  dbname=app connect_timeout=5" -c "SELECT 1;"
```

**Expected:** Connection timeout or `storage-full` / `incompatible-parameters` status.

## Step 2: Verify Replica Health and Lag

```bash
aws rds describe-db-instances \
  --db-instance-identifier prod-replica \
  --query 'DBInstances[0].[DBInstanceStatus, StatusInfos]'

aws cloudwatch get-metric-statistics \
  --namespace AWS/RDS --metric-name ReplicaLag \
  --dimensions Name=DBInstanceIdentifier,Value=prod-replica \
  --start-time "$(date -u -v-10M +%Y-%m-%dT%H:%M:%S)" \
  --end-time "$(date -u +%Y-%m-%dT%H:%M:%S)" \
  --period 60 --statistics Average
```

**Go/No-Go:** Proceed only if ReplicaLag < 5 seconds.

## Step 3: Promote Replica

```bash
aws rds promote-read-replica \
  --db-instance-identifier prod-replica \
  --backup-retention-period 7

# Wait for promotion (typically 5-8 minutes)
aws rds wait db-instance-available \
  --db-instance-identifier prod-replica
```

## Step 4: Redirect Application Connections

```bash
# Update the connection string in Parameter Store
aws ssm put-parameter \
  --name "/app/production/DATABASE_HOST" \
  --value "prod-replica.xxxxx.us-east-1.rds.amazonaws.com" \
  --type SecureString --overwrite

# Rolling restart of application pods to pick up new config
kubectl rollout restart deployment/api -n production
kubectl rollout status deployment/api -n production --timeout=120s
```

## Step 5: Verify Data Integrity

```bash
psql "host=prod-replica.xxxxx.us-east-1.rds.amazonaws.com dbname=app" <<SQL
  SELECT count(*) FROM orders WHERE created_at > now() - interval '1 hour';
  SELECT max(id) FROM orders;
  SELECT pg_postmaster_start_time();
SQL
```

Compare row counts with the last known good checkpoint from monitoring.

## Step 6: Post-Failover Cleanup

1. Create a new read replica from the promoted instance
2. Update CloudWatch alarms to point to the new primary
3. Update the runbook with the new instance identifiers
4. File an incident postmortem within 48 hours
