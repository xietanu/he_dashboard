from plotly import express as px

def timeseries(
    dataframe,
    xaxis,
    yaxis,
    group
):
    return px.line(
        dataframe,
        x = xaxis,
        y = yaxis,
        color = group
    )
