import time
from behave import *
from features.lib.pages.login_Page_Concert import LoginPage
from data_Reader.read_Properties import ReadConfig
base_URL = ReadConfig.get_application_url()


@given('Open Concert & Verify title')
def open_concert(context):
    context.logger.info("Opening concert web client application")
    page = LoginPage(context)
    page.visit(base_URL)
    time.sleep(10)
    assert "Sign in to mOS" in page.get_title()


@then('Login concert & Verify title')
def login_concert(context):
    page = LoginPage(context)
    page.login()
    time.sleep(10)
    assert "DevelopmentCluster" in page.get_title()


@then('Logout Concert & Verify title')
def logout(context):
    page = LoginPage(context)
    time.sleep(5)
    page.click_user_button()
    time.sleep(5)
    page.click_logout()
    time.sleep(5)
    assert "Sign in to mOS" in page.get_title()


