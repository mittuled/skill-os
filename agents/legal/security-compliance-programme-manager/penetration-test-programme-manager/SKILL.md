---
name: penetration-test-programme-manager
description: >
  This skill manages the annual penetration testing programme including scope
  definition, vendor selection, and remediation tracking. Use when asked to plan
  a penetration test, scope a pentest engagement, or track remediation of pentest
  findings. Also consider when SOC 2 or customer contracts require annual testing.
  Suggest when the user has not conducted a penetration test in over 12 months.
department: legal
agent: security-compliance-programme-manager
version: 1.0.0
complexity: medium
related-skills:
  - ../soc2-programme-manager/SKILL.md
  - ../../../legal/product-counsel/security-auditor-legal/SKILL.md
---

# penetration-test-programme-manager

## Agent: Security & Compliance Programme Manager

L2 security and compliance programme manager (1x) responsible for SOC 2, security awareness training, disaster recovery, GDPR/CCPA compliance, and penetration test programme management.

Department ethos: [ideal-legal.md](../../../../departments/legal/ideal-legal.md)

## Skill Description

Manages the annual penetration testing programme including engagement scoping, vendor coordination, rules of engagement, findings triage, remediation tracking, and compliance evidence generation.

## When to Use

- When the annual penetration testing cycle is due for planning and execution as required by SOC 2, customer contracts, or internal security policy.
- When a significant product launch, infrastructure change, or acquisition introduces new attack surface that warrants targeted penetration testing.
- When enterprise customers or prospects require evidence of recent penetration testing as a condition of procurement or contract renewal.

## Workflow

1. **Scope Definition**: Define the penetration test scope including target systems (web applications, APIs, infrastructure, mobile apps, cloud configuration), testing methodology (black-box, grey-box, white-box), excluded systems, and testing window. Coordinate with engineering to identify any systems that require special handling. Deliverable: penetration test scope document with target inventory and testing constraints.
2. **Vendor Engagement**: Select or re-engage the penetration testing firm. Review qualifications (CREST, OSCP, relevant industry experience), negotiate the statement of work, and execute the engagement agreement including liability limitations, data handling provisions, and NDA requirements. Deliverable: executed pentest engagement agreement with SOW.
3. **Rules of Engagement**: Establish rules of engagement including authorized testing techniques, escalation procedures for critical findings discovered during testing, communication channels, emergency stop procedures, and data handling requirements for any sensitive data encountered. Deliverable: signed rules of engagement document.
4. **Testing Coordination**: Coordinate the testing execution window with engineering and operations. Provide necessary access credentials (for grey-box/white-box), API documentation, and environment details. Monitor testing progress and respond to tester questions. Deliverable: testing coordination log with access provisions and progress updates.
5. **Findings Triage and Remediation**: Receive the penetration test report, triage findings by severity (critical, high, medium, low, informational), validate findings with engineering, and create remediation tickets. Track remediation to completion with defined SLAs (critical: 7 days, high: 30 days, medium: 90 days). Deliverable: remediation tracker with finding-to-ticket mapping, SLA targets, and completion status.
6. **Compliance Evidence**: Package the test report, remediation evidence, and management response for SOC 2 auditors, customer security questionnaires, and internal compliance records. Deliverable: pentest compliance package ready for auditor or customer review.

## Anti-Patterns

- **Scope-limiting to pass**: Deliberately narrowing the test scope to exclude known weak areas and produce a "clean" report. *Why*: the purpose of a penetration test is to find vulnerabilities before attackers do; a scoped-to-pass test provides false assurance and wastes the investment.
- **Findings without remediation tracking**: Receiving the pentest report and filing it without creating remediation tickets or tracking fixes. *Why*: untracked findings remain unresolved; the next pentest will find the same issues, and auditors will flag the lack of remediation as a control failure.
- **Annual-only testing**: Conducting penetration testing only on the annual compliance cycle without testing after significant changes. *Why*: major releases, infrastructure migrations, and acquisitions introduce new attack surface; annual-only testing leaves gaps between the test and the change.

## Output

**On success**: Produces the penetration test compliance package containing the scope document, executed engagement agreement, rules of engagement, test report, remediation tracker with completion status, and compliance evidence package. Delivered to the security team, compliance records, and available for customer/auditor requests.

**On failure**: Report which testing could not be completed (e.g., environment unavailable, vendor scheduling conflict, scope dispute), what partial testing was conducted, and the rescheduled timeline.

## Related Skills

- [`soc2-programme-manager`](../soc2-programme-manager/SKILL.md) -- SOC 2 audits require evidence of regular penetration testing; this skill produces that evidence.
- [`security-auditor-legal`](../../../legal/product-counsel/security-auditor-legal/SKILL.md) -- Legal review of pentest findings determines whether disclosure obligations are triggered.
