"""
A dashboard page showing a timeseries of student enrolments at universities
"""
from dash import Input, Output
from pandas import read_csv

from components.card import card
from components.main import main
from components.card_row import card_row
from components.filter_panel import filter_panel
from components.dropdown import dropdown
from components.graph import graph

from figures.timeseries import timeseries

from data.students.columns import StudentColumns

from index import app

timeseries_data = read_csv("data/students/student_timeseries_data.csv")


def student_enrolment_timeseries():
    """Create and return the dashboard layout for display in the application."""

    content = [card(children=[], element_id="student-enrolment-timeseries-content")]

    return main(
        [
            filter_panel(
                [
                    dropdown(
                        label="HE Provider",
                        options=timeseries_data[StudentColumns.HE_PROVIDER_NAME.value]
                        .sort_values()
                        .unique(),
                        selected=None,
                        element_id="HE-provider-selection",
                    )
                ]
            ),
            card_row(content),
        ],
    )


@app.callback(
    Output("student-enrolment-timeseries-content", "children"),
    Input("HE-provider-selection", "value"),
)
def update_student_enrolment_timeseries(selected_university=None):
    """Update the student enrolment timeseries when a filter is applied"""
    dataframe = timeseries_data.copy()
    if selected_university:
        dataframe = dataframe[
            dataframe[StudentColumns.HE_PROVIDER_NAME.value] == selected_university
        ]
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
