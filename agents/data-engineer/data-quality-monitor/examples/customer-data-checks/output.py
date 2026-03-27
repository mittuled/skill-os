"""Data quality checks for the customers table using Great Expectations-style assertions."""

import logging
from dataclasses import dataclass
from datetime import datetime, timedelta

import sqlalchemy as sa

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

DB_URL = "postgresql://readonly:${DB_PASSWORD}@warehouse.internal:5432/analytics"
engine = sa.create_engine(DB_URL)


@dataclass
class CheckResult:
    name: str
    passed: bool
    details: str
    rows_affected: int = 0


def check_not_null(conn: sa.Connection) -> CheckResult:
    """Required fields must not be null."""
    result = conn.execute(sa.text(
        "SELECT count(*) FROM customers "
        "WHERE email IS NULL OR name IS NULL OR created_at IS NULL"
    ))
    count = result.scalar()
    return CheckResult("not_null_required_fields", count == 0, f"{count} rows with nulls", count)


def check_email_format(conn: sa.Connection) -> CheckResult:
    """Emails must match basic format: text@text.text."""
    result = conn.execute(sa.text(
        "SELECT count(*) FROM customers "
        "WHERE email !~ '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$'"
    ))
    count = result.scalar()
    return CheckResult("email_format", count == 0, f"{count} invalid emails", count)


def check_duplicates(conn: sa.Connection) -> CheckResult:
    """No duplicate customers by email."""
    result = conn.execute(sa.text(
        "SELECT count(*) FROM ("
        "  SELECT email FROM customers GROUP BY email HAVING count(*) > 1"
        ") dupes"
    ))
    count = result.scalar()
    return CheckResult("no_duplicate_emails", count == 0, f"{count} duplicate email groups", count)


def check_referential_integrity(conn: sa.Connection) -> CheckResult:
    """All orders must reference a valid customer."""
    result = conn.execute(sa.text(
        "SELECT count(*) FROM orders o "
        "LEFT JOIN customers c ON o.customer_id = c.id "
        "WHERE c.id IS NULL"
    ))
    count = result.scalar()
    return CheckResult("orders_customer_fk", count == 0, f"{count} orphaned orders", count)


def check_freshness(conn: sa.Connection) -> CheckResult:
    """Most recent customer must have been created within the last 24 hours."""
    result = conn.execute(sa.text("SELECT max(created_at) FROM customers"))
    latest = result.scalar()
    threshold = datetime.utcnow() - timedelta(hours=24)
    is_fresh = latest is not None and latest >= threshold
    age = (datetime.utcnow() - latest).total_seconds() / 3600 if latest else float("inf")
    return CheckResult("data_freshness_24h", is_fresh, f"Latest record: {age:.1f}h ago")


def run_all_checks() -> list[CheckResult]:
    checks = [
        check_not_null,
        check_email_format,
        check_duplicates,
        check_referential_integrity,
        check_freshness,
    ]
    results = []
    with engine.connect() as conn:
        for check_fn in checks:
            result = check_fn(conn)
            status = "PASS" if result.passed else "FAIL"
            log.info("[%s] %s — %s", status, result.name, result.details)
            results.append(result)

    failed = [r for r in results if not r.passed]
    if failed:
        log.error("%d/%d checks failed: %s", len(failed), len(results),
                  ", ".join(r.name for r in failed))
    else:
        log.info("All %d checks passed", len(results))
    return results


if __name__ == "__main__":
    run_all_checks()
