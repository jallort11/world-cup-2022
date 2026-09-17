# World Cup 2022 API ⚽

A small FastAPI project for the **Programming Thinking** pre-course.

The goal is not to build a complex application. The goal is to practice:

- reading and understanding an existing repository;
- working with Git branches;
- filtering, sorting and aggregating data with Pandas;
- designing simple API endpoints;
- testing an API through FastAPI `/docs`;
- creating commits, pushing a branch and opening a Pull Request.

## Setup

Create and activate a virtual environment, then install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate       # macOS/Linux
# .venv\\Scripts\\activate      # Windows
pip install -r requirements.txt
```

Add the two CSV files described in `data/README.md`, then run:

```bash
uvicorn app.main:app --reload
```

Open:

- API: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs

## Git workflow

Each team creates its own branch. For example:

```bash
git checkout -b feature/most-played
```

After implementing and testing the endpoint:

```bash
git add .
git commit -m "Add most played players endpoint"
git push -u origin feature/most-played
```

Then open a Pull Request on GitHub.

---

# Team challenges

## Team 1 — Iron Players 🏃

Implement:

```http
GET /players/most-played?limit=10
```

Return the players with the most minutes, ordered from highest to lowest.

Expected fields:

```json
[
  {"player": "...", "team": "...", "minutes": 690}
]
```

### Bonus

Support:

```http
GET /players/most-played?limit=10&team=Argentina
```

Think about:

- How do you sort a DataFrame?
- How do you return only N rows?
- What should happen with an unknown team?
- What should happen if `limit=0` or `limit=-5`?

---

## Team 2 — Top Scorers ⚽

Implement:

```http
GET /players/top-scorers?limit=10
```

Return the leading scorers with fields such as:

```json
[
  {"player": "...", "team": "...", "goals": 8, "assists": 2}
]
```

### Bonus

Support:

```http
GET /players/top-scorers?sort_by=goals
GET /players/top-scorers?sort_by=assists
```

Think about validation: what should happen with `sort_by=bananas`?

---

## Team 3 — Team Ranking 🏆

Implement:

```http
GET /teams/ranking?metric=goals
```

Allow useful metrics from the dataset, for example:

```text
goals
possession
shots
assists
```

Example response:

```json
[
  {"team": "...", "value": 16},
  {"team": "...", "value": 15}
]
```

Think about:

- How can one endpoint sort using different columns?
- Which metrics should be allowed?
- What HTTP error should be returned for an invalid metric?

---

## Team 4 — Team Profile 🔎

Implement:

```http
GET /teams/{team}
```

Build a summary from the player data. For example:

```json
{
  "team": "Argentina",
  "players": 26,
  "total_goals": 15,
  "total_assists": 8,
  "average_age": 27.8,
  "top_scorer": "..."
}
```

Think about:

- How do you filter all players belonging to one team?
- How do you calculate aggregate values?
- What should `/teams/Patatonia` return?

---

# Final challenge 🚀

After all Pull Requests have been merged, design together:

```http
GET /players/most-efficient?limit=10
```

Define attacking contributions as:

```text
contributions = goals + assists
```

and calculate contributions per 90 minutes:

```text
contributions_per_90 = (goals + assists) / minutes * 90
```

Discuss edge cases before writing the code.

## Dataset note

For a quick classroom setup, use a 2022 World Cup player/team statistics dataset and commit a **small cleaned copy** to `data/`. Do not make students download or clean the source dataset during this exercise unless that is itself part of the lesson.

Useful public reference data exists in FBref's 2022 World Cup statistics and in the Fjelstul World Cup Database/DataHub. Check the source licence before redistributing a derived CSV and keep attribution in this README.
