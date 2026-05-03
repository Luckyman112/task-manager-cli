from typing import List
from models.itask import ITask
from strategies.isort_strategy import ISortStrategy 

class SortByDateStrategy(ISortStrategy):
    def sort(self, tasks: List[ITask]) -> List[ITask]:
        return sorted(tasks, key=lambda task: task.due_date if task.due_date else "9999-12-31")

class SortByPriorityStrategy(ISortStrategy):
    def sort(self, tasks: List[ITask]) -> List[ITask]:
        priority_map = {'High': 1, 'Medium': 2, 'Low': 3}
        return sorted(tasks, key=lambda task: priority_map.get(getattr(task, 'priority', 'Low'), 4))

class TaskSorter:
    def __init__(self, strategy: ISortStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: ISortStrategy):
        self._strategy = strategy

    def execute_sort(self, tasks: List[ITask]) -> List[ITask]:
        return self._strategy.sort(tasks)
