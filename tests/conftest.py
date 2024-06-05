import pytest
from selene import browser


@pytest.fixture()
def setting_browser_desctop():
    browser.config.base_url = 'https://github.com/'
    browser.config.window_height = 1050
    browser.config.window_width = 1680

    yield

    browser.quit()


@pytest.fixture()
def setting_browser_mobile():
    browser.config.base_url = 'https://github.com/'
    browser.config.window_height = 844
    browser.config.window_width = 390

    yield

    browser.quit()


@pytest.fixture(params=['desctop', 'mobile'])
def driver(request):
    if request.param == 'desctop':
        browser.config.window_height = 1050
        browser.config.window_width = 1680
    else:
        browser.config.window_height = 844
        browser.config.window_width = 390

    yield

    browser.quit()


@pytest.fixture(params=[(1680, 1050), (390, 844)])
def driver_setup(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]