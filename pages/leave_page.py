from pages.base_page import BasePage

class LeavePage(BasePage):

    LEAVE_MENU = "//span[text()='Leave']"

    # Tabs
    APPLY_TAB = "//a[text()='Apply']"
    MY_LEAVE_TAB = "//a[text()='My Leave']"
    ENTITLEMENTS_TAB = "//span[text()='Entitlements']"

    # Apply Leave
    LEAVE_TYPE_DROPDOWN = ".oxd-select-text"
    DATE_FROM = "(//input[@placeholder='yyyy-mm-dd'])[1]"
    DATE_TO = "(//input[@placeholder='yyyy-mm-dd'])[2]"
    APPLY_BTN = "//button[normalize-space()='Apply']"

    # Actions
    APPROVE_BTN = "//button[normalize-space()='Approve']"
    CANCEL_BTN = "//button[normalize-space()='Cancel']"
    SEARCH_BTN = "//button[normalize-space()='Search']"

    SUCCESS_MSG = "text=Successfully"
    CONFIGURE_MENU = "//span[text()='Configure ']"
    LEAVE_TYPE_OPTION = "//a[text()='Leave Types']"

    ADD_BTN = "//button[normalize-space()='Add']"
    LEAVE_TYPE_NAME = "(//input[@class='oxd-input oxd-input--active'])[2]"
    SAVE_BTN = "//button[normalize-space()='Save']"

    # SUCCESS_MSG = "text=Successfully Saved"
    ENTITLEMENTS_MENU = "Entitlements"
    # ENTITLEMENTS_MENU = "//span[text()='Entitlements']"
    ADD_ENTITLEMENT_OPTION = "//a[text()='Add Entitlements']"
    EMPLOYEE_NAME_INPUT = "//input[@placeholder='Type for hints...']"
    ENTITLEMENT_INPUT = "//input[@class='oxd-input oxd-input--active']"
    CONFIRM_BTN = "//button[normalize-space()='Confirm']"
    ASSIGN_BTN = "Assign"

    # SUCCESS_MSG = "text=Successfully Saved"


    def navigate(self):
        self.click(self.LEAVE_MENU)

    def apply_leave(self, leave_type, from_date, to_date):
        self.click(self.APPLY_TAB)

        self.page.locator(self.LEAVE_TYPE_DROPDOWN).first.click()
        self.page.get_by_text(leave_type).click()

        self.fill(self.DATE_FROM, from_date)
        self.fill(self.DATE_TO, to_date)

        self.click(self.APPLY_BTN)
        self.page.locator(self.SUCCESS_MSG).wait_for()

    def approve_leave(self):
        self.click(self.APPROVE_BTN)
        self.page.locator(self.SUCCESS_MSG).wait_for()

    def cancel_leave(self):
        self.click(self.CANCEL_BTN)
        self.page.locator(self.SUCCESS_MSG).wait_for()

    def search_leave(self):
        self.click(self.SEARCH_BTN)

    def is_status_visible(self, status):
        return self.page.locator("div[role='row']").filter(has_text=status).count() > 0

    def get_leave_balance(self):
        return self.page.locator("text=Balance").inner_text()

    def navigate_to_leave_types(self):
        self.click(self.LEAVE_MENU)
        self.click(self.CONFIGURE_MENU)
        self.click(self.LEAVE_TYPE_OPTION)


    def add_leave_type(self, name):
        self.click(self.ADD_BTN)

        field = self.page.locator(self.LEAVE_TYPE_NAME)
        field.wait_for(state="visible")

        field.fill(name)

        self.click(self.SAVE_BTN)

        self.page.locator(self.SUCCESS_MSG).wait_for()

    def assign_leave_type(self, context, employee_name, leave_type, days="10"):

        self.click(self.LEAVE_MENU)
        # self.click(self.ENTITLEMENTS_MENU)
        self.page.get_by_text(self.ENTITLEMENTS_MENU).click()
        self.click(self.ADD_ENTITLEMENT_OPTION)
        self.fill(self.EMPLOYEE_NAME_INPUT, employee_name)
        self.page.get_by_text(employee_name).click()
        # self.fill(self.ENTITLEMENT_INPUT, days)
        field = context.page.locator(
            "//label[text()='Entitlement']/following::input[1]"
        )

        field.wait_for()
        field.fill("10")
        self.page.locator(self.LEAVE_TYPE_DROPDOWN).first.click()
        self.page.get_by_text(leave_type).click()
        self.click(self.SAVE_BTN)
        self.click(self.CONFIRM_BTN)

        self.page.get_by_role("link", name="Assign Leave").click()
        # Employee selection
        self.fill(self.EMPLOYEE_NAME_INPUT, employee_name)
        self.page.get_by_text(employee_name).click()

        # Leave type selection
        self.page.locator(self.LEAVE_TYPE_DROPDOWN).first.click()
        self.page.get_by_text(leave_type).click()

        from_date = context.page.get_by_placeholder("yyyy-dd-mm").nth(0)
        to_date = context.page.get_by_placeholder("yyyy-dd-mm").nth(1)

        from_date.fill("2026-25-03")
        to_date.click()
        to_date.press("Meta+A")
        to_date.press("Backspace")
        to_date.fill("2026-26-03")
        self.page.get_by_role("button", name=self.ASSIGN_BTN).click()

        # Confirm popup
        self.click(self.CONFIRM_BTN)

        # Wait for success
        self.page.locator(self.SUCCESS_MSG).wait_for()