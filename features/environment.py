from playwright.sync_api import sync_playwright
from utils import data_loader

def before_all(context):
    context.users = data_loader.load_test_data()
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)

def before_scenario(context, scenario):
    context.page = context.browser.new_page()
    context.base_url = "https://opensource-demo.orangehrmlive.com"

def after_scenario(context, scenario):
    if scenario.status == "failed":
        context.page.screenshot(path=f"screenshots/{scenario.name}.png")
    context.page.close()

def after_all(context):
    context.browser.close()
    context.playwright.stop()