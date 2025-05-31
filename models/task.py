from datetime import datetime
from models.itask import ITask

class Task(ITask):
    _id_counter = 1

    def __init__(self, title: str, description: str = "", priority: int = 1):
        self._id = Task._id_counter
        Task._id_counter += 1

        self._title = title
        self._description = description
        self._priority = priority
        self._completed = False

    def get_id(self) -> int:
        return self._id

    def get_title(self) -> str:
        return self._title

    def is_completed(self) -> bool:
        return self._completed

    def mark_completed(self) -> None:
        self._completed = True

    def get_info(self) -> str:
        status = "✓" if self._completed else "✗"
        return f"[{status}] (#{self._id}) {self._title} (Priority: {self._priority})"

    def get_due_date(self) -> datetime | None:
        # Базовая задача не имеет дедлайна
        return None
