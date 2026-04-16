# Logic Flow: Recurring Date Calculator

```mermaid
graph TD
    A[Start: current_date, interval_days] --> B{Is interval_days > 0?}
    B -- No --> C[Raise ValueError: Interval must be strictly positive]
    B -- Yes --> D[Calculate: current_date + timedelta days=interval_days]
    D --> E[Return new_date object]

    ---
