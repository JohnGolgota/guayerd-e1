import pandas as pd

from src import data


def test_summarize_df_basic():
    df = pd.DataFrame({
        "a": [1, 2, 2, None],
        "b": [" x", "y", "y", "z"],
    })

    summary = data.summarize_df(df)

    assert summary["rows"] == 4
    assert summary["cols"] == 2
    # one missing value in column 'a'
    assert summary["total_missing"] == 1
    assert summary["cols_with_missing"] == 1
    assert "a" in summary["dtypes"]

    # check quantiles for column 'a' (non-NaN values: [1,2,2])
    q = summary["quantiles"]["a"]
    # pandas may return floats; check expected keys
    assert 0.5 in q and 0.25 in q and 0.75 in q
    assert q[0.5] == 2.0


def test_clean_df_behavior():
    df = pd.DataFrame(
        [
            {"a": 1, "b": " x "},
            {"a": 1, "b": " x "},
            {"a": None, "b": " z "},
        ]
    )

    # default drop_duplicates True and strip_strings True
    cleaned = data.clean_df(df, drop_duplicates=True, fillna={"a": 0}, strip_strings=True)

    # duplicates removed -> original 3 rows become 2
    assert cleaned.shape[0] == 2

    # fillna applied
    assert cleaned["a"].isna().sum() == 0

    # string columns stripped
    assert cleaned["b"].iloc[0] == "x"
