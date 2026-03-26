from datetime import datetime, timedelta
from behave import *
from pages.leave_page import LeavePage
from pages.login_page import LoginPage

def get_dates():
    today = datetime.today()
    from_date = today.strftime("%Y-%m-%d")
    to_date = (today + timedelta(days=1)).strftime("%Y-%m-%d")
    return from_date, to_date

@when("employee applies for leave")
def step_impl(context):

    context.leave_page = LeavePage(context.page)
    context.leave_page.navigate()

    context.from_date, context.to_date = get_dates()

    context.leave_page.apply_leave(
        "CAN - Personal",
        context.from_date,
        context.to_date
    )

@then("leave should be in pending status")
def step_impl(context):

    context.leave_page.search_leave()

    assert context.leave_page.is_status_visible("Pending"), """
❌ Leave not in Pending state
"""

@then("leave should be approved")
def step_impl(context):

    assert context.leave_page.is_status_visible("Approved"), """
❌ Leave not approved
"""

@then("leave balance should be deducted")
def step_impl(context):

    balance = context.leave_page.get_leave_balance()

    print("Balance:", balance)

    assert balance is not None, """
❌ Leave balance not updated
"""

@when("employee cancels the leave")
def step_impl(context):

    context.leave_page.cancel_leave()

@then("leave balance should be restored")
def step_impl(context):

    balance = context.leave_page.get_leave_balance()

    assert balance is not None, """
❌ Leave balance not restored
"""

@when("employee applies overlapping leave")
def step_impl(context):

    context.leave_page.apply_leave(
        "CAN - Personal",
        context.from_date,
        context.to_date
    )

@then("overlap error should be shown")
def step_impl(context):

    error = context.page.locator(".oxd-input-field-error").inner_text()

    assert "overlapping" in error.lower(), f"""
❌ Overlap error not shown
Actual: {error}
"""

@when("manager approves leave request")
def step_impl(context):
    context.page.goto(context.base_url)
    login = LoginPage(context.page)
    login.login(context, "valid_user")
    context.leave_page.navigate()
    context.leave_page.search_leave()
    context.leave_page.approve_leave()

import random

@given("admin creates leave type")
def step_impl(context):
    context.leave_page = LeavePage(context.page)
    context.leave_type_name = f"AutoLeave{random.randint(1000,9999)}"
    context.leave_page.navigate_to_leave_types()
    context.leave_page.add_leave_type(context.leave_type_name)

@when("employee applies leave using assigned type")
def step_impl(context):
    context.leave_page.navigate()
    context.from_date, context.to_date = get_dates()
    context.leave_page.apply_leave(
        context.leave_type_name,
        context.from_date,
        context.to_date
    )

@when("admin assigns leave type to employee")
def step_impl(context):
    context.from_date, context.to_date = get_dates()
    context.leave_page.assign_leave_type(
        context,
        employee_name="Auto Testing",
        leave_type=context.leave_type_name,
        days="10"
    )




