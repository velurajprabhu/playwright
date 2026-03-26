from pages.base_page import BasePage

class PimPage(BasePage):

    PIM_MENU = "//span[text()='PIM']"
    ADD_BTN = "//button[normalize-space()='Add']"
    FIRST_NAME = "input[name='firstName']"
    LAST_NAME = "input[name='lastName']"
    SAVE_BTN = "(//button[normalize-space()='Save'])[1]"
    EMPLOYEE_ID = "(//input[contains(@class,'oxd-input')])[5]"
    SEARCH_NAME_INPUT = "(//input[@placeholder='Type for hints...'])[1]"
    SEARCH_BTN = "//button[normalize-space()='Search']"
    EMPLOYEE_RESULT = "//div[@role='row']"
    EDIT_FIRST_NAME = "input[name='firstName']"
    DELETE_BTN = "//i[contains(@class,'bi-trash')]"
    CONFIRM_DELETE = "//button[normalize-space()='Yes, Delete']"


    def navigate_to_pim(self):
        self.click(self.PIM_MENU)

    def click_add_employee(self,context):
        self.click(self.ADD_BTN)
        context.emp_id = context.pim_page.add_employee(
            context.first_name,
            context.last_name
        )

    def add_employee(self, first_name, last_name):
        self.fill(self.FIRST_NAME, first_name)
        self.fill(self.LAST_NAME, last_name)
        emp_id = self.page.locator(self.EMPLOYEE_ID).input_value()
        self.click(self.SAVE_BTN)
        return emp_id

    def search_employee(self, name):
        self.fill(self.SEARCH_NAME_INPUT, name)
        self.click(self.SEARCH_BTN)

    def is_employee_present(self, name):
        return self.page.locator(self.EMPLOYEE_RESULT).filter(has_text=name).count() > 0

    def edit_employee_name(self, new_name):
        field = self.page.locator(self.EDIT_FIRST_NAME)
        field.wait_for(state="visible")
        field.click()
        field.press("Meta+A")
        field.press("Backspace")
        field.type(new_name)
        field.press("Tab")
        self.page.locator(
            "//h6[text()='Personal Details']/following::form[1]//button[@type='submit']"
        ).click()
        self.page.locator("text=Successfully Updated").wait_for()
        self.page.wait_for_load_state("networkidle")

    def delete_employee_by_name(self, name):
        row = self.page.locator("div[role='row']").filter(has_text=name).first
        row.locator("button").nth(1).click()
        self.page.locator("text=Yes, Delete").click()
        self.page.locator("text=Successfully Deleted").wait_for()

    def open_employee_record(self, name):
        self.page.locator(f"//div[@role='row']//div[contains(text(),'{name}')]").click()