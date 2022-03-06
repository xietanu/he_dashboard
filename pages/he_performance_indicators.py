"""
A dashboard page showing a timeseries of student enrolments at universities
"""
from dash import Input, Output
from numpy import column_stack
from pandas import read_csv

from components.card import card
from components.main import main
from components.card_row import card_row
from components.filter_panel import filter_panel
from components.dropdown import dropdown
from components.graph import graph

from figures.grouped_jitter_plot import grouped_jitter_plot

from data.research.columns import REFColumns

from index import app

research_quality_metrics = read_csv("data/research/research_quality_metrics.csv")


def he_performance_indicators():
    """Create and return the dashboard layout for display in the application."""

    content = [card(children=[], element_id="performance-indicators-content")]

    return main(
        [
            filter_panel(
                [
                    dropdown(
                        label="HE Provider",
                        options=research_quality_metrics[
                            REFColumns.HE_PROVIDER_NAME.value
                        ]
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
    Output("performance-indicators-content", "children"),
    Input("HE-provider-selection", "value"),
)
def update_student_enrolment_timeseries(selected_university=None):
    """Update the student enrolment timeseries when a filter is applied"""
    dataframe = research_quality_metrics

    visualisation = grouped_jitter_plot(
        dataframe,
        metrics_to_plot=[
            REFColumns.QUALITY_WEIGHTED_VOLUME_Z.value,
            REFColumns.QUALITY_SCORE_Z.value,
        ],
        name_column = REFColumns.HE_PROVIDER_NAME.value,
        selected_unis = [selected_university]
    )

    return [graph(element_id="performance-indicators-vis", figure=visualisation)]
