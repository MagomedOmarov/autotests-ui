from playwright.sync_api import sync_playwright, expect
import json


def test_auth_and_courses():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        print("1. Открываем страницу регистрации и заполняем форму")
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        page.get_by_test_id('registration-form-email-input').locator('input').fill("test.user@example.com")
        page.get_by_test_id('registration-form-username-input').locator('input').fill("testuser")
        page.get_by_test_id('registration-form-password-input').locator('input').fill("password123")
        page.get_by_test_id('registration-page-registration-button').click()

        expect(page).to_have_url("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
        print("2. Открывается страница Dashboard. Сохраняем состояние браузера")

        storage = context.storage_state()
        with open("auth_state.json", "w") as f:
            json.dump(storage, f)

        context.close()
        browser.close()

        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="auth_state.json")
        page = context.new_page()

        print("3. Открываем страницу Courses используя сохраненный контекст")
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        print("Проверяем наличие элементов")
        expect(page.get_by_role("heading", name="Courses")).to_be_visible()
        expect(page.get_by_text("There is no results")).to_be_visible()

        context.close()
        browser.close()


if __name__ == "__main__":
    test_auth_and_courses()