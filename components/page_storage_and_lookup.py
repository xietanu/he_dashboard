""" 
PageStorageAndLookup - A container for dashboard pages, providing tools to store and find them.
"""
from importlib.resources import path
from components.page import Page


class PageStorageAndLookup:
    """
    A container for dashboard pages, providing tools to store and find them.
    """

    def __init__(self) -> None:
        self.pages = {}
        self.homepage = None

    def add_page(self, page: Page) -> None:
        """
        Add a page to the store.

        Args:
            page (Page): The dashboard page to add.

        Raises:
            ValueError: If the URL path of the page is already in use.
        """
        url_path = page.get_url_path()

        if url_path in self.pages:
            raise ValueError(f"URL path: {url_path} already assigned to page.")

        self.pages[url_path] = page
        if not self.homepage:
            self.homepage = page

    def add_pages(self, pages: list[Page]) -> None:
        """
        Add multiple pages at once to the store.

        Args:
            pages (list[Page]): List of pages to add.
        """
        for page in pages:
            self.add_page(page)

    def get_page(self, pathname: str) -> Page:
        """
        Find a stored page from its URL path.

        Args:
            pathname (str): The URL path to the page.

        Returns:
            Page: The associated dashboard page. None if no page found.
        """
        if pathname == "/":
            return self.homepage
        if pathname in self.pages:
            return self.pages[pathname]
        return None

    def get_pages(self) -> list[Page]:
        """
        Get the pages as a list.

        Returns:
            list[Page]: A list of the dashboard pages stored.
        """
        return [page for _, page in self.pages.items()]
