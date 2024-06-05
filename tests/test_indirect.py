import pytest
from models.github_page import github_page


@pytest.mark.parametrize('driver', ['desctop'], indirect=True)
def test_github_desctop(driver):
    github_page.open()
    github_page.sign_in()
    github_page.should_have_text_sign_in()


@pytest.mark.parametrize('driver', ['mobile'], indirect=True)
def test_github_mobile(driver):
    github_page.open()
    github_page.click_button_from_mobile()
    github_page.sign_in()
    github_page.should_have_text_sign_in()