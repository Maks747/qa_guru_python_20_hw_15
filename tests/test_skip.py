"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser,have,by


def test_github_desktop(driver_config):
    if browser.config.window_height < 1000:
        pytest.skip("Разрешение экрана для Mobile")
    browser.open('https://github.com/')
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.element("h1").should(have.text("Sign in to GitHub"))

def test_github_mobile(driver_config):
    if browser.config.window_height > 1000:
        pytest.skip("Разрешение экрана для Desktop")
    browser.open('https://github.com/')
    browser.element('[class=Button-content]').click()
    browser.element(by.text("Sign up")).click()
    browser.element("h2").should(have.text("Sign up to GitHub"))