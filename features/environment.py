from playwright.sync_api import sync_playwright
from utils import data_loader
from utils.api_helper import generate_token
from services.api_client import APIClient
import re
from pages.pim_page import PimPage
from pages.login_page import LoginPage
from pages.leave_page import LeavePage

def before_all(context):
    context.users = data_loader.load_test_data()
    context.api = APIClient(
        "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2"
    )
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)

def before_scenario(context, scenario):
    context.page = context.browser.new_page()
    context.login_page = LoginPage(context.page)
    context.pim_page = PimPage(context.page)
    context.leave_page = LeavePage(context.page)
    context.base_url = "https://opensource-demo.orangehrmlive.com"
    # generate_token(context.api)

def after_scenario(context, scenario):
    if scenario.status == "failed" and context.page:
        try:
            safe_name = re.sub(r'[^A-Za-z0-9]+', '_', scenario.name)

            context.page.screenshot(
                path=f"screenshots/{safe_name}.png",
                full_page=True
            )
            print(f"📸 Screenshot captured: {safe_name}.png")

        except Exception as e:
            print("❌ Screenshot failed:", e)

    context.page.close()

def after_all(context):
    context.browser.close()
    context.playwright.stop()