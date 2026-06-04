# Final Report: Software Engineering - I (Part-time, 2026)
**Project Title:** AI-Native Task Management System (CLI & Streamlit Web Dashboard)  
**Student:** Sergejs Kravecs (st85052)  
**Repository:** https://github.com/Luckyman112/task-manager-cli  
**Production Web App URL:** https://task-manager-cli-njzehatesjviqqmc4bguwz.streamlit.app/  

---

## 1. Product Concept & Problem Statement

### Project Pitch
This project delivers a pattern-driven, AI-Native task management ecosystem engineered to handle simple, deadline-oriented, and recurring tasks seamlessly. It provides a dual-interface experience: a lightweight, keyboard-centric Command Line Interface (CLI) for fast terminal workflows and an interactive, stateful Streamlit Web Dashboard for visual tracking and real-time management.

### Problem & Target Audience
Software engineers, system administrators, and power users often find heavy, commercial GUI task managers distracting and detached from their terminal-driven environment. This system bridges that gap. It operates purely on a lightweight core with zero unnecessary overhead, offering terminal speed combined with rich background business logic—such as real-time deadline warnings and automatic recurring interval calculations.

---

## 2. AI-Native Project Management Approach

The development process deviated from traditional workflows by adopting a **Hybrid Kanban (Human + AI)** framework. This methodology focuses on a continuous flow of tasks pulled from a backlog, processed within strict AI guardrails, and thoroughly reviewed by the Human Engineer before being integrated into production.

### Responsibility Matrix
To maximize LLM efficiency and completely prevent architectural drift or code hallucinations, responsibilities were divided using a strict operational matrix:

| Task Category | Primary Owner | Description / Rules |
| :--- | :--- | :--- |
| **Architecture & OOP Design** | Human | Defines interfaces, abstract base classes, and overall GoF design patterns (e.g., Observer, Strategy). |
| **Business Logic Implementation** | AI Agent | Writes concrete implementations of interfaces and pure functions for data transformations. |
| **Unit Testing** | AI Agent | Generates edge-case tests and standard library `unittest` coverage suites. |
| **Code Review & Merge** | Human | Verifies that the AI did not hallucinate dependencies or break object encapsulation. |
| **Refactoring** | Hybrid | AI identifies code smells; Human evaluates and approves the final refactoring strategy. |

The structural organization of these project management assets, architectural configurations, and requirements specifications is maintained directly within the project's repository under the `/docs` directory.

---

## 3. Requirements & Specification (BDD Approach)

To ensure the AI Agent generated deterministic, production-grade business logic, all system features were specified using **Behavior-Driven Development (BDD)** paradigms with *Given / When / Then* scenarios.

### Feature Focus: Recurring Task Next Date Calculation
The core date shift logic for recurring tasks was isolated and defined via explicit user stories and acceptance criteria:

*   **User Story:** As a user with recurring tasks, I want the system to calculate the exact next run date based on my interval, so that my schedule remains accurate when I complete a task.
*   **Scenario 1: Calculate standard recurrence**
    *   *Given* a current run date of `"2026-04-17"` and an interval of `1` day.
    *   *When* the calculation function is called.
    *   *Then* the result should be a new datetime object representing `"2026-04-18"`.
*   **Scenario 2: Handle invalid negative intervals**
    *   *Given* an interval of `-2` days.
    *   *When* the calculation function is called.
    *   *Then* the system should raise a `ValueError`.

### Logic Flow Diagram
The BDD acceptance criteria were translated into an explicit control-flow graph via a Mermaid block. This flowchart acted as an unambiguous layout for the AI to convert into a pure function:

```mermaid
graph TD
A[Start: current_date, interval_days] --> B{Is interval_days > 0?}
B -- No --> C[Raise ValueError: Interval must be strictly positive]
B -- Yes --> D[Calculate: current_date + timedelta days=interval_days]
D --> E[Return new_date object]
