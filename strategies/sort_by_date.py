from typing import List
from datetime import datetime
from models.itask import ITask
from strategies.sort_strategy import ISortStrategy

class SortByDate(ISortStrategy):
    def sort(self, tasks: List[ITask]) -> List[ITask]:
        def date_key(t):
            d = t.get_due_date()
            return d if d is not None else datetime.max
        return sorted(tasks, key=date_key)
