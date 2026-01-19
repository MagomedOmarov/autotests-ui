from playwright.sync_api import expect, Page

from components.base_component import BaseComponent
from elements.input import Input


class RegistrationFormComponent(BaseComponent):
  def __init__(self, page: Page):
    super().__init__(page)

    self.email_input = Input(
        page,
        'registration-form-email-input',
        'Email'
    )

    self.username_input = Input(
        page,
        'registration-form-username-input',
        'Username')

    self.password_input = Input(
        page,
        'registration-form-password-input',
        'Password')

  def fill(self, email, username, password):
    self.email_input.fill(email)
    self.email_input.check_have_value(email)

    self.username_input.fill(username)
    self.username_input.check_have_value(username)

    self.password_input.fill(password)
    self.password_input.check_have_value(password)
