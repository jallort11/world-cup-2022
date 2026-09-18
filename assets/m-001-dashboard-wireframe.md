# M-001 — Dashboard wireframe (Binding)

Single page at `/dashboard`. Desktop-first, readable at 360px. No login.

```text
+------------------------------------------------------------------+
| WORLD CUP 2022                                                   |
| Tournament dashboard                                             |
| [API docs]                                                       |
+------------------------------------------------------------------+
| Overview: N players loaded · N teams loaded                      |
+------------------------------------------------------------------+
| Filters                                                          |
| Limit [ 10 ]  Scorers sort [ goals v ]  Minutes team [      ]    |
| [Apply]  [Reset]                                                 |
+------------------------------------------------------------------+
| TOP SCORERS                          source: GET /players/top-scorers |
| [======= bar chart, one bar per player =======]                  |
| table: player | team | goals | assists                           |
+------------------------------------------------------------------+
| MOST MINUTES                         source: GET /players/most-played |
| [======= bar chart, one bar per player =======]                  |
| table: player | team | minutes                                   |
+------------------------------------------------------------------+
| TEAM PROFILE                         source: GET /teams/{team}   |
| Team name [ Argentina ] [Look up]                                |
| cards: players | total goals | total assists | avg age | top scorer |
+------------------------------------------------------------------+
```

**Must preserve**

- Page title identifies the tournament and that this is a dashboard.
- Each visualization names its API source.
- Shared filters drive top-scorers and most-played.
- Team profile has its own lookup field and button.
- Every chart has a data table under it.
- Loading, error, and empty copy appear in the section they belong to — never a blank panel.
