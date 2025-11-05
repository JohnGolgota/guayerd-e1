"""Small plotting helpers using matplotlib / seaborn for notebooks.

Functions return the Matplotlib Figure so notebooks can display or further
customize the plots.
"""
from __future__ import annotations

from typing import Optional

import matplotlib.pyplot as plt
import seaborn as sns


def plot_hist(df, column: str, bins: int = 30, figsize=(8, 4)):
    """Plot a histogram for a numeric column and return the Figure."""
    fig, ax = plt.subplots(figsize=figsize)
    sns.histplot(df[column].dropna(), bins=bins, ax=ax, kde=True)
    ax.set_title(f"Histograma: {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Frecuencia")
    plt.tight_layout()
    return fig


def plot_box(df, column: str, figsize=(6, 4)):
    """Plot a boxplot for a numeric column and return the Figure."""
    fig, ax = plt.subplots(figsize=figsize)
    sns.boxplot(x=df[column], ax=ax)
    ax.set_title(f"Boxplot: {column}")
    plt.tight_layout()
    return fig


def plot_count(df, column: str, top: Optional[int] = 10, figsize=(8, 4)):
    """Plot a bar chart of value counts for a column (top N)."""
    vc = df[column].value_counts(dropna=False).head(top)
    fig, ax = plt.subplots(figsize=figsize)
    sns.barplot(x=vc.values, y=vc.index, ax=ax)
    ax.set_xlabel("Count")
    ax.set_ylabel(column)
    ax.set_title(f"Conteo por valor: {column}")
    plt.tight_layout()
    return fig
