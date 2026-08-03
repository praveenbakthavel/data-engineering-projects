import pandas as pd

from marketing_analytics_pipeline.validate import validate_metrics, validate_schema


def test_marketing_schema_validation():
    df = pd.DataFrame(
        {
            "event_date": ["2026-08-01"],
            "channel": ["search"],
            "campaign": ["brand"],
            "sessions": [100],
            "leads": [10],
            "conversions": [2],
            "spend": [500],
        }
    )

    validate_schema(df)
    validate_metrics(df)
