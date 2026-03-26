# from playwright.sync_api import sync_playwright
# from utils import data_loader
# from utils.api_helper import generate_token
# from services.api_client import APIClient
# import re
# from pages.pim_page import PimPage
# from pages.login_page import LoginPage
# from pages.leave_page import LeavePage
#
# def before_all(context):
#     context.users = data_loader.load_test_data()
#     context.api = APIClient(
#         "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2"
#     )
#     context.playwright = sync_playwright().start()
#     context.browser = context.playwright.chromium.launch(headless=False)
#
# def before_scenario(context, scenario):
#     context.page = context.browser.new_page()
#     context.login_page = LoginPage(context.page)
#     context.pim_page = PimPage(context.page)
#     context.leave_page = LeavePage(context.page)
#     context.base_url = "https://opensource-demo.orangehrmlive.com"
#     # generate_token(context.api)
#
# def after_scenario(context, scenario):
#     if scenario.status == "failed" and context.page:
#         try:
#             safe_name = re.sub(r'[^A-Za-z0-9]+', '_', scenario.name)
#
#             context.page.screenshot(
#                 path=f"screenshots/{safe_name}.png",
#                 full_page=True
#             )
#             print(f"📸 Screenshot captured: {safe_name}.png")
#
#         except Exception as e:
#             print("❌ Screenshot failed:", e)
#
#     context.page.close()
#
# def after_all(context):
#     context.browser.close()
#     context.playwright.stop()

from playwright.sync_api import sync_playwright
from utils import data_loader
from services.api_client import APIClient
import re
import os
import allure

from pages.pim_page import PimPage
from pages.login_page import LoginPage
from pages.leave_page import LeavePage


def before_all(context):
    os.makedirs("screenshots", exist_ok=True)
    os.makedirs("videos", exist_ok=True)

    context.users = data_loader.load_test_data()
    context.api = APIClient(
        "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2"
    )

    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)


def before_scenario(context, scenario):
    context.context = context.browser.new_context(
        record_video_dir="videos/",
        record_video_size={"width": 1280, "height": 720}
    )

    context.page = context.context.new_page()

    # 🔗 Page objects
    context.login_page = LoginPage(context.page)
    context.pim_page = PimPage(context.page)
    context.leave_page = LeavePage(context.page)

    context.base_url = "https://opensource-demo.orangehrmlive.com"


def after_scenario(context, scenario):
    safe_name = re.sub(r'[^A-Za-z0-9]+', '_', scenario.name)

    # 📸 Screenshot on failure
    if scenario.status == "failed" and context.page:
        try:
            screenshot_path = f"screenshots/{safe_name}.png"

            context.page.screenshot(
                path=screenshot_path,
                full_page=True
            )

            print(f"📸 Screenshot captured: {safe_name}.png")

            # 📎 Attach to Allure
            allure.attach.file(
                screenshot_path,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

        except Exception as e:
            print("❌ Screenshot failed:", e)

    # 🔴 Close page + context (REQUIRED for video saving)
    context.page.close()
    context.context.close()

    # 🎥 Attach video (only for failed scenarios)
    if scenario.status == "failed":
        try:
            video_path = context.page.video.path()

            allure.attach.file(
                video_path,
                name="Failure Video",
                attachment_type=allure.attachment_type.WEBM
            )

            print(f"🎥 Video attached: {video_path}")

        except Exception as e:
            print("❌ Video attach failed:", e)


def after_all(context):
    context.browser.close()
    context.playwright.stop()