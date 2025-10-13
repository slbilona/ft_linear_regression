import pandas as pd
from pathlib import Path


def load(path: str):
    if not isinstance(path, str):
        return None
    ext = Path(path).suffix.lower()
    if ext not in [".csv"]:
        return None
    if not Path(path).exists():
        return None
    df = pd.read_csv(path)
    print("Loading dataset of dimensions", df.shape)
    return df
