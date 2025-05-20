"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""


import pytest
from selene import browser, be, have


@pytest.fixture(params=['1920x1080', '1366x768', '1280x1024'])
def desktop(request):
    width, height = map(int, request.param.split('x'))
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


@pytest.fixture(params=['640x480', '320x568', '360x640'])
def mobile(request):
    width, height = map(int, request.param.split('x'))
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


def test_github_desktop(desktop):
    browser.open("https://github.com")
    browser.element(".HeaderMenu-link--sign-in").should(be.clickable).click()


def test_github_mobile(mobile):
    browser.open('https://github.com/')
    browser.element('.flex-1 > a[href="/login"]').should(have.exact_text('Sign in')).click()