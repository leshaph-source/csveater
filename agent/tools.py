import pandas as pd
import numpy as np


def load_dataset(filepath):
    """
    Загрузка CSV или Excel.
    """

    if filepath.endswith(".csv"):
        df = pd.read_csv(filepath)
    else:
        df = pd.read_excel(filepath)

    return df


def basic_eda(df):
    """
    Сбор статистики по датасету.
    """

    report = {}

    report["rows"] = len(df)
    report["columns"] = len(df.columns)

    report["column_names"] = list(df.columns)

    report["dtypes"] = {
        col: str(dtype)
        for col, dtype in df.dtypes.items()
    }

    report["missing_values"] = (
        df.isnull()
        .sum()
        .to_dict()
    )

    report["duplicates"] = int(df.duplicated().sum())

    numeric_df = df.select_dtypes(
        include=np.number
    )

    if not numeric_df.empty:
        report["describe"] = (
            numeric_df.describe()
            .to_dict()
        )

        report["correlation"] = (
            numeric_df.corr(
                numeric_only=True
            )
            .round(3)
            .to_dict()
        )

    return report
