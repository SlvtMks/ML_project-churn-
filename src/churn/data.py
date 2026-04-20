from pathlib import Path

import pandas as pd


def load_dataset() -> pd.DataFrame:
    candidate_paths = [
        Path("data/WA_Fn-UseC_-Telco-Customer-Churn.csv"),
        Path("../data/WA_Fn-UseC_-Telco-Customer-Churn.csv"),
    ]

    data_path = next((path for path in candidate_paths if path.exists()), None)

    if data_path is None:
        raise FileNotFoundError("CSV file not found in project data/ directory.")

    return pd.read_csv(data_path)
