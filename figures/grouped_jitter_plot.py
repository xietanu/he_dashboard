"""A grouped jitter plot figure, for comparing institutions against each other."""
from plotly import graph_objects as go

from styles.colours import VisColours


def grouped_jitter_plot(
    dataframe,
    metrics_to_plot: list[str],
    name_column: str,
    selected_unis: list[str],
    metrics_column: str = "Metric",
    value_column: str = "Value",
):
    """A grouped jitter plot figure, for comparing institutions against each other across a range of metrics."""
    unselected_unis_df = dataframe[
        (dataframe[metrics_column].isin(metrics_to_plot))
        & (~dataframe[name_column].isin(selected_unis))
    ]

    fig = go.Figure()
    fig.add_trace(
        create_jitter_trace(
            unselected_unis_df,
            name_column,
            metrics_column,
            value_column,
            colour=VisColours.PRIMARY.value,
            opacity=0.4,
        )
    )

    for color, selected_uni in enumerate(selected_unis):
        selected_uni_df = dataframe[
            (dataframe[metrics_column].isin(metrics_to_plot))
            & (dataframe[name_column] == selected_uni)
        ]
        fig.add_trace(
            create_jitter_trace(
                selected_uni_df,
                name_column,
                metrics_column,
                value_column,
                colour=VisColours.COLOURFUL_SERIES.value[color + 1],
                opacity=1,
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


def create_jitter_trace(df, name_column, metrics_column, value_column, colour, opacity):
    return go.Box(
        x=df[value_column],
        y=df[metrics_column],
        text=df[name_column],
        marker={"color": colour, "opacity": opacity},
        jitter=1,
        boxpoints="all",
        fillcolor="rgba(0,0,0,0)",
        line={"width": 0},
        pointpos=0,
        orientation="h",
        hoveron="points",
        showlegend=False,
    )
