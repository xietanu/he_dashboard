"""Component that allows the user to select options from a pre-determined list"""
from dash import html, dcc


def dropdown(label, options, selected, element_id):
    """Component that allows the user to select options from a pre-determined list
    Must have default selection."""
    return html.Div(
        [
            html.Label(
                label,
                htmlFor=element_id,
            ),
            dcc.Dropdown(
                id=element_id,
                options=options,
                value=selected,
                clearable=False,
            ),
        ],
    )
