import os

import pytest
from _pytest.fixtures import Parser
from decouple import config
from playwright.sync_api import sync_playwright

from pages.base_page import BasePage
from pages.registration_page import  RegistrationPage


def pytest_addoption(parser: Parser):
    group_browser_settings = parser.getgroup("browser-options", "Параметры браузера")
    group_browser_settings.addoption("--brows",
                                     choices=['webkit', 'firefox', 'chromium', 'chrome', 'msedge'],
                                     type=str,
                                     dest='brows',
                                     default=os.getenv('BROWSER', 'chrome'),
                                     help='Хук для проброски браузера'
                                     )
    group_browser_settings.addoption('--resolution',
                                     type=str,
                                     dest='resolution',
                                     default=os.getenv('RESOLUTION', '1400_1080'),
                                     help='Хук для проброски разрешения экрана width_height')
    group_browser_settings.addoption('--headless',
                                     dest='headless',
                                     default=os.getenv('HEADLESS', 'False'),
                                     help='Хук для настройки включения\\отключения вывода на экран')

    group_browser_settings.addoption('--wt',
                                     type=int,
                                     dest='wt',
                                     default=int(os.getenv('WT', 30)),
                                     help='Хук для проброски дефолтного времени ожидания элементов')

    group_browser_settings.addoption('--url',
                                     type=str,
                                     dest='url',
                                     default=os.getenv(key='BASE_DEV_URL', default=config("BASE_DEV_URL")),
                                     help='Хук для проброски базового URL для тестирования')

    group_browser_settings.addoption('--login',
                                     type=str,
                                     dest='login',
                                     default=os.getenv('LOGIN', config('LOGIN')),
                                     help='Логин для авторизации')

    group_browser_settings.addoption('--password',
                                     type=str,
                                     dest='password',
                                     default=os.getenv('PASSWORD', config('PASSWORD')),
                                     help='Пароль для авторизации')


@pytest.fixture(scope='session')
def playwright():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope='session')
def context(browser, pytestconfig):
    resolution = pytestconfig.getoption('resolution')
    width, height = map(int, resolution.split('_'))
    timeout = pytestconfig.getoption('wt') * 1000  # Преобразуем в миллисекунды

    context = browser.new_context(
        viewport={'width': width, 'height': height},
        screen={'width': width, 'height': height},
        accept_downloads=True
    )
    context.set_default_timeout(timeout)

    yield context
    context.close()


@pytest.fixture(scope='session')
def browser(playwright, pytestconfig):
    browser_name = pytestconfig.getoption('brows')
    headless = pytestconfig.getoption('headless').lower() == 'true'

    # Для chrome и msedge используем chromium с channel
    if browser_name in ['chrome', 'msedge']:
        browser_type = playwright.chromium
        browser = browser_type.launch(channel=browser_name, headless=headless)
    else:
        browser_type = getattr(playwright, browser_name)
        browser = browser_type.launch(headless=headless)

    yield browser
    browser.close()

@pytest.fixture(scope='function')
def pages(context):
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture()
def registration():
    page = BasePage()
    page.regist(url='https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    page = RegistrationPage()
    page.fill_email('magomed.omarov.it@gmail.com')
    page.user_name_input('Магомед')
    page.fill_password('Montana000avar!')
    page.submit()




