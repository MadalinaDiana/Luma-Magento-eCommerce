from browser import Browser
from pages.create_account import CreateAccount
from pages.home_page import HomePage


def before_all(context):
    context.browser = Browser()
    context.form_page = CreateAccount(context.browser.driver)
    context.home_page = HomePage(context.browser.driver)


def after_all(context):
    context.browser.close()
