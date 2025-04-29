from decouple import config
from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(headless=False)
    page = chromium.new_page()

    page.goto(config("AUTH_URL"))
