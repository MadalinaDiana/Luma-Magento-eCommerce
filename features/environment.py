from browser import Browser
from pages.create_account import CreateAccount
from pages.begin_home_page import HomePage
from pages.enter_sign_in import SignIn
from pages.functionality_account import AccountFunction

def before_all(context):
    context.browser = Browser()
    context.create_account = CreateAccount(context.browser.driver)
    context.begin_home_page = HomePage(context.browser.driver)
    context.enter_sign_in = SignIn(context.browser.driver)
    context.functionality_account = AccountFunction(context.browser.driver)

def after_all(context):
    context.browser.close()
