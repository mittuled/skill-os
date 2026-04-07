# Scenario: CSV-to-Warehouse ETL Pipeline

Build a Python ETL pipeline that:

1. Reads CSV files from an S3 bucket
2. Validates and cleans the data (null checks, type casting, deduplication)
3. Transforms columns (date parsing, enum mapping)
4. Loads into a PostgreSQL data warehouse
5. Logs row counts at each stage
