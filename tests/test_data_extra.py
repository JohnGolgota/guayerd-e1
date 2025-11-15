import os
import pandas as pd
from pathlib import Path
import tempfile

from src import data


def test_load_csv_with_absolute_path(tmp_path):
    # crear CSV con separador ',' y encoding utf-8
    p = tmp_path / "ventas_test.csv"
    content = "id,value\n1,10\n2,20\n"
    p.write_text(content, encoding="utf-8")

    df = data.load_csv(str(p))
    assert df.shape == (2, 2)
    assert list(df.columns) == ["id", "value"]


def test_load_csv_file_not_found():
    fake = Path("/this/path/does/not/exist.csv")
    try:
        data.load_csv(str(fake))
        assert False, "Expected FileNotFoundError"
    except FileNotFoundError:
        assert True


def test_summarize_and_clean_integration():
    df = pd.DataFrame(
        {
            "a": [1, 2, 2, None],
            "b": ["x ", " y", " y", "z"],
        }
    )
    cleaned = data.clean_df(df, drop_duplicates=True, fillna={"a": 0}, strip_strings=True)
    summary = data.summarize_df(cleaned)

    # after cleaning, duplicates removed -> 3 rows (one duplicate removed)
    assert summary["rows"] == 3
    # no missing after fillna
    assert summary["total_missing"] == 0
    # check stripped values (no trailing spaces)
    assert cleaned["b"].str.contains(" ").sum() == 0
