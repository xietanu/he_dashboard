"""HEData and HEDataColumn classes"""
from enum import Enum
from typing import Union
from pandas import DataFrame

from util.filter_dataframe import filter_dataframe


class HEDataColumn(Enum):
    """Standard columns to apply to HEData"""

    ACADEMIC_YEAR = "Academic year"
    PROVIDER_NAME = "HE provider"
    METRIC = "Metric"
    VALUE = "Value"


class HEData:
    """Wrapper class for a DataFrame to standardise how it is accessed."""

    def __init__(
        self,
        dataframe: DataFrame,
        column_lookup: dict,
    ) -> None:
        self.dataframe = dataframe.reset_index().copy()
        self.dataframe.rename(
            inplace=True,
            columns=column_lookup,
        )

    def get_dataframe(
        self,
        academic_years: Union[str, list[str]] = None,
        metrics: Union[str, list[str]] = None,
        providers: Union[str, list[str]] = None,
        invert_univerities_selection: bool = False,
    ) -> DataFrame:
        """
        Get the dataframe associated with the HEData.
        May be filtered by HE provider, metric or academic year.

        Args:
            academic_years (str | list[str], optional): Academic years to filter to.
                Defaults to None.
            metrics (str | list[str], optional): Metrics to filter down to. Defaults to None.
            providers (str | list[str]] optional): HE providers to filter to. Defaults to None.
            invert_univerities_selection (bool, optional): Whether to return
                non-selected universities. Defaults to False.

        Returns:
            DataFrame: The filtered dataframe.
        """
        output_df = self.dataframe.copy()

        if providers:
            output_df = filter_dataframe(
                output_df,
                HEDataColumn.PROVIDER_NAME.value,
                providers,
                invert_univerities_selection,
            )

        if academic_years:
            output_df = filter_dataframe(
                output_df, HEDataColumn.ACADEMIC_YEAR.value, academic_years
            )

        if metrics:
            output_df = filter_dataframe(output_df, HEDataColumn.METRIC.value, metrics)

        return output_df

    def get_dataframe_wide(
        self,
        academic_years: Union[str, list[str]] = None,
        metrics: Union[str, list[str]] = None,
        providers: Union[str, list[str]] = None,
        invert_univerities_selection: bool = False,
    ):
        """
        Get filtered dataframe formatted in a wide format, with metrics converted to columns.

        Args:
            academic_years (str | list[str], optional): Academic years to filter to.
                Defaults to None.
            metrics (str | list[str], optional): Metrics to filter down to. Defaults to None.
            providers (str | list[str]] optional): HE providers to filter to. Defaults to None.
            invert_univerities_selection (bool, optional): Whether to return
                non-selected universities. Defaults to False.

        Returns:
            DataFrame: The filtered dataframe.
        """
        output_df = self.get_dataframe(
            academic_years, metrics, providers, invert_univerities_selection
        )

        indexes = [
            column
            for column in [
                HEDataColumn.ACADEMIC_YEAR.value,
                HEDataColumn.PROVIDER_NAME.value,
            ]
            if column in output_df.columns
        ]

        return output_df.pivot(
            index=indexes,
            columns=HEDataColumn.METRIC.value,
            value=HEDataColumn.VALUE.value,
        ).reset_index()
