from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
PLAYERS_FILE = DATA_DIR / "players.csv"
TEAMS_FILE = DATA_DIR / "teams.csv"


def _load_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(
            f"Missing dataset: {path}. See data/README.md for setup instructions."
        )
    return pd.read_csv(path)


def load_players() -> pd.DataFrame:
    return _load_csv(PLAYERS_FILE)


def load_teams() -> pd.DataFrame:
    return _load_csv(TEAMS_FILE)
