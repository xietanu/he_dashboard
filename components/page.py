"""Page class"""
from typing import Callable

from dash import html

from components.filter import Filter
from components.filter_panel import filter_panel
from components.main import main
from util.he_data import HEData
from util.query_string import query_string_to_kwargs


class Page:
    """Represents a page on the dashboard and its associated information."""

    def __init__(
        self,
        title: str,
        url_path: str,
        html_template: list,
        update_function: Callable,
        data: HEData = None,
        filters: list[Filter] = None,
    ) -> None:
        """
        Args:
            title (str): Name of the page to display to the user
            url_path (str): URL path to assign to the page.
            html_template (list): List of HTML elements to make up the main content of the page.
            update_function (Callable): Function to call when page needs to be updated
                due to user input.
            data (HEData): Data object associated with the page, and used to inform visualisations.
                Defaults to None.
            filters (list[Filter], optional): List of Filters used on the page. Defaults to None.
        """
        self.title = title
        self.url_path = url_path
        self.filters = filters if filters else []
        self.html_template = html_template
        self.data = data
        self.update_function = update_function

    def get_url_path(self):
        """
        Get the url path associated with the page.

        Returns:
            str: The url path
        """
        return self.url_path

    def to_html(self, query_string: str) -> html.Main:
        """
        Creates the HTML needed to display the page, using the pages's template.

        Args:
            query_string (str): The query string containing information on filters.

        Returns:
            html.Main: The HTML main element containing the page's content.
        """
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

    def update(self, **filter_values):
        """
        Updates the page with the specified filter values.

        Args:
            **filter_values: Arguments for filter_ids with their associated values.
                May contain any filters, not just those for this page.

        Returns:
            list: List of the HTML elements to fill in the page.
        """
        relevant_filters = {
            key: value
            for key, value in filter_values.items()
            if key in [flter.filter_id for flter in self.filters]
        }

        return self.update_function(self.data, **relevant_filters)
