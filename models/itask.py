from abc import ABC, abstractmethod
from datetime import datetime

class ITask(ABC):
    @abstractmethod
    def get_id(self) -> int:
        """Возвращает уникальный идентификатор задачи."""
        pass

    @abstractmethod
    def get_title(self) -> str:
        """Возвращает заголовок задачи."""
        pass

    @abstractmethod
    def is_completed(self) -> bool:
        """Проверяет, завершена ли задача."""
        pass

    @abstractmethod
    def mark_completed(self) -> None:
        """Помечает задачу как выполненную."""
        pass

    @abstractmethod
    def get_info(self) -> str:
        """Возвращает строку с подробной информацией о задаче."""
        pass

    @abstractmethod
    def get_due_date(self) -> datetime | None:
        """Возвращает дату дедлайна или None, если задачи нет."""
        pass
