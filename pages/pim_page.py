from pages.base_page import BasePage

class PimPage(BasePage):

    PIM_MENU = "//span[text()='PIM']"
    ADD_BTN = "//button[normalize-space()='Add']"
    FIRST_NAME = "input[name='firstName']"
    LAST_NAME = "input[name='lastName']"
    SAVE_BTN = "//button[@type='submit']"

    def go_to_pim(self):
        self.click(self.PIM_MENU)

    def add_employee(self, first_name, last_name):
        self.click(self.ADD_BTN)
        self.fill(self.FIRST_NAME, first_name)
        self.fill(self.LAST_NAME, last_name)
        self.click(self.SAVE_BTN)