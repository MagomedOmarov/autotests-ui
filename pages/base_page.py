from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page=None):
        self.page = page

    def regist(self, url: str):
        self.page.goto(url=url)

