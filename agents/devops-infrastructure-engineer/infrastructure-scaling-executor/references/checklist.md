# Checklist: infrastructure-scaling-executor

Step-by-step verification checklist for executing infrastructure scaling operations safely.

## Phase 1: Pre-Scaling Assessment

- [ ] Identify the scaling trigger: alert, load test result, or growth projection
- [ ] Collect current resource utilization baselines: CPU %, memory %, disk I/O, network throughput
- [ ] Review DORA metrics (deployment frequency, lead time, MTTR) for context on system health
- [ ] Determine bottleneck tier: web, app, database, cache, or message queue
- [ ] Classify scaling type: horizontal (more instances), vertical (larger instances), or architectural
- [ ] Calculate target capacity: peak load × 1.3 safety factor minimum
- [ ] Check cloud provider quotas for the target instance types and regions
- [ ] Estimate cost impact: current monthly spend vs. post-scaling estimate

**Exit criteria**: Scaling approach documented, bottleneck tier confirmed, cost estimate approved.

## Phase 2: Change Planning

- [ ] Define specific changes: instance counts, instance types, auto-scaling min/max bounds
- [ ] For Kubernetes: update HPA target CPU/memory thresholds and replica counts
- [ ] For VMs/ASGs: update launch template, min/max/desired instance counts
- [ ] For databases: specify read replica count, instance class upgrade, or connection pooler tuning
- [ ] For caches: specify cluster size, node type, or eviction policy changes
- [ ] Define auto-scaling policies with scale-out and scale-in cooldown periods
- [ ] Select execution window: low-traffic period (typically off-peak hours)
- [ ] Prepare rollback procedure: instance count revert or previous instance type restoration

**Exit criteria**: Change plan reviewed by a second engineer, rollback procedure documented.

## Phase 3: Execution [GATE — requires approval before proceeding]

- [ ] Confirm infrastructure-as-code is updated (Terraform, Pulumi, or CloudFormation)
- [ ] Run `terraform plan` or equivalent and review the diff — no unintended changes
- [ ] Apply changes via IaC tool, not manual console clicks
- [ ] Monitor deployment log for errors during application
- [ ] Verify new instances pass health checks before receiving traffic
- [ ] Confirm auto-scaling policies are active and correctly configured
- [ ] Record deployment timestamp, change description, and operator in the deployment log

**Exit criteria**: IaC applied without errors, all new resources healthy.

## Phase 4: Validation

- [ ] Monitor p50/p95/p99 latency for 15 minutes post-scaling
- [ ] Verify error rate has not increased from pre-scaling baseline
- [ ] Confirm resource utilization has decreased to target range (target: CPU < 60%)
- [ ] Run targeted load test if the scaling was triggered by load test results
- [ ] Check auto-scaling activity: confirm scale-out events fire at expected thresholds
- [ ] Verify cost monitoring reflects the new infrastructure cost
- [ ] Confirm no related services degraded due to the scaling changes

**Exit criteria**: All metrics within SLO targets for 15 minutes sustained observation.

## Phase 5: Documentation Update

- [ ] Update IaC state in source control (committed and merged)
- [ ] Update capacity plan with new baseline figures
- [ ] Adjust alert thresholds to reflect new resource capacity (e.g., CPU alert at 70% of new capacity)
- [ ] Update runbook with the new instance configuration
- [ ] Record findings in the post-change summary (trigger, action taken, outcome, cost delta)
- [ ] Notify the engineering team of the completed scaling change

**Exit criteria**: Documentation updated and communicated to the engineering team.
