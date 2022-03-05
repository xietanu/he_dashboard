from plotly import express as px

from styles.colours import VisColours

def timeseries(
    dataframe,
    xaxis,
    yaxis,
    group
):
    fig = px.line(
        dataframe,
        x = xaxis,
        y = yaxis,
        color = group,
        color_discrete_sequence=VisColours.COLOURFUL_SERIES.value,
    )

    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")

    return fig
