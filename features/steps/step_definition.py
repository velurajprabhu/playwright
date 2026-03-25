from behave import *
from pages.login_page import LoginPage


@given("user navigates to login page")
def step_impl(context):
    context.page.goto("https://opensource-demo.orangehrmlive.com")
    context.login_page = LoginPage(context.page)


@when("user logs in with username {username} and password {password}")
def step_impl(context, username, password):
    context.login_page.login(username, password)


@then("user should see dashboard")
def step_impl(context):
    assert "dashboard" in context.page.url.lower()


@then("user should see login error message")
def step_impl(context):
    assert context.login_page.get_error() != ""