"""Components for a navigation sidebar"""

from dash import html, dcc
from components.page_storage_and_lookup import PageStorageAndLookup
from components.page import Page


def generate_nav_sidebar(
    dashboard_pages: PageStorageAndLookup, current_page: Page, query_string: str
) -> html.Nav:
    """
    Creates a navigation sidebar component with links to the specified pages.

    Args:
        dashboard_pages (PageStorageAndLookup): Container of the dashboard pages.
        current_page (Page): The current page being displayed.
        query_string (str): The query string for the current filters.

    Returns:
        html.Nav: The navigation siderbar component.
    """
    return html.Nav(
        html.Ul(
            [
                html.Li(
                    dcc.Link(
                        page.title,
                        href=page.url_path + query_string,
                        className="nav_sidebar_link",
                    ),
                    className="active_item" if page is current_page else "",
                )
                for page in dashboard_pages.get_pages()
            ],
        ),
        role="navigation",
        className="nav_sidebar",
    )
