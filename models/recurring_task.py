from datetime import datetime, timedelta
from models.task import Task

class RecurringTask(Task):
    def __init__(self, title: str, interval_days: int, next_run: datetime, description: str = "", priority: int = 1):
        super().__init__(title, description, priority)
        self._interval = interval_days
        self._next_run = next_run

    def get_due_date(self) -> datetime:
        return self._next_run

    def mark_completed(self) -> None:
        """Перезапланировать на следующий период."""
        self._next_run = self._next_run + timedelta(days=self._interval)
        self._completed = False

    def get_info(self) -> str:
        base_info = super().get_info()
        next_run_str = self._next_run.strftime("%Y-%m-%d")
        return f"{base_info}  [Every {self._interval}d, Next: {next_run_str}]"
