"""
A dashboard page showing a timeseries of student enrolments at universities
"""
from time import time
from urllib import response
from dash import Input, Output, dcc
from pandas import read_csv

from components.card import card
from components.main import main
from components.card_row import card_row

from figures.timeseries import timeseries

from data.students.columns import StudentColumns

from index import app

timeseries_data = read_csv("data/students/student_timeseries_data.csv")


def student_enrolment_timeseries():
    """Create and return the dashboard layout for display in the application."""

    content = [card(children=[], element_id="student-enrolment-timeseries-content")]

    return main(
        [
            card_row(content),
        ],
    )


@app.callback(
    Output("student-enrolment-timeseries-content", "children"),
    Input("url", "pathname"),
)
def update_student_enrolment_timeseries(url=None):
    dataframe = timeseries_data.groupby(
        by=[StudentColumns.ACADEMIC_YEAR.value, StudentColumns.LEVEL_OF_STUDY.value],
        as_index=False,
    )[StudentColumns.NUMBER.value].sum()

    visualisation = timeseries(dataframe,StudentColumns.ACADEMIC_YEAR.value,StudentColumns.NUMBER.value,StudentColumns.LEVEL_OF_STUDY.value)

    return [dcc.Graph(id = "student-enrolment-timeseries", responsive=True,figure = visualisation)]
