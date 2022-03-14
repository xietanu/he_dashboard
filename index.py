"""
Index outlining the dashboard's layout and links to pages.
"""

from dash import dcc, html, Input, Output
import pandas as pd

from app import app
from components.header import header
from components.nav_sidebar import generate_nav_sidebar
from pages.he_performance_indicators import he_performance_indicators
from pages.student_enrolments_timeseries import student_enrolment_timeseries

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
                dcc.Location(id="url", refresh=False),
                html.Div([], id="page-content", className="page_content"),
            ],
            className="main_content_box",
        ),
    ]
)


@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname"),
    Input("url", "search"),
)
def display_page(pathname, query_string):
    """Show the user the correct page for the given path"""
    try:
        paths = {
            "/": {
                "page": lambda: student_enrolment_timeseries(),
            },
            "/student-enrolment-timeseries": {
                "title": "Student enrolments",
                "page": lambda: student_enrolment_timeseries(),
            },
            "/HE-performance-indicators": {
                "title": "HE performance indicators",
                "page": lambda: he_performance_indicators(),
            },
        }

        for path, route in paths.items():
            if pathname == path:
                return [
                    html.Div(
                        [
                            generate_nav_sidebar(paths, path),
                            route["page"](),
                        ],
                        className="dashboard_container",
                    ),
                ]

    except Exception as exception:
        raise exception

    page_not_found = "404"
    return [page_not_found]
