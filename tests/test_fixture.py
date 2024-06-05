from models.github_page import github_page


def test_github_desctop(setting_browser_desctop):
    github_page.open()
    github_page.sign_in()
    github_page.should_have_text_sign_in()



def test_github_mobile(setting_browser_mobile):
    github_page.open()
    github_page.click_button_from_mobile()
    github_page.sign_in()
    github_page.should_have_text_sign_in()