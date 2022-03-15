"""Components for a navigation sidebar"""

from dash import html, dcc
from components.page_storage_and_lookup import PageStorageAndLookup
from components.page import Page


def generate_nav_sidebar(
    dashboard_pages: PageStorageAndLookup, current_page: Page, query_string: str
) -> html.Nav:
    """Generate the nav sidebar with links to the pages in the dashboard"""
    links = [
        nav_sidebar_link(
            page.title, page.url_path + query_string, active=page is current_page
        )
        for page in dashboard_pages.get_pages()
    ]
    return nav_sidebar(links)


def nav_sidebar(links):
    """A navigation bar for switching between dashboard pages."""
    return html.Nav(
        html.Ul(
            links,
        ),
        role="navigation",
        className="nav_sidebar",
    )


def nav_sidebar_link(text: str, href: str, active=False):
    """A link to another dashboard
    If active, indicate this to the user"""
    return html.Li(
        dcc.Link(
            text,
            href=href,
            className="nav_sidebar_link",
        ),
        className="active_item" if active else "",
    )
