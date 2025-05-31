from typing import List
from models.itask import ITask
from strategies.sort_strategy import ISortStrategy

class SortByPriority(ISortStrategy):
    def sort(self, tasks: List[ITask]) -> List[ITask]:
        return sorted(tasks, key=lambda t: getattr(t, "_priority", 0))
