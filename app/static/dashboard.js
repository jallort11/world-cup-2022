function $(id) {
  return document.getElementById(id);
}

function setStatus(id, message, isError = false) {
  const node = $(id);
  node.hidden = false;
  node.textContent = message;
  node.classList.toggle("error", isError);
}

async function readError(response) {
  try {
    const body = await response.json();
    if (typeof body.detail === "string") {
      return body.detail;
    }
    if (Array.isArray(body.detail) && body.detail[0]?.msg) {
      return body.detail[0].msg;
    }
    return `Request failed (${response.status})`;
  } catch {
    return `Request failed (${response.status})`;
  }
}

function renderBars(container, rows, valueKey) {
  const max = Math.max(...rows.map((row) => Number(row[valueKey])), 1);
  container.replaceChildren();
  container.hidden = false;
  for (const row of rows) {
    const value = Number(row[valueKey]);
    const item = document.createElement("div");
    item.className = "bar-row";

    const name = document.createElement("span");
    name.className = "bar-label";
    name.textContent = row.player;

    const track = document.createElement("div");
    track.className = "bar-track";
    const fill = document.createElement("div");
    fill.className = "bar-fill";
    fill.style.width = `${(value / max) * 100}%`;
    track.appendChild(fill);

    const amount = document.createElement("span");
    amount.className = "bar-value";
    amount.textContent = String(value);

    item.append(name, track, amount);
    container.appendChild(item);
  }
}

function renderTable(table, rows, columns) {
  const body = table.querySelector("tbody");
  body.replaceChildren();
  table.hidden = false;
  for (const row of rows) {
    const tr = document.createElement("tr");
    for (const column of columns) {
      const td = document.createElement("td");
      td.textContent = String(row[column]);
      tr.appendChild(td);
    }
    body.appendChild(tr);
  }
}

function hideVisuals(...nodes) {
  for (const node of nodes) {
    node.hidden = true;
  }
}

async function loadOverview() {
  const dataNode = $("overview-data");
  dataNode.hidden = true;
  $("overview-status").parentElement.setAttribute("aria-busy", "true");
  setStatus("overview-status", "Loading…");
  try {
    const response = await fetch("/");
    if (!response.ok) {
      throw new Error(await readError(response));
    }
    const data = await response.json();
    dataNode.hidden = false;
    dataNode.textContent = `${data.players_loaded} players loaded · ${data.teams_loaded} teams loaded`;
    setStatus("overview-status", "");
    $("overview-status").hidden = true;
  } catch (error) {
    setStatus("overview-status", `Could not load this view: ${error.message}`, true);
  } finally {
    $("overview-status").parentElement.removeAttribute("aria-busy");
  }
}

async function loadScorers() {
  const chart = $("scorers-chart");
  const table = $("scorers-table");
  hideVisuals(chart, table);
  $("scorers-status").parentElement.setAttribute("aria-busy", "true");
  setStatus("scorers-status", "Loading…");

  const limit = $("limit").value;
  const sortBy = $("sort-by").value;
  const params = new URLSearchParams({ limit, sort_by: sortBy });

  try {
    const response = await fetch(`/players/top-scorers?${params}`);
    if (!response.ok) {
      throw new Error(await readError(response));
    }
    const rows = await response.json();
    if (!rows.length) {
      setStatus("scorers-status", "No players returned for these filters.");
      return;
    }
    renderBars(chart, rows, sortBy);
    renderTable(table, rows, ["player", "team", "goals", "assists"]);
    $("scorers-status").hidden = true;
  } catch (error) {
    setStatus("scorers-status", `Could not load this view: ${error.message}`, true);
  } finally {
    $("scorers-status").parentElement.removeAttribute("aria-busy");
  }
}

async function loadMinutes() {
  const chart = $("minutes-chart");
  const table = $("minutes-table");
  hideVisuals(chart, table);
  $("minutes-status").parentElement.setAttribute("aria-busy", "true");
  setStatus("minutes-status", "Loading…");

  const params = new URLSearchParams({ limit: $("limit").value });
  const team = $("minutes-team").value.trim();
  if (team) {
    params.set("team", team);
  }

  try {
    const response = await fetch(`/players/most-played?${params}`);
    if (!response.ok) {
      throw new Error(await readError(response));
    }
    const rows = await response.json();
    if (!rows.length) {
      setStatus("minutes-status", "No players returned for these filters.");
      return;
    }
    renderBars(chart, rows, "minutes");
    renderTable(table, rows, ["player", "team", "minutes"]);
    $("minutes-status").hidden = true;
  } catch (error) {
    setStatus("minutes-status", `Could not load this view: ${error.message}`, true);
  } finally {
    $("minutes-status").parentElement.removeAttribute("aria-busy");
  }
}

async function loadTeam(event) {
  event.preventDefault();
  const cards = $("team-cards");
  cards.hidden = true;
  cards.replaceChildren();
  $("team-status").parentElement.setAttribute("aria-busy", "true");
  setStatus("team-status", "Loading…");

  const team = $("team-name").value.trim();
  if (!team) {
    setStatus("team-status", "Look up a team to see its profile.");
    $("team-status").parentElement.removeAttribute("aria-busy");
    return;
  }

  try {
    const response = await fetch(`/teams/${encodeURIComponent(team)}`);
    const data = await response.json();
    if (!response.ok || !data.team) {
      const message = typeof data.detail === "string" ? data.detail : "Team not found";
      throw new Error(message);
    }
    const fields = [
      ["Players", data.players],
      ["Total goals", data.total_goals],
      ["Total assists", data.total_assists],
      ["Average age", data.average_age],
      ["Top scorer", data.top_scorer],
    ];
    for (const [label, value] of fields) {
      const wrap = document.createElement("div");
      const dt = document.createElement("dt");
      dt.textContent = label;
      const dd = document.createElement("dd");
      dd.textContent = String(value);
      wrap.append(dt, dd);
      cards.appendChild(wrap);
    }
    cards.hidden = false;
    $("team-status").hidden = true;
  } catch (error) {
    setStatus("team-status", `Could not load this view: ${error.message}`, true);
  } finally {
    $("team-status").parentElement.removeAttribute("aria-busy");
  }
}

function applyFilters(event) {
  event.preventDefault();
  loadScorers();
  loadMinutes();
}

function resetFilters() {
  window.setTimeout(() => {
    loadScorers();
    loadMinutes();
  }, 0);
}

$("filters").addEventListener("submit", applyFilters);
$("filters").addEventListener("reset", resetFilters);
$("team-form").addEventListener("submit", loadTeam);

loadOverview();
loadScorers();
loadMinutes();
