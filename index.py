"""
Index outlining the dashboard's layout and links to pages.
"""

from dash import dcc, html, Input, Output, State
import pandas as pd

from app import app
from components.card import card
from components.card_row import card_row
from components.dropdown import Dropdown
from components.graph import graph
from components.header import header
from components.nav_sidebar import generate_nav_sidebar
from components.page import Page
from components.page_storage_and_lookup import PageStorageAndLookup
from data.students.columns import StudentColumns
from figures.timeseries import timeseries
from util.he_data import HEData
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
            data=HEData(
                pd.read_csv("data/students/student_timeseries_data.csv"),
                academic_year_column=StudentColumns.ACADEMIC_YEAR.value,
                provider_column=StudentColumns.HE_PROVIDER_NAME.value,
            ),
            html_template=[
                card_row(card(children=[], element_id="student-enrolments-content"))
            ],
            filters=[HE_provider_filter],
        ),
        Page(
            title="Performance indicators",
            url_path="/performance-indicators",
            data=pd.read_csv("data/research/research_quality_metrics.csv"),
            html_template=[
                card_row(card(children=[], element_id="performance-indicators-content"))
            ],
            filters=[HE_provider_filter],
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
    State("url", "pathname"),
    Input("selected_university", "value"),
)
def update_query_string(pathname, selected_university):
    """Update the query string in the url and in the navbar when a filter is changed"""
    page = dashboard_pages.get_page(pathname)
    query_string = kwargs_to_query_string(selected_university=selected_university)
    nav_sidebar = generate_nav_sidebar(dashboard_pages, page, query_string)
    return query_string, nav_sidebar


@app.callback(
    Output("student-enrolments-content", "children"),
    Input("selected_university", "value"),
)
def update_student_enrolment_timeseries(selected_university):
    """Update the student enrolment timeseries when a filter is applied"""
    data = dashboard_pages.get_page("/student-enrolment-timeseries").data

    dataframe = data.get_filtered_dataframe(selected_university=selected_university)

    dataframe = dataframe.groupby(
        by=[StudentColumns.ACADEMIC_YEAR.value, StudentColumns.LEVEL_OF_STUDY.value],
        as_index=False,
    )[StudentColumns.NUMBER.value].sum()

    visualisation = timeseries(
        dataframe,
        StudentColumns.ACADEMIC_YEAR.value,
        StudentColumns.NUMBER.value,
        StudentColumns.LEVEL_OF_STUDY.value,
    )

    return [graph(element_id="student-enrolment-timeseries", figure=visualisation)]
