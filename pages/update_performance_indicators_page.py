from components.graph import graph
from data.research.columns import REFColumns
from figures.grouped_jitter_plot import grouped_jitter_plot


def update_performance_indicators_page(data, selected_university):
    visualisation = grouped_jitter_plot(
        data.get_dataframe(),
        metrics_to_plot=[
            REFColumns.QUALITY_WEIGHTED_VOLUME_Z.value,
            REFColumns.QUALITY_SCORE_Z.value,
        ],
        name_column=REFColumns.HE_PROVIDER_NAME.value,
        selected_unis=[selected_university],
    )

    return [graph(element_id="performance-indicators-vis", figure=visualisation)]
