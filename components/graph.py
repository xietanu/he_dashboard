"""Graph component to standardise display"""
from dash import dcc


def graph(figure, element_id: str, style: dict = None) -> dcc.Graph:
    """Graph component to standardise display
    Sets a default height if one not given."""
    if style is None:
        style = {"height": "450px"}
    if "height" not in style:
        style["height"] = "450px"

    return dcc.Graph(figure=figure, id=element_id, style=style, responsive=True)
