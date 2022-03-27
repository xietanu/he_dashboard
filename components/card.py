"""Card component for containing dashboard elements"""
from dash import html


def card(children: list, element_id: str = None) -> html.Div:
    """
    A rectangle with an off-white background.
    Used to wrap individual elements of a dashboard.

    Args:
        children (list): HTML elements making up the content of the card.
        element_id (str, optional): id to assign to card for targeting with react elements.
            Defaults to None.

    Returns:
        html.Div: The card HTML element
    """
    if element_id:
        return html.Div(children, className="card", id=element_id)
    return html.Div(children, className="card")
