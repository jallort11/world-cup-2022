# World Cup 2022 API

FastAPI teaching project for **Programming Thinking**. It serves 2022 World Cup player and team stats from CSV files, plus a browser dashboard that visualizes those endpoints.

Team 2 added the dashboard, pytest coverage, and GitHub Actions.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate       # macOS/Linux
# .venv\Scripts\activate        # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

If port 8000 is already in use:

```bash
uvicorn app.main:app --reload --port 8001
```

| Page | URL |
|------|-----|
| Dashboard | http://127.0.0.1:8000/dashboard |
| API welcome | http://127.0.0.1:8000 |
| Swagger UI | http://127.0.0.1:8000/docs |

## Dashboard

`GET /dashboard` loads a single page that calls the JSON API:

- Overview from `GET /`
- Top scorers chart and table (`limit`, `sort_by=goals|assists`)
- Most minutes chart and table (`limit`, optional team)
- Team profile lookup (`GET /teams/{team}`)

Each panel shows loading, empty, and error states. Charts have a data table underneath.

## API

Interactive docs: http://127.0.0.1:8000/docs

### `GET /`

Returns how many rows were loaded and links to docs and the dashboard.

```json
{
  "message": "Welcome to the World Cup 2022 API",
  "players_loaded": 40,
  "teams_loaded": 32,
  "docs": "/docs",
  "dashboard": "/dashboard"
}
```

### `GET /players/top-scorers`

| Query | Default | Notes |
|-------|---------|--------|
| `limit` | `10` | Must be ≥ 1 (otherwise 422) |
| `sort_by` | `goals` | `goals` or `assists`. Anything else (e.g. `bananas`) → 422 |

```http
GET /players/top-scorers?limit=10
GET /players/top-scorers?sort_by=assists&limit=5
```

```json
[
  {"player": "Kylian Mbappe", "team": "France", "goals": 8, "assists": 2}
]
```

### `GET /players/most-played`

| Query | Default | Notes |
|-------|---------|--------|
| `limit` | `10` | Must be ≥ 1 (otherwise 400) |
| `team` | omitted | Case-insensitive. Unknown team → 404 |

```http
GET /players/most-played?limit=10
GET /players/most-played?limit=10&team=Argentina
```

```json
[
  {"player": "Lionel Messi", "team": "Argentina", "minutes": 690}
]
```

### `GET /teams/{team}`

```http
GET /teams/Argentina
```

```json
{
  "team": "Argentina",
  "players": 5,
  "total_goals": 15,
  "total_assists": 8,
  "average_age": 26.2,
  "top_scorer": "Lionel Messi"
}
```

Unknown team currently returns `{"detail": "Team not found"}` with HTTP 200 (existing contract).

## Tests

```bash
source .venv/bin/activate
pytest
```

The suite covers top scorers, most-played, team profile, and that `/dashboard` is served.

## CI

Pull requests and pushes to `main` run `.github/workflows/tests.yml` (job **pytest**): install `requirements.txt`, then `pytest -q`.

Do not merge while that check is red. Optional: in GitHub, protect `main` with **Require status checks to pass** → `pytest`.

## Dataset

Teaching CSVs in `data/` (`players.csv`, `teams.csv`). See `data/README.md`. Not an official statistical source.

## Spec-driven documents

This change was specified before code. Start here if you are reviewing the process:

| File | Role |
|------|------|
| [00-constitution.md](00-constitution.md) | Stable rules |
| [01-requirements.md](01-requirements.md) | User stories and requirements |
| [assets/m-001-dashboard-wireframe.md](assets/m-001-dashboard-wireframe.md) | Binding UI plan |
| [02-design.md](02-design.md) | Design |
| [03-tasks.md](03-tasks.md) | Tasks |
| [04-verification.md](04-verification.md) | Evidence |
| [docs/sdd-kit.md](docs/sdd-kit.md) | How to use the SDD kit |
