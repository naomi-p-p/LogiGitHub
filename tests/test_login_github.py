from pages.login_github import LoginPage
from playwright.sync_api import Page, expect
from utilities.config import TEST_EMAIL_GITHUB, TEST_PASSWORD_GITHUB

def test_sign_in_to_gmail(page: Page):
    signInPage = LoginPage(page)
    signInPage.open()
    
    signInPage.clickOnSignInButton()
    signInPage.waitForLoginPagetoLoad()
    
    assert TEST_EMAIL_GITHUB is not None
    assert TEST_PASSWORD_GITHUB is not None

    signInPage.emailField.fill(TEST_EMAIL_GITHUB)
    signInPage.passwordField.fill(TEST_PASSWORD_GITHUB)

    expect(signInPage.signInButtonWithCredentials).to_be_visible()