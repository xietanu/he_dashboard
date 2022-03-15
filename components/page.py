"""page.py"""
from components.filter import Filter
from components.filter_panel import filter_panel
from components.main import main
from util.he_data import HEData
from util.query_string import query_string_to_kwargs


class Page:
    """A parent class for each dashboard page"""

    def __init__(
        self,
        title: str,
        url_path: str,
        data: HEData,
        html_template: list,
        filters: list[Filter] = None,
    ) -> None:
        self.title = title
        self.url_path = url_path
        self.filters = filters if filters else []
        self.html_template = html_template
        self.data = data

    def get_url_path(self):
        return self.url_path

    def to_html(self, query_string):
        kwargs = query_string_to_kwargs(query_string)
        for dashboard_filter in self.filters:
            if dashboard_filter.filter_id not in kwargs:
                kwargs[dashboard_filter.filter_id] = dashboard_filter.default_value

        return main(
            [
                filter_panel(
                    [
                        dashboard_filter.to_html(kwargs[dashboard_filter.filter_id])
                        for dashboard_filter in self.filters
                    ]
                )
            ]
            + self.html_template
        )
