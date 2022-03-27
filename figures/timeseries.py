"""timeseries function"""
from pandas import DataFrame
from plotly import express as px
from plotly import graph_objects

from styles.colours import VisColours


def timeseries(
    dataframe: DataFrame, xaxis_column: str, yaxis_column: str, group_column: str
) -> graph_objects.Figure:
    """
    Creates plotly express timeseries chart, with specified value.

    Args:
        dataframe (DataFrame): Dataframe used to populate the chart.
        xaxis_column (str): Column to use for the x axis
        yaxis_column (str): Column to use for the y axis
        group_column (str): Column to use for the grouping for different lines.

    Returns:
        graph_objects.Figure: Timeseries figure.
    """
    fig = px.line(
        dataframe,
        x=xaxis_column,
        y=yaxis_column,
        color=group_column,
        color_discrete_sequence=VisColours.COLOURFUL_SERIES.value,
    )

    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")

    return fig
