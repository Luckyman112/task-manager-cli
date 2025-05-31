from datetime import datetime
from models.task import Task

class DeadlineTask(Task):
    def __init__(self, title: str, due_date: datetime, description: str = "", priority: int = 1):
        super().__init__(title, description, priority)
        self._due_date = due_date

    def get_due_date(self) -> datetime:
        return self._due_date

    def get_info(self) -> str:
        base_info = super().get_info()
        due_str = self._due_date.strftime("%Y-%m-%d %H:%M")
        return f"{base_info}  [Due: {due_str}]"
