
from playwright.sync_api import Page

from pages.base_page import BasePage


class RegistrationPage(BasePage):

    def __init__(self, page: Page=None):
        super().__init__(page)
        self.base = BasePage(page)
        self.email_input = self.page.get_by_test_id('registration-form-email-input').locator('input')
        self.name_input = self.page.get_by_test_id('registration-form-username-input').locator('input')
        self.password_input = self.page.get_by_test_id('registration-form-password-input').locator('input')
        self.submit_button = self.page.get_by_test_id('registration-page-registration-button')

    def goto(self):
        self.page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        return self

    def fill_email(self, email: str):
        self.email_input.fill(email)
        return self
    def user_name_input(self, name: str):
        self.name_input.fill(name)
        return self

    def fill_password(self, password: str):
        self.password_input.fill(password)
        return self

    def submit(self):
        self.submit_button.click()