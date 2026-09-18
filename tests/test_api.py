def test_root_includes_dashboard_link(client):
    response = client.get("/")
    assert response.status_code == 200
    body = response.json()
    assert body["dashboard"] == "/dashboard"
    assert body["players_loaded"] > 0
    assert body["teams_loaded"] > 0


def test_top_scorers_default_order(client):
    response = client.get("/players/top-scorers")
    assert response.status_code == 200
    rows = response.json()
    assert len(rows) == 10
    assert rows[0]["player"] == "Kylian Mbappe"
    assert rows[0]["goals"] == 8
    assert {"player", "team", "goals", "assists"} <= set(rows[0])


def test_top_scorers_sort_by_assists(client):
    response = client.get("/players/top-scorers", params={"sort_by": "assists", "limit": 4})
    assert response.status_code == 200
    rows = response.json()
    assists = [row["assists"] for row in rows]
    assert assists == sorted(assists, reverse=True)
    assert all(row["assists"] == 3 for row in rows)


def test_top_scorers_rejects_invalid_sort(client):
    response = client.get("/players/top-scorers", params={"sort_by": "bananas"})
    assert response.status_code == 422


def test_most_played_default_order(client):
    response = client.get("/players/most-played")
    assert response.status_code == 200
    rows = response.json()
    assert len(rows) == 10
    minutes = [row["minutes"] for row in rows]
    assert minutes == sorted(minutes, reverse=True)
    assert {"player", "team", "minutes"} <= set(rows[0])


def test_most_played_filters_team(client):
    response = client.get("/players/most-played", params={"team": "Argentina", "limit": 5})
    assert response.status_code == 200
    rows = response.json()
    assert rows
    assert all(row["team"] == "Argentina" for row in rows)


def test_most_played_unknown_team(client):
    response = client.get("/players/most-played", params={"team": "Patatonia"})
    assert response.status_code == 404
    assert "Patatonia" in response.json()["detail"]


def test_most_played_rejects_invalid_limit(client):
    response = client.get("/players/most-played", params={"limit": 0})
    assert response.status_code == 400


def test_team_profile_known_team(client):
    response = client.get("/teams/Argentina")
    assert response.status_code == 200
    body = response.json()
    assert body["team"] == "Argentina"
    assert body["top_scorer"] == "Lionel Messi"
    assert {"players", "total_goals", "total_assists", "average_age", "top_scorer"} <= set(body)


def test_team_profile_unknown_team(client):
    response = client.get("/teams/Patatonia")
    assert response.status_code == 200
    assert response.json()["detail"] == "Team not found"
