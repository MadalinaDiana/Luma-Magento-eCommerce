from browser import Browser
from pages.create_account import CreateAccount
from pages.home_page import HomePage
from pages.sign_in import SignIn

def before_all(context):
    context.browser = Browser()
    context.create_account = CreateAccount(context.browser.driver)
    context.home_page = HomePage(context.browser.driver)
    context.sign_in = SignIn(context.browser.driver)

def after_all(context):
    context.browser.close()
