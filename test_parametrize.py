"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, be, have


@pytest.fixture(
    params=['1920x1080', '1366x768', '1280x1024', '640x480', '320x568', '360x640']

)
def browser_settings(request):
    width, height = map(int, request.param.split('x'))
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


desktop = pytest.mark.parametrize(
    'browser_settings', ['1920x1080', '1366x768', '1280x1024'], indirect=True
)

mobile = pytest.mark.parametrize(
    'browser_settings', ['640x480', '320x568', '360x640'], indirect=True
)


@desktop
def test_github_desktop(browser_settings):
    browser.open("https://github.com")
    browser.element(".HeaderMenu-link--sign-in").should(be.clickable).click()


@mobile
def test_github_mobile(browser_settings):
    browser.open('https://github.com/')
    browser.element('.flex-1 > a[href="/login"]').should(have.exact_text('Sign in')).click()