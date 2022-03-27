"""add_z_score"""
from pandas import DataFrame


def add_z_score(dataframe: DataFrame, column: str, z_column_name: str) -> None:
    """Add a z-scored version of a column to the specified dataframe"""
    dataframe[z_column_name] = (
        dataframe[column] - dataframe[column].mean()
    ) / dataframe[column].std(ddof=0)
