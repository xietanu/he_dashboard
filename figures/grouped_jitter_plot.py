"""A grouped jitter plot figure, for comparing institutions against each other."""
from pandas import DataFrame
from plotly import graph_objects as go

from styles.colours import VisColours
from util.he_data import HEData, HEDataColumn


def grouped_jitter_plot(
    data: HEData,
    metrics_to_plot: list[str],
    selected_unis: list[str],
):
    """
    Creates a grouped jitter plot visualisation, plotting how universities compare across
    a range of metrics specified.

    Args:
        data (HEData): The data used to inform the plot.
        metrics_to_plot (list[str]): A list of the metrics to display.
        selected_unis (list[str]): Selected HE providers to highlight.

    Returns:
        graph_objects.Figure: Figure containing the jitter plot.
    """
    unselected_unis_df = data.get_dataframe(
        metrics=metrics_to_plot,
        providers=selected_unis,
        invert_univerities_selection=True,
    )

    fig = go.Figure()

    fig.add_trace(
        create_jitter_trace(
            unselected_unis_df,
            marker={
                "color": VisColours.PRIMARY.value,
                "opacity": 0.4,
            },
        )
    )

    for color, selected_uni in enumerate(selected_unis, 1):
        selected_uni_df = data.get_dataframe(
            metrics=metrics_to_plot, providers=selected_uni
        )
        fig.add_trace(
            create_jitter_trace(
                selected_uni_df,
                marker={
                    "color": VisColours.COLOURFUL_SERIES.value[color],
                    "opacity": 1,
                    "size": 10,
                    "line": {"width": 2, "color": "black"},
                },
            )
        )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis={"showgrid": False},
        yaxis={"showgrid": False},
    )

    fig.add_vrect(
        x0=-1,
        x1=1,
        fillcolor=VisColours.SHADE.value,
        opacity=0.1,
        layer="below",
        line_width=0,
    )

    return fig


def create_jitter_trace(
    dataframe: DataFrame,
    marker: dict,
):
    """
    Creates a jitter plot trace for adding to the overall figure with data
    from specified dataframe.

    Args:
        dataframe (DataFrame): Dataframe from HEData containing data to plot.
        marker (dict): Dictionary of formatting to use for the dot markers.

    Returns:
        graph_objects.Box: Box plot trace showing just undering data.
    """
    return go.Box(
        x=dataframe[HEDataColumn.VALUE.value],
        y=dataframe[HEDataColumn.METRIC.value],
        text=dataframe[HEDataColumn.PROVIDER_NAME.value],
        marker=marker,
        jitter=1,
        boxpoints="all",
        fillcolor="rgba(0,0,0,0)",
        line={"width": 0},
        pointpos=0,
        orientation="h",
        hoveron="points",
        showlegend=False,
    )
