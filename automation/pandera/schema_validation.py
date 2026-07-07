import pandas as pd
import pandera as pa


def validate_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    schema = pa.DataFrameSchema({
        'id': pa.Column(pa.Int, nullable=False),
        'value': pa.Column(pa.Float, nullable=True),
    })
    return schema.validate(df)
