# Requirements: World Cup 2022 API dashboard

**Change ID:** dashboard-api-viz  
**Status:** Approved  
**Version:** v1.0  
**Owner:** feature/sdd-kit

## Objective

**Problem:** The API is only usable through `/docs` or raw JSON. A student or reviewer cannot see endpoint results as charts and tables.  
**Success measure:** Opening `/dashboard` shows live data from the existing player and team endpoints, filters update those views, and pytest covers API behavior plus dashboard serving.  
**Out of scope:** New API endpoints (including `/teams/ranking`), authentication, persistence, deployment, and mobile-native apps.

## Visual and reference material

| ID | Link or path | Role | Status | Notes |
|---|---|---|---|---|
| M-001 | [Dashboard wireframe](assets/m-001-dashboard-wireframe.md) | Interface reference | Binding | Layout, labeled sources, filters, table-under-chart, in-section states |

No image mock exists. M-001 is the binding UI plan. Error, empty, and loading copy are specified below rather than inferred from a screenshot.

## User stories

### US-001 — See tournament overview, P1

**As a** student exploring the API  
**I want** a dashboard that shows how much data was loaded  
**So that** I know the app is running against the teaching dataset.

**Acceptance criteria**

- Given the server is running, when I open `/dashboard`, then I see player and team counts from `GET /`.
- Given `GET /` fails, when the page loads, then the overview shows an error message, not invented numbers.

### US-002 — Compare leading scorers, P1

**As a** student  
**I want** a chart and table of `/players/top-scorers`  
**So that** I can compare goals or assists without reading JSON.

**Acceptance criteria**

- Given default filters, when the dashboard loads, then top scorers are shown as a bar chart and a table with player, team, goals, and assists.
- Given I set `sort_by` to assists and apply, then the scorer view is ranked by assists.
- Given the endpoint returns an error, when I apply filters, then that section shows the error and keeps previous layout chrome (heading + source).

### US-003 — Compare minutes played, P1

**As a** student  
**I want** a chart and table of `/players/most-played`  
**So that** I can see who played the most minutes, optionally for one team.

**Acceptance criteria**

- Given default filters, when the dashboard loads, then most-played players are shown as a bar chart and a table with player, team, and minutes.
- Given I enter a known team and apply, then the minutes view is limited to that team.
- Given I enter an unknown team and apply, then the minutes section shows a not-found error.

### US-004 — Inspect a team profile, P1

**As a** student  
**I want** to look up `/teams/{team}`  
**So that** I can see aggregate team stats in one place.

**Acceptance criteria**

- Given I look up a known team, when the request succeeds, then I see players, total goals, total assists, average age, and top scorer.
- Given I look up an unknown team, when the request returns not found, then the profile section shows an error, not empty cards.

### US-005 — Trust the features with tests, P1

**As a** reviewer  
**I want** automated tests for the API endpoints and the dashboard page  
**So that** regressions are caught without clicking through `/docs`.

**Acceptance criteria**

- Given the test suite is run, when it finishes, then tests covering top-scorers, most-played, team profile, and dashboard HTML have passed.

## Functional requirements

| ID | Requirement |
|---|---|
| FR-001 | WHEN a client opens `/dashboard`, THE SYSTEM SHALL return an HTML page that matches M-001: overview, filters, top scorers, most minutes, and team profile. |
| FR-002 | WHEN the dashboard loads, THE SYSTEM SHALL call `GET /` and display `players_loaded` and `teams_loaded`. |
| FR-003 | WHEN the dashboard loads or the user applies filters, THE SYSTEM SHALL call `GET /players/top-scorers` with the current `limit` and `sort_by` and render a bar chart plus a table of player, team, goals, and assists. |
| FR-004 | WHEN the dashboard loads or the user applies filters, THE SYSTEM SHALL call `GET /players/most-played` with the current `limit` and optional `team` and render a bar chart plus a table of player, team, and minutes. |
| FR-005 | WHEN the user submits a team name in the profile form, THE SYSTEM SHALL call `GET /teams/{team}` and display players, total_goals, total_assists, average_age, and top_scorer. |
| FR-006 | WHILE any dashboard section is waiting on the API, THE SYSTEM SHALL show a loading message inside that section. |
| FR-007 | IF an API call fails or returns a not-found payload, THEN THE SYSTEM SHALL show an error message inside that section and SHALL NOT invent substitute statistics. |
| FR-008 | IF a successful list endpoint returns no rows, THEN THE SYSTEM SHALL show an empty message in that section. |
| FR-009 | WHEN `GET /` is called, THE SYSTEM SHALL include a `dashboard` URL pointing at `/dashboard`. |
| FR-010 | THE SYSTEM SHALL keep existing JSON endpoint contracts for `/players/top-scorers`, `/players/most-played`, and `/teams/{team}`. |
| FR-011 | THE SYSTEM SHALL provide automated tests for top-scorers (including invalid `sort_by`), most-played (including unknown team and invalid limit), team profile (known and unknown team), and the dashboard page. |

## Non-functional requirements and constraints

| ID | Category | Measurable requirement |
|---|---|---|
| NFR-001 | Accessibility | All filter and lookup controls have visible labels. Buttons have an accessible name. Charts have a data table alternative. |
| NFR-002 | Accessibility | Filters, apply, reset, and team lookup are operable with the keyboard only. |
| NFR-003 | Performance | Dashboard first load issues at most one request per section (overview, scorers, minutes, and profile only after lookup). |
| NFR-004 | Usability | Section headings name the visualization and the API source path. |
| C-001 | Constraint | Serve the UI from the FastAPI app as static HTML/CSS/JS. No React, Vue, or npm frontend build. |
| C-002 | Constraint | Do not add `/teams/ranking` or other new data endpoints. |
| C-003 | Constraint | Tests run with pytest against FastAPI TestClient. |

## Rules, assumptions, and questions

- Default limit is 10. Default scorer sort is `goals`. Minutes team filter is optional.
- Team profile lookup may be empty until the user submits a name.
- Unknown team handling follows the current API: most-played uses HTTP 404; team profile may return a JSON body with `detail` and no profile fields.

| ID | Type | Statement | Impact | Status |
|---|---|---|---|---|
| A-001 | Assumption | Visualize only endpoints that exist on current `main`. | High | Accepted |
| A-002 | Assumption | Team profile starts empty until lookup; that is the empty state for US-004. | Medium | Accepted |

## Approval checklist

- [x] Scope and success measure are clear.
- [x] All requirements are observable and testable.
- [x] Binding assets are explicitly identified.
- [x] High-impact questions are resolved.

**Decision:** Approve  
**Approved by / date:** Product request 2026-09-18
