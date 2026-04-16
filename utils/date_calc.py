from datetime import datetime, timedelta

def calculate_next_run_date(current_date: datetime, interval_days: int) -> datetime:
    """
    Pure function to calculate the next run date.
    No side effects, stateless, deterministic.
    """
    if interval_days <= 0:
        raise ValueError("Interval must be strictly positive")
    return current_date + timedelta(days=interval_days)
