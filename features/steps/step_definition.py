from behave import *


@given("user navigate to {url}")
def navigate_to_url(context, url):
    context.page.goto(url)
