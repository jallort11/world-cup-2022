# Design: World Cup 2022 API dashboard

**Change ID:** dashboard-api-viz  
**Requirements version:** v1.1  
**Status:** Approved

## Solution summary

Serve a single static page from FastAPI at `/dashboard`. Browser JavaScript calls the existing JSON endpoints and renders CSS bar charts plus tables. Pytest + TestClient covers endpoint contracts and that the dashboard HTML includes the M-001 regions. GitHub Actions runs that suite on pull requests to `main`.

## Coverage

| Requirement | Design element | Related asset | Authorized deviation |
|---|---|---|---|
| FR-001 | `GET /dashboard` → `app/static/dashboard.html` | M-001 | No |
| FR-002 | `loadOverview()` → `GET /` | M-001 | No |
| FR-003 | `loadScorers()` → `GET /players/top-scorers` | M-001 | No |
| FR-004 | `loadMinutes()` → `GET /players/most-played` | M-001 | No |
| FR-005 | `loadTeam()` → `GET /teams/{team}` | M-001 | No |
| FR-006 | Per-section `.status` node with `Loading…` | M-001 | No |
| FR-007 | Per-section error text from HTTP body or `detail` | M-001 | No |
| FR-008 | Per-section empty copy when arrays are `[]` | M-001 | No |
| FR-009 | Root JSON adds `"dashboard": "/dashboard"` | — | No |
| FR-010 | No change to query params or list field names | — | No |
| FR-011 | `tests/` with pytest + TestClient | — | No |
| NFR-001 | `<label>` + table under each chart | M-001 | No |
| NFR-002 | Native form controls and submit/reset | M-001 | No |
| NFR-003 | One fetch per section; profile only on submit | — | No |
| NFR-004 | `h2` + `.source` with the path | M-001 | No |
| C-001 | Static files, no SPA framework | — | No |
| C-002 | No ranking endpoint | — | No |
| C-003 | pytest | — | No |
| C-004 | `.github/workflows/tests.yml` | — | No |
| FR-012 | GitHub Actions job `pytest` on PRs to `main` | — | No |

## Architecture and flow

```text
Browser  --GET /dashboard-->  FastAPI FileResponse (HTML/CSS/JS)
Browser  --GET / -->          root()
Browser  --GET /players/top-scorers-->  top_scorers()
Browser  --GET /players/most-played-->  most_played()
Browser  --GET /teams/{team}-->         team_profile()
pytest   --TestClient-->      same routes
GitHub Actions --PR to main-->  pip install -r requirements.txt && pytest -q
```

On load: overview + scorers + minutes (three requests). Profile waits for submit.

## Components and data

| Element | Responsibility | Interface or data | Requirements |
|---|---|---|---|
| `GET /dashboard` | Serve the page | HTML | FR-001 |
| `app/static/dashboard.css` | Layout matching M-001 | — | FR-001, NFR-001 |
| `app/static/dashboard.js` | Fetch, states, charts, tables | JSON from existing APIs | FR-002–FR-008 |
| Root JSON | Discoverability | `dashboard` path | FR-009 |
| Existing endpoints | Unchanged contracts | current query params and fields | FR-010 |
| `tests/test_api.py` | Endpoint behavior | pytest | FR-011 |
| `tests/test_dashboard.py` | Page served and structure | pytest | FR-001, FR-011, NFR-004 |
| `.github/workflows/tests.yml` | CI gate on PRs to `main` | pytest on GitHub-hosted Python 3.12 | FR-012, C-004 |

## Decisions

| ID | Decision | Alternatives | Rationale | Consequence |
|---|---|---|---|---|
| D-001 | Static HTML/CSS/JS, no Chart.js/npm | React; Chart.js CDN | C-001; CSS bars avoid a CDN dependency | Charts are simple bars, not interactive canvases |
| D-002 | Same-origin fetches | Separate frontend port | Simplest local run with one `uvicorn` | Dashboard only works when served by FastAPI |
| D-003 | Profile empty until lookup | Auto-load Argentina | A-002; avoids inventing a default team | First paint has no profile numbers |
| D-004 | Treat team-profile `{detail}` without `team` as error | Change API to HTTP 404 | FR-010: do not change existing contract | UI must inspect payload shape |
| D-005 | pytest + TestClient, not browser E2E | Playwright | C-003; course-sized suite | Keyboard/visual checks are manual (VT-a11y) |
| D-006 | GitHub Actions for CI | GitLab CI; local-only pytest | Already on GitHub; FR-012 needs a check on the PR | Token needs `workflow` scope to push `.yml` files |

## States and test strategy

- **Loading:** each section sets status text to `Loading…` and `aria-busy="true"`.
- **Empty lists:** `No players returned for these filters.`
- **Empty profile:** `Look up a team to see its profile.` until submit.
- **Error:** show `Could not load this view: {message}`. For HTTP errors, prefer `detail` from JSON.
- **Accessibility:** labeled inputs; tables for chart data; keyboard-native forms.

| Requirement | Test type | Expected evidence |
|---|---|---|
| FR-001, NFR-004 | Integration | Dashboard 200 and required landmarks in HTML |
| FR-002, FR-009 | Integration | Root JSON has counts and `dashboard` |
| FR-003, FR-010, FR-011 | Integration | Top scorers order, `sort_by=assists`, invalid `sort_by` → 422 |
| FR-004, FR-011 | Integration | Most-played order, team filter, unknown team → 404, `limit=0` → 400 |
| FR-005, FR-011 | Integration | Known team profile fields; unknown team `detail` |
| FR-006–FR-008 | Manual | Loading/error/empty visible in the section |
| NFR-001, NFR-002 | Manual | Keyboard tab through filters; labels present (also asserted in HTML test) |
| FR-012, C-004 | CI | Green `pytest` check on the pull request |

## Approval checklist

- [x] Every FR and NFR is covered.
- [x] Binding assets have no unauthorized deviation.
- [x] Failure, empty, and accessibility states are addressed.
- [x] Each requirement has a verification approach.

**Decision:** Approve  
**Approved by / date:** Product request 2026-09-18
