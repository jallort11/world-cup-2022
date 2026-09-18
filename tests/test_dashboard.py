def test_dashboard_page_matches_wireframe(client):
    response = client.get("/dashboard")
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/html")
    html = response.text
    assert "Tournament dashboard" in html
    assert "source: GET /" in html
    assert "source: GET /players/top-scorers" in html
    assert "source: GET /players/most-played" in html
    assert "source: GET /teams/{team}" in html
    assert 'id="filters"' in html
    assert 'for="limit"' in html
    assert 'for="sort-by"' in html
    assert 'for="minutes-team"' in html
    assert 'for="team-name"' in html
    assert "scorers-table" in html
    assert "minutes-table" in html
    assert "/static/dashboard.js" in html


def test_dashboard_assets_are_served(client):
    css = client.get("/static/dashboard.css")
    js = client.get("/static/dashboard.js")
    assert css.status_code == 200
    assert js.status_code == 200
    assert "bar-fill" in css.text
    assert "loadScorers" in js.text
