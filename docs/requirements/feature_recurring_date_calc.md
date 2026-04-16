# Feature: Recurring Task Next Date Calculation

## User Story
**As a** user with repeating tasks,
**I want** the system to calculate the exact next run date based on my interval,
**So that** my schedule remains accurate without manual updates.

## Acceptance Criteria (BDD)
### Scenario 1: Calculate standard daily recurrence
- **Given** a current run date of "2026-04-17" and an interval of 1 day
- **When** the next date calculation is requested
- **Then** the result should be a new date object representing "2026-04-18"

### Scenario 2: Calculate weekly recurrence crossing a month boundary
- **Given** a current run date of "2026-04-28" and an interval of 7 days
- **When** the next date calculation is requested
- **Then** the result should be a new date object representing "2026-05-05"

### Scenario 3: Handle invalid negative intervals
- **Given** an interval of -2 days
- **When** the next date calculation is requested
- **Then** the system should raise a ValueError
