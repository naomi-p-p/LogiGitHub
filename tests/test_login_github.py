
from playwright.sync_api import Locator, Page , expect
from pages.base_page import BasePage
from utilities import config
import re
from pages.login_github import LoginPage
from utilities.config import TEST_PASSWORD_GITHUB, TEST_EMAIL_GITHUB




class LoginPage(BasePage):
    PATH = config.GITHUB_URL




    def __init__(self, page: Page):
        super().__init__(page)


    def clickOnSignButton(self):
        self.page.get_by_role("link", name="Sign in").click()




    def SignInButton(self) -> Locator:
        return self.page.get_by_role("link", name="Sign in")
    
    def clickOnSingin(self) -> None:
        self.page.get_by_role("link", name="Sign in").click()
       
    def waitForLoginPageLoad(self):
        self.page.wait_for_url("**/login**")
    def emailField(self):
       return self.page.get_by_role("textbox", name="Username or email address")
    def PasswordField(self):
       return self.page.get_by_role("textbox", name="Password")   
    def singInWithCredent(self)->Locator:
        return self.page.get_by_role("button", name="Sign in", exact=True)
    def userMenu(self) -> Locator:
        return self.page.get_by_role("button", name="Open user navigation menu")
    def expectNotOnLoginPage(self) -> None:
        expect(self.page).not_to_have_url(re.compile(r".*/login"))






def test_sign_in_to_github(page: Page):
    login = LoginPage(page)
    login.open()
    login.clickOnSignButton()
    login.waitForLoginPageLoad()


    assert TEST_EMAIL_GITHUB is not None
    assert TEST_PASSWORD_GITHUB is not None






    login.emailField().fill(TEST_EMAIL_GITHUB)
    login.PasswordField().fill(TEST_PASSWORD_GITHUB)
    login.singInWithCredent().click()