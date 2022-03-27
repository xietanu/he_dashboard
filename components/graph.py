"""Graph component to standardise display"""
from dash import dcc


def graph(figure, element_id: str, style: dict = None, **graph_kwargs) -> dcc.Graph:
    """
    Displays visualisations in a standard way.
    Sets a height if none given.

    Args:
        figure: A plotly figure to display.
        element_id (str): id to assign the graph element for targeting with callbacks.
        style (dict, optional): Any specific style to apply. Defaults to None.
        **graph_kwargs: Any additional keyword arguments to pass to dcc.Graph.

    Returns:
        dcc.Graph: The dash element containing the visualisation.
    """
    if style is None:
        style = {"height": "450px"}
    if "height" not in style:
        style["height"] = "450px"

    return dcc.Graph(
        figure=figure, id=element_id, style=style, responsive=True, **graph_kwargs
    )
