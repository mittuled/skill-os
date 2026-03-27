"""ETL pipeline: S3 CSV -> PostgreSQL warehouse."""

import logging
from datetime import datetime
import boto3
import pandas as pd
from sqlalchemy import create_engine

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

S3_BUCKET = "data-lake-raw"
S3_PREFIX = "orders/"
DB_URL = "postgresql://etl_user:${DB_PASSWORD}@warehouse.internal:5432/analytics"

STATUS_MAP = {"P": "pending", "S": "shipped", "D": "delivered", "C": "cancelled"}


def extract(bucket: str, prefix: str) -> pd.DataFrame:
    """Read all CSV files under an S3 prefix into a single DataFrame."""
    s3 = boto3.client("s3")
    objects = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)
    frames = []
    for obj in objects.get("Contents", []):
        if obj["Key"].endswith(".csv"):
            path = f"s3://{bucket}/{obj['Key']}"
            frames.append(pd.read_csv(path))
            log.info("Read %s (%d bytes)", obj["Key"], obj["Size"])
    df = pd.concat(frames, ignore_index=True)
    log.info("Extract complete: %d rows", len(df))
    return df


def validate(df: pd.DataFrame) -> pd.DataFrame:
    """Drop invalid rows and deduplicate."""
    initial = len(df)
    # Drop rows missing required fields
    df = df.dropna(subset=["order_id", "customer_id", "amount"])
    # Remove duplicates by order_id
    df = df.drop_duplicates(subset=["order_id"], keep="last")
    # Enforce positive amounts
    df = df[df["amount"] > 0]
    log.info("Validation: %d -> %d rows (%d removed)", initial, len(df), initial - len(df))
    return df


def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Parse dates, map enums, cast types."""
    df["order_date"] = pd.to_datetime(df["order_date"], format="%Y-%m-%d", errors="coerce")
    df["status"] = df["status_code"].map(STATUS_MAP).fillna("unknown")
    df["amount"] = df["amount"].round(2)
    df["loaded_at"] = datetime.utcnow()
    df = df.drop(columns=["status_code"])
    log.info("Transform complete: %d rows, columns: %s", len(df), list(df.columns))
    return df


def load(df: pd.DataFrame, table: str = "fact_orders") -> None:
    """Write DataFrame to PostgreSQL, appending to existing table."""
    engine = create_engine(DB_URL)
    df.to_sql(table, engine, if_exists="append", index=False, method="multi", chunksize=1000)
    log.info("Loaded %d rows into %s", len(df), table)


def run() -> None:
    """Execute the full ETL pipeline."""
    log.info("Pipeline started")
    raw = extract(S3_BUCKET, S3_PREFIX)
    clean = validate(raw)
    transformed = transform(clean)
    load(transformed)
    log.info("Pipeline finished: %d rows loaded", len(transformed))


if __name__ == "__main__":
    run()
