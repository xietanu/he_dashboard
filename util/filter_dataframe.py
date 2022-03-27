"""filter_dataframe function"""
from typing import Union

from pandas import DataFrame


def filter_dataframe(
    dataframe: DataFrame,
    column: str,
    values: Union[str, list[str]],
    invert_selection: bool = False,
) -> DataFrame:
    """
    Filter dataframe, looking in column for given value.
    Can provide inverted selection if desired.

    Args:
        dataframe (DataFrame): The dataframe to filter.
        column (str): The label of the column to use.
        values (Union[str, list[str]]): Either single value or list of values to filter by.
        invert_selection (bool, optional): Whether to invert the selection. Defaults to False.

    Returns:
        DataFrame: Filtered dataframe.
    """
    if isinstance(values, str):
        values = [values]

    return (
        dataframe[~dataframe[column].isin(values)].copy()
        if invert_selection
        else dataframe[dataframe[column].isin(values)].copy()
    )
