"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""

from selene import browser,have


def test_github_desktop(desktop_browser):
    browser.open('https://github.com/')
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.element("h1").should(have.text("Sign in to GitHub"))


def test_github_mobile(mobile_browser):
    browser.open('https://github.com/')
    #browser.element(".Button-label").click()
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.element("h1").should(have.text("Sign in to GitHub"))
