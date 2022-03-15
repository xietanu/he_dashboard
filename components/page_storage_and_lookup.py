from importlib.resources import path
from components.page import Page


class PageStorageAndLookup:
    def __init__(self) -> None:
        self.pages = {}
        self.homepage = None

    def add_page(self, page: Page) -> None:
        self.pages[page.get_url_path()] = page
        if not self.homepage:
            self.homepage = page

    def add_pages(self, pages: list[Page]) -> None:
        for page in pages:
            self.add_page(page)

    def get_page(self, pathname: str) -> Page:
        if pathname == "/":
            return self.homepage
        if pathname in self.pages:
            return self.pages[pathname]
        return None

    def get_pages(self) -> list[Page]:
        return [page for _, page in self.pages.items()]
