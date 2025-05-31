# storage/file_storage.py
import json
from typing import List
from models.itask import ITask
from models.simple_task import SimpleTask
from models.deadline_task import DeadlineTask
from models.recurring_task import RecurringTask
from datetime import datetime

class FileStorageManager:
    def save(self, filename: str, tasks: List[ITask]) -> None:
        data = []
        for t in tasks:
            ttype = t.__class__.__name__
            base = {
                "id": t.get_id(),
                "title": t.get_title(),
                "is_completed": t.is_completed(),
                "priority": getattr(t, "_priority", 1),
                "type": ttype
            }
            if ttype == "SimpleTask":
                data.append(base)
            elif ttype == "DeadlineTask":
                base["due_date"] = t.get_due_date().strftime("%Y-%m-%d %H:%M")
                data.append(base)
            elif ttype == "RecurringTask":
                rd = t.get_due_date()
                base["interval_days"] = getattr(t, "_interval", 1)
                base["next_run"] = rd.strftime("%Y-%m-%d")
                data.append(base)
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load(self, filename: str) -> List[ITask]:
        tasks = []
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        for item in data:
            ttype = item.get("type")
            if ttype == "SimpleTask":
                t = SimpleTask(item["title"], "", item["priority"])
                if item["is_completed"]:
                    t.mark_completed()
                tasks.append(t)
            elif ttype == "DeadlineTask":
                due = datetime.strptime(item["due_date"], "%Y-%m-%d %H:%M")
                t = DeadlineTask(item["title"], due, "", item["priority"])
                if item["is_completed"]:
                    t.mark_completed()
                tasks.append(t)
            elif ttype == "RecurringTask":
                next_run = datetime.strptime(item["next_run"], "%Y-%m-%d")
                t = RecurringTask(item["title"], item["interval_days"], next_run, "", item["priority"])
                if item["is_completed"]:
                    t.mark_completed()
                tasks.append(t)
        return tasks
