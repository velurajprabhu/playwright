from behave import *
from pages.pim_page import PimPage
import random


def generate_name():
    return f"User{random.randint(1000,9999)}"


@given("user is on PIM page")
def step_impl(context):
    context.pim_page = PimPage(context.page)
    context.pim_page.navigate_to_pim()

@when("user adds a new employee")
def step_impl(context):
    context.first_name = generate_name()
    context.last_name = "Test"
    context.pim_page.click_add_employee(context)

@then("employee should be created with employee id")
def step_impl(context):
    assert context.emp_id is not None, f"""
❌ Employee ID not generated
Value: {context.emp_id}
"""

@when("user searches for the employee")
def step_impl(context):
    context.pim_page.navigate_to_pim()
    context.pim_page.search_employee(context.first_name)


@then("employee should appear in search results")
def step_impl(context):
    context.page.wait_for_load_state("networkidle")
    assert context.pim_page.is_employee_present(context.first_name), f"""
❌ Employee not found in search
Name: {context.first_name}
"""

@when("user edits employee details")
def step_impl(context):
    context.pim_page.navigate_to_pim()
    context.pim_page.search_employee(context.first_name)
    context.pim_page.open_employee_record(context.first_name)
    context.new_name = context.first_name + "_Updated"
    context.pim_page.edit_employee_name(context.new_name)


@then("changes should be saved")
def step_impl(context):
    context.page.locator("input[name='firstName']").wait_for()
    updated_value = context.page.locator("input[name='firstName']").input_value()

    assert updated_value == context.new_name, f"""
❌ Employee update failed
Expected: {context.new_name}
Actual: {updated_value}
"""

@when("user deletes the employee")
def step_impl(context):
    context.pim_page.navigate_to_pim()
    context.pim_page.search_employee(context.new_name)
    context.pim_page.delete_employee_by_name(context.new_name)


@then("employee should be removed from list")
def step_impl(context):
    context.pim_page.search_employee(context.new_name)

    assert not context.pim_page.is_employee_present(context.new_name), f"""
❌ Employee still exists after deletion
Name: {context.new_name}
"""