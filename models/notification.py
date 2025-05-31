from abc import ABC, abstractmethod
from typing import List
from datetime import datetime, timedelta
from models.itask import ITask

class INotificationSubscriber(ABC):
    @abstractmethod
    def update(self, task: ITask, message: str) -> None:
        pass

class NotificationPublisher:
    def __init__(self):
        self._subscribers: List[INotificationSubscriber] = []

    def subscribe(self, subscriber: INotificationSubscriber) -> None:
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber: INotificationSubscriber) -> None:
        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)

    def notify_all(self, task: ITask, message: str) -> None:
        for sub in self._subscribers:
            sub.update(task, message)

    def check_tasks(self, tasks: List[ITask]) -> None:
        now = datetime.now()
        for t in tasks:
            due = t.get_due_date()
            if due is not None:
                if now + timedelta(hours=1) >= due and not t.is_completed():
                    print()
                    msg = f"Задача '{t.get_title()}' должна быть выполнена до {due.strftime('%Y-%m-%d %H:%M')}!"
                    self.notify_all(t, msg)
