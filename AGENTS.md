# AI Agent Instructions & Harness

## Project Concept
- **Goal:** A lightweight, pure-Python command-line application for managing Simple, Deadline, and Recurring tasks.
- **Tech Stack:** Python 3 (Standard Library only, no external dependencies).
- **Architecture:** Strict Object-Oriented Programming (OOP) utilizing Design Patterns (Factory, Observer, Strategy, Singleton).

## Engineering Rules
- **Language:** English for all code, variable names, and documentation.
- **Coding Style:** Follow PEP 8 strictly. Use type hinting (`-> int`, `: str`) for all new methods.
- **Encapsulation:** Do not break encapsulation. Use getters/setters or properties. Keep private variables prefixed with an underscore (e.g., `_title`).
- **Persistence:** All data is serialized/deserialized via `storage/file_storage.py` into JSON. Do not invent new database connections.

## STRICT CONTEXT PROTOCOL
You must **ALWAYS** refer to the `/docs` folder for detailed context, project management approaches, and architectural decisions before proposing any structural changes or writing new features. Do not guess the architecture.
