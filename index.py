"""
Create paths to serve different dashboards.  Add new paths in the display_page callback.
"""
from dash import dcc, html
import pandas as pd

from app import app


data = {
    "Category": ["Category 1", "Category 2", "Category 3"],
    "Value": [30, 15, 20],
}
df = pd.DataFrame(data)

app.title = "Higher Education in the UK"

app.layout = html.Div(
    [
        html.Div([app.title]),
        html.Div(
            [
                html.Div(
                    [
                        dcc.Location(id="url", refresh=False),
                        html.Div(["Content goes here"], id="page-content"),
                    ],
                )
            ],
        ),
    ]
)
