import io
import pandas as pd
import contextlib


def load_dataset(filepath):

    if filepath.endswith(".csv"):
        return pd.read_csv(filepath)

    return pd.read_excel(filepath)


def execute_python(code: str, df):

    local_vars = {
        "df": df,
        "pd": pd
    }

    buffer = io.StringIO()

    try:

        with contextlib.redirect_stdout(buffer):

            exec(code, {}, local_vars)

        output = buffer.getvalue()

        if not output:
            output = "Code executed successfully."

        return output

    except Exception as e:
        return f"ERROR: {str(e)}"
