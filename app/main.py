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


@app.get("/players/most-played")
def most_played(
    limit: int = Query(10, description="Number of players to return (must be 1 or more)."),
    team: str | None = Query(None, description="Filter by team, e.g. Argentina."),
    
):
    # A limit of 0 or a negative number makes no sense: reject it instead of returning nothing.
    if limit < 1:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid limit '{limit}': limit must be a positive integer (1 or more).",
        )

    result = players

    # Filters are case-insensitive; an unknown value is a 404, not an empty list.
    if team is not None:
        result = result[result["team"].str.lower() == team.strip().lower()]
        if result.empty:
            raise HTTPException(status_code=404, detail=f"Team '{team}' not found.")


    # Highest minutes first (ascending=False). Ties on minutes are broken
    # alphabetically by player so the output is stable.
    result = result.sort_values(["minutes", "player"], ascending=[False, True]).head(limit)
    return result[["player", "team", "minutes"]].to_dict(orient="records")


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
