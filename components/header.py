"""Header component for top of page"""
from dash import html


def header(title: str) -> html.Div:
    """
    Creates a header for the top of the page with the specified title.

    Args:
        title (str): The page title

    Returns:
        html.Header: The Header element
    """
    return html.Header(
        [html.Div([html.H1(title, className="header_title")], className="header_flex")],
        className="header_container",
    )
