from abc import ABC, abstractmethod
from typing import List
from models.itask import ITask

class ISortStrategy(ABC):
    @abstractmethod
    def sort(self, tasks: List[ITask]) -> List[ITask]:
        pass
