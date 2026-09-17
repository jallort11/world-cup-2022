from fastapi import FastAPI

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
