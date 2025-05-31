# Task Management System (Python)

## Overview
**Task Management System** is a simple command-line application written in Python that allows users to manage different types of tasks:
- **Simple tasks** (`SimpleTask`)
- **Deadline tasks** (`DeadlineTask`)
- **Recurring tasks** (`RecurringTask`)

It demonstrates core Object-Oriented Programming (OOP) principles (Encapsulation, Inheritance, Polymorphism, Abstraction) and implements several design patterns (Factory Method, Observer, Strategy, and optionally Singleton). Users can create, list, mark complete, delete, sort, save, and load tasks. Deadline tasks trigger notifications when their due time is within one hour (or already passed).

## Features
- **Create tasks** of three types:
  1. Simple task (no due date)
  2. Deadline task (with a due date and time)
  3. Recurring task (executes repeatedly at a specified interval)
- **List all tasks** using different sorting strategies:
  - Sort by name
  - Sort by priority
  - Sort by due date
- **Mark tasks complete** (including automatic rescheduling for recurring tasks)
- **Delete tasks** by ID
- **Save** and **load** all tasks to/from a JSON file
- **Deadline notifications** (Observer pattern): prints a console notification when a deadline is within one hour or already passed
- Follows clean OOP architecture, organized into separate modules/packages

## Installation & Setup

1. **Clone the repository** (or unzip the archive):
   ```bash
   git clone https://github.com/YourUsername/task-manager-cli.git
   cd task-manager-cli
   ```

2. **(Optional) Create and activate a virtual environment**:
   - **Windows (PowerShell or CMD)**:
     ```powershell
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Install dependencies** (if using any external packages). This project uses only the Python standard library. If you add third-party packages, list them in `requirements.txt` and run:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python main.py
   ```
   Or, on some systems:
   ```bash
   python3 main.py
   ```

## How to Use

When you start the application (`python main.py`), you will see a menu in the console:

```
=== TASK MANAGEMENT SYSTEM ===
1) Add a simple task
2) Add a deadline task
3) Add a recurring task
4) List all tasks
5) Mark a task as completed
6) Delete a task
7) Change sorting strategy
8) Save tasks to file
9) Load tasks from file
0) Exit
==============================
```

### 1) Add a Simple Task
- Select option `1`.
- Enter task title (e.g., `Buy groceries`).
- Enter an optional description (or press Enter to skip).
- Enter priority (integer, where `1` = highest priority).
- The console will confirm:
  ```
   SimpleTask added.
  ```
- If any deadline-based notifications are due, they will appear immediately after.

### 2) Add a Deadline Task
- Select option `2`.
- Enter task title (e.g., `Submit report`).
- Enter optional description (or press Enter).
- Enter priority (e.g., `1`).
- Enter due date and time in `YYYY-MM-DD HH:MM` format (e.g., `2025-05-12 18:00`).
- The console will confirm:
  ```
   DeadlineTask added.
  ```
- If the due date is within one hour (or already passed), you will immediately see:
  ```
  [NOTIFICATION] Task 'Submit report' is due by 2025-06-14 18:00!
  ```

### 3) Add a Recurring Task
- Select option `3`.
- Enter task title (e.g., `Daily backup`).
- Enter optional description (or press Enter).
- Enter priority (e.g., `2`).
- Enter repeat interval in days (e.g., `1` for daily).
- Enter the next run date in `YYYY-MM-DD` format (e.g., `2025-05-01`).
- The console will confirm:
  ```
   RecurringTask added.
  ```
- When you mark a recurring task as completed, its next run date is automatically advanced by the interval.

### 4) List All Tasks
- Select option `4`.
- All tasks will be printed, sorted by the currently selected strategy (default: sort by name). Example:
  ```
  ---- All Tasks ----
  [✗] (#2) Submit report (Priority: 1)  [Due: 2025-06-14 18:00]
  [✗] (#1) Buy groceries (Priority: 2)
  [✗] (#3) Daily backup (Priority: 3)  [Every 1d, Next: 2025-06-01]
  -------------------
  ```
  - `[#]` is the Task ID assigned automatically.
  - `✗` means not completed; `✓` indicates a completed task.
  - Deadline and recurring tasks display extra information in brackets.
- If any tasks have a deadline within one hour, a notification will appear immediately before the task list.

### 5) Mark a Task as Completed
- Select option `5`.
- Enter the Task ID you want to mark complete (e.g., `2`).
- If successful, you will see:
  ```
   Task #2 marked as completed.
  ```
- For a `RecurringTask`, marking it completed also pushes its next run date forward by the interval.  
- If the ID is invalid or the task is already completed, you will see:
  ```
   Task #X not found or already completed.
  ```
- Any notifications for that task will no longer appear (since `is_completed()` returns `True`).

### 6) Delete a Task
- Select option `6`.
- Enter the Task ID to delete (e.g., `3`).
- If successful:
  ```
   Task #3 deleted.
  ```
- If not found:
  ```
   Task #3 not found.
  ```

### 7) Change Sorting Strategy
- Select option `7`.
- You will see:
  ```
  1) Sort by name
  2) Sort by priority
  3) Sort by due date
  ```
- Enter `1`, `2`, or `3`. Example: `2`.
- Confirmation will appear:
  ```
   Sorting strategy: by priority.
  ```
- Subsequent “List all tasks” (`4`) will use this new strategy.

### 8) Save Tasks to File
- Select option `8`.
- Enter a file name (e.g., `tasks.json`).
- If successful:
  ```
   Tasks saved to 'tasks.json'.
  ```
- The JSON file will contain a list of serialized tasks, with their IDs, titles, priorities, completion status, and additional fields for deadlines/recurrence.

### 9) Load Tasks from File
- Select option `9`.
- Enter the file name to load (e.g., `tasks.json`).
- If successful:
  ```
   Tasks loaded from 'tasks.json'.
  ```
- Existing in-memory tasks will be replaced by the loaded ones.  
- If any loaded deadline is within one hour (or already passed), a notification will appear immediately after loading.

### 0) Exit
- Select option `0` to exit the application:
  ```
  Exiting. Goodbye!
  ```

## Object-Oriented Design

1. **Encapsulation**  
   - All task-related data (`_title`, `_priority`, `_due_date`, `_completed`) is marked private or “protected” (leading underscore).  
   - Access is provided only public methods (`get_info()`, `mark_completed()`, `get_due_date()`, etc.).  

2. **Inheritance & Abstraction**  
   - `ITask` (abstract base class) defines the contract for all tasks.  
   - `Task` (could be an abstract or partially concrete class) implements common logic and fields.  
   - `SimpleTask`, `DeadlineTask`, and `RecurringTask` inherit from `Task` and override/extend behavior.  

3. **Polymorphism**  
   - `TaskManager` stores a list of `ITask` references. When calling `t.get_info()` or `t.mark_completed()`, the correct overridden method executes, depending on the actual subclass.  
   - Sorting strategies implement `ISortStrategy`; at runtime, `TaskManager` calls `current_strategy.sort(self._tasks)` without knowing the concrete class.

4. **Design Patterns**  
   - **Factory Method (`TaskFactory`)**:  
     - Centralizes creation of task objects. Based on a string key (`"simple"`, `"deadline"`, `"recurring"`), it returns an instance of the appropriate subclass.  
     - Client code (in `main.py` / `TaskManager`) does not need to import or instantiate specific task subclasses directly.  
   - **Observer (`NotificationPublisher` / `INotificationSubscriber`)**:  
     - `NotificationPublisher` maintains a list of subscribers.  
     - Whenever `check_tasks()` detects a deadline within one hour, it calls `notify_all()`, which iterates through subscribers (e.g., `ConsoleSubscriber`) and invokes `update()`.  
     - Easily extensible: add an `EmailSubscriber` or `SMSSubscriber` without modifying the publisher.  
   - **Strategy (`ISortStrategy` + concrete `SortByName`, `SortByPriority`, `SortByDate`)**:  
     - Sorting logic is decoupled from `TaskManager`. To change sorting behavior, simply swap the `ISortStrategy` instance.  
   - **Singleton (optional, `Logger`)**:  
     - Ensures a single global instance of `Logger` for consistent logging throughout the application.  

## File Storage (Persistence)
- Implemented by `storage/file_storage.py` (class `FileStorageManager`).
- **Saving**:  
  - Iterates over a list of `ITask` instances.  
  - For each task, writes a JSON object containing `id`, `title`, `is_completed`, `priority`, `type`, and, if applicable, `due_date` or `interval_days` + `next_run`.  
- **Loading**:  
  - Reads JSON from file.  
  - For each JSON object, reconstructs the correct task subclass based on the `"type"` field.  
  - If a task was marked completed in the file, calls `mark_completed()` in memory.  
  - Returns a list of `ITask` objects to replace the in-memory task list.
