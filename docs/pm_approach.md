# Project Management Approach

## Framework: Hybrid Kanban (Human + AI)
We utilize a lean, continuous-flow Kanban system adapted for an AI-Native workflow. Tasks are pulled from the backlog, passed to the AI for generation within strict boundaries, and then reviewed by the Human Engineer before being merged into the `main` branch.

## Responsibility Matrix
| Task Category | Primary Owner | Description / Rules |
| :--- | :--- | :--- |
| **Architecture & OOP Design** | Human | Defines interfaces, abstract classes, and overall design patterns (e.g., Observer for notifications). |
| **Business Logic Implementation** | AI Agent | Writes concrete implementations of interfaces and pure functions for data transformation. |
| **Unit Testing** | AI Agent | Generates edge-case tests and standard library `unittest` coverage. |
| **Code Review & Merge** | Human | Verifies that AI did not hallucinate dependencies or break encapsulation. |
| **Refactoring** | Hybrid | AI identifies code smells; Human approves the refactoring strategy. |
