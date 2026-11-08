from playwright.sync_api import Locator, Page


from pages.base_page import BasePage
from utilities import config
import re




class LoginPage(BasePage):
    PATH = config.GITHUB_URL


    def __init__(self, page: Page):
        super().__init__(page)

    def clickOnSignInButton(self):
        self.page.get_by_role("link", name="Sign in").click()


    def waitForLoginPagetoload(self):
        self.page.get_by_role(
            "textbox",
            name="Username or email address"
        ).wait_for()


    def fill_username(self, username):
        self.page.get_by_role(
            "textbox",
          name="Username or email address"
      ).fill(username)


    def fill_password(self, password):
        self.page.get_by_label("Password").fill(password)