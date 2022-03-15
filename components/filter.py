from dash import html


class Filter:
    def __init__(self, title: str, filter_id: str, default_value: str) -> None:
        self.title = title
        self.filter_id = filter_id
        self.default_value = default_value

    def get_html(self, selected_value: str = None) -> html.Div:
        return html.Div([selected_value])
