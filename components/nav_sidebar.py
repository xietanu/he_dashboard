"""Components for a navigation sidebar"""

from dash import html, dcc


def generate_nav_sidebar(paths, current_path):
    """Generate the nav sidebar with links to the pages in the dashboard"""
    links = [
        nav_sidebar_link(path["title"], key, active=key == current_path)
        for key, path in paths.items()
        if key != "/"
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
