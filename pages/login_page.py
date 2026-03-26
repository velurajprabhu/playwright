from time import sleep

from pages.base_page import BasePage

class LoginPage(BasePage):

    USERNAME = "input[name='username']"
    PASSWORD = "input[name='password']"
    LOGIN_BTN = "button[type='submit']"
    ERROR_MSG = ".oxd-alert-content-text"
    REQUIRED_FIELDS = ".oxd-input-field-error-message"
    PROFILE_ICON = ".oxd-userdropdown-tab"

    def get_required_field_errors(self, context, username):
        expected = [e.strip() for e in self.page.locator(self.REQUIRED_FIELDS).all_inner_texts()]
        self.compare(expected ,context.users[username]['error_msg'])

    def login(self,context, username):
        self.fill(self.USERNAME, context.users[username]['username'])
        self.fill(self.PASSWORD, context.users[username]['password'])
        self.click(self.LOGIN_BTN)

    def get_error(self,context,username):
        self.compare(self.get_text(self.ERROR_MSG), context.users[username]['error_msg'])

    def logout(self,context):
        self.click(self.PROFILE_ICON)
        logout = self.get_role("menuitem", "Logout")
        logout.click()
        self.is_visible(self.USERNAME)

    def session_validation(self,context):
        context.page.goto(context.base_url+"/web/index.php/dashboard/index")
        context.page.wait_for_load_state("networkidle")
        current_url = context.page.url
        assert "login" in current_url.lower(), f"""
        ❌ Session still active after logout
        Expected redirect to login page
        Actual URL: {current_url}
        """