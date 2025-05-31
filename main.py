# main.py
import sys
from datetime import datetime, timedelta
from task_manager import TaskManager
from factories.task_factory import TaskFactory
from strategies.sort_by_name import SortByName
from strategies.sort_by_priority import SortByPriority
from strategies.sort_by_date import SortByDate

def print_menu():
    print()
    print("=== TASK MANAGEMENT SYSTEM ===")
    print("1) Добавить простую задачу")
    print("2) Добавить задачу с дедлайном")
    print("3) Добавить повторяющуюся задачу")
    print("4) Показать все задачи")
    print("5) Отметить задачу как выполненную")
    print("6) Удалить задачу")
    print("7) Изменить стратегию сортировки")
    print("8) Сохранить задачи в файл")
    print("9) Загрузить задачи из файла")
    print("0) Выход")
    print("==============================\n")

def main():
    manager = TaskManager()

    while True:
        manager.check_notifications()
        print_menu()
        choice = input("Выберите пункт: ").strip()

        if choice == "1":
            title = input("Название задачи: ").strip()
            desc = input("Описание (можно пусто): ").strip()
            pr = int(input("Приоритет (1 = самый высокий, больше = ниже): ").strip())
            task = TaskFactory.create_task("simple", title=title, description=desc, priority=pr)
            manager.add_task(task)
            print()
            print("SimpleTask добавлена.\n")

        elif choice == "2":
            title = input("Название задачи: ").strip()
            desc = input("Описание (можно пусто): ").strip()
            pr = int(input("Приоритет (1 = самый высокий): ").strip())
            due_str = input("Дедлайн (YYYY-MM-DD HH:MM): ").strip()
            due_dt = datetime.strptime(due_str, "%Y-%m-%d %H:%M")
            task = TaskFactory.create_task("deadline", title=title, description=desc, priority=pr, due_date=due_dt)
            manager.add_task(task)
            print()
            print("DeadlineTask добавлена.\n")

        elif choice == "3":
            title = input("Название задачи: ").strip()
            desc = input("Описание (можно пусто): ").strip()
            pr = int(input("Приоритет (1 = самый высокий): ").strip())
            interval = int(input("Интервал повтора (дней): ").strip())
            next_run_str = input("Следующая дата запуска (YYYY-MM-DD): ").strip()
            next_run_dt = datetime.strptime(next_run_str, "%Y-%m-%d")
            task = TaskFactory.create_task(
                "recurring",
                title=title, description=desc, priority=pr,
                interval_days=interval, next_run=next_run_dt
            )
            manager.add_task(task)
            print()
            print("RecurringTask добавлена.\n")

        elif choice == "4":
            manager.list_tasks()

        elif choice == "5":
            tid = int(input("ID задачи для отметки выполненной: ").strip())
            ok = manager.mark_task_completed(tid)
            print()
            print("Задача помечена как выполненная." if ok else "Задача не найдена или уже выполнена.", "\n")

        elif choice == "6":
            tid = int(input("ID задачи для удаления: ").strip())
            ok = manager.remove_task(tid)
            print()
            print("Задача удалена." if ok else "Задача не найдена.", "\n")

        elif choice == "7":
            print("1) Сортировать по имени")
            print("2) Сортировать по приоритету")
            print("3) Сортировать по дате дедлайна")
            s_choice = input("Выберите стратегию: ").strip()
            if s_choice == "1":
                manager.set_sort_strategy(SortByName())
            elif s_choice == "2":
                manager.set_sort_strategy(SortByPriority())
            elif s_choice == "3":
                manager.set_sort_strategy(SortByDate())
            else:
                print()
                print("Неверный выбор, оставляем текущее.\n")
            print()
            print("Стратегия изменена.\n")

        elif choice == "8":
            fname = input("Имя файла для сохранения (например, tasks.json): ").strip()
            manager.save_to_file(fname)
            print()
            print(f"Задачи сохранены в {fname}.\n")

        elif choice == "9":
            fname = input("Имя файла для загрузки: ").strip()
            manager.load_from_file(fname)
            print()
            print(f"Задачи загружены из {fname}.\n")

        elif choice == "0":
            print()
            print("Выход из программы. Пока!")
            sys.exit(0)

        else:
            print()
            print("Неверный выбор. Попробуйте снова.\n")

if __name__ == "__main__":
    main()
