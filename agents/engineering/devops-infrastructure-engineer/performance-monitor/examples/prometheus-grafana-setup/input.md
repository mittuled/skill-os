# Scenario: Prometheus + Grafana Monitoring Stack

Create a Docker Compose configuration that:

1. Runs Prometheus with scrape configs for a web app on port 8080
2. Runs Grafana with a pre-provisioned Prometheus data source
3. Configures retention and storage limits
4. Includes a recording rule for request rate
