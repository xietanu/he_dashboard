"""add_z_score"""
from pandas import DataFrame


def add_z_score(df: DataFrame, column: str, z_column_name: str) -> None:
    """Add a z-scored version of a column to the specified dataframe"""
    df[z_column_name] = (df[column] - df[column].mean()) / df[column].std(ddof=0)
