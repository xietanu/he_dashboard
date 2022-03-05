"""
Index outlining the dashboard's layout and links to pages.
"""
from dash import dcc, html
import pandas as pd

from app import app
from components.header import header

data = {
    "Category": ["Category 1", "Category 2", "Category 3"],
    "Value": [30, 15, 20],
}
df = pd.DataFrame(data)

app.title = "Higher Education in the UK"

app.layout = html.Div(
    [
        header(app.title),
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
