"""Component that allows the user to select options from a pre-determined list"""
from dash import html, dcc
from components.filter import Filter


class Dropdown(Filter):
    """Component that allows the user to select options from a pre-determined list
    Must have default selection."""

    def __init__(
        self,
        title: str,
        filter_id: str,
        options: list,
        default_value: str,
    ):
        super().__init__(title, filter_id, default_value)
        self.options = options

    def to_html(self, selected_value: str = None):
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
