import pytest
from selene import browser

from models.github_page import github_page


def test_github_desctop(driver_setup):
    if browser.config.window_width < 1000:
        pytest.skip('Mobile version')
    github_page.open()
    github_page.sign_in()
    github_page.should_have_text_sign_in()



def test_github_mobile(driver_setup):
    if browser.config.window_width > 1000:
        pytest.skip('Desctop version')
    github_page.open()
    github_page.click_button_from_mobile()
    github_page.sign_in()
    github_page.should_have_text_sign_in()