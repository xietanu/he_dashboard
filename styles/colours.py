"""Enums for the colours used across the dashboard"""
from enum import Enum


class DashboardColours(Enum):
    """The primary colours used in the dashboard"""

    PRIMARY = "#141B41"
    SECONDARY = "#2D7DD2"
    CONTRAST = "#EFF1F3"
    HIGHLIGHT = "#FF7F11"
    WARNING = "#FF1B1C"

class VisColours(Enum):
    """Colours to be used in visualisation in the dashboard"""

    PRIMARY = "#2D7DD2"
    COLOURFUL_SERIES = ["#2D7DD2","#3DDC97","#F5B841","#FF495C"]
