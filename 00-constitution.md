# Project Constitution

**Status:** Approved  
**Phase:** 0 (stable rules)  
**Date:** 2026-09-18

## Purpose

This workspace specifies and delivers a **World Cup 2022 dashboard**: a browser UI that visualizes the existing FastAPI endpoints, automated tests for those features, and a GitHub Actions check that runs pytest on pull requests to `main` before merge.

The pipeline is constitution → requirements → design → tasks → implementation → verification.

## Rules

1. **Quality:** Keep every change small, readable, and traceable. Requirement IDs (`US-###`, `FR-###`, `NFR-###`, `C-###`) stay stable once a requirements version is approved. Prefer the simplest design that satisfies approved requirements. Do not add unrequested features. Do not invent new API endpoints unless a requirement names them.
2. **Testing:** Every approved `FR` and `NFR` must have at least one verification item in `04-verification.md`. A requirement is done only when its evidence is recorded. Automated tests (pytest) are the default evidence for API and dashboard-serving behavior. Pull requests to `main` must run that suite in GitHub Actions (`.github/workflows/tests.yml`).
3. **Accessibility and UX:** Binding mocks labeled **Binding** in `01-requirements.md` are non-negotiable unless an authorized deviation is recorded in design. Interactive elements must be operable by keyboard and must expose an accessible name. Empty, loading, and error states must be specified rather than invented at code time. Charts must have a table (or equivalent text) alternative.
4. **Security and privacy:** Do not commit secrets, credentials, or live personal data. The teaching CSVs in `data/` are public sample statistics, not personal data. Do not implement authentication, payment, or personal-data collection.
5. **Constraints:** Work from approved requirements and design. Link decisions, tasks, and tests to requirement IDs. English is the language of specification, UI copy, and code comments. Stack: FastAPI, pandas, static HTML/CSS/JS served by the same app, pytest, GitHub Actions. No new frontend framework (React/Vue) and no new backend framework.

## Definition of Done

- [x] Acceptance criteria are verified.
- [x] Evidence is recorded in `04-verification.md`.
- [x] No binding mock, requirement, or rule in this file is contradicted.
- [x] Relevant documentation is updated.
- [x] Every approved requirement ID maps to design, tasks, and verification with no silent gaps.

## Open questions and assumptions

| ID    | Type       | Statement                                                                                         | Impact | Status   |
| ----- | ---------- | ------------------------------------------------------------------------------------------------- | ------ | -------- |
| Q-001 | Question   | What is the product, assignment, or change to specify?                                            | High   | Resolved |
| Q-002 | Question   | Is the deliverable UI, API, document-only, or mixed?                                              | High   | Resolved |
| Q-003 | Question   | What stack, deadline, and prohibited tools apply?                                                 | High   | Resolved |
| Q-004 | Question   | Will the system store or process personal data?                                                   | High   | Resolved |
| Q-005 | Question   | Should this constitution govern `world-cup-2022` or a follow-on feature?                          | High   | Resolved |
| A-001 | Assumption | Visualize existing endpoints only (`/`, `/players/top-scorers`, `/players/most-played`, `/teams/{team}`). | High   | Accepted |
| A-002 | Assumption | `GET /teams/ranking` is out of scope because it is not implemented on current `main`.             | Medium | Accepted |
| A-003 | Assumption | Specs, UI copy, and comments are in English.                                                      | Low    | Accepted |

**Resolutions**

- Q-001: Build a local dashboard that visualizes World Cup 2022 API endpoints.
- Q-002: Mixed — existing JSON API + new HTML dashboard + tests + CI.
- Q-003: FastAPI + pandas + static HTML/CSS/JS + pytest + GitHub Actions. No React/Vue. No auth.
- Q-004: No. Dataset is a public teaching subset of tournament statistics.
- Q-005: Yes. This constitution governs this follow-on dashboard in `world-cup-2022`.

**Decision:** Approve  
**Approved by / date:** Product request 2026-09-18 (dashboard + tests, follow SDD plan)
