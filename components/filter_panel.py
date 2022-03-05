"""
A row with a card for containing filters.
"""
from components.card_row import card_row
from components.card import card


def filter_panel(children):
    """
    A row with a card for containing filters (e.g. dropdowns).
    """
    return card_row(
        card(
            [
                "Select from the following filters:",
            ]
            + children
        )
    )
