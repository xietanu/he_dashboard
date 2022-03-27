"""Component that allows the user to select options from a pre-determined list"""
from dash import html, dcc
from components.filter import Filter


class Dropdown(Filter):
    """
    A filter that allows the user to select options from a pre-determined list.
    """

    def __init__(
        self,
        title: str,
        filter_id: str,
        options: list,
        default_value: str = None,
    ):
        """
        Args:
            title (str): Label to use for the filter
            filter_id (str): Variable name to be used for the filter.
            options (list): List of pre-determined options for the user to pick from.
            default_value (str, optional): Default option to be selected. Defaults to None.
        """
        super().__init__(title, filter_id, default_value)
        self.options = options

    def to_html(self, selected_value: str = None) -> html.Div:
        """
        Returns a HTML dropdown representing the filter for the user to select an option from.

        Args:
            selected_value (str, optional): Currently selected option. Defaults to None.

        Returns:
            html.Div: The HTML element reprsenting the filter
        """
        if selected_value is None:
            selected_value = self.default_value

        return html.Div(
            [
                html.Label(
                    self.title,
                    htmlFor=self.filter_id,
                ),
                dcc.Dropdown(
                    id=self.filter_id,
                    options=self.options,
                    value=selected_value,
                    clearable=False,
                ),
            ],
        )
