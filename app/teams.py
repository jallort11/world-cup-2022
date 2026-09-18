from app.data_loader import load_players, load_teams

players = load_players()
teams = load_teams()

def team_profile(team: str):
    team_players = players[players["team"].str.lower() == team.lower()]
    country = teams[teams["team"].str.lower() == team.lower()]

    if team_players.empty:
        return {"detail": "Team not found"}

    total_goals = int(country["goals"].iloc[0])
    total_assists = int(country["assists"].iloc[0])
    average_age = float(team_players["age"].mean())
    top_scorer_index = team_players["goals"].idxmax()
    top_scorer = team_players.loc[top_scorer_index, "player"]

    return {
        "team": team.title(),
        "players": int(len(team_players)),
        "total_goals": total_goals,
        "total_assists": total_assists,
        "average_age": round(average_age, 1),
        "top_scorer": top_scorer,
    }