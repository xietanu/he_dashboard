"""
A row with a card for containing filters.
"""
from logging import Filter
from components.card_row import card_row
from components.card import card


def filter_panel(children: list):
    """
    A dedicated card for displaying filters

    Args:
        children (list): List of HTML elements for filters or other elements to include.

    Returns:
        HTML.div: The card row containing the filter panel card.
    """
    return card_row(
        card(
            [
                "Select from the following filters:",
            ]
            + children,
            element_id="filter-panel",
        )
    )
