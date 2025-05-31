from datetime import datetime
from typing import Union
from models.simple_task import SimpleTask
from models.deadline_task import DeadlineTask
from models.recurring_task import RecurringTask

class TaskFactory:
    @staticmethod
    def create_task(task_type: str, **kwargs) -> Union[SimpleTask, DeadlineTask, RecurringTask]:
        ttype = task_type.lower()
        if ttype == "simple":
            return SimpleTask(kwargs["title"], kwargs.get("description", ""), kwargs.get("priority", 1))
        elif ttype == "deadline":
            return DeadlineTask(kwargs["title"], kwargs["due_date"], kwargs.get("description", ""), kwargs.get("priority", 1))
        elif ttype == "recurring":
            return RecurringTask(kwargs["title"], kwargs["interval_days"], kwargs["next_run"], kwargs.get("description", ""), kwargs.get("priority", 1))
        else:
            raise ValueError(f"Unknown task type: {task_type}")
