"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser,have,by,be

@pytest.mark.parametrize("driver", ["desktop"], indirect=True)
def test_github_desktop(driver):
    browser.open('https://github.com/')
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.element("h1").should(have.text("Sign in to GitHub"))


@pytest.mark.parametrize("driver", ["mobile"], indirect=True)
def test_github_mobile(driver):
    browser.open('https://github.com/')
    browser.element('[class=Button-content]').click()
    browser.element(by.text("Sign up")).click()
    browser.element('#login').should(be.visible)