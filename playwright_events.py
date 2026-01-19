from playwright.sync_api import sync_playwright, Request, Response


def logRequest(request: Request):
  print(f'Request: {request.url}')


def logResponse(response: Response):
  print(f'Response: {response.url}')


with sync_playwright() as playwright:
  browser = playwright.chromium.launch(headless=False)
  page = browser.new_page()

  page.on("request", logRequest)
  page.on("response", logResponse)

  page.goto(
      'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

  page.wait_for_timeout(3000)