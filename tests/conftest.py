import pytest
from selene import browser,have

@pytest.fixture
def desktop_browser():
    browser.config.window_width = 1366
    browser.config.window_height = 768
    yield
    browser.quit()


@pytest.fixture
def mobile_browser():
    browser.config.window_width = 414
    browser.config.window_height = 896
    yield
    browser.quit()


@pytest.fixture(params=['desktop', 'mobile'])
def driver(request):
    if request.param == 'desktop':
        browser.config.window_width = 1366
        browser.config.window_height = 768
    else:
        browser.config.window_width = 414
        browser.config.window_height = 896
    yield
    browser.quit()


@pytest.fixture(params=[(1366, 768), (414, 896)])
def driver_setup(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]