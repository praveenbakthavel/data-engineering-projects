import pandas as pd


def prepare_campaign_data(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result["conversion_rate"] = (
        result["conversions"] / result["sessions"].replace(0, pd.NA)
    )
    result["cost_per_lead"] = result["spend"] / result["leads"].replace(0, pd.NA)
    return result
