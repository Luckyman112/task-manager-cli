from typing import List
from models.itask import ITask
from factories.task_factory import TaskFactory
from models.notification import NotificationPublisher
from models.console_subscriber import ConsoleSubscriber
from strategies.isort_strategy import ISortStrategy
from strategies.sort_by_name import SortByName

class TaskManager:
    def __init__(self):
        self._tasks: List[ITask] = []
        
        self._publisher = NotificationPublisher()
        self._console_sub = ConsoleSubscriber()
        self._publisher.subscribe(self._console_sub)

        self._sort_strategy: ISortStrategy = SortByName()

    def set_sort_strategy(self, strategy: ISortStrategy) -> None:
        self._sort_strategy = strategy

    def add_task(self, task: ITask) -> None:
        self._tasks.append(task)

    def remove_task(self, task_id: int) -> bool:
        for t in self._tasks:
            if t.get_id() == task_id:
                self._tasks.remove(t)
                return True
        return False

    def mark_task_completed(self, task_id: int) -> bool:
        for t in self._tasks:
            if t.get_id() == task_id and not t.is_completed():
                t.mark_completed()
                return True
        return False

    def get_all_tasks(self) -> List[ITask]:
        return self._sort_strategy.sort(self._tasks)

    def list_tasks(self) -> None:
        sorted_list = self.get_all_tasks()
        print("\n---- All Tasks ----")
        for t in sorted_list:
            print(t.get_info())
        print("-------------------\n")

    def check_notifications(self) -> None:
        self._publisher.check_tasks(self._tasks)

    def save_to_file(self, filename: str) -> None:
        from storage.file_storage import FileStorageManager
        fsm = FileStorageManager()
        fsm.save(filename, self._tasks)

    def load_from_file(self, filename: str) -> None:
        from storage.file_storage import FileStorageManager
        fsm = FileStorageManager()
        self._tasks = fsm.load(filename)
