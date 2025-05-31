from models.notification import INotificationSubscriber
from models.itask import ITask

class ConsoleSubscriber(INotificationSubscriber):
    def update(self, task: ITask, message: str) -> None:
        print(f"[NOTIFICATION] {message}")
