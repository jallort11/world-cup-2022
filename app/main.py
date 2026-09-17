from fastapi import FastAPI, HTTPException, Query

from app.data_loader import load_players, load_teams

app = FastAPI(
    title="World Cup 2022 API",
    description="Programming Thinking exercise: build a data API with FastAPI.",
    version="0.1.0",
)

# Data is loaded once when the application starts.
players = load_players()
teams = load_teams()


@app.get("/")
def root():
    return {
        "message": "Welcome to the World Cup 2022 API",
        "players_loaded": len(players),
        "teams_loaded": len(teams),
        "docs": "/docs",
    }


# -----------------------------------------------------------------------------
# STUDENT EXERCISE
# -----------------------------------------------------------------------------
# Implement the endpoints described in README.md.
# Suggested routes:
#   GET /players/most-played
#   GET /players/top-scorers
#   GET /teams/ranking
#   GET /teams/{team}
#
# Do not implement them on main: each team should work on its own Git branch.

# --- Team 3: Team Ranking ---------------------------------------------------
# GET /teams/ranking?metric=goals
#
# Ranks all teams by a chosen numeric column from teams.csv, highest first.
# `teams` is already loaded once at startup above (via load_teams()), so we
# just filter/sort/validate it here instead of re-reading the CSV.

# Only expose the columns the README's example calls out as ranking
# metrics. Easy to extend with "matches", "yellow_cards", "red_cards" later.
ALLOWED_RANKING_METRICS = ["goals", "possession", "shots", "assists"]


@app.get("/teams/ranking")
def team_ranking(
    metric: str = Query(
        ...,
        description=f"Column to rank teams by. One of: {', '.join(ALLOWED_RANKING_METRICS)}",
    )
):
    # Validate against the allow-list first, so an unsupported metric
    # returns a clean 400 instead of a Pandas KeyError / 500.
    if metric not in ALLOWED_RANKING_METRICS:
        raise HTTPException(
            status_code=400,
            detail=(
                f"Invalid metric '{metric}'. "
                f"Must be one of: {', '.join(ALLOWED_RANKING_METRICS)}"
            ),
        )

    # Sort descending (best first), keep only the columns we need,
    # then rename the metric column to "value" to match the response spec.
    ranked = teams.sort_values(by=metric, ascending=False)[["team", metric]]
    ranked = ranked.rename(columns={metric: "value"})

    # DataFrame -> list of plain dicts, which FastAPI serializes to JSON.
    return ranked.to_dict(orient="records")
