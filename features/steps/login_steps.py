from behave import *
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage


@given("user navigates to login page")
def step_impl(context):
    context.page.goto(context.base_url)
    context.login_page = LoginPage(context.page)


@when("user logs in with {username}")
def step_impl(context, username):
    context.login_page.login(context,username)


@then("user should see dashboard")
def step_impl(context):
    context.page.locator(".oxd-layout-context").wait_for(state="visible")
    assert "dashboard" in context.page.url.lower()


@then("user should see login error message for {username}")
def step_impl(context, username):
    context.login_page.get_error(context, username)

@then("validation messages should be displayed for {username}")
def step_impl(context,username):
    context.login_page.get_required_field_errors(context, username)

@then("user logout of the application")
def step_impl(context):
    context.login_page.logout(context)

@then("session should not persist after logout")
def step_impl(context):
    context.login_page.session_validation(context)

from behave import when

@when("user loads login page with performance check")
def step_impl(context):
    context.page.goto(context.base_url)
    perf = context.page.evaluate("window.performance.timing")
    load_time = (perf["loadEventEnd"] - perf["navigationStart"]) / 1000
    print(f"⏱ Login Page Load: {load_time:.2f}s")

    assert load_time < 2, f"""
❌ Login page too slow
Expected: < 2s
Actual: {load_time:.2f}s
"""