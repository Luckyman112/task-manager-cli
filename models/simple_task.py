from models.task import Task

class SimpleTask(Task):
    def __init__(self, title: str, description: str = "", priority: int = 1):
        super().__init__(title, description, priority)
