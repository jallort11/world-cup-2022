# Tasks: World Cup 2022 API dashboard

**Change ID:** dashboard-api-viz  
**Approved input:** requirements v1.1, design v1.1  
**Status:** Complete

## Conventions

- `[ ]` Pending; `[-]` In progress; `[x]` Complete; `[!]` Blocked.
- Every task must link to requirements and state its expected evidence.
- Use `[P]` only for tasks that can safely run in parallel.

## Preparation

- [x] T-001 [C-003] [depends on: —] Add pytest and httpx to `requirements.txt`; evidence: packages install.
- [x] T-002 [FR-009] [depends on: —] Add `dashboard` to `GET /`; evidence: VT-009.

## US-001 / US-002 / US-003 / US-004 — Dashboard UI

- [x] T-010 [FR-001, NFR-001, NFR-002, NFR-004] [depends on: —] Build `dashboard.html` / `.css` matching M-001; evidence: VT-001.
- [x] T-011 [FR-002, FR-003, FR-004, FR-005, FR-006, FR-007, FR-008, NFR-003] [depends on: T-010] Implement `dashboard.js` fetches, CSS bars, tables, and states; evidence: VT-003, VT-006.
- [x] T-012 [FR-001] [depends on: T-010] Serve `/dashboard` from FastAPI; evidence: VT-001.

## US-005 — Tests

- [x] T-020 [P] [FR-010, FR-011] [depends on: T-001] Tests for `/players/top-scorers`; evidence: VT-010.
- [x] T-021 [P] [FR-010, FR-011] [depends on: T-001] Tests for `/players/most-played`; evidence: VT-011.
- [x] T-022 [P] [FR-010, FR-011] [depends on: T-001] Tests for `/teams/{team}`; evidence: VT-012.
- [x] T-023 [FR-001, FR-009, FR-011, NFR-001, NFR-004] [depends on: T-012] Tests for `/` and `/dashboard` HTML; evidence: VT-001, VT-009.
- [x] T-024 [FR-012, C-004] [depends on: T-020, T-021, T-022, T-023] Add `.github/workflows/tests.yml` so PRs to `main` run pytest; evidence: VT-014.

## Integration and quality

- [x] T-090 [NFR-001, NFR-002] [depends on: T-011, T-012] Keyboard/manual pass of filters and lookup; evidence: VT-013.
- [x] T-091 [FR-..., NFR-...] [depends on: T-020, T-021, T-022, T-023, T-090] Fill `04-verification.md` and run pytest to completion; evidence: this file.

## Coverage check

| Requirement | Implementing task(s) | Test or evidence |
|---|---|---|
| FR-001 | T-010, T-012, T-023 | VT-001 |
| FR-002 | T-011 | VT-003 |
| FR-003 | T-011, T-020 | VT-010 |
| FR-004 | T-011, T-021 | VT-011 |
| FR-005 | T-011, T-022 | VT-012 |
| FR-006 | T-011 | VT-006 |
| FR-007 | T-011 | VT-006 |
| FR-008 | T-011 | VT-006 |
| FR-009 | T-002, T-023 | VT-009 |
| FR-010 | T-020, T-021, T-022 | VT-010, VT-011, VT-012 |
| FR-011 | T-020–T-023 | pytest log |
| FR-012 | T-024 | VT-014 |
| NFR-001 | T-010, T-023 | VT-001, VT-013 |
| NFR-002 | T-010, T-090 | VT-013 |
| NFR-003 | T-011 | VT-003 |
| NFR-004 | T-010, T-023 | VT-001 |
| C-001 | T-010, T-012 | static files |
| C-002 | — | no ranking route added |
| C-003 | T-001 | pytest |
| C-004 | T-024 | VT-014 |

- [x] Every approved requirement has at least one task and one test.
- [x] Dependencies are explicit.
- [x] No task introduces unapproved scope.
