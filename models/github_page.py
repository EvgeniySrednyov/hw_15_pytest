from selene import browser, have


class GithubPage:
    def open(self):
        browser.open('https://github.com/')

    def sign_in(self):
        browser.element('.HeaderMenu-link--sign-in').click()

    def click_button_from_mobile(self):
        browser.element('.Button-content').click()

    def should_have_text_sign_in(self):
        browser.element('h1').should(have.text('Sign in to GitHub'))


github_page = GithubPage()