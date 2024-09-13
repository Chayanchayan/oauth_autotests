from playwright.sync_api import Page
from playwright.sync_api import expect
from pages.base import Base


class Assertions(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def check_url(self, url, msg):
        expect(self.page).to_have_url(url, timeout=10000), msg

    def has_text(self, locator, text: str, msg):  # элемент имеет текст
        loc = self.page.locator(locator)
        expect(loc).to_have_text(text), msg

    def check_presence(self, locator, msg):
        loc = self.page.locator(locator)
        expect(loc).to_be_visible(visible=True, timeout=12000), msg

    def is_element_containing_text(self, locator, text: str, msg):  # элемент содержит текст
        loc = self.page.locator(locator)
        expect(loc).to_contain_text(text, timeout=10000), msg

    def select_has_values(self, locator, options: list, msg):  # Select имеет опции для выбора (опция передается
        # аргументом к проверке)
        loc = self.page.locator(locator)
        loc.select_option(options)
        expect(loc).to_have_values(options), msg
