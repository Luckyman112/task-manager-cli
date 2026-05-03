# UI Design Specification (SDD)

## 1. Concept & Vibe
A clean, developer-friendly Task Management Dashboard.

## 2. Layout Structure
- **Sidebar**: Form to add new tasks (Title, Type, Priority).
- **Main Content**: Metric cards (Total, Completed, Pending) and Task List.

## 3. Technical Constraints
- Framework: `streamlit`.
- The UI MUST import and use `TaskManager` directly. No mocked logic.
- Strategy pattern must be switchable via UI radio buttons.