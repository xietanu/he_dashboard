"""Creates a horizontal row used to contain cards."""
from dash import html


def card_row(cards: list[html.Div]) -> html.Div:
    """
    Creates a horizontal row used to contain cards. The card and card_row work together to create a
    layout that stretches and shrinks when the user changes the size of the window, or accesses the
    dashboard from a mobile device.

    Args:
        cards (list[html.Div]): List of card <div> elements

    Returns:
        html.Div: The card row element
    """
    return html.Div(
        cards,
        className="card_row",
    )
