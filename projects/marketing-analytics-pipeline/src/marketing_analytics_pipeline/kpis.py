import pandas as pd


def campaign_kpi_summary(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("channel", as_index=False)
        .agg(
            sessions=("sessions", "sum"),
            leads=("leads", "sum"),
            conversions=("conversions", "sum"),
            spend=("spend", "sum"),
        )
        .assign(
            conversion_rate=lambda x: x["conversions"] / x["sessions"],
            cost_per_lead=lambda x: x["spend"] / x["leads"],
        )
    )
