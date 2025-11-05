"""Inventory CSV files under the `db/` folder.

This script scans the `db/` directory for CSV files, attempts to read
each file with a few common encodings and separators, and produces
`db/inventory.csv` with a summary for each file.

Usage:
    python src/inventory.py

The output `db/inventory.csv` contains one row per file with these columns:
- filename, path, status (ok|error), rows, cols, total_missing,
- cols_with_missing, columns (JSON), dtypes (JSON), sample_head (string), error

"""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

import pandas as pd


DB_DIR = Path(__file__).resolve().parents[1] / "db"
INVENTORY_CSV = DB_DIR / "inventory.csv"


def find_candidate_csvs(db_dir: Path) -> List[Path]:
    """Return a list of files in db_dir that look like CSVs.

    We accept files whose name endswith '.csv' (case-insensitive).
    """
    files: List[Path] = []
    if not db_dir.exists():
        return files
    for p in db_dir.iterdir():
        if p.is_file() and p.name.lower().endswith(".csv"):
            files.append(p)
    return sorted(files)


def try_read_csv(path: Path) -> pd.DataFrame:
    """Try reading a CSV using several encodings and separators.

    Raises the last exception if all attempts fail.
    """
    encodings = ["utf-8", "latin1", "cp1252"]
    seps = [",", ";", "\t"]
    last_err: Optional[Exception] = None
    for enc in encodings:
        for sep in seps:
            try:
                # engine='python' is more tolerant with malformed CSVs
                df = pd.read_csv(path, encoding=enc, sep=sep, engine="python")
                return df
            except Exception as e:
                last_err = e
                continue
    raise last_err if last_err is not None else ValueError("Could not read CSV")


def summarize_df(df: pd.DataFrame) -> Dict[str, Any]:
    """Return a compact summary dict for a DataFrame.

    The returned dict contains rows, cols, column names, dtypes,
    missing counts and a small sample head as CSV string.
    """
    rows, cols = df.shape
    cols_list = list(map(str, df.columns.tolist()))
    dtypes = {str(col): str(dtype) for col, dtype in df.dtypes.items()}
    missing = df.isna().sum().to_dict()
    total_missing = int(sum(missing.values()))
    cols_with_missing = int(sum(1 for v in missing.values() if v > 0))
    # small sample head as CSV (up to 3 rows) - ensure no newlines break CSV
    try:
        sample = df.head(3).to_csv(index=False)
        sample = sample.replace("\n", "\\n")
    except Exception:
        sample = ""

    return {
        "rows": int(rows),
        "cols": int(cols),
        "columns": cols_list,
        "dtypes": dtypes,
        "total_missing": total_missing,
        "cols_with_missing": cols_with_missing,
        "sample_head": sample,
    }


def inventory_db(db_dir: Path) -> List[Dict[str, Any]]:
    results: List[Dict[str, Any]] = []
    candidates = find_candidate_csvs(db_dir)
    for p in candidates:
        row: Dict[str, Any] = {
            "filename": p.name,
            "path": str(p),
            "status": "error",
            "rows": None,
            "cols": None,
            "total_missing": None,
            "cols_with_missing": None,
            "columns": None,
            "dtypes": None,
            "sample_head": None,
            "error": None,
        }
        try:
            df = try_read_csv(p)
            summary = summarize_df(df)
            row.update({
                "status": "ok",
                "rows": summary["rows"],
                "cols": summary["cols"],
                "total_missing": summary["total_missing"],
                "cols_with_missing": summary["cols_with_missing"],
                "columns": json.dumps(summary["columns"], ensure_ascii=False),
                "dtypes": json.dumps(summary["dtypes"], ensure_ascii=False),
                "sample_head": summary["sample_head"],
            })
        except Exception as e:
            row["error"] = str(e)
        results.append(row)
    return results


def write_inventory(results: List[Dict[str, Any]], out_path: Path) -> None:
    if not out_path.parent.exists():
        out_path.parent.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(results)
    # ensure a stable column order
    cols = [
        "filename",
        "path",
        "status",
        "rows",
        "cols",
        "total_missing",
        "cols_with_missing",
        "columns",
        "dtypes",
        "sample_head",
        "error",
    ]
    df = df.reindex(columns=cols)
    df.to_csv(out_path, index=False)


def main() -> int:
    print(f"Scanning CSV files under: {DB_DIR}")
    results = inventory_db(DB_DIR)
    write_inventory(results, INVENTORY_CSV)
    print(f"Wrote inventory to: {INVENTORY_CSV}")
    ok_count = sum(1 for r in results if r.get("status") == "ok")
    err_count = len(results) - ok_count
    print(f"Files scanned: {len(results)} (ok={ok_count}, error={err_count})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
