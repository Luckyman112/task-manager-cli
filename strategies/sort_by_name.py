from typing import List
from datetime import datetime
from models.itask import ITask
from strategies.sort_strategy import ISortStrategy

class SortByName(ISortStrategy):
    def sort(self, tasks: List[ITask]) -> List[ITask]:
        return sorted(tasks, key=lambda t: t.get_title().lower())
