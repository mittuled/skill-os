# Scenario: Web Application Alerting Rules

Configure Prometheus alerting rules for a web application that:

1. Alerts when error rate exceeds 5% of total requests
2. Alerts when p99 latency exceeds 2 seconds
3. Alerts when any instance has been down for more than 1 minute
4. Alerts when disk usage exceeds 85%
5. Groups alerts by severity (critical vs warning)
