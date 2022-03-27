"""Filter class for users to specify the data they want to see"""
from dash import html


class Filter:
    """
    A Filter is used by the dashboard to get information from users
    to specify what data to display.

    This is a generic parent class for types of filtes to be built off of.
    """

    def __init__(self, title: str, filter_id: str, default_value: str = None) -> None:
        """
        Args:
            title (str): Label for the filter to display to the user
            filter_id (str): Internal variable used to identify the filter
            default_value (str): Any default value to use before the user has made a selection.
                Defaults to None.
        """
        self.title = title
        self.filter_id = filter_id
        self.default_value = default_value

    def to_html(self, selected_value: str = None) -> html.Div:
        """
        Creates a HTML representation of the filter.

        Dummy function to be built on top of for child classes.

        Args:
            selected_value (str, optional): Currently selected value. Defaults to None.

        Returns:
            html.Div: The HTML element representing the filter.
        """
        return html.Div([selected_value])
