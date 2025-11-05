"""Utilities for loading and cleaning tabular data from `db/`.

Functions:
- load_csv(path_or_name) -> pd.DataFrame
- summarize_df(df, top=5) -> dict
- clean_df(df, drop_duplicates=True, fillna=None) -> pd.DataFrame

This module is intentionally small and documented so you can follow the
implementation step-by-step for learning purposes.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Optional

import pandas as pd


DB_DIR = Path(__file__).resolve().parents[1] / "db"


def load_csv(path_or_name: str | Path, verbose: bool = False) -> pd.DataFrame:
    """Load a CSV (or Excel) file from disk.

    The function accepts a filename (relative to `db/`) or an absolute path.
    It will try several encodings and separators for CSVs. If the file looks
    like Excel (xlsx/xls) it will use `pd.read_excel`.

    Raises any exception from pandas if reading fails.
    """
    p = Path(path_or_name)
    if not p.is_absolute():
        p = DB_DIR / p

    if not p.exists():
        raise FileNotFoundError(f"File not found: {p}")

    suffix = p.suffix.lower()
    if suffix in (".xlsx", ".xls") or p.name.lower().endswith(".xlsx"):
        if verbose:
            print(f"Reading Excel: {p}")
        return pd.read_excel(p)

    # For CSV-like files, try common encodings/separators
    encodings = ["utf-8", "latin1", "cp1252"]
    seps = [",", ";", "\t"]
    last_err: Optional[Exception] = None
    for enc in encodings:
        for sep in seps:
            try:
                if verbose:
                    print(f"Trying read_csv(path={p}, encoding={enc}, sep={sep})")
                df = pd.read_csv(p, encoding=enc, sep=sep, engine="python")
                return df
            except Exception as e:
                last_err = e
                continue

    # If we reached here, we could not read it
    raise last_err if last_err is not None else ValueError("Could not read file")


def summarize_df(df: pd.DataFrame, top: int = 5) -> Dict[str, Any]:
    """Return a summary dictionary for a DataFrame.

    Keys include: rows, cols, columns, dtypes, missing (per column),
    total_missing, cols_with_missing, describe (numeric), top_values (per column)
    """
    rows, cols = df.shape
    columns = list(map(str, df.columns.tolist()))
    dtypes = {str(c): str(dt) for c, dt in df.dtypes.items()}
    missing = df.isna().sum().to_dict()
    total_missing = int(sum(missing.values()))
    cols_with_missing = int(sum(1 for v in missing.values() if v > 0))

    # numeric description
    describe = df.describe(include=["number"]).to_dict()

    # top values for object / categorical columns
    top_values = {}
    for col in df.columns:
        try:
            vc = df[col].value_counts(dropna=False).head(top).to_dict()
            top_values[str(col)] = vc
        except Exception:
            top_values[str(col)] = {}

    # quantiles (25, 50, 75) for numeric
    # compute quantiles per numeric column to avoid issues when object
    # blocks cause DataFrame.quantile to fail on mixed-type internals
    quantiles = {}
    for col in df.select_dtypes(include=["number"]).columns:
        try:
            q = df[col].quantile([0.25, 0.5, 0.75]).to_dict()
            quantiles[str(col)] = q
        except Exception:
            quantiles[str(col)] = {}

    return {
        "rows": int(rows),
        "cols": int(cols),
        "columns": columns,
        "dtypes": dtypes,
        "missing": missing,
        "total_missing": total_missing,
        "cols_with_missing": cols_with_missing,
        "describe": describe,
        "top_values": top_values,
        "quantiles": quantiles,
    }


def clean_df(
    df: pd.DataFrame,
    drop_duplicates: bool = True,
    fillna: Optional[Dict[str, Any]] = None,
    strip_strings: bool = True,
) -> pd.DataFrame:
    """Perform lightweight cleaning:

    - Optionally drop duplicate rows.
    - Optionally fill NA values using `fillna` mapping or a scalar.
    - Optionally strip string columns of leading/trailing whitespace.

    Returns a new DataFrame (does not modify the input in place).
    """
    out = df.copy()
    if drop_duplicates:
        out = out.drop_duplicates()

    if strip_strings:
        for col in out.select_dtypes(include=["object"]).columns:
            try:
                out[col] = out[col].astype(str).str.strip()
            except Exception:
                # ignore columns that cannot be converted to str
                pass

    if fillna is not None:
        out = out.fillna(fillna)

    return out


if __name__ == "__main__":
    # small demo when run directly
    print("Demo: scanning db/ for CSV files...")
    from pprint import pprint

    for p in sorted(DB_DIR.glob("*.*")):
        print(p.name)
    print("Use load_csv('yourfile.csv') to load a file from db/")
