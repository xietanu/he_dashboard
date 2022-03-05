"""Card component for containing dashboard elements"""
from dash import html


def card(children: list, element_id: str = None) -> html.Div:
    """A rectangle with an off-white background.
    Used to wrap individual elements of a dashboard"""
    if element_id:
        return html.Div(children, className="card", id=element_id)
    return html.Div(children, className="card")
