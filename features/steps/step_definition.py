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