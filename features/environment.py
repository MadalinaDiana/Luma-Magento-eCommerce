from behave import fixture, use_fixture
from browser import Browser
from pages.create_account import CreateAccount
from pages.begin_home_page import HomePage
from pages.enter_sign_in import SignIn
from pages.functionality_account import AccountFunction

@fixture
def launch_browser(context):
    context.browser = Browser()
    context.create_account = CreateAccount(context.browser.driver)
    context.begin_home_page = HomePage(context.browser.driver)
    context.enter_sign_in = SignIn(context.browser.driver)
    context.functionality_account = AccountFunction(context.browser.driver)

def before_scenario(context,scenario):
    the_fixture1 = use_fixture(launch_browser, context)
def after_scenario(context, scenario):
    context.browser.close()
