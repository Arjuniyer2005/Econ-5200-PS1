"""Utilities for auditing basket-value data and computing robust summary measures."""

import numpy as np
import pandas as pd
from scipy import stats
from typing import Sequence


def audit_report(df: pd.DataFrame) -> pd.DataFrame:
    """Return missingness, dtype, skew, and IQR-based outlier count for each column."""
    rows = []

    for col in df.columns:
        series = df[col]

        missingness = series.isna().sum()
        dtype = series.dtype

        if pd.api.types.is_numeric_dtype(series):
            clean = series.dropna()
            skew = clean.skew()

            q1 = clean.quantile(0.25)
            q3 = clean.quantile(0.75)
            iqr = q3 - q1

            lower = q1 - 1.5 * iqr
            upper = q3 + 1.5 * iqr

            outlier_count = ((clean < lower) | (clean > upper)).sum()
        else:
            skew = np.nan
            outlier_count = np.nan

        rows.append({
            "column": col,
            "missingness": missingness,
            "dtype": str(dtype),
            "skew": skew,
            "outlier_count": outlier_count
        })

    return pd.DataFrame(rows).set_index("column")


def robust_mean(x: Sequence[float], method: str = "median") -> float:
    """Return a robust centre using median, trimmed mean, or B2B exclusion."""
    x = pd.Series(x).dropna()

    if method == "median":
        return float(x.median())

    if method == "trimmed":
        return float(stats.trim_mean(x, 0.1))

    if method == "rule":
        b2b_cutoff = 1000
        return float(x[x < b2b_cutoff].mean())

    raise ValueError("method must be 'median', 'trimmed', or 'rule'")


if __name__ == "__main__":
    demo = pd.DataFrame({
        "basket_value": [40, 45, 50, 55, 60, 5000]
    })

    print("Audit report:")
    print(audit_report(demo))

    print("\nMedian:")
    print(robust_mean(demo["basket_value"], method="median"))

    print("\nTrimmed mean:")
    print(robust_mean(demo["basket_value"], method="trimmed"))

    print("\nMean after B2B exclusion:")
    print(robust_mean(demo["basket_value"], method="rule"))
