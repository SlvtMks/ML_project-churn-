import pandas as pd


def add_total_charges_numeric(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["TotalCharges_num"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    return df


def add_churn_binary(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Churn_binary"] = df["Churn"].map({"No": 0, "Yes": 1})
    return df


def prepare_modeling_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["TotalCharges_num"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df["Churn_binary"] = df["Churn"].map({"No": 0, "Yes": 1})

    df = df.drop(columns=["customerID", "TotalCharges", "Churn"])
    df = df.dropna(subset=["TotalCharges_num"]).copy()

    return df
