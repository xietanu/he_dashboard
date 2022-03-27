"""Wrapper for the main content of the dashboard, containing visualisations."""
from dash import html


def main(children: list) -> html.Main:
    """
    Wrapper for the main content of the dashboard, containing visualisations.

    Args:
        children (list): List of the elements contained on the page. Usually card rows.

    Returns:
        html.Main: The HTML <main> element.
    """
    return html.Main(children, className="main", id="main-content", role="main")
