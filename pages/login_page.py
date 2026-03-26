from time import sleep

from pages.base_page import BasePage

class LoginPage(BasePage):

    USERNAME = "input[name='username']"
    PASSWORD = "input[name='password']"
    LOGIN_BTN = "button[type='submit']"
    ERROR_MSG = ".oxd-alert-content-text"

    def login(self,context, username):
        self.fill(self.USERNAME, context.users[username]['username'])
        self.fill(self.PASSWORD, context.users[username]['password'])
        self.click(self.LOGIN_BTN)

    def get_error(self,context,username):
        self.compare(self.get_text(self.ERROR_MSG), context.users[username]['error_msg'])