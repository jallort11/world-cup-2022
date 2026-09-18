# Verification: World Cup 2022 API dashboard

**Change ID:** dashboard-api-viz  
**Specification version:** v1.1  
**Status:** Verified

## Evidence by requirement

| ID | Scenario | Type | Evidence | Result |
|---|---|---|---|---|
| VT-001 / FR-001 | Given the server is running, when GET `/dashboard`, then HTML includes overview, filters, scorers, minutes, team profile, labels, and source paths | Test | `tests/test_dashboard.py::test_dashboard_page_matches_wireframe` | Pass |
| VT-003 / FR-002 | Given the dashboard loads, when overview fetch completes, then it shows `40 players loaded · 32 teams loaded` | Manual | Browser at `/dashboard` | Pass |
| VT-006 / FR-006–008 | Given filters are applied, when a section is in-flight it shows `Loading…`; unknown team shows an error and hides stale bars; empty profile copy until lookup | Manual | Browser: loading status, Patatonia error with `display:none` on chart | Pass |
| VT-009 / FR-009 | Given GET `/`, when JSON is returned, then `dashboard` is `/dashboard` | Test | `test_root_includes_dashboard_link` | Pass |
| VT-010 / FR-003, FR-010 | Given top-scorers defaults, sort_by=assists, and sort_by=bananas | Test | `test_top_scorers_*` | Pass |
| VT-011 / FR-004 | Given most-played defaults, Argentina filter, unknown team, limit=0 | Test | `test_most_played_*` | Pass |
| VT-012 / FR-005 | Given `/teams/Argentina` and `/teams/Patatonia` | Test | `test_team_profile_*` | Pass |
| VT-013 / NFR-001, NFR-002 | Given the dashboard, when tabbing, controls have names Limit, Scorers sort, Minutes team, Apply, Reset, Team name, Look up | Manual | Accessibility snapshot of `/dashboard` | Pass |
| VT-014 / FR-012, C-004 | Given PR #6 targets `main`, when GitHub Actions runs, then the `pytest` job passes | CI | [pytest on PR #6](https://github.com/jallort11/world-cup-2022/actions/runs/35334707881/job/105566757503) | Pass |

Automated suite: **12 passed** locally (`pytest -q`) and on GitHub Actions (`pytest` check, 23s).

## Binding-asset validation

| Asset | Element checked | Result | Approved deviation |
|---|---|---|---|
| M-001 | Title, API docs link, overview, filter bar, two player panels with source lines, tables under charts, team lookup | Pass | None |
| M-001 | In-section loading/error/empty | Pass | None |

## Traceability

| Requirement | Design | Task(s) | Verification | Verdict |
|---|---|---|---|---|
| FR-001 | D-001, D-002 | T-010, T-012, T-023 | VT-001 | Covered |
| FR-002 | loadOverview | T-011 | VT-003 | Covered |
| FR-003 | loadScorers | T-011, T-020 | VT-010 | Covered |
| FR-004 | loadMinutes | T-011, T-021 | VT-011 | Covered |
| FR-005 | loadTeam | T-011, T-022 | VT-012 | Covered |
| FR-006 | per-section status | T-011 | VT-006 | Covered |
| FR-007 | error copy + hide visuals | T-011 | VT-006 | Covered |
| FR-008 | empty list copy | T-011 | VT-006 | Covered |
| FR-009 | root JSON | T-002, T-023 | VT-009 | Covered |
| FR-010 | unchanged contracts | T-020–T-022 | VT-010–012 | Covered |
| FR-011 | pytest | T-020–T-023 | 12 passed | Covered |
| NFR-001 | labels + tables | T-010, T-023 | VT-001, VT-013 | Covered |
| NFR-002 | native forms | T-010, T-090 | VT-013 | Covered |
| NFR-003 | one fetch per section | T-011 | VT-003 | Covered |
| NFR-004 | source paths | T-010 | VT-001 | Covered |
| C-001 | static HTML/CSS/JS | T-010, T-012 | files under `app/static/` | Covered |
| C-002 | no ranking endpoint | — | `app/main.py` has no `/teams/ranking` | Covered |
| C-003 | pytest | T-001 | pytest.ini + 12 passed | Covered |
| C-004 | D-006 | T-024 | VT-014 | Covered |
| FR-012 | D-006 | T-024 | VT-014 | Covered |

## Findings

| Severity | Finding | Requirement | Next action |
|---|---|---|---|
| Low | `.bars { display: flex }` overrode `[hidden]` until a global `[hidden] { display: none }` rule was added | FR-007 | Fixed in `dashboard.css` |

## Convergence

- [x] **Converged:** every approved requirement has valid evidence and there are no unauthorized deviations.
- [ ] **Not converged:** create the required follow-up tasks in `03-tasks.md`.

## How to run

See [README.md](README.md) for setup, API examples, dashboard, tests, and CI.

```bash
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
pytest
```

Open http://127.0.0.1:8000/dashboard

Pull requests to `main` run `.github/workflows/tests.yml` (job `pytest`). Evidence: [PR #6 check](https://github.com/jallort11/world-cup-2022/actions/runs/35334707881/job/105566757503).

**Reviewed by / date:** Agent verification 2026-09-18
