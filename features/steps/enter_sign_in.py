from behave import *


@given('Opened the Sign in page.')
def step_impl(context):
    context.enter_sign_in.go_home()


@then('The page redirect to the "{expected_page}" page.')
def step_impl(context, expected_page):
    expected_url = "https://magento.softwaretestingboard.com/" + expected_page
    assert context.browser.get_current_url() == expected_url
