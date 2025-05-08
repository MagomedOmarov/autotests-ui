import json
import os
from playwright.sync_api import sync_playwright, expect


def test_empty_courses_list():
    with sync_playwright() as playwright:
        auth_file = "auth_state.json"

        if not os.path.exists(auth_file):
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
            page.get_by_test_id('registration-form-email-input').locator('input').fill("test.user@example.com")
            page.get_by_test_id('registration-form-username-input').locator('input').fill("testuser")
            page.get_by_test_id('registration-form-password-input').locator('input').fill("password123")
            page.get_by_test_id('registration-page-registration-button').click()

            expect(page).to_have_url("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

            storage = context.storage_state(path=auth_file)
            context.close()
            browser.close()

        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state=auth_file)
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        expect(page.get_by_role("heading", name="Courses")).to_be_visible()
        expect(page.get_by_text("There is no results")).to_be_visible()

        context.close()
        browser.close()
