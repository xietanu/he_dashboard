"""update_performance_indicators_page function"""
from components.graph import graph
from data.research.columns import REFColumns
from figures.grouped_jitter_plot import grouped_jitter_plot
from util.he_data import HEData


def update_performance_indicators_page(data: HEData, selected_university: str) -> list:
    """
    Function to update the performance indicators page with selected univerities.

    Args:
        data (HEData): Data containing the performance indicators.
        selected_university (str): University selected to be displayed.

    Returns:
        list: List of HTML elements to display.
    """
    visualisation = grouped_jitter_plot(
        data,
        metrics_to_plot=[
            REFColumns.QUALITY_WEIGHTED_VOLUME_Z.value,
            REFColumns.QUALITY_SCORE_Z.value,
        ],
        selected_unis=[selected_university],
    )

    return [graph(element_id="performance-indicators-vis", figure=visualisation)]
