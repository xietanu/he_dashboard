"""Header component for top of page"""
from dash import html


def header(title: str) -> html.Div:
    """Return <div> containing header box with specified title"""
    return html.Div(
        [html.Div([html.H1(title, className="header_title")], className="header_flex")],
        className='header_container',
    )
