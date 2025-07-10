import pytest
from selene import browser

@pytest.fixture
def desktop_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()


@pytest.fixture
def mobile_browser():
    browser.config.window_width = 416
    browser.config.window_height = 896
    yield
    browser.quit()


@pytest.fixture(params=['desktop', 'mobile'])
def driver(request):
    if request.param == 'desktop':
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    else:
        browser.config.window_width = 416
        browser.config.window_height = 896
    yield
    browser.quit()


@pytest.fixture(params=[(1920, 1080), (416, 896)])
def driver_config(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]