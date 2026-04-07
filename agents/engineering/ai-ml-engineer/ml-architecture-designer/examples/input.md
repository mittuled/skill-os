# Scenario: Designing ML Architecture for Real-Time Fraud Detection

A fintech startup needs to detect fraudulent transactions in real time. The system must score each transaction within 50ms. Feature sources include transaction data, user history, device fingerprints, and merchant metadata. The team has decided the serving pattern is real-time.

## Input Parameters

```json
{
  "system_name": "Real-Time Fraud Detection System",
  "task_type": "classification",
  "serving_pattern": "real_time",
  "feature_sources": ["transaction_stream", "user_history_db", "device_fingerprint_service", "merchant_metadata_db"],
  "feature_complexity": "streaming",
  "training_compute": "GPU cluster (A100s, spot instances)"
}
```
