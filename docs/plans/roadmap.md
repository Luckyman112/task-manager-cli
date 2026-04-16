# Project Roadmap

## Phase 1: Core Architecture & MVP (Current State)
- [x] Define abstract base classes (`ITask`, `Task`) and concrete implementations (`SimpleTask`, `DeadlineTask`, `RecurringTask`).
- [x] Implement Factory Method for dynamic task instantiation.
- [x] Implement Strategy Pattern for task sorting (Name, Priority, Due Date).
- [x] Implement Observer Pattern for deadline notifications.
- [x] JSON file persistence (Save/Load).
- [x] Interactive CLI Menu.

## Phase 2: Polish & AI-Harness Preparation
- [x] Define `AGENTS.md` to establish strict coding boundaries for LLMs.
- [ ] Refactor complex calculations (e.g., date math) into strict Pure Functions.
- [ ] Add comprehensive `unittest` coverage for all core logic.

## Phase 3: Future Releases (Post-MVP)
- [ ] **AI Task Prioritization:** Use local AI/LLM API to suggest which task to do next based on text analysis of the description.
- [ ] **Sub-tasks:** Allow tasks to have a nested list of smaller sub-tasks.
- [ ] **Export to CSV/Markdown:** Generate reports of completed tasks for external use.
