from typing import Dict
import pandas as pd

def clear_columns_names(data: pd.DataFrame) -> pd.DataFrame:
    data.columns = [col.replace("_", "").replace(" ", "") for col in data.columns]
    return data

def fix_data_schema(data: pd.DataFrame, schema: Dict[str, str]) -> pd.DataFrame:
    assert all(
        [i in data.columns for i in schema.keys()]
    ), "All fields in schema must be in the columns."

    assert all(
        [i in schema.keys() for i in data.columns]
    ), "All fields in data must be in his schema definition."
    float_cols = []
    for element, data_type in schema.items():
        if data_type.lower() == "numeric":
            float_cols.append(element)

    data[float_cols] = data[float_cols].apply(pd.to_numeric, errors="coerce")

    return data