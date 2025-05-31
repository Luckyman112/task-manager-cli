import threading

class Logger:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(Logger, cls).__new__(cls)
            return cls._instance

    def log(self, message: str) -> None:
        print(f"[LOG] {message}")
