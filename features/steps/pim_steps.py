from behave import *
from pages.pim_page import PimPage


@when("user adds a new employee")
def step_impl(context):
    context.pim_page = PimPage(context.page)
    context.pim_page.go_to_pim()
    context.pim_page.add_employee("John", "Doe")


@then("employee should be created successfully")
def step_impl(context):
    assert "viewPersonalDetails" in context.page.url