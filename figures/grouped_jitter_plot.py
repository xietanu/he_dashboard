"""A grouped jitter plot figure, for comparing institutions against each other."""
from plotly import graph_objects as go

from styles.colours import VisColours


def grouped_jitter_plot(
    dataframe,
    metrics_to_plot: list[str],
    name_column: str,
    metrics_column: str = "Metric",
    value_column: str = "Value",
):
    """A grouped jitter plot figure, for comparing institutions against each other across a range of metrics."""
    dataframe = dataframe[dataframe[metrics_column].isin(metrics_to_plot)]

    fig = go.Figure()
    fig.add_trace(
        go.Box(
            x=dataframe[value_column],
            y=dataframe[metrics_column],
            jitter=1,
            boxpoints="all",
            fillcolor="rgba(0,0,0,0)",
            line={"width": 0},
            pointpos=0,
            orientation="h",
            text=dataframe[name_column],
            marker={"color": VisColours.PRIMARY.value, "opacity": 0.4},
            hoveron="points",
        )
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
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
