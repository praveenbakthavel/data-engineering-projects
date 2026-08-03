from pathlib import Path

import pandas as pd


def read_marketing_csv(path: str | Path) -> pd.DataFrame:
    """Read raw marketing campaign data."""
    return pd.read_csv(path)
