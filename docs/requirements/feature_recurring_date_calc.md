# Feature: Recurring Task Next Date Calculation

## User Story
**As a** user with recurring tasks,
**I want** the system to calculate the exact next run date based on my interval,
**So that** my schedule remains accurate when I complete a task.

## Acceptance Criteria (BDD)
### Scenario 1: Calculate standard recurrence
- **Given** a current run date of "2026-04-17" and an interval of 1 day
- **When** the calculation function is called
- **Then** the result should be a new datetime object representing "2026-04-18"

### Scenario 2: Handle invalid negative intervals
- **Given** an interval of -2 days
- **When** the calculation function is called
- **Then** the system should raise a ValueError
