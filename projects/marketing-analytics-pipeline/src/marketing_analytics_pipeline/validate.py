import pandas as pd

from .schema import REQUIRED_COLUMNS


def validate_schema(df: pd.DataFrame) -> None:
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")


def validate_metrics(df: pd.DataFrame) -> None:
    numeric_columns = ["sessions", "leads", "conversions", "spend"]
    if (df[numeric_columns] < 0).any().any():
        raise ValueError("Metrics cannot contain negative values")
