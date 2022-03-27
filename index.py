"""
Index outlining the dashboard's layout and links to pages.
"""

from dash import dcc, html, Input, Output, State
import pandas as pd

from app import app
from components.card import card
from components.card_row import card_row
from components.dropdown import Dropdown
from components.header import header
from components.nav_sidebar import generate_nav_sidebar
from components.page import Page
from components.page_storage_and_lookup import PageStorageAndLookup
from data.research.columns import REFColumns
from data.students.columns import StudentColumns
from pages.update_performance_indicators_page import update_performance_indicators_page
from pages.update_student_timeseries_page import update_student_timeseries_page
from util.he_data import HEData, HEDataColumn
from util.query_string import kwargs_to_query_string

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

he_providers = (
    pd.read_csv("data/students/student_timeseries_data.csv")[
        StudentColumns.HE_PROVIDER_NAME.value
    ]
    .sort_values()
    .unique()
)

HE_provider_filter = Dropdown(
    title="Select HE provider",
    filter_id="selected_university",
    options=list(he_providers),
    default_value=None,
)

filters = [HE_provider_filter]

dashboard_pages = PageStorageAndLookup()

dashboard_pages.add_pages(
    [
        Page(
            title="Student enrolments",
            url_path="/student-enrolment-timeseries",
            html_template=[
                card_row(card(children=["Loading..."], element_id="react-content"))
            ],
            filters=[HE_provider_filter],
            update_function=update_student_timeseries_page,
            data=HEData(
                pd.read_csv("data/students/student_timeseries_data.csv"),
                column_lookup={
                    StudentColumns.ACADEMIC_YEAR.value: HEDataColumn.ACADEMIC_YEAR.value,
                    StudentColumns.HE_PROVIDER_NAME.value: HEDataColumn.PROVIDER_NAME.value,
                },
            ),
        ),
        Page(
            title="Performance indicators",
            url_path="/performance-indicators",
            html_template=[
                card_row(card(children=["Loading..."], element_id="react-content"))
            ],
            filters=[HE_provider_filter],
            update_function=update_performance_indicators_page,
            data=HEData(
                pd.read_csv("data/research/research_quality_metrics.csv"),
                academic_year_column=None,
                provider_column=REFColumns.HE_PROVIDER_NAME.value,
            ),
        ),
    ]
)


@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname"),
    State("url", "search"),
)
def display_page(pathname, query_string):
    """Show the user the correct page for the given path"""
    try:
        page = dashboard_pages.get_page(pathname)

        nav_sidebar = generate_nav_sidebar(dashboard_pages, page, query_string)

        return [
            html.Div(
                [html.Div(nav_sidebar, id="nav_sidebar"), page.to_html(query_string)],
                className="dashboard_container",
            ),
        ]

    except Exception as exception:
        raise exception


@app.callback(
    Output("url", "search"),
    Output("nav_sidebar", "children"),
    Output("react-content", "children"),
    State("url", "pathname"),
    [Input(flter.filter_id, "value") for flter in filters],
)
def update_query_string(pathname, *filter_values):
    """Update the query string in the url and in the navbar when a filter is changed"""
    page = dashboard_pages.get_page(pathname)

    kwargs = {
        flter.filter_id: filter_value
        for flter, filter_value in zip(filters, filter_values)
    }

    query_string = kwargs_to_query_string(**kwargs)
    nav_sidebar = generate_nav_sidebar(dashboard_pages, page, query_string)

    content = page.update(**kwargs)

    return query_string, nav_sidebar, content
