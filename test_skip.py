"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, be, have

@pytest.fixture(
    params=['1920x1080', '1366x768', '1280x1024', '640x480', '320x568', '360x640']
)
def resolution(request):
    width, height = map(int, request.param.split("x"))
    browser.config.window_width = width
    browser.config.window_height = height
    if request.param in ['1920x1080', '1366x768', '1280x1024']:
        yield "desktop"
    else:
        yield "mobile"

    browser.quit()


def test_github_desktop(resolution):
    if resolution == "mobile":
        pytest.skip(reason="skip mobile")

    browser.open("https://github.com")
    browser.element(".HeaderMenu-link--sign-in").should(be.clickable).click()


def test_github_mobile(resolution):
    if resolution == "desktop":
        pytest.skip("Это десктопное разрешение")
    browser.open("https://github.com")
    browser.element('.flex-1 > a[href="/login"]').should(have.exact_text('Sign in')).click()