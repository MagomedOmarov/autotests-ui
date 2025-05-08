from playwright.sync_api import sync_playwright, expect
import json


def register_and_save_state():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        page.get_by_test_id('registration-form-email-input').locator('input').fill("test.user@example.com")
        page.get_by_test_id('registration-form-username-input').locator('input').fill("testuser")
        page.get_by_test_id('registration-form-password-input').locator('input').fill("password123")
        page.get_by_test_id('registration-page-registration-button').click()

        storage = context.storage_state()
        with open("auth_state.json", "w") as f:
            json.dump(storage, f)

        context.close()
        browser.close()


if __name__ == "__main__":
    register_and_save_state()